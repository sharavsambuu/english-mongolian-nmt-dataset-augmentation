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
You are a world-class Mongolian to English translator, renowned for your unwavering commitment to accuracy and clarity. Your mission is to elevate existing Mongolian-to-English translations to the highest possible standard, ensuring they are flawlessly accurate in conveying the original meaning. While naturalness and fluency in English are desirable, they must *never* come at the expense of even the slightest deviation from the source text's intended message. **Accuracy of meaning is your absolute, non-negotiable priority.**

**Your Rigorous and Meaning-Focused Translation Improvement Process (Incorporating Backtranslation Check):**

1. **In-Depth Meaning Analysis:** Begin with a meticulous examination of the Mongolian source text to fully grasp its core meaning, intended message, nuances, and communicative purpose. Then, carefully read the provided English translation to understand its current rendition of the Mongolian text.
2. **Contextual and Cultural Understanding (Meaning Preservation Lens):** Deeply consider the context of the text – its subject matter, intended audience, purpose, tone, and style. Identify any cultural references, idioms, or domain-specific terminology that are crucial for accurate and culturally appropriate meaning transfer. Always evaluate these elements in terms of how they impact the *precise meaning* of the text.
3. **Initial Quality Assessment (Accuracy-Centric):** Objectively assess the provided English translation, with a laser focus on meaning accuracy and then fluency. Pinpoint specific weaknesses, categorized as follows:

    *   **Meaning Accuracy Errors:** Identify any instances where the English translation *distorts, misrepresents, or omits* any aspect of the original Mongolian meaning. This is the most critical category.
    *   **Clarity and Fluency Deficiencies:** Identify areas where the English phrasing is unclear, awkward, or difficult to understand, *without* changing the underlying meaning.
    *   **Assign a Quality Score (Accuracy-Centric Scale 0.0 - 1.0):** Assign a quality score from 0.0 (meaning significantly distorted or lost) to 1.0 (meaning perfectly preserved and clearly expressed). **Meaning accuracy should be the overwhelming factor in this score.** Fluency contributes, but only secondarily to meaning.
4. **Generate Initial Translation:** Based on your assessment, create an initial English translation. This will be your `initial_answer`.
5. **First Pass Refinement - Accuracy Rectification (Meaning Priority):** Your *primary* focus in the first refinement pass is to rectify any meaning inaccuracies in your `initial_answer`. Correct any mistranslations, ensure no part of the original message is lost or distorted, and confirm that the English translation is a faithful and precise representation of the Mongolian source in terms of content.
6. **Clarity and Readability Enhancement:** *Once meaning accuracy is fully secured,* improve the clarity and readability of the translation. Restructure sentences, refine word choices, and adjust phrasing to make the text easier to understand, *but only make changes that do not introduce any alteration to the established, accurate meaning.*
7. **Generate Final Translation:** After these refinements, create your final English translation. This is your `final_answer`.
8. **Terminology and Register Confirmation (Meaning Consistency):** Verify the accuracy and appropriateness of terminology, especially for specialized or domain-specific terms. Ensure that the register (formality level) is consistent with the Mongolian text and appropriate for the intended audience, again, always checking that any adjustments maintain perfect meaning fidelity.
9. **Backtranslation and Meaning Divergence Check:**
    *   **Generate Backtranslation:** Now, perform a *backtranslation* of your `final_answer` back into Mongolian.
    *   **Compare and Identify Meaning Divergences:** Compare this backtranslation to the *original Mongolian text*. Identify any points where your backtranslation differs in meaning from the original Mongolian. Focus on *meaning*, not just wording.
    *   **Rectify Meaning Divergences (If Any) in Final Translation:** If you identify any meaning shifts, immediately adjust your `final_answer` to eliminate these divergences and ensure perfect alignment with the original Mongolian meaning. **Meaning accuracy is paramount.**

**Reasoning Documentation:**

You must document your entire process within the `<reasoning>` tag. This should include:

1. **Overall Meaning and Context:** Explain your comprehensive understanding of the Mongolian text's core message, context, and purpose.
2. **Initial Translation Evaluation & Accuracy-Centric Quality Score:** Critically assess the provided English translation, specifically identifying meaning accuracy errors and clarity/fluency issues. Assign a quality score from 0.0 to 1.0, justifying it based on meaning accuracy and clarity, with meaning accuracy being the dominant factor.
3. **Key Meaning-Related Challenges:** Highlight the most significant translation challenges you encountered in maintaining perfect meaning fidelity for this specific text, including instances of unknown words and how you handled them.
4. **Initial Translation Rationale:** Briefly explain the reasoning behind your `initial_answer`.
5. **Initial Translation Text:** Provide initial translated text here
6. **Translation Choices (First Refinement - Meaning Accuracy Focus):** Detail your key decisions and changes during the first refinement pass, explicitly focusing on how you rectified meaning inaccuracies in the `initial_answer` and ensured precise meaning transfer.
7. **Clarity and Readability Enhancement Details:** Describe the clarity improvements you implemented between the `initial_answer` and `final_answer`, *while strictly maintaining the established accurate meaning* from the first refinement.
8. **Terminology & Register Confirmation Notes (Meaning Integrity):** Document any terminology research or register considerations, explicitly stating how these choices reinforce meaning accuracy and cultural appropriateness.
9. **Refined translation:** Provide your refined english translation text here.
10. **Backtranslation:** Provide your backtranslation of the `final_answer` into Mongolian. You also print backtranslated text here.
11. **Meaning Divergence Analysis:** Detail your comparison of the backtranslation and the original Mongolian text. Note any meaning divergences found and how they were addressed in the `final_answer`. If no divergences were found, explicitly state that.
12. **If backtranslation doesn't match, suggest your best translation attempt here, also don't forget best translation attemp. If previous step doesn't found significant backtranslation divergence, you can leave this step empty.


**CRITICAL WARNING: Output Format and Accuracy are Non-Negotiable**

*   **Output Format:** You must **strictly** adhere to the output format specified below. Any deviation from this format, including extra text outside the designated tags or multiple instances of the same tag, will be considered an error. **There should be only ONE `<reasoning>` tag, ONE `<initial_answer>` tag, ONE `<final_answer>` tag, and ONE `<output>` tag in your entire response.**
*   **Tag Closure:** **All opening tags (e.g., `<reasoning>`) must be properly closed with their corresponding closing tags (e.g., `</reasoning>`). Failure to close any tag will be considered a critical error.**
*   **Meaning Accuracy:** **Do NOT make any changes during the refinement process that could even slightly alter the original meaning of the Mongolian text *as verified by backtranslation*. Accuracy of meaning, confirmed by backtranslation, is non-negotiable.** The goal is clarity and precision *within the confines of perfect meaning preservation, rigorously checked by backtranslation.*

**Handling Unknown Words (Transliteration):**

As a world-class translator, you may encounter Mongolian words that are not present in current translation datasets or are otherwise untranslatable. In such cases, follow this protocol:

1. **Attempt Translation First:** Always attempt to translate the word based on its context, morphology (word structure), and any available resources.
2. **Transliteration as a Fallback:** If a direct translation is impossible and the word's meaning cannot be accurately conveyed through other means (e.g., paraphrasing), transliterate the word using a standard Mongolian to English transliteration system (e.g., a widely accepted Latin script representation of the Mongolian Cyrillic).
3. **Flag and Explain:** Clearly indicate in the `<reasoning>` section that the word has been transliterated. Briefly explain why a direct translation was not possible. If possible provide a concise explanation or a closely related English word within brackets after the transliteration to hint at its possible meaning.

**Example:**

*   Mongolian: "Байгаль"
*   If you cannot find a suitable translation for "Байгаль" you can transliterate it as "Baigal" and put the closest possible meaning within brackets like this "Baigal [nature]"

**Ambiguity:**

The Mongolian language, like any language, may contain inherent ambiguities. As a world-class translator, you must handle these with care and precision:

1. **Preserve Ambiguity When Possible:** If the Mongolian text is open to multiple interpretations, strive to preserve that same level of ambiguity in your English translation. This is preferred, as long as the resulting English is still understandable and doesn't create confusion where none existed in the original.
2. **Flag Significant Ambiguities:** If an ambiguity in the source text significantly impacts the core meaning or creates substantial difficulty in understanding, clearly flag this in the `<reasoning>` section. Note the different possible interpretations and the potential impact of each. If the context allows, suggest that clarification of the original Mongolian text might be necessary.
3. **Justify Interpretation When Necessary:** If preserving the ambiguity is impossible without rendering the English translation unintelligible, use your expert judgment to select the most likely interpretation. Base this decision on a thorough analysis of the context, considering factors like the source material type, intended audience, and purpose. In the `<reasoning>` section, meticulously document your decision-making process, explaining why you chose one interpretation over others. Transparency is crucial.

**Accuracy, Fluency, and the "Natural While Accurate" Principle:**

Your primary mission is to ensure **absolute accuracy** in conveying the meaning of the Mongolian text. However, a truly world-class translation is also natural and fluent in the target language. Therefore, while accuracy is non-negotiable, always strive for the most natural and idiomatic English phrasing *possible, without introducing even the slightest alteration to the meaning* that was meticulously established in the first refinement pass and rigorously verified through backtranslation.

**Example of Acceptable Stylistic Changes:**

*   **Passive to Active Voice (Meaning-Preserving):**
    *   Mongolian (Hypothetical): "The ball was kicked by the boy."
    *   Initial Translation (Literal): "The ball was kicked by the boy."
    *   Improved Translation (Natural): "The boy kicked the ball." (Acceptable if the emphasis is not specifically on the ball)
*   **Synonym for Repetition (Meaning-Preserving):**
    *   Initial Translation: "The house was big. The rooms in the house were also big."
    *   Improved Translation: "The house was large. The rooms inside were also spacious." (Acceptable if "big," "large," and "spacious" are truly interchangeable in this context).

**Examples of Unacceptable Meaning Deviations (Illustrative):**

| Mongolian (Hypothetical)                            | Initial English Translation (Incorrect)                                                        | Explanation of Error                                                                                                                                                                  | Acceptable Translation                                                                   |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------- |
| Нохой хүн рүү дайрсан. (Dog attacked a person)      | The man was attacked by the dog.                                                               | Changes the emphasis. The original focuses on the dog's action, while the translation focuses on the man being the recipient of the action. This might seem minor but is a meaning shift. | The dog attacked a person.                                                              |
| Тэр явсан байх. (He might have gone.)               | He went.                                                                                       | Loses the uncertainty expressed by "байх" (might have). This is a significant meaning error.                                                                                            | He might have gone. / It's possible that he went. / Perhaps he went.                      |
| Тэр өндөр. (He is tall.)                            | He is very tall.                                                                               | Adds an intensifier ("very") not present in the original. This is a slight but unacceptable modification of the meaning.                                                                     | He is tall.                                                                           |
| Маргааш бороо орно. (It will rain tomorrow.)        | It might rain tomorrow.                                                                        | Introduces uncertainty ("might") not present in the original. The original is a statement of fact or prediction, while the translation expresses possibility.                               | It will rain tomorrow. / It is going to rain tomorrow. (Depending on context)          |
| Тэр гоё дуулдаг. (She sings beautifully.)           | She can sing.                                                                                  | Significantly diminishes the meaning. The original conveys that she sings very well, while the translation merely states she has the ability to sing.                                         | She sings beautifully. / She is a wonderful singer. / She has a beautiful singing voice. |
| Тэр ирэхгүй гэж хэлсэн. (He said he wouldn't come.) | He said he might not come.                                                                     | Changes the certainty. "Wouldn't come" implies a definite decision, while "might not come" suggests a possibility.                                                                          | He said he wouldn't come.                                                              |

**Response Format:**

For the Mongolian text and its initial English translation provided below, meticulously perform the evaluation and improvement process detailed above, incorporating the backtranslation check.

**Your response must *exclusively* contain the following tags, and *only one* of each:**

*   `<reasoning>`
*   `<initial_answer>`
*   `<final_answer>`
*   `<output>`

** Don't forget to close tag in appopriate place.

**Do not include *any* text outside of these tags. The content within each tag should be a single, continuous block of text or properly formatted JSON (in the case of the `<output>` tag).**
**Prevent markdown characters text and json contents in the tags. Remember I will parse output by those tags and also json.

**Example of Correct Output Format:**

```
<reasoning>
1. Overall Meaning and Context: ... (content for reasoning)
2. Initial Translation Evaluation & Accuracy-Centric Quality Score: ... (content for evaluation)
... (rest of the reasoning content, including backtranslation and validation)
</reasoning>

<initial_answer>
... (Your first refined English translation)
</initial_answer>

<final_answer>
... (Your final, highly polished English translation)
</final_answer>

<output>
**CRITICAL: Output ONLY valid JSON within the `<output>` tags. Do NOT include any text, comments, or markdown delimiters (like ```json, ```, ''', etc.) before, after, or around the JSON. The content within `<output>` MUST be purely and exclusively JSON.**
{{
  "quality_score": ...,
  "initial_english_translation": "...",
  "final_english_translation": "..."
}}
</output>
'''

**Mongolian Text:** {translation_pair[0]}

**English Translation:** {translation_pair[1]}
"""


response = hello_lmstudio_call(system_promtp=system_prompt, user_prompt=task_prompt)

print(response)


#%%


#%%
def extract_content(response_text):
    content = {}
    reasoning_pattern         = r"<reasoning>(.*?)</reasoning>"
    initial_answer_pattern    = r"<initial_answer>(.*?)</initial_answer>"
    final_answer_pattern      = r"<final_answer>(.*?)</final_answer>"
    output_pattern            = r"<output>(.*?)</output>"
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


