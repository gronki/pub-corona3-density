F=''
find data/ -name \*.par | parallel --eta cat {} \| diskvert $F -o data/d/{/.}
find data/ -name \*.par | parallel --eta cat {} \| diskvert -compton -post $F -o data/x/{/.}
