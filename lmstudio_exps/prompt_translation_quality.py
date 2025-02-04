#%%
# Run lmstudio
# Local Server -> Start Server
#
# Make sure to load the llama 3.1 in the Chat
#

#%%
import requests
import json
import re


#%%


#%%
#llm_name = "deepseek-r1-distill-llama-8b"
llm_name = "Meta-Llama-3.1-8B-Instruct-GGUF"
def hello_lmstudio_call(system_promtp="", user_prompt="'"):
    url = 'http://localhost:1234/v1/chat/completions'
    headers = {
        'Content-Type': "application/json"
    }
    data = {
        "model":"lmstudio-community/{llm_name}",
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
"""

translation_pair = [
    "Хөтөлбөрийн хүрээнд энэ насны иргэдэд Хөдөлмөр эрхлэлтийн үйлчилгээний төвөөс нийгмийн үйлчилгээний чиглэлээр ажил санал болгож, хийсэн ажилд нь хөлс урамшуулал олгох аж",
    "Within the framework of the program, the Employment Service Center will offer social work services to those aged and will be paid compensation."
]

task_prompt = f"""
You are a highly skilled Mongolian-to-English translator. Your primary goal is to produce accurate and clear English translations of Mongolian text. Meaning accuracy is your top priority. While fluency in English is important, it should never compromise the original meaning of the source text.

**Translation Process:**

1. **Analyze:** Carefully examine the Mongolian text to understand its meaning, context, and purpose.
2. **Evaluate Initial Translation:** Assess the provided English translation, focusing on meaning accuracy and clarity.
3. **Assign Accuracy Score:** Assign a score from 0.0 (completely inaccurate) to 1.0 (perfectly accurate) based solely on how well the initial translation preserves the meaning of the original text.
4. **Translate:** Create a refined English translation that accurately conveys the original meaning.
5. **Backtranslate:** Translate your refined English translation back into Mongolian.
6. **Validate:** Compare the backtranslation to the original Mongolian text. If there are any meaning discrepancies, revise your English translation to ensure perfect accuracy.

**Handling Unknown Words:**

If you encounter a Mongolian word that cannot be directly translated, transliterate it using a standard Mongolian-to-English transliteration system. Indicate this in your reasoning.

**Ambiguity:**

If the Mongolian text is ambiguous, try to preserve that ambiguity in your English translation if possible. If not, choose the most likely interpretation based on context and explain your choice in your reasoning.

**Reasoning Documentation (within `<reasoning>` tag):**

1. **Overall Meaning and Context:** Briefly describe the main idea and context of the Mongolian text.
2. **Initial Translation Evaluation & Accuracy-Centric Quality Score:** Critically assess the provided English translation, specifically identifying meaning accuracy errors and clarity/fluency issues. Assign a quality score from 0.0 to 1.0, justifying it based on meaning accuracy and clarity, with meaning accuracy being the dominant factor.
3. **Initial Translated version:** Provide initally translated text.
4. **Key Meaning-Related Challenges:** Highlight the most significant translation challenges you encountered in maintaining perfect meaning fidelity for this specific text, including instances of unknown words and how you handled them.
5. **Translation Rationale:** Briefly explain the reasoning behind your translation choices.
6. **Refined translation:** Provide your refined english translation of the `final_answer`.
7. **Backtranslation:** Provide your backtranslation of the `final_answer` into Mongolian. You also print backtranslated text here.
8. **Meaning Divergence Analysis:** Detail your comparison of the backtranslation and the original Mongolian text. Note any meaning divergences found and how they were addressed in the `final_answer`. If no divergences were found, explicitly state that.
9. **Backtranslation doesn't match:** If the backtranslation doesn't match, suggest your best translation attempt here, also don't forget best translation attempt. If the previous step doesn't find significant backtranslation divergence, you can leave this step empty.

**Output Format:**

Your response must contain the following tags, and only one of each:

*   `<reasoning>`
*   `<final_answer>`
*   `<score>`

**Do not include any text outside of these tags. Do not use any markdown formatting within the tags. The content of each tag should be plain text, except for the `<output>` tag, which should contain only valid JSON.**

**Example of Correct Output Format:**

```
<reasoning>
Overall Meaning: ...
Initial Translation Evaluation: ...
Inital Translated version
Accuracy Score: ...
Translation Challenges: ...
Translation Rationale: ...
Refined Translation: ...
Backtranslation: ...
Meaning Divergence Analysis: ...
</reasoning>

<final_answer>
... (Your final, accurate English translation)
</final_answer>

<score>
    0.4 (Your assessed score for provided translation)
</score>
```

**Mongolian Text:** {translation_pair[0]}

**English Translation:** {translation_pair[1]}
"""

response = hello_lmstudio_call(system_promtp=system_prompt, user_prompt=task_prompt)

print(response)


#%%
print(response)


#%%
def extract_content(response_text):
    content = {}
    reasoning_pattern         = r"<reasoning>(.*?)</reasoning>"
    final_answer_pattern      = r"<final_answer>(.*?)</final_answer>"
    score_pattern             = r"<score>(.*?)</score>"
    content["reasoning"     ] = re.search(reasoning_pattern, response_text, re.DOTALL).group(1).strip() if re.search(reasoning_pattern, response_text, re.DOTALL) else None
    content["final_answer"  ] = re.search(final_answer_pattern, response_text, re.DOTALL).group(1).strip() if re.search(final_answer_pattern, response_text, re.DOTALL) else None
    content["score"         ] = re.search(score_pattern, response_text, re.DOTALL).group(1).strip() if re.search(score_pattern, response_text, re.DOTALL) else None
    return content

response_json = extract_content(response_text=response)
response_json


#%%
print(response_json)


#%%
print(response_json['reasoning'])

#%%
print(response_json['final_answer'])

#%%
print(response_json['score'])

#%%


#%%
print("### Translation Pair ###")
print(f"Mongolian : {translation_pair[0]}")
print(f"English   : {translation_pair[1]}")

print(f"### Evalution and improvements ###")
print(f"quality score : {response_json['score']}")
print(f"improved      : {response_json['final_answer']}")


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


