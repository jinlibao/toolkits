/**
 * merge_sort.c
 * Concise implementation for merge sort.
 * Author: Libao Jin
 * Email: jinlibao@outlook.com
 * Date: 07/18/2018
 * Copyright (c) 2018 Libao Jin
 * All rights reserved
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#define N 1000

void merge_sort(int *a, int n);

int main(int argc, char* argv[])
{
    int a[N] = {0};
    srand(time(0));
    for (int i = 0; i < N; a[i] = rand() % 1000, i++) {}
    printf("Original array: \n[");
    for (int i = 0; i < N; printf("%d, ", a[i++])) {} printf("\b\b]\n");
    merge_sort(a, N);
    printf("\nSorted array: \n[");
    for (int i = 0; i < N; printf("%d, ", a[i++])) {} printf("\b\b]\n");
    return 0;
}

void merge_sort(int *a, int n)
{
    if (n <= 1)
        return;
    int l = n / 2, r = n - l;
    merge_sort(a, l), merge_sort(a + l, r);
    int *sa = malloc(n * sizeof(int));
    for (int i = 0, j = 0, k = 0; k < n;)
        sa[k++] = (i < l && j < r && a[i] < a[l + j]) || (i < l && j >= r) ? a[i++] : a[l + j++];
    for (int i = 0; i < n; a[i] = sa[i], i++) {}
    free(sa);
}
