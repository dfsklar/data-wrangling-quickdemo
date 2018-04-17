/bin/rm -rf root
mkdir root
python build_left_side.py  > root/leftside.tab
python build_right_side.py < root/leftside.tab | sort | tr '\t' '\001' > root/rightside.txt
echo "cd into root to start"
