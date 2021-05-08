#include<string.h>
#include<stdio.h>

int main(){
    char s[6][30] = {"asd", "aaaa", "aab", "abba", "zzzzzz"};
    char temp[30];
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < i; j++){
            if(strcmp(s[j], s[j+1])){
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    for(int i = 0; i < 5; i++)
        printf("%s\n", s[i]);
    
    return 0;
}