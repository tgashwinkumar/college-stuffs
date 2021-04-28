#include<stdio.h>
#include<stdlib.h>

int main(){
    char ch;
    float total;
    int id = 1;
    printf("Enter value - 0: ");
    scanf(" %f", &total);
    do{
        float val;
        char dummy;
        op:
        printf("\n\nEnter the choice of operator ( + | - | * | / | = ): ");
        // printf("\n\n");
        scanf("\n%c", &ch);
        printf("\nEnter value - %d: ", id);
        scanf(" %f", &val);
        switch(ch){
            case '+':
                total += val;
                break;
            case '-':
                total -= val;
                break;
            case '*':
                total *= val;
                break;
            case '/':
                while(val == 0){
                    printf("\nERROR: ZeroDivisionError\nEnter value - %d: ", id);
                    scanf(" %f", &val);
                }
                total /= val;
                break;
            case '=':
                break;
            default:
                printf("\nInvalid Operator.");
                goto op;
        }
        id++;
    }while(ch != '=');
    printf("\n\nTotal: %.2f", total);
    return 0;
}