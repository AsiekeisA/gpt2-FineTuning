from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, GPT2TokenizerFast, GPT2Tokenizer
import torch

model_path = './models/'
sequence = ' '
sequence0 = 'Q: How to convert for loop to parallel stream in java?\n'
sequence1 = "How to convert for loop to parallel stream in java:"
sequence2 ='convert forloop to parallel stream in java:'
max_length=200
top_k=1
tp_k = [1, 10]

def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer


def generate_text(model_path, sequence, max_length,top_k, i):
    model = load_model(model_path+str(i))
    tokenizer = load_tokenizer(model_path+str(i))
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        ids,
        do_sample=True,
	    max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        top_k=top_k,
        top_p=0.95,
    )
    print(tokenizer.decode(final_outputs[0], skip_special_tokens=True))

for i in range(1):
    for k in tp_k:
        if i == 0:
            print(">>>>>>>>>> Model",i)
            print(">>>>>>>>>> Top_k", k)
            generate_text(model_path, sequence0, max_length, k, i)
        print(">>>>>>>>>> Model",i)
        print(">>>>>>>>>> Top_k", k)
        generate_text(model_path, sequence, max_length, k, i)
        print("--------------------------------------------\n")
        print(">>>>>>>>>> Model",i)
        print(">>>>>>>>>> Top_k", k)
        generate_text(model_path, sequence2, max_length, k, i)
        print("--------------------------------------------\n")

