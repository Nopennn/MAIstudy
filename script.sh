#!/bin/bash

suff=$(cat)


echo "Созданы синонимы этих файлов с двумя и более связями с суффиксом $suff:"

ls -o | awk '{if ($2 > 1) print $8}' | grep "$suff"

ls -o | awk '{if ($2 > 1) print $8}' | grep "$suff" | awk -F "." '{OFS = ""; print $2,$1}' | xargs touch

