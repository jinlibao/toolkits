/**
 * permute.c
 * Permute a given array using recursion.
 * Author: Libao Jin
 * Email: jinlibao@outlook.com
 * Date: 07/19/2018
 * Copyright (c) 2018 Libao Jin
 * All rights reserved
 */

#include <stdio.h>
#include <stdlib.h>

int factorial(int n);
int** permute(int* nums, int numsSize, int* returnSize);

int main(int argc, char* argv[])
{
    int a[4] = {1, 2, 3, 4};
    int **sa, size;
    sa = permute(a, 4, &size);
    for (int i = 0; i < size; printf("\n"), i++)
        for (int j = 0; j < 4; printf("%d ", sa[i][j]), j++) {}
}

int factorial(int n)
{
    if (n == 0)
        return 1;
    return factorial(n - 1) * n;
}

int** permute(int* nums, int numsSize, int* returnSize)
{
    int **pnums;
    *returnSize = factorial(numsSize);
    pnums = malloc(*returnSize * sizeof(int*));

    if (numsSize == 0 || numsSize == 1)
    {
        pnums[0] = malloc(numsSize * sizeof(int));
        if (numsSize == 1)
            pnums[0][0] = nums[0];
    }
    else
    {
        for (int i = 0; i < numsSize; i++)
        {
            int **snums, subSize, *tnums = malloc((numsSize - 1) * sizeof(int));
            for (int j = 0, m = 0; j < numsSize; j++)
                if (j != i)
                    tnums[m++] = nums[j];
            snums = permute(tnums, numsSize - 1, &subSize);
            for (int j = 0; j < subSize; j++)
            {
                pnums[i * subSize + j] = malloc(numsSize * sizeof(int));
                pnums[i * subSize + j][0] = nums[i];
                for (int k = 0; k < numsSize - 1; k++)
                    pnums[i * subSize + j][k + 1] = snums[j][k];
                free(snums[j]);
            }
            free(tnums);
            free(snums);
        }
    }
    return pnums;
}
