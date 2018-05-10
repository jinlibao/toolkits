/**********************************************
 * sort_chars.c
 * Libao Jin
 * Dec 28, 2015
 * imthomasking@gmail.com
 *
 * Copyright (c) 2015 Libao Jin
 * All rights reserved
 * MIT LICENSE
 **********************************************/

#include <stdio.h>

#define N 10

void sort_chars(char* chars)
{
    for(int i = 0; i < N - 1; i++)
    {
        int min_index = i;
        for(int j = i; j < N; j++)
        {
            if(chars[min_index] > chars[j])
            {
                min_index = j;
            }
        }
        char tmp = chars[i];
        chars[i] = chars[min_index];
        chars[min_index] = tmp;
    }
}

void print_chars(char* chars)
{
    for(int i = 0; i < N; i++)
    {
        printf("%c", chars[i]);
    }
}

void input_chars(char* chars)
{
    for(int i = 0; i < N; i++)
    {
        scanf("%c", chars + i);
    }
}

int main()
{
    char chars[N];
    input_chars(chars);
    print_chars(chars);
    printf(" -> ");
    sort_chars(chars);
    print_chars(chars);
    printf("\n");
    return 0;
}
