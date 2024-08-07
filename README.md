# mitya-0.0

### Model Description

mitya is a model based on Dostoevsky's renowned works, including but not limited to: The Brothers Karamazov, Crime & Punishment, Demons, etc. 
It is trained upon the open-sourced model Mistral-7b-v0.3 and comes in 6 distinct sizes and quantizations.

- **Developed by:** tri282
- **Funded by:** my sincere adoration for his ideals
- **Model type:** question-answering
- **Language(s) (NLP):** English (primary), though it can interpret other languages and answer in English
- **Finetuned from model:** mistral-7b-v0.3
- **Repository:** https://github.com/tri2802/mitya-0.0 (to be updated)
- **Local Download:** https://ollama.com/tri282/mitya/tags
- Inference/Download: https://huggingface.co/tri282/dostoevskyGPT_merged
    
## Intended Cause

before everyone, for everyone and everything

## Bias, Risks, and Limitations

this model was initially trained on 7,000 question-answer pairs with LoRA, and later on adapted to its base model. given the limited training examples it
was fine-tuned on, expect minor, if not any (for i spitefully claim), errors with regards to its syntax and so on

## Usage
- **Inference:**

from transformers import AutoTokenizer, AutoModelForCausalLM  
import torch

path = "tri282/dostoevskyGPT_merged"  

tokenizer = AutoTokenizer.from_pretrained(path)  
model = AutoModelForCausalLM.from_pretrained(path)

input_text = "your text here"  
inputs = tokenizer(input_text, return_tensors = "pt")

with torch.no_grad():  
____outputs = model.generate(**inputs, max_new_tokens = 250)

output_text = tokenizer.decode(outputs[0], skip_special_tokens = True)  
print(output_text)

- **Download:**

from huggingface_hub import snapshot_download

path = "tri282/dostoevskyGPT_merged"  
snapshot_download(repo_id = path, local_dir = "./your_directory_here")

### Training Data

currently propriety

#### Training Hyperparameters

- **Training regime:** fp16 mixed precision
- **Epochs:** 3
- **Learning Rate:** 2e-4
- **Batch Size:** 16
- **Rank, LoRA Alpha, LoRA Dropout:** 64, 96, 0.1

#### Speeds, Sizes, Times [optional]

this model was trained for 6 hours on Tesla L4 GPU. it is roughly 27GB with float32 precision, with other quantizations available on Ollama

#### Evaluation

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66a14c1ad723c565bb551702/n_8x038xNH_sSxdxJiQ_e.png)

#### Summary

i hold firm awareness of the current limitations with regards to my model, that being said, i had a great time testing it out.
i ask nothing but your great expectations on future optimizations and versions


#### Citations
special thanks to Dostoevsky himself, cordially
