#!/bin/bash	
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
	llc-mp-3.3 a.ll  -filetype=obj
	gcc a.o runtime.c 
	echo $file
	if [ -r a.out ]
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