.PHONY: all test zip
all: sortsmodule.c
	gcc -I/usr/include/python2.7/ -fPIC -O3 -c -o sortsmodule.o sortsmodule.c
	gcc -shared sortsmodule.o -L/usr/local/lib -o sorts.so
test: test.c sortsmodule.c
	gcc -g -I/usr/include/python2.7/ -o test test.c sortsmodule.c
