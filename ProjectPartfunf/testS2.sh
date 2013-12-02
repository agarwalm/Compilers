#!/bin/bash	
gcc -c -m32 ./runtime/runtime-1.c -o ./runtime/runtime-1.o
rm -rf result.txt
for file in ./tests/*
do
# if [-z $x]
# 	then 
# 	echo "hello"
echo $file
python compile.py $file >a.ll
if [ -r a.ll ]
	then
	llc-mp-3.3 a.ll  -filetype=obj -march=x86
	gcc -m32 -Wall -std=c99 -o ./r.out  ./a.o ./runtime/runtime-1.o 
	echo $file
	if [ -r r.out ]
		then
		echo $file executed Right>>result.txt
		./a.out >> result.txt
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