#include<stdio.h>

void delete(int* arr, int len, int index){
    if(index == -1) return;
    else{
        for(int i = index; i < len; i++){
            arr[i] = arr[i+1];
        }
    }
}

int main(){
    int arr[] = {0, 1, 2, 3, 4};
    printf("Array before deleting:\n");
    for(int i = 0; i < 5; i++)
        printf("%d\t", arr[i]);
    delete(arr, 5, 2);
    printf("\n\nArray after deleting:\n");
    for(int i = 0; i < 4; i++)
        printf("%d\t", arr[i]);
    return 0;
}