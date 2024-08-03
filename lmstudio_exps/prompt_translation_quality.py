#%%
# Run lmstudio
# Local Server -> Start Server
#
# Make sure to load the llama 3.1 in the Chat
#

#%%
import requests
import json


#%%


#%%
def hello_lmstudio_call(system_promtp="", user_prompt="'"):
    url = 'http://localhost:1234/v1/chat/completions'
    headers = {
        'Content-Type': "application/json"
    }
    data = {
        "model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
        'messages': [
            {'role': 'system', 'content': f"{system_promtp}"},
            {'role': 'user'  , 'content': f"{user_prompt}"}
        ],
        "temperature" : 0.8,
        "max_tokens"  : -1,
        "stream"      : False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return None
    else:
        print(f"failed to get response : {response.status_code}, {response.text}")
        return None


#%%


#%%
system_prompt = """
You are a knowledgeable, efficient, and direct Al assistant. 
You are also fluent in English and Mongolian languages.
You are very direct and respond short.
"""

translation_pair = [
    "Хөтөлбөрийн хүрээнд энэ насны иргэдэд Хөдөлмөр эрхлэлтийн үйлчилгээний төвөөс нийгмийн үйлчилгээний чиглэлээр ажил санал болгож, хийсэн ажилд нь хөлс урамшуулал олгох аж",
    "Within the framework of the program, the Employment Service Center will offer social work services to those aged and will be paid compensation."
]

task_prompt = f"""
Instruction:
I will provide a Mongolian-to-English translation pair. Your task is to evaluate the quality of the translation on a scale from 0 to 1 and suggest an improved English translation.

Response:
Please provide the response in JSON format only. Do not include any explanations, additional text, or comments. No additional translation pairs are needed.

JSON format:
{{
  "quality": 0.4,
  "suggested_english_translation": "bla bla bla... etc"
}}

Here is the translation:

Mongolian text:
"{translation_pair[0]}"


English translation:
"{translation_pair[1]}"
"""

response = hello_lmstudio_call(system_promtp=system_prompt, user_prompt=task_prompt)


#%%


#%%
response_json = json.loads(response)

print("### Translation Pair")
print(f"Mongolian : {translation_pair[0]}")
print(f"English   : {translation_pair[1]}")

print(f"### Evalution")
print(f"quality score : {response_json['quality']}")
print(f"suggested     : {response_json['suggested_english_translation']}")



#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


