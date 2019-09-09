#!/bin/bash

#translate() {
#  mn_sentence="$1"
#  en_sentence=$(torify trans -brief "$mn_sentence")
#  echo "$mn_sentence", "+++++SEP+++++", "$en_sentence" >> mn_en_sentences.txt
#}
#export -f translate
#cat filtered_sentences.txt | parallel -j0 -k translate 
#cat filtered_sentences.txt | parallel -j0 -k translate 

function join_by { local IFS="$1"; shift; echo "$*"; }

i=1
cat $1 | 
  while read LINE; do 
    arr1=($(echo $LINE | awk '{split($0,array,"+++++SEP+++++")} END{print array[1]}'))
    arr2=($(echo $LINE | awk '{split($0,array,"+++++SEP+++++")} END{print array[2]}'))
    arr2=("${arr2[@]:1}")
    mon_sent=$( IFS=$' '; echo "${arr1[*]}" ) # mongolian sentence
    mon_sent=$(echo $mon_sent | sed 's/^\///;s/\// /g')
    eng_sent=$( IFS=$' '; echo "${arr2[*]}" ) # english sentence
    if [ -z "$eng_sent" ]
    then
      echo "processing at line number $i"
      while true; do
        eng_result=$(torify trans -brief "$mon_sent")
        if [ -z "$eng_result" ]
        then
          # try another node, the default restarting limit is to allow 5 restarts in a 10sec period.
          sleep 3; sudo service tor restart
        else
          translated_pair="$mon_sent +++++SEP+++++ $eng_result"
          sed -i "${i}s/.*/$translated_pair/" $1
          echo "translation result at line $i :"
          echo $translated_pair
          break
        fi
      done
    else
      echo "sentence at line number $i is already translated, so skipped"
    fi
    ((i++))
  done

