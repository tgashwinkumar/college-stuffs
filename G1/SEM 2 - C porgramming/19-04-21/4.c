#include<string.h>
#include<stdio.h>

int indexOf(char str[], char c){
    for(int i = 0; i < strlen(str); i++){
        if(str[i] == c) return i;
    }
    return -1;
}

int main(){
    int count[100], index = 0, MAX = 0, maxid;
    char str[100] = "", s[100];
    fgets(s, 100, stdin);
    for(int i = 0; i < strlen(s); i++){
        int id = indexOf(str, s[i]);
        if(id == -1){
            str[index] = s[i];
            count[index] = 1;
            index += 1;
        }else{
            count[id] += 1;
        }
    }
    for(int i = 0; i <= index; i++){
        if(count[i] > MAX){
            MAX = count[i];
            maxid = i;
        }
    }
    printf("\nMaximum occuring character is %c", str[maxid]);
    return 0;
}