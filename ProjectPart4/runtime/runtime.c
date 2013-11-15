// Mrigya Agarwal, Giuseppe Mendola, Christine Graff

#include <stdio.h>
#include <string.h>
#include <gc.h>

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

//Hashmap implementation

typedef struct Entry{
	char *key;
	int *value;
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
	ht=GC_malloc(sizeof(Hashtable));
	ht->table=GC_malloc(sizeof(Entry)* size);
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
	if((entry=GC_malloc(sizeof(Entry)))==NULL){
		return NULL;
	}
	entry->key=strdup(key);
	entry->value=value;
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

int main( int argc, char **argv ) {
	GC_init();
 
	Hashtable *hashtable = createHt( 20 );
	htInsert(hashtable,"key11",1);
	htInsert(hashtable,"key21",2);
	htInsert(hashtable,"key31",3);
	htInsert(hashtable,"key41",4);
	htInsert(hashtable,"key51",5);

	printf("%d\n", htGet(hashtable, "key11"));
	printf("%d\n", htGet(hashtable, "key21"));
	printf("%d\n", htGet(hashtable, "key31"));
	printf("%d\n", htGet(hashtable, "key41"));
	printf("%d\n", htGet(hashtable, "key51"));
	printf("%d\n", htGet(hashtable, "key61"));


 	int i;
 	char dig;
 	char str[6];
 	for(i=0; i<40; i++){
 		dig = (char)(((int)'0')+i);
 		strcpy(str,"key");
 		int len = strlen(str);
        str[len] = dig;
        str[len+1] = '\0';
		htInsert(hashtable,str,i);
	}

	//htDelete(hashtable, "k4");
 	 for (i=0;i<41;i++){
 		dig = (char)(((int)'0')+i);
 		strcpy(str,"key");
 		int len = strlen(str);
        str[len] = dig;
        str[len+1] = '\0';
		printf("%d\n", htGet(hashtable, str));
	}

 
	return 0;
}
