# if the file already exists or $1 is empty, exit.
if [[ -f "$1.py" || -z "$1" ]]; then
    exit
fi

touch $1.in
cp template/template.py $1.py

code $1.py $1.in