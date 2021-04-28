#include<stdio.h>
#include<stdlib.h>

int main(){
    int dec, bin = 0, token = 1;
    // scanf("%d", &dec);
    dec = 5;
    while(dec > 0){
        bin += token*(dec % 2);
        token *= 10;
        dec = dec / 2;
    }
    printf("\n%d", bin);
    return 0;
}
