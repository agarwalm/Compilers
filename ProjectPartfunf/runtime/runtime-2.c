// Mrigya Agarwal, Giuseppe Mendola, Christine Graff

#include <stdio.h>
#include <string.h>
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

//Objects function and structs
typdef struct class_struct{
	char* name;
	Hashtable *attributes;
	Hashtable *methods;
	/*Hashtable *classes;*/
}class_struct;

typdef struct py_obj{
	char *name;
	class_struct* class;
}py_obj;

class_struct* create_class(char* name,Hashtable *attributes,Hashtable *methods/*,Hashtable *classes*/){
	class_struct* c=(class_struct *) malloc(sizeof(class_struct));
	c->name=name;
	c->attributes=attributes;
	c->methods=methods;
	/*maybe better for methods do hashtable with 
	*func_name key and func_ptr as value
	*/
	/*c->classes=classes*/
	return c
}

py_obj* create_object(char* name, class_struct class){
	py_obj* o=(py_obj*)malloc(sizeof(py_obj));
	o->name=name;
	o->class=class;
	return o;
}

class_struct* get_class(py_obj o){
	return o->class;

}
int has_attr(py_obj o, char* attr){
	return htHasKey(o->class->attributes,attr);
}
int get_attr(py_obj c, char* attr){
	return htGet(o->class->attributes,attr);
}
void set_attr(py_obj c, char* attr, int val){
	htSetVal(o->class->attributes,attr,val);
}

// //Hashmap implementation

// int main(int argc,char **argv){
// 	GC_INIT();
// 	void* p;
// 	function* f=make_closure(p,16);
// 	 char* x="envx";
// 	 char* y="envy";
// 	 char* z="envz";
// 	 insertFreeVar(f,x,1);
// 	insertFreeVar(f,y,2);
// 	 insertFreeVar(f,z,3);
// 	 int x1=getFreeVar(f,x);
// 	 int y1=getFreeVar(f,y);
// 	 int z1=getFreeVar(f,z);
// 	 printf("%d , %d , %d\n",x1,y1,z1);
// 	return 0;
// }

// int main( int argc, char **argv ) {
// 	GC_init();
 
// 	Hashtable *hashtable = createHt( 20 );
// 	htInsert(hashtable,"key11",1);
// 	htInsert(hashtable,"key21",2);
// 	htInsert(hashtable,"key31",3);
// 	htInsert(hashtable,"key41",4);
// 	htInsert(hashtable,"key51",5);

// 	printf("%d\n", htGet(hashtable, "key11"));
// 	printf("%d\n", htGet(hashtable, "key21"));
// 	printf("%d\n", htGet(hashtable, "key31"));
// 	printf("%d\n", htGet(hashtable, "key41"));
// 	printf("%d\n", htGet(hashtable, "key51"));
// 	printf("%d\n", htGet(hashtable, "key61"));


//  	int i;
//  	char dig;
//  	char str[6];
//  	for(i=0; i<40; i++){
//  		dig = (char)(((int)'0')+i);
//  		strcpy(str,"key");
//  		int len = strlen(str);
//         str[len] = dig;
//         str[len+1] = '\0';
// 		htInsert(hashtable,str,i);
// 	}

// 	//htDelete(hashtable, "k4");
//  	 for (i=0;i<41;i++){
//  		dig = (char)(((int)'0')+i);
//  		strcpy(str,"key");
//  		int len = strlen(str);
//         str[len] = dig;
//         str[len+1] = '\0';
// 		printf("%d\n", htGet(hashtable, str));
// 	}

 
// 	return 0;
// }

//int main(int argc,char **argv){return 0;}