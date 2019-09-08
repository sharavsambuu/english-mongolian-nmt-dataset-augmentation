#!/bin/bash

rm mn_en_sentences.txt && touch mn_en_sentences.txt

cat filtered_sentences.txt | while read LINE; do echo "$LINE +++++SEP+++++ " >> mn_en_sentences.txt; done
