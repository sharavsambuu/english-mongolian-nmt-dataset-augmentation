#!/bin/bash

translate() {
  mn_sentence="$1"
  en_sentence=$(torify trans $mn_sentence)
  echo "$sentence", "+++++SEP+++++", "$en_sentence"
}

export -f translate

cat filtered_sentences.txt | parallel -j0 -k translate >> mn_en_sentences.txt


