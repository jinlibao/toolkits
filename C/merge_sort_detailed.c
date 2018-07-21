/**
 * merge_sort_detailed.c
 * Implementation for merge sort (detailed).
 * Author: Libao Jin
 * Email: jinlibao@outlook.com
 * Date: 07/18/2018
 * Copyright (c) 2018 Libao Jin
 * All rights reserved
 */

#include <stdio.h>
#include <stdlib.h>
#define N 7

void merge_sort(int *nums, int numsSize);

int main(int argc, char* argv[])
{
    int nums[N] = {6, 3, 7, 2, 1, 5, 4};
    merge_sort(nums, N);

    for (int i = 0; i < N; printf(" %d", nums[i]), i++) {}
    printf("\n");

    return 0;
}

void merge_sort(int *nums, int numsSize)
{
    if (numsSize <= 1)
        return;

    // Split array into two halves, and sort each half respectively
    int l = numsSize / 2, r = numsSize - l, i = 0, j = 0, k = 0;
    int *snums = malloc(numsSize * sizeof(int));
    merge_sort(&nums[0], l);
    merge_sort(&nums[l], r);

    // Merge two halves

    // Original form
    /*
    while (k < numsSize)
        if (i < l)
            if (j < r)
                if (nums[i] < nums[l + j])
                    snums[k++] = nums[i++];
                else
                    snums[k++] = nums[l + j++];
            else
                snums[k++] = nums[i++];
        else
            snums[k++] = nums[l + j++];
    */

    // Simpler form
    /*
    while (i < l && j < r)
        snums[k++] = nums[i] < nums[l + j] ? nums[i++] : nums[l + j++];
    while (i < l && k < numsSize)
        snums[k++] = nums[i++];
    while (j < r && i + j < numsSize)
        snums[k++] = nums[l + j++];
    */

    // Simplest form
    while (k < numsSize)
        snums[k++] = (i < l && j < r && nums[i] < nums[l + j]) || (i < l && j >= r) ? nums[i++] : nums[l + j++];

    // Write the sorted array into the original array
    for (int i = 0; i < numsSize; nums[i] = snums[i], i++) {}
    free(snums);
}
