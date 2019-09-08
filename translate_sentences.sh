#!/bin/bash

rm mn_en_sentences.txt && touch mn_en_sentences.txt

translate() {
  mn_sentence="$1"
  en_sentence=$(torify trans -brief "$mn_sentence")
  echo "$mn_sentence", "+++++SEP+++++", "$en_sentence" >> mn_en_sentences.txt
}

export -f translate

cat filtered_sentences.txt | parallel -j0 -k translate 


