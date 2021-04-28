#include<stdio.h>
#include<string.h>

int main(){
    int n = 10;
    // scanf("%d\n", &n);
    char strings[20][20] = {"aab", "gaggg", "zzzzc", "xvxv", "aaaaa"}, temp[10];
    // for(int i = 0; i < n; i++)
    //     fgets(strings[i], 10, stdin);  
    for(int i = 0; i < n-1; i++){
        for(int j = 0; j < n-i-1; j++){
            if(strcmp(strings[j], strings[j+1]) > 0){
                strcpy(temp, strings[j]);
                strcpy(strings[j], strings[j+1]);
                strcpy(strings[j+1], temp);
            }
        }
    }
    for(int i = 0; i < n; i++)
        printf("%d %s\n", i+1, strings[i]);
    return 0;
}