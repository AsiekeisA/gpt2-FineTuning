#!pip install transformers

import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

gpt2 = 'gpt2'
gpt2_medium = 'gpt2-medium'
gpt2_large = 'gpt2-large'
gpt2_xl = 'gpt2-xl'
model_name = gpt2

train_file_path = 'files'
files=os.listdir(train_file_path)

output_dir = './model-gpt'
overwrite_output_dir = False
per_device_train_batch_size = 8
num_train_epochs = 15.0
no_deprecation_warning = True
save_steps = 500


def load_dataset(file_path, tokenizer, block_size=256):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
    )
    return dataset

def load_data_collator(tokenizer, mlm=False):
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=mlm,
    )
    return data_collator

def train(train_file_path, model_name,
          output_dir,
          overwrite_output_dir,
          per_device_train_batch_size,
          num_train_epochs,
          save_steps):
    print('>>>>>>>>>>>>>  model: ', model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    print('tokenizer')
    data_collator = load_data_collator(tokenizer)
    print('collator')

    start_dir = output_dir + '/0'
    os.makedirs(start_dir, exist_ok=True)
    tokenizer.save_pretrained(start_dir)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    model.save_pretrained(start_dir)
    trainer = None

    for i in range(1, int(num_train_epochs) + 1):
        new_output_dir = os.path.join(output_dir, str(i))
        os.makedirs(new_output_dir, exist_ok=True)

        tokenizer.save_pretrained(new_output_dir)
        model = GPT2LMHeadModel.from_pretrained(os.path.join(output_dir, str(i - 1)))
        model.save_pretrained(new_output_dir)

        training_args = TrainingArguments(
            output_dir=new_output_dir,
            overwrite_output_dir=overwrite_output_dir,
            per_device_train_batch_size=per_device_train_batch_size,
            num_train_epochs=1.0
        )

        x = 0
        metrics_file = open(os.path.join(new_output_dir, 'epoch_metrics.txt'), 'w', encoding='utf-8')

        for filename in files:
            if 'cached' in filename:
                continue
            else:
                x += 1
                print('Epoch -', i, ' file -', x, 'of 1623 :', filename)
                file_path = os.path.join(train_file_path, filename)
                train_dataset = load_dataset(file_path, tokenizer)
                print('train_dataset')

                model = GPT2LMHeadModel.from_pretrained(new_output_dir)
                trainer = Trainer(
                    model=model,
                    args=training_args,
                    data_collator=data_collator,
                    train_dataset=train_dataset,
                )

                train_results = trainer.train()
                metrics = train_results.metrics
                metrics_file.write('File:' + str(x) +' '+filename+
                                   ' Runtime: ' + str(metrics['train_runtime']) +
                                   ' Samples_per_second: ' + str(metrics['train_samples_per_second']) +
                                   ' Train_Loss: ' + str(metrics['train_loss'])+ '\n')
                trainer.save_model()
        metrics_file.close()
        print('Saving epoch:', i)
        trainer.save_model()

train(
    train_file_path=train_file_path,
    model_name=model_name,
    output_dir=output_dir,
    overwrite_output_dir=overwrite_output_dir,
    per_device_train_batch_size=per_device_train_batch_size,
    num_train_epochs=num_train_epochs,
    save_steps=save_steps,
)
