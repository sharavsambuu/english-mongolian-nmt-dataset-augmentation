#!/bin/bash

# print sentences greater than 10 words
awk -v COUNT=10 'NF>COUNT' sentences.txt > filtered_sentences.txt
