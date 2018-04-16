BEGIN {
    # Establish tab character as the field delimiter
    FS="\t"; OFS="\t"; 
}

# Next line is done for each input line
{ 
    $3 = int($3+0.5);
    $4 = int($4+0.5);
    print;
}
