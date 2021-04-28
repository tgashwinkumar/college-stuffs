#include<stdio.h>
#include<stdlib.h>

int fact(int n){
    if(n == 1 || n== 0){
        return 1;
    }else{
        return n*fact(n-1);
    }
}

int combin(int n, int r){
    return fact(n)/(fact(n-r)*fact(r));
}

int main(){
    int n;
    // scanf("%d", &n);
    n = 5;
    for(int i = 0; i <= n; i++){
        for(int s = n; s >=i; s--){
            printf(" ");
        }
        for(int j = 0; j <= i; j++){
            printf("%d ", combin(i, j));
        }
        printf("\n");
    }

    return 0;
}