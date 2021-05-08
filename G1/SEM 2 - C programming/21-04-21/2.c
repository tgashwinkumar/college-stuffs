#include<stdio.h>
#include<string.h>

int f(int n){
    if(n <= 1) return 1;
    return n*f(n-1)
}

void main(){
    int n = 10;
    printf("%d", f(n));
}