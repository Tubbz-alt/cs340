OBJ = binary_tree.o treesmodule.o

.PHONY: all clean test

all: trees.so
trees.so: $(OBJ)
	gcc -shared $^ -o $@
%.o: %.c
	gcc -I/usr/include/python2.7 -fPIC -O3 -c -o $@ $^
test: binary_tree.c test.c
	gcc -g binary_tree.c test.c -o test
clean:
	rm -f *.o *.so test
