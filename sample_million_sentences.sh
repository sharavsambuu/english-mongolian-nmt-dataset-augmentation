#!/bin/bash

rm sampled_million_sentences.txt && touch sampled_million_sentences.txt

echo "sampling process beings..."

ls ./sentences_parts -I "mn_en_sentences_split.txtaa" | while read file; do
	filepath="./sentences_parts/$file"
	echo "sampling from $filepath ..."
	sort -R $filepath | head -n 20000 >> sampled_million_sentences.txt
done

echo "sampling is done."
