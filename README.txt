# Notes

  700 million word Mongolian news data set
  https://github.com/tugstugi/mongolian-bert

  Python library for google translation, textblob
  https://textblob.readthedocs.io/en/dev/

# Steps

  sudo apt install parallel tor
  ./install_translate.sh
  python3 datasets/dl_and_preprop_mn_news.py
  ./generate_sentences.sh && ./criterion_sentences.sh && ./prepare_translation.sh && ./split_sentences.sh
  ./run.sh

# References
  https://opensource.com/article/18/5/gnu-parallel

  
