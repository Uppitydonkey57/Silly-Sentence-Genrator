while :
do
sentence=`python3 main.py`

rm Output.txt
touch Output.txt

echo $sentence >> Output.txt
echo $sentence

espeak -s 140 -g 12  < Output.txt
done
