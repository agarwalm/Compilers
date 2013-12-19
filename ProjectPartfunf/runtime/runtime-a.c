// Mrigya Agarwal, Giuseppe Mendola, Christine Graff

#include <stdio.h>
#include <string.h>
//#include "gc.h"

//llc-mp-3.3 notpoop.ll -filetype=obj -march=x86
//gcc -m32 -c -o runtime.o ProjectPartfunf/runtime/runtime-a.c
//gcc -m32 -o main runtime.o notpoop.o

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

int bitwise_and(int l, int r){
	
	int right = r >> 2;
#printf("r: %d ",r);
	int left = l >> 2;
#printf("l: %d ",l);
	int solution = left & right;
#	printf("\n%d", l&3);
	if ((l&3) == 0 ){
		//printf("int!");
		printf("\nint: %d ",solution);
		return solution << 2;
		
	}
	
	else if ((r&3) == 0 ){
		//printf("int!");
		printf("\nint: %d ",solution);
		return solution << 2;
	}
	
	else
	{
		//printf("bool!");
		int temp = solution <<2;
		int temp2 = temp ^ 1;
		//printf("solution: %d ",temp2);
		printf("\nbool: %d ",temp2);
		return temp2;
		
		
	}
	
}

int tag_int(int i){
	
	return i<<2;
	
}

int tag_bool(int b){
	
	return (b<<2)^1;
	
	
}

int bitwise_or(int l, int r){
	
	int right = r >> 2;
	//printf("r: %d ",r);
	int left = l >> 2;
	//printf("l: %d ",l);
	int solution = right | left;
	
	if (l&3 == 0 | r&3 == 0) {
		//printf("int!");
		return solution << 2;
		
	}
	
	else
	{
		//printf("bool!");
		int temp = solution <<2;
		int temp2 = temp ^ 1;
		//printf("solution: %d ",temp2);
		return temp2;
		
		
	}
	
}

int bitwise_xor(int l, int r){
	
	int right = r >> 2;
	//printf("r: %d ",r);
	int left = l >> 2;
	//printf("l: %d ",l);
	int solution = right ^ left;
	
	if (l&3 == 0 | r&3 == 0) {
		//printf("int!");
		return solution << 2;
		
	}
	
	else
	{
		//printf("bool!");
		int temp = solution <<2;
		int temp2 = temp ^ 1;
		//printf("solution: %d ",temp2);
		return temp2;
		
		
	}
	
}

int logical_and(int l, int r){
	
	int right = r >> 2;
	//printf("r: %d ",r);
	int left = l >> 2;
	//printf("l: %d ",l);
	int solution = right && left;
	
	if (l&3 == 0 | r&3 == 0) {
		//printf("int!");
		return solution << 2;
		
	}
	
	else
	{
		//printf("bool!");
		int temp = solution <<2;
		int temp2 = temp ^ 1;
		//printf("solution: %d ",temp2);
		return temp2;
		
		
	}
	
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
		printf("%s: FOUND k = %s v = %d\n", __func__, key, entry->value);
		return entry->value;
	}
}



// //closure
typedef struct function{
    void* func_ptr;
    Hashtable* free_vars;
}function;




  int make_closure(void* func_ptr,int size){

    function *f=(function *) malloc(sizeof( function));
    f->func_ptr=func_ptr;
    f->free_vars=createHt(size);
	// return f;
	 
	printf("%s:%p\n", __func__, f);
    return (int)(((void *)f)+3);
}

int getFreeVar( function* func_ptr, char* var){
    return htGet(func_ptr->free_vars,var);
}

int insertFreeVar( int func_ptr, char* var, int* value){
	function *fptr = (function *)(func_ptr - 3);
	printf("%s:f = %p, k = %s, %d \n", __func__, fptr, var, *value);
	htInsert(fptr->free_vars, var, value);
	return 0;
}

void* get_func_ptr( function* f){
	// TODO : Fix me
//	func -= 3;
	printf("%s:%p\n", __func__, f);
	return f->func_ptr;
} 

void *get_func_ptr1(int f){
	function *f1 = (function *)(f - 3);
	return get_func_ptr(f1);
}

void exception(char *message)
{
	fputs(stderr, message);
	exit(-1);
}

Hashtable* get_free_vars( int func_ptr){
	function *fptr;
	if ((func_ptr & 3) != 3)
		exception("EXCEPTION: Trying to call non-function");
	fptr = (function *)(func_ptr - 3);
	return fptr->free_vars;
}

//to be defined

void closure_call(){

}

