// Mrigya Agarwal, Giuseppe Mendola, Christine Graff

#include <stdio.h>
#include <string.h>
#include <errno.h> 
//#include "gc.h"

int initialized = 0;

int input ()
{
	int n;
	scanf("%d", &n);
	return n;
}

int print_int_nl(int x){
	if ((x&3) == 0){
		int temp = x>>2;
		printf("%d\n",temp);
	}
	else{
		int temp = x>>2;
		if(temp == 0){
			printf("%s\n","False");
		}
		else{
			printf("%s\n","True");
		}
	}
	return 0;
}





typedef struct Entry{
	char *key;
	int value;
	struct Entry *next;
}Entry;

typedef struct Hashtable{
	int size;
	struct Entry **table;
}Hashtable;

Hashtable *createHt(int size){
	if(size<1){
		return NULL;
	}

	Hashtable *ht=NULL;
	int i;
//	if (!initialized) {
//		GC_INIT();
//		initialized = 1;
//	}
	ht=malloc(sizeof(Hashtable));
	ht->table=malloc(sizeof(Entry)* size);
	for(i=0; i<size;i++){
		ht->table[i]=NULL;
	}
	ht->size=size;
	return ht;
}

int hash(char *s,Hashtable *ht){
	int n = strlen(s);
	unsigned int h=ht->size;
	int i;
	for (i=0;i<n;i++){
		int c=s[i];
		if(i%2==0){
			c=c<<1;
		}
		if(i%3==0){
			c=c<<2;
		}
		h=h^c;
	}
	return h%ht->size;;
}

Entry *createEntry(char *key, int *value){
	Entry *entry;
//	if (!initialized) {
//		GC_INIT();
//		initialized = 1;
//	}
	if((entry=malloc(sizeof(Entry)))==NULL){
		return NULL;
	}
	entry->key=strdup(key);
	entry->value=*value;
	entry->next=NULL;
	return entry;
}

void htInsert(Hashtable *ht,char *key,int *value){
	Entry *entry =NULL;
	Entry *next=NULL;
	Entry *last=NULL;
	int index=hash(key,ht);
	next=ht->table[index];
	while (next!= NULL  && strcmp(key,next->key)!=0){
		last=next;
		next=next->next;
	}
	if (next!= NULL  && strcmp(key,next->key)==0){
		next->value = value;
	}
	else{
		entry=createEntry(key,value);
		if(next==ht->table[index]){
			entry->next=next;
			ht->table[index]=entry;
		}else if(next==NULL){
			last->next=entry;
		}else{
			entry->next=next;
			last->next=entry;
		}
	}
}
 //for envref call this func, with makeEnv

int htGet(Hashtable *ht,char *key){
	int index =hash(key,ht);

	Entry *entry = ht->table[index];
	while(entry!=NULL &&  strcmp(entry->key,key)!=0){
		entry=entry->next;
	}

	if(entry==NULL){
		return -1;
	} 
	else{
		return entry->value;
	}
}

int htHasKey(Hashtable *ht,char *key){
	int index =hash(key,ht);

	Entry *entry = ht->table[index];
	while(entry!=NULL &&  strcmp(entry->key,key)!=0){
		entry=entry->next;
	}

	if(entry==NULL){
		return 0;
	} 
	else{
		return 1;
	}
}

void htSetVal(Hashtable *ht,char *key,char *val){
	int index =hash(key,ht);

	Entry *entry = ht->table[index];
	while(entry!=NULL &&  strcmp(entry->key,key)!=0){
		entry=entry->next;
	}

	if(entry==NULL){
		return;
	} 
	else{
		 entry->value=val;
	}
}


// //Env functions
// // Hashtable* make_env(){
// //     return createHt(16);
// // }

// //closure
typedef struct function{
    void* func_ptr;
    Hashtable* free_vars;
}function;

// // function* make_closure(void* func_ptr,Hashtable* free_vars){

// //     function f= function GC_malloc(sizeof(function));
// //     f.func_ptr=func_ptr;
// //     f.free_vars=createHt(16);
// //     return f;
// // }


 function *make_closure(void* func_ptr,int size){
// 	if (!initialized) {
//		GC_INIT();
//		initialized = 1;
//	}
    function *f=(function *) malloc(sizeof( function));
    f->func_ptr=func_ptr;
    f->free_vars=createHt(size);
    return f;
}

int getFreeVar( function* func_ptr, char* var){
    return htGet(func_ptr->free_vars,var);
}

void insertFreeVar( function* func_ptr, char* var, int* value){
	htInsert(func_ptr->free_vars, var, value);
}

void* get_func_ptr( function f){
	return f.func_ptr;
} 

Hashtable* get_free_vars( function* func_ptr){
	return func_ptr->free_vars;
}

//to be defined

void closure_call(){

}


typedef struct list{
	int size;
	int *arrayptr;
}list;

//list functions
int* createList(int size){
	list *l =(list *) malloc(sizeof(list));
	int* a = (int *) malloc(sizeof(int) * size);
	int s=malloc(sizeof(int));
	s=size;
	l->size=s;
	l->arrayptr=a;
	return (int *) l;
}

void insertList(list *listptr,int position, int* element){
	if(position>=listptr->size){
		printf("%d\n", listptr->size);
		puts("list out of range");
	    puts(strerror(errno));
 	}
 	else{
 		int *ptr=listptr->arrayptr;
 		*(ptr+position)=*element;
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


void extendList(list *listptr, int element){
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
