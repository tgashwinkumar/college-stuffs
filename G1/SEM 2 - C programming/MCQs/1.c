#include <stdio.h>
int main()
{
    int a;
    int b = 1;
    int x[5] = { 1, 2, 3, 4, 5 };
    a = 5 * 4 + x[--b] - (9 / b);
    printf("%d", a);
    return 0;
}
