#include <stdio.h>
int main()
{
    int x;
    x = 5 < 8 ? 1 != 2 < 5 == 0 ? 10 : 20 : 30;
    printf("%d\n", 1 != 5 == 0);
    printf("%d\n", 2 < 5 == 0);
    printf("%d\n", 1 != 2 < 5);
    printf("Value of x:%d", x);
    return 0;
}
