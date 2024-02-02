import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

ANYSCALE_API_KEY = os.getenv("ANYSCALE_API_KEY")

OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

llm_client = openai.OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = ANYSCALE_API_KEY
)

openai_client = openai.OpenAI(
    api_key = OPENAI_API_KEY
)


#Available Models
mistral_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llama_model = "meta-llama/Llama-2-70b-chat-hf"
gpt_turbo_model = "gpt-3.5-turbo-0125"
phi_model = "local-model"

def call_llm(prompt, model,temperature,max_tokens = 4000):
    completion = llm_client.completions.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion

def call_openai(prompt, model,temperature,max_tokens = 1500):
    completion = openai_client.chat.completions.create(
        model=model,
        messages= [{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion

def call_phi(prompt, model,temperature,max_tokens = 1500):
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1235/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model=model, # this field is currently unused
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
    max_tokens=max_tokens,
    
  )

  return completion.choices[0].message.content

