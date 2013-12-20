#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h> 

typedef struct list{
	int size;
	int *arrayptr;
}list;

//list functions
list * createList(int size){
	list *l =(list *) malloc(sizeof(list));
	int* a = (int*)malloc(sizeof(int) * size);
	int s=malloc(sizeof(int));
	s=size;
	l->size=s;
	// l->size=size;
	l->arrayptr=a;
	return l;
}

void  insertList(list *listptr,int position, int element){
	if(position>=listptr->size){
		printf("%d\n", listptr->size);
		puts("list out of range");
	    puts(strerror(errno));
 	}
 	else{
 		int *ptr=listptr->arrayptr;
 		*(ptr+position)=element;
 	}
}
int getElementFromList(list *listptr,int position){
	if(position>=listptr->size){
		puts("list out of range");
	    puts(strerror(errno));
 	}else{
	return *(listptr->arrayptr+position);
	}
}


void appendList(list *listptr, int element){
	int size=listptr->size;
	int tempSize=malloc(sizeof(int));
	tempSize=size+1;
	int *tempPtr=(int *)malloc(sizeof(int)*tempSize);
	int i;
	int *ptr=listptr->arrayptr;
	for (i=0;i<size;i++){
		*(tempPtr+i)=*(ptr+i);
	}
	*(tempPtr+size)=element;
	listptr->size=tempSize;
	free(listptr->arrayptr);
	listptr->arrayptr=tempPtr;
}

int main(){
	list *ptr=createList(3);
	insertList(ptr,0,1);
	insertList(ptr,1,2);
	insertList(ptr,2,3);
	insertList(ptr,2,4);
	appendList(ptr,5);
	int i1=getElementFromList(ptr,0);
	int i2=getElementFromList(ptr,1);
	int i3=getElementFromList(ptr,2);
	int i4=getElementFromList(ptr,3);

	printf("%d\n" ,i1);
	printf("%d\n" ,i2);
	printf("%d\n" ,i3);
	printf("%d\n" ,i4);
	return 0;
}
