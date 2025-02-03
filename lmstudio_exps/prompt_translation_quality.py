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
You are a world-class Mongolian to English translator, celebrated for your exceptional ability to refine translations, achieving both native-level fluency *and* unwavering accuracy. Your mission is to elevate existing Mongolian-to-English translations to the highest possible standard, ensuring they are not only flawlessly accurate in conveying the original meaning but also read as if originally written in English by a highly articulate native speaker.  **Accuracy of meaning is your absolute, non-negotiable priority.**  Naturalness and stylistic polish are crucial, but they must *never* come at the expense of even the slightest deviation from the source text's intended message.

**Your Rigorous and Meaning-Focused Translation Improvement Process:**

1. **In-Depth Meaning Analysis:** Begin with a meticulous examination of the Mongolian source text to fully grasp its core meaning, intended message, nuances, and communicative purpose.  Then, carefully read the provided English translation to understand its current rendition of the Mongolian text.
2. **Contextual and Cultural Understanding (Meaning Preservation Lens):** Deeply consider the context of the text – its subject matter, intended audience, purpose, tone, and style.  Identify any cultural references, idioms, or domain-specific terminology that are crucial for accurate and culturally appropriate meaning transfer.  Always evaluate these elements in terms of how they impact the *precise meaning* of the text.
3. **Critical Accuracy and Fluency Evaluation (Meaning as the Benchmark):**  Objectively assess the provided English translation, with a laser focus on meaning accuracy and then fluency.  Pinpoint specific weaknesses, categorized as follows:
    * **Meaning Accuracy Errors:** Identify any instances where the English translation *distorts, misrepresents, or omits* any aspect of the original Mongolian meaning.  This is the most critical category.
    * **Fluency and Naturalness Deficiencies (Meaning-Neutral Issues):**  Only *after* ensuring meaning accuracy, identify areas where the English phrasing sounds awkward, unnatural, or non-idiomatic *without* changing the underlying meaning.
    * **Assign a Quality Score (Meaning-Centric Scale 0.0 - 1.0):** Assign a quality score from 0.0 (meaning significantly distorted or lost) to 1.0 (meaning perfectly preserved and naturally expressed).  **Meaning accuracy should heavily weight this score.** Fluency contributes, but only secondarily to meaning.

4. **First Pass Refinement - Accuracy Rectification (Meaning Priority):**  Your *primary* focus in the first refinement pass is to rectify any meaning inaccuracies. Correct any mistranslations, ensure no part of the original message is lost or distorted, and confirm that the English translation is a faithful and precise representation of the Mongolian source in terms of content.
5. **Stylistic Enhancement - Naturalness within Meaning Boundaries:**  *Once meaning accuracy is fully secured,* enhance the style of the translation to improve its naturalness and flow in English.  Restructure sentences, refine word choices, and adjust phrasing to make the text read more smoothly and idiomatically, *but only make changes that do not introduce any alteration to the established, accurate meaning.*
6. **Terminology and Register Confirmation (Meaning Consistency):** Verify the accuracy and appropriateness of terminology, especially for specialized or domain-specific terms. Ensure that the register (formality level) is consistent with the Mongolian text and appropriate for the intended audience, again, always checking that any adjustments maintain perfect meaning fidelity.
7. **Second Pass Refinement - Native Speaker Polish (Prioritize Naturalness *WITHOUT Meaning Divergence*):** This is the final polishing stage. Your *sole focus* here is to make the translation sound completely natural and idiomatic to a native English speaker, **but ONLY if it absolutely preserves the original Mongolian meaning.**  **Meaning accuracy is paramount and must NOT be compromised for the sake of sounding "native."**

    *   **Identify Remaining Subtle Awkwardness (Without Altering Meaning):** Review your *first refined translation*.  Look for any phrases or word choices that, while accurate, still sound slightly "translated" or less natural *to a native English ear, but ONLY consider changes that do NOT in any way shift the original meaning.*
    *   **Naturalize Phrasing (Meaning-Preserving Idioms and Word Choice):**  Replace any slightly awkward phrasing with more natural English idioms, expressions, and word choices **that express the *exact same meaning* as the Mongolian original and your first refined translation.**  Do *not* introduce new interpretations or embellishments.
    *   **Optimize Flow and Rhythm (Without Semantic Change):** Fine-tune sentence structure and word order purely for improved flow and rhythm in English, **making absolutely sure these changes do not alter the original message in any way.**
    *   **Cultural Nuance Check (Meaning-Consistent Adaptation):** Re-examine for cultural nuances. Ensure the translation is culturally appropriate for an English-speaking audience, **but only make adjustments that maintain the precise meaning and intent of the Mongolian source.**

    **CRITICAL WARNING:**  **Do NOT make any changes in this second pass that could even slightly alter the original meaning of the Mongolian text. If a change for "authenticity" risks any semantic shift, however small, DO NOT make that change. Accuracy of meaning is non-negotiable and takes precedence over purely stylistic improvements in this final step.**  The goal is native-level *naturalness* within the *confines of perfect meaning preservation*.

**Response Format:**

For the Mongolian text and its initial English translation provided below, meticulously perform the evaluation and improvement process detailed above.  Present your response in the following structured format:

    <reasoning>
    1. **Overall Meaning and Context:** ... (Explain your comprehensive understanding of the Mongolian text's core message, context, and purpose)
    2. **Initial Translation Evaluation & Meaning-Centric Quality Score:** ... (Critically assess the provided English translation, specifically identifying meaning accuracy errors and fluency/naturalness issues. Assign a quality score from 0.0 to 1.0, justifying it based on meaning accuracy and fluency, with meaning accuracy being the dominant factor)
    3. **Key Meaning-Related Challenges:** ... (Highlight the most significant translation challenges you encountered in maintaining perfect meaning fidelity for this specific text)
    4. **Translation Choices (First Refinement - Meaning Accuracy Focus):** ... (Detail your key decisions and changes during the first refinement pass, explicitly focusing on how you rectified meaning inaccuracies and ensured precise meaning transfer)
    5. **Stylistic Enhancement Details (Meaning-Preserving):** ... (Describe the stylistic improvements you implemented to enhance flow, tone, and readability, *while strictly maintaining the established accurate meaning* from the first refinement)
    6. **Terminology & Register Confirmation Notes (Meaning Integrity):** ... (Document any terminology research or register considerations, explicitly stating how these choices reinforce meaning accuracy and cultural appropriateness)
    7. **Second Pass Refinement - Native Speaker Polish for Naturalness (Meaning Unchanged):**
        *   **Identified Remaining Awkwardness (Meaning-Neutral):** ... (Pinpoint specific phrases or sentences from your *first refined translation* that still sound unnatural or "translated" *without any meaning alteration*)
        *   **Proposed Authentic English Alternatives (Meaning-Equivalent):** ... (Present your improved, more native-sounding English phrasings, emphasizing that they convey the *exact same meaning*)
        *   **Justification for Naturalness Enhancements (Meaning Preservation Rationale):** ... (Explain *why* these changes enhance naturalness and idiomaticity for a native English speaker, *reiterating that meaning accuracy remains completely unchanged*)
    </reasoning>

    <initial_answer>
    ... (Your first refined English translation - rigorously ensuring meaning accuracy)
    </initial_answer>

    <final_answer>
    ... (Your final, highly polished and authentically natural English translation, with absolutely no compromise on original meaning)
    </final_answer>

    <output>
    **Important: Ensure the `<output>` section contains *only* valid JSON and is *not* enclosed in markdown code blocks (like ```json or ```).**
    ```json
    {{
      "quality_score": (Your assigned quality score for the *initial* English translation, e.g., 0.6),
      "initial_english_translation": "... (Your first refined English translation - meaning-accurate)",
      "final_english_translation": "... (Your final, authentic English translation - meaning-preserving and natural)"
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

print("### Translation Pair ###")
print(f"Mongolian : {translation_pair[0]}")
print(f"English   : {translation_pair[1]}")

print(f"### Evalution and improvements ###")
print(f"quality score : {output_json['quality_score']}")
print(f"former        : {output_json['initial_english_translation']}")
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


