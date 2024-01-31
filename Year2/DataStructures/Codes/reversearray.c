#include <stdio.h>
#include <stdlib.h>
int *reverse(int a[100], int n) {
    int *reversedArray = malloc(n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        reversedArray[n - i - 1] = a[i];
    }
    return reversedArray;
}
int main() {
    int a[100], i, n;
    printf("Enter the dimensions of the array: ");
    scanf("%d", &n);
    printf("Enter the elements in the array: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    // Using Pointers to print normal array//
    for (i = 0; i < n; i++) {
        printf("%p\t", (void *)&a[i]);
    }
    // Using Function//
    int *reversed = reverse(a, n);
    // Print the reversed array//
    for (i = 0; i < n; i++) {
        printf("%d\t", reversed[i]);
    }
    free(reversed);
    return 0;
}