# Notes

  700 million word Mongolian news data set
  https://github.com/tugstugi/mongolian-bert

  Python library for google translation, textblob
  https://textblob.readthedocs.io/en/dev/

# Steps

  sudo apt install parallel tor build-essential rar virtualenv
  virtualenv -p python3 env && source env/bin/activate && pip install -r requirements.txt
  ./install_translate.sh
  python3 datasets/dl_and_preprop_mn_news.py
  ./generate_sentences.sh && ./criterion_sentences.sh && ./prepare_translation.sh && ./split_sentences.sh
  ./runtask.sh

# References

  https://opensource.com/article/18/5/gnu-parallel
  https://askubuntu.com/questions/147241/execute-sudo-without-password

  
# Released datasets

  [2019/09/10] Unvalidated 5 thousand sentence pairs of english to mongolian.
  https://gist.github.com/sharavsambuu/be9001ddcb954565606466a3556bbf27
  
