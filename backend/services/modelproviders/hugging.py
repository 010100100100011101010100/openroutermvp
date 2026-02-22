from huggingface_hub import InferenceClient
import os

client=InferenceClient(api_key=os.environ.get("HUGGINGFACE_API_KEY"))

async def hugging_completions_query(model:str,prompt:str,max_tokens:int=100,temperature:float=0.5,system_prompt:str="You are a helpful assistant")->str:
    chat_completions=client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":prompt}
        ]
    )
    return chat_completions.choices[0].message.content