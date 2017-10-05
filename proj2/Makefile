OBJ = trees.o treesmodule.o

.PHONY: all clean test

all: trees.so
trees.so: $(OBJ)
	gcc -shared $^ -o $@
%.o: %.c
	gcc -I/usr/include/python2.7 -fPIC -O3 -c -o $@ $^
test: trees.c test.c
	gcc -g trees.c test.c -o test
clean:
	rm -f *.o *.so test
zip:
	zip -r proj2.zip Makefile main.py trees.c trees.h treesmodule.c perm sorted README plots
