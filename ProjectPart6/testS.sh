#!/bin/bash	
rm -rf result.txt
for file in ./tests/*
do
# if [-z $x]
# 	then 
# 	echo "hello"
echo $file
python compile.py $file >a.ll
t2=python $file
if [ -r a.ll ]
	then
	llc-mp-3.3 a.ll  -filetype=obj
	gcc -Wall -std=c99 -o ./a  ./a.o ./runtime/runtime.o -lgc
	echo $file
	if [ -r a ]
		then
		echo $file executed Right>>result.txt
		t1=./a
		./a >> result.txt
		else
		echo $file executed wrong>>result.txt
		echo python compile.py $file 2>>result.txt
	fi
	else
	echo $file executed wrong>>result.txt
	echo python compile.py $file 2>>result.txt
fi
echo \ >>result.txt
done
open result.txt