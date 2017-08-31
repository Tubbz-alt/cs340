.PHONY: all clean test
all: binary_tree.o
binary_tree.o: binary_tree.c
	gcc -g -O3 binary_tree.c -c -o binary_tree.o
clean:
	rm -f *.o test
test: binary_tree.c test.c
	gcc -g binary_tree.c test.c -o test
