#!/usr/bin/env bash
clear
rm outputs/*.png
rm outputs/*.mp4
for animpy in manim_code/*.py
do
    baseanim=$(basename "$animpy" .py)
    manim -qh --progress_bar none --output_file "$PWD"/outputs/"$baseanim".mp4 --frame_rate 60 "$animpy" "$baseanim"
done
clear

for filemp4 in outputs/*.mp4; do 
    ffmpeg -i "$filemp4" 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//; 
done | awk -F: '{ sec += ($1 * 3600) + ($2 * 60) + $3 } END { printf "Total: %02d:%02d:%06.3f\n", sec/3600, (sec%3600)/60, sec%60 }'
