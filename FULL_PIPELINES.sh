cat rightside.txt | tr '\001' '\t' | sort -n -k2 > rightsideREADY.tab
cat leftside.tab | cut -f 2,3,6,4 | awk -f leftside_fix_precision.awk > leftsideREADY.tab
