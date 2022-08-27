VENDORS=(
    D-Link
    Linksys
    Netgear
    Zyxel
)
for vendor in ${VENDORS[@]} do
    ./download.sh $vendor
done