#include <stdio.h>
int main(void)
{
    int a;
    int i = 1;
    int b = 10 * i + sizeof(--i) + 4 - (10 / i);
    printf("%d %d", b, sizeof(0));
    return 0;
}
