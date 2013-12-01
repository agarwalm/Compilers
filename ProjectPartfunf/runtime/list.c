
#include <stdlib.h>
#include "gc.h"

struct pair {
	void *car, *cdr;
};

struct pair *cons(void *car, void *cdr)
{
	struct pair *r = GC_MALLOC(sizeof(struct pair));
	r->car = car;
	r->cdr = cdr;

	return r;
}

typedef struct pair *list;

list reverse_aux(list l, list a)
{
	if (!l)
		return a;

	return reverse_aux((list)l->cdr, cons(l->car, a));
}

list reverse(list l)
{
	return reverse_aux(l, NULL);
}

typedef int *Int;

Int mkInt(int x)
{
	Int r = GC_MALLOC(sizeof(int));
	*r = x;
	return r;
}

int main()
{
	int n = 10000;
	int m = 100000;
	int i;
	list l = NULL;

	GC_INIT();

	for (i = 0; i < n; i++)
		l = cons(mkInt(i), l);

	for (i = 0; i < m; i++)
		l = reverse(l);

	return 0;
}
	
