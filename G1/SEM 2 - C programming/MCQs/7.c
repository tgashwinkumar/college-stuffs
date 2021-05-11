#include <stdio.h>
int main()
{
    unsigned int a = 0xffff;
    unsigned int k = ~a;
    printf("%d %d\n", a, k);
    return 0;
}
