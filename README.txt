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

# References

  https://opensource.com/article/18/5/gnu-parallel
  https://askubuntu.com/questions/147241/execute-sudo-without-password

  
# Released datasets

  [2019/09/10] 5K unvalidated sentences of pairs for english to mongolian.
  https://gist.github.com/sharavsambuu/be9001ddcb954565606466a3556bbf27
  [2019/09/13] 94K unvalidated sentences of pairs for english to mongolian.
  https://drive.google.com/file/d/1GNo1XJxRFxjey5VDsHjLvj9upXJOqd3e/view?usp=sharing
  [2017/10/10] 1M mongolian-to-english sentence pairs.
  https://drive.google.com/file/d/14AtTVgibirSdHYTBFM9G1XPS7DvM5SdE/view?usp=sharing
  
# Neural machine translation colab experiment, based on official tensorflow transformer tutorial

  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JMu96PYaDMDlqmpArxmE-kTkwIPSZDfB)
