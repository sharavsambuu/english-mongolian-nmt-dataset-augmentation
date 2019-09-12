#!/bin/bash

mkdir -p 1m_sentences_parts
split -l 250000 ./sampled_million_uniq_sentences.txt ./1m_sentences_parts/sampled_million_part.txt


