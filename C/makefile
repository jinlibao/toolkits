CC = gcc
CFLAGS = -g --std=c99 -Wall

ALLPROGS = merge_sort merge_sort_detailed permute hash_table

all: $(ALLPROGS)


hash_table: hash_table.o
	$(CC) $(CFLAGS) -o $@ $<

permute: permute.o
	$(CC) $(CFLAGS) -o $@ $<

merge_sort_detailed: merge_sort_detailed.o
	$(CC) $(CFLAGS) -o $@ $<

merge_sort: merge_sort.o
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -rf $(ALLPROGS:=.o) $(ALLPROGS:=.dSYM)

distclean: clean
	rm -rf $(ALLPROGS)
