#include <stdio.h>
int main()
{
    int x, a = 0;
    x = sizeof(a++) ? printf("How are you") : 0;
    printf("Value of x:%d\n", x);
    printf("Value of a:%d", a);
    return 0;
}
