from groq import Groq
import os

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

async def groq_completions_query(ai:str,prompt:str,max_tokens:int=100,temperature:float=0.5,system_prompt:str="You are a helpful assistant")->str:
    chat_completion=client.chat.completions.create(
        model=ai,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":prompt}
        ]
    )
    return chat_completion.choices[0].message.content


