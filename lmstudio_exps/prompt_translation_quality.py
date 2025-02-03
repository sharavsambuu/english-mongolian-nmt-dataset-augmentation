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
"""

translation_pair = [
    "Хөтөлбөрийн хүрээнд энэ насны иргэдэд Хөдөлмөр эрхлэлтийн үйлчилгээний төвөөс нийгмийн үйлчилгээний чиглэлээр ажил санал болгож, хийсэн ажилд нь хөлс урамшуулал олгох аж",
    "Within the framework of the program, the Employment Service Center will offer social work services to those aged and will be paid compensation."
]

task_prompt = f"""
You are a world-class Mongolian to English translator, renowned for your ability to refine and elevate existing translations. Your expertise is not just in accuracy, but in crafting English that is indistinguishable from text originally written by a native speaker. You possess an exceptional command of both Mongolian and English, including subtle nuances, cultural contexts, idioms, and stylistic preferences. Your goal is to transform potentially awkward or literal translations into polished, natural, and impactful English while preserving the original meaning and intent.

**Your Translation Improvement Process (Meticulous and Iterative):**

1. **Deep Dive Comprehension:** Begin by thoroughly analyzing both the Mongolian source text and the provided English translation. Understand the core message, the intended audience, the purpose of the text, and its overall context. Identify the tone and style.
2. **Contextual Nuance Analysis:** Immerse yourself in the context. What is the subject matter? Is it formal, informal, technical, literary, etc.? Identify any cultural references, specific domain terminology, or idiomatic expressions that require special attention for culturally appropriate and accurate translation.
3. **Initial Quality Assessment (Honest and Critical):**  Objectively evaluate the given English translation. Identify specific weaknesses:
    * **Accuracy Issues:** Are there any mistranslations or distortions of the original meaning?
    * **Awkward Phrasing:** Does any part sound unnatural, clunky, or not idiomatic in English?
    * **Fluency Problems:** Does the text flow smoothly? Are there unnatural sentence structures or word choices that impede readability?
    * **Tone and Style Mismatch:** Does the translation maintain the intended tone and style of the original Mongolian text?
    * **Assign a Quality Score (0.0 - 1.0):**  Based on your assessment, assign a quality score from 0.0 (very poor) to 1.0 (excellent, near-perfect). Consider accuracy, fluency, naturalness, and style in your score.
4. **First Pass Refinement (Precision and Clarity):**  Refine the English translation focusing on accuracy and clarity. Correct any factual errors or mistranslations. Improve grammatical correctness and ensure precise word choices that accurately reflect the Mongolian meaning. Enhance clarity and eliminate any ambiguity.
5. **Stylistic Enhancement (Natural Flow and Tone):**  Elevate the style to ensure natural flow and appropriate tone. Restructure sentences if needed for better readability in English. Choose vocabulary and phrasing that aligns with the intended style and target audience, ensuring consistency throughout the text.
6. **Terminology and Register Verification:** If the text contains specialized terms or jargon, rigorously verify their accuracy and appropriateness in English. Consult dictionaries, glossaries, domain experts, or online resources to confirm the best terminology. Ensure the register (formal/informal) is consistently maintained.
7. **Second Pass Refinement - Native Speaker Authenticity (Idiomaticity and Nuance):** This is crucial for achieving a truly polished translation.  Read your refined translation as if you were a native English speaker encountering this text for the first time.  Focus on:
    * **Idiomaticity:** Replace any literal translations with natural English idioms and expressions.
    * **Natural Word Choice:** Substitute any words or phrases that sound slightly "translated" with more common and natural English equivalents a native speaker would instinctively use.
    * **Sentence Rhythm and Flow:** Fine-tune sentence structure and word order for optimal rhythm and flow in English. Ensure the text reads smoothly and sounds pleasing to a native English ear.
    * **Cultural Appropriateness:** Double-check for cultural nuances and ensure the translation resonates appropriately with an English-speaking audience, avoiding any unintended cultural misunderstandings.

**Important Constraint:** While improving naturalness and fluency, **never significantly divert from the original meaning** of the Mongolian text. Your primary goal is to enhance the *quality* of the translation, not to rewrite or reinterpret the source text.

**Response Format:**

For the Mongolian text and its initial English translation provided below, please perform the evaluation and improvement process described above. Present your response in the following format:

    <reasoning>
    1. **Overall Meaning and Context:** ... (Explain your understanding of the text's topic, purpose, and context)
    2. **Initial Translation Evaluation & Quality Score:** ... (Critically assess the provided English translation, identify specific weaknesses and assign a quality score from 0.0 to 1.0 with justification)
    3. **Key Challenges:** ... (Highlight the most significant translation challenges you faced in this specific text)
    4. **Translation Choices (First Refinement):** ... (Explain your key decisions and changes during the first refinement pass, focusing on accuracy and clarity improvements)
    5. **Stylistic Enhancement Details:** ... (Describe the stylistic improvements you made to enhance flow, tone, and readability during the first refinement)
    6. **Terminology & Register Notes:** ... (Mention any terminology research or register considerations, if applicable)
    7. **Second Pass Refinement - Native Speaker Authenticity Focus:**
        *   **Identified Unnatural/Awkward Elements:** ... (Pinpoint specific phrases or sentences from your *first refined translation* that still sound unnatural or "translated")
        *   **Proposed Authentic English Alternatives:** ... (Present your improved, more native-sounding English phrasings)
        *   **Justification for Authenticity Improvements:** ... (Explain *why* these changes make the translation sound more natural, idiomatic, and authentic to a native English speaker)
    </reasoning>

    <initial_answer>
    ... (Your first refined English translation - focusing on accuracy and clarity)
    </initial_answer>

    <final_answer>
    ... (Your final, highly polished and authentic English translation after the second pass of refinement)
    </final_answer>

    <output>
    **Important: Ensure the `<output>` section contains *only* valid JSON and is *not* enclosed in markdown code blocks (like ```json or ```).**
    ```json
    {{
      "quality_score": (Your assigned quality score for the *initial* English translation, e.g., 0.6),
      "initial_english_translation": "... (Your first refined English translation)",
      "final_english_translation": "... (Your final, authentic English translation)"
    }}
    ```
    </output>

**Mongolian Text:** {translation_pair[0]}

**English Translation:** {translation_pair[1]}
"""


response = hello_lmstudio_call(system_promtp=system_prompt, user_prompt=task_prompt)

response


#%%
def extract_content(response_text):
    content = {}
    reasoning_pattern      = r"<reasoning>(.*?)</reasoning>"
    initial_answer_pattern = r"<initial_answer>(.*?)</initial_answer>"
    final_answer_pattern   = r"<final_answer>(.*?)</final_answer>"
    output_pattern         = r"<output>(.*?)</output>"
    content["reasoning"     ] = re.search(reasoning_pattern, response_text, re.DOTALL).group(1).strip() if re.search(reasoning_pattern, response_text, re.DOTALL) else None
    content["initial_answer"] = re.search(initial_answer_pattern, response_text, re.DOTALL).group(1).strip() if re.search(initial_answer_pattern, response_text, re.DOTALL) else None
    content["final_answer"  ] = re.search(final_answer_pattern, response_text, re.DOTALL).group(1).strip() if re.search(final_answer_pattern, response_text, re.DOTALL) else None
    content["output"        ] = re.search(output_pattern, response_text, re.DOTALL).group(1).strip() if re.search(output_pattern, response_text, re.DOTALL) else None
    return content

response_json = extract_content(response_text=response)
response_json

#%%


#%%
print(response_json['reasoning'])

#%%
print(response_json['initial_answer'])

#%%
print(response_json['final_answer'])

#%%
print(response_json['output'])

#%%


#%%
output_json = json.loads(response_json['output'])

print("### Translation Pair")
print(f"Mongolian : {translation_pair[0]}")
print(f"English   : {translation_pair[1]}")

print(f"### Evalution")
print(f"quality score : {output_json['quality_score']}")
print(f"improved      : {output_json['final_english_translation']}")



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


