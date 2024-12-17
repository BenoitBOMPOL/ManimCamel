#!/usr/bin/env bash
clear
rm outputs/*.png
rm outputs/*.mp4
rm -r manim_code/__pycache__
for animpy in manim_code/*.py
do
    baseanim=$(basename "$animpy" .py)
    manim -spqh --output_file ~/Desktop/VoyageurDesert/outputs/"$baseanim".png "$animpy" "$baseanim"
    manim -qh --output_file ~/Desktop/VoyageurDesert/outputs/"$baseanim".mp4 --frame_rate 60 "$animpy" "$baseanim"
done
vlc outputs/*.mp4
