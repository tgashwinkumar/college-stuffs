#include<string.h>
#include<stdio.h>
#include<ctype.h>
int main(){
    char s[100];
    int vowels = 0, cons = 0;
    fgets(s, 100, stdin);
    for(int i = 0; i < strlen(s); i++){
        if(s[i] == 'a' || s[i] == 'A' || s[i] == 'e' || s[i] == 'E' || s[i] == 'i' || s[i] == 'I' || s[i] == 'o' || s[i] == 'O' || s[i] == 'u' || s[i] == 'U')
            vowels += 1;
        else if(isalpha(s[i]))
            cons += 1;
    }
    printf("\nVowels: %d\nConsonants: %d", vowels, cons);
    return 0;
}