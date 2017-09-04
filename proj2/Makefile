OBJ = trees.o treesmodule.o

.PHONY: all clean test

all: trees.so
trees.so: $(OBJ)
	gcc -shared $^ -o $@
%.o: %.c
	gcc -I/usr/include/python2.7 -fPIC -O3 -c -o $@ $^
test: trees.o test.c
	gcc -g trees.o test.c -o test
clean:
	rm -f *.o *.so test
