python compile.py ./test.py >./test.ll
llc-mp-3.3 ./test.ll  -filetype=obj -march=x86
#llc-mp-3.3 ./test.ll  -filetype=obj 
gcc -m32 -Wall -std=c99 -o ./test  ./test.o ./runtime/runtime.o -lgc
./test
#rm -r ./test.o
#rm -r ./test.ll
#rm -r ./test