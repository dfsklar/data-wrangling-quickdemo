python build_left_side.py > leftside.tab
python build_right_side.py < leftside.tab  | sort | tr '\t' '\001' > rightside.txt
