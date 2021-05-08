#include<string.h>
#include<stdio.h>
#include<ctype.h>
int main(){
    char s[100];
    int alpha = 0, digit = 0, special = -1;
    fgets(s, 100, stdin);
    for(int i = 0; i < strlen(s); i++){
        if(isalpha(s[i])) alpha += 1;
        else if(isdigit(s[i])) digit += 1;
        else special += 1;
    }
    printf("\nTotal characters: %d\n\tAlphabet: %d\n\tDigits: %d\n\tSpecial characters: %d", strlen(s), alpha, digit, special);
    return 0;
}