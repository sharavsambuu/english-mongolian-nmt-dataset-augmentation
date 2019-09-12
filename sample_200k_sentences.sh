#!/bin/bash

rm sampled_200k_sentences.txt && touch sampled_200k_sentences.txt

echo "sampling process beings..."

ls ./sentences_parts -I "mn_en_sentences_split.txtaa" | while read file; do
	filepath="./sentences_parts/$file"
	echo "sampleing from $filepath ..."
	sort -R $filepath | head -n 4000 >> sampled_200k_sentences.txt
done

echo "sampling is done."
