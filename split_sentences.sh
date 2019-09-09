#!/bin/bash

mkdir -p sentences_parts
split -b 25M mn_en_sentences.txt ./sentences_parts/mn_en_sentences_split.txt


