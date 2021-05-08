#include<stdio.h>

void insert(int* arr, int len, int element, int index){
    if(index == -1) arr[len] = element;
    else {
        arr[len] = arr[len-1];
        for(int i = len - 1; i > index; i--){
            arr[i+1] = arr[i];
        }
        arr[index] = element;
    }
}

int main(){
    int arr[] = {0, 1, 2, 3, 5};
    printf("Array before inserting:\n");
    for(int i = 0; i < 5; i++)
        printf("%d\t", arr[i]);
    insert(arr, 5, 4, 3);
    printf("\n\nArray after inserting:\n");
    for(int i = 0; i < 6; i++)
        printf("%d\t", arr[i]);
    return 0;
}