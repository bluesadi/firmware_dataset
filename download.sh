#!/bin/bash
cache_file=cache/$1.txt
download_dir=download/$1
crawler_script=scripts/crawler_$1.py

if [ ! -f $cache_file ]; then
    python $crawler_script
fi
# wget -q --show-progress -nc --no-check-certificate -i $cache_file -P $download_dir
