#include<stdio.h>

void fun(int arr[]){
    // unsigned int n = sizeof(arr)/sizeof(arr[0]);
    unsigned int n = sizeof(arr);
    printf("\nArray size inside: %d", n);
}

int main(){
    int arr[] = {1, 2, 4, 564, 453, 3435, 345, 69, 453, 34534, 5, 345345,34 ,53};
    printf("Size of int: %d", sizeof(int*));
    // unsigned int n = sizeof(arr) / sizeof(arr[0]);
    unsigned int n = sizeof(arr);
    printf("\nArray size outside: %d", n);
    fun(arr);
    return 0;
}
    // char arr[] = "qwertyui";
// void fun(char arr[]){