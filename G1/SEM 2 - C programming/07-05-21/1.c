#include <stdio.h>

int main(){
    char c = 125;
    for(int i = 0; i < 10; i++){
        c += 1;
        printf("%d\n", c);
    }
    return 0;
}