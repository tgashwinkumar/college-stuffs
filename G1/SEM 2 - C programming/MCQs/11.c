#include <stdio.h>
int main()
{
    int i = 3;
    printf("%d", (++i)++);
    return 0;
}


// In C/C++ the pre-increment (decrement) and the post-increment (decrement) operators require an L-value expression as operand. Providing an R-value or a const qualified variable results in compilation error.

// In the above program, the expression -i results in R-value which is operand of pre-increment operator. The pre-increment operator requires an L-value as operand, hence the compiler throws an error.



// The increment/decrement operators needs to update the operand after the sequence point, so they need an L-value. The unary operators such as -, +, won’t need L-value as operand. The expression -(++i) is valid.

// In C++ the rules are little complicated because of references. We can apply these pre/post increment (decrement) operators on references variables that are not qualified by const. References can also be returned from functions.