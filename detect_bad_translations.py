#
# Usage :
#   python detect_bad_translation temp/mn_en.txt 0.5
#
#

import sys
import json
import requests


input_file        = sys.argv[1]
quality_threshold = float(sys.argv[2])


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


def evaluate_translation(mn_text, en_text):
    system_prompt = """
        You are a knowledgeable, efficient, and direct Al assistant. 
        You are also fluent in English and Mongolian languages.
        You are very direct and respond short.
    """

    task_prompt = f"""
        Instruction:
        I will provide a Mongolian-to-English translation pair. 
        Your task is to evaluate the quality of the translation on a scale from 0 to 1, where 0 is not understandable and 1 is perfectly accurate. 
        Also, provide a revised English translation that better conveys the meaning of the Mongolian text in natural, fluent English.

        Response:
        Please provide the response in JSON format only. Do not include any explanations, additional text, or comments. No additional translation pairs are needed.

        JSON format:
        {{
            "quality": 0.4,
            "improved_english_translation": "bla bla bla... etc"
        }}

        Here is the translation:

        Mongolian text:
        "{mn_text}"

        English translation:
        "{en_text}"
    """

    response = hello_lmstudio_call(system_promtp=system_prompt, user_prompt=task_prompt)
    response_json = json.loads(response)

    return response_json['quality'], response_json['improved_english_translation']


try:
    sep = "+++++SEP+++++"
    with open(input_file, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            try:
                chunks  = line.split(sep)
                mn_text = chunks[0].strip()
                en_text = chunks[1].strip()
                quality, improved_en = evaluate_translation(mn_text=mn_text, en_text=en_text)
                if quality <= quality_threshold:
                    print(f"Quality : {quality} : {mn_text} --- {en_text} #####  improved --> {improved_en}")
            except:
                continue
except KeyboardInterrupt:
    print("\nInterrupted by user.")