.PHONY: all test zip clean
all: sorts.so
test: test.c sorts.c
	gcc -g sorts.c test.c -o test
sortsmodule.o: sortsmodule.c
	gcc -I/usr/include/python2.7/ -fPIC -O3 -c -o sortsmodule.o sortsmodule.c
sorts.o: sorts.c
	gcc -fPIC -O3 -c -o sorts.o sorts.c
sorts.so: sortsmodule.o sorts.o
	gcc -shared sortsmodule.o sorts.o -o sorts.so
clean:
	rm -f *.o *.pyc
zip:
	zip -r proj1.zip Makefile main.py sorts.c sortsmodule.c perm sorted runs.csv README
