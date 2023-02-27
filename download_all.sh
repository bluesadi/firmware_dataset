#!/bin/bash
VENDORS=(
    D-Link
    Linksys
    Netgear
    Zyxel
    TP-Link
    WD
    Tomato
)
for vendor in ${VENDORS[@]} 
do
    ./download.sh $vendor
done
