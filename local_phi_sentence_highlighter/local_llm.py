# Example: reuse your existing OpenAI setup
from openai import OpenAI



def call_phi(prompt):
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1235/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": "Only Answer True or False. Do not say anything else."},
      {"role": "user", "content": f"{prompt}"}
    ],
    temperature=0.7,
    max_tokens=2,
    
  )

  return completion.choices[0].message.content

# print(completion.choices[0].message)

