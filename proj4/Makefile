.PHONY: all test zip clean
all: sorts.so
sortsmodule.o: sortsmodule.c
	gcc -I/usr/include/python2.7/ -fPIC -O3 -c -o sortsmodule.o sortsmodule.c
sorts.o: sorts.c
	gcc -fPIC -O3 -c -o sorts.o sorts.c
sorts.so: sortsmodule.o sorts.o
	gcc -shared sortsmodule.o sorts.o -o sorts.so
clean:
	rm -f *.o *.pyc *.so
