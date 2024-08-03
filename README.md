

# Tasks

  Main goal is to improve existing translation pairs using Llama 3.1 and some prompts

  1. Find a way to call LM Studio using Python
  2. Prepare a prompt to detect badly translated pairs
  3. Prepare a prompt to improve mongolian to english translation pair
  4. Publish improved translations
  5. Train on improved translation dataset on the Colab and Tensorflow 2`





# Notes

  700 million word Mongolian news data set
  https://github.com/tugstugi/mongolian-bert

  Python library for google translation, textblob
  https://textblob.readthedocs.io/en/dev/

# Steps

  sudo apt install parallel tor build-essential rar virtualenv bsdmainutils
  
  virtualenv -p python3 env && source env/bin/activate && pip install -r requirements.txt
  
  ./install_translate.sh
  
  python3 datasets/dl_and_preprop_mn_news.py
  
  ./generate_sentences.sh && ./criterion_sentences.sh && ./prepare_translation.sh && ./split_sentences.sh
  
  ./runtask.sh

# References and links

  https://lmstudio.ai/

  https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF

  https://opensource.com/article/18/5/gnu-parallel
  
  https://askubuntu.com/questions/147241/execute-sudo-without-password

  
# Released datasets

  [2019/09/10] 5K unvalidated sentences of pairs for english to mongolian.
  
  https://gist.github.com/sharavsambuu/be9001ddcb954565606466a3556bbf27
  
  [2019/09/13] 94K unvalidated sentences of pairs for english to mongolian.
  
  https://drive.google.com/file/d/1GNo1XJxRFxjey5VDsHjLvj9upXJOqd3e/view?usp=sharing
  
  [2019/10/10] 1 million mongolian to english sentence pairs.
  
  https://drive.google.com/file/d/14AtTVgibirSdHYTBFM9G1XPS7DvM5SdE/view?usp=sharing
  
  
# Neural machine translation colab experiment, based on official tensorflow transformer tutorial

Pretrained version for fast inference [![Inference pretrained version](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xnwQLlh_5C1UOYUVEuu7D9_IUORn0YRK)

Train on Colab [![Train In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Qkzo624DrXjaEumK54sjf2KQX_zBsiLq)
