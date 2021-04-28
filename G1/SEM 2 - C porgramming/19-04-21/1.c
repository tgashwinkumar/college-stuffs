#include<stdio.h>
#include<string.h>
int main(){
    char s[100];
    int count = 1;
    fgets(s, 100, stdin);
    for(int i = 0; i < strlen(s); i++){
        if(s[i] == ' ') count += 1;
    }
    printf("\nThe no. of words is %d", count);
    return 0;
}