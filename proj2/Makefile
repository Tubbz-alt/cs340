.PHONY: all clean test
all: trees.o
trees.o: trees.c
	gcc -g -O3 trees.c -c -o trees.o
clean:
	rm -f *.o test
test: trees.c test.c
	gcc -g trees.c test.c -o test
