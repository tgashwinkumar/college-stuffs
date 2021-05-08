#include<stdio.h>

int main(){
    int n = 4;
    int arr[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    
    printf("Matrix before conversion:\n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }

    printf("\n\nMatrix after conversion:\n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j < i) arr[i][j] = 0;
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}