#include <stdio.h>
#include <stdlib.h>

int main(){
    char name[] = "Ashwin Kumar";
    fgets(name, sizeof(name), stdin);
    printf("Name: ");
    puts(name);
    printf("\n%d", sizeof(name));

    return 0;
}
