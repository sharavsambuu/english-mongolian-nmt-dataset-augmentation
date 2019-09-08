#!/bin/bash

python sentences.py mn_corpus/mn_news_700m_1.txt > sentences.txt
python sentences.py mn_corpus/mn_news_700m_2.txt >> sentences.txt
python sentences.py mn_corpus/mn_news_700m_3.txt >> sentences.txt
python sentences.py mn_corpus/mn_news_700m_5.txt >> sentences.txt
python sentences.py mn_corpus/mn_news_700m_6.txt >> sentences.txt

cat sentences.txt | wc -l
