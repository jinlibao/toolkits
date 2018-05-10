/**********************************************
 * student_scores.c
 * Libao Jin
 * Dec 28, 2015
 * imthomasking@gmail.com
 *
 * Copyright (c) 2015 Libao Jin
 * All rights reserved
 * MIT LICENSE
 **********************************************/

#include <stdio.h>

#define M 10
#define N 5

void avg_student(double student_scores[M][N], double averages_stu[N])
{
    /* double averages_stu[M]; */
    for(int i = 0; i < M; i++)
    {
        double tmp = 0;
        for(int j = 0; j < N; j++)
        {
            tmp += student_scores[i][j];
        }
        averages_stu[i] = tmp / N;
    }
}

void avg_course(double student_scores[M][N], double averages_course[M])
{
    /* double averages_course[N]; */
    for(int i = 0; i < N; i++)
    {
        double tmp = 0;
        for(int j = 0; j < M; j++)
        {
            tmp += student_scores[j][i];
        }
        averages_course[i] = tmp / M;
    }
}

int* max_score(double student_scores[M][N])
{
    int poss[2];
    int* pos;
    int max_i, max_j;
    double current_max = -1;
    for(int i = 0; i < M; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if(student_scores[i][j] > current_max)
            {
                current_max = student_scores[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }
    poss[0] = max_i;
    poss[1] = max_j;
    pos = poss;
    return pos;
}

void input_scores(double student_scores[M][N])
{
    for(int i = 0; i < M; i++)
    {
        for(int j = 0; j < N; j++)
        {
            scanf("%lf", *(student_scores + i) + j);
        }
    }
}

void print_scores(double student_scores[M][N])
{
    for(int i = 0; i < M; i++)
    {
        for(int j = 0; j < N; j++)
        {
            printf("%.2f ", student_scores[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void print_averages(double averages[], int n)
{
    for(int i = 0; i < n; i++)
    {
        {
            printf("%.2f ", averages[i]);
        }
    }
    printf("\n");
}

int main()
{
    double student_scores[M][N];
    double averages_stu[M];
    double averages_course[N];
    int* max_pos;
    input_scores(student_scores);
    /* print_scores(student_scores); */
    avg_student(student_scores, averages_stu);
    avg_course(student_scores, averages_course);
    printf("Average score for each student: ");
    print_averages(averages_stu, M);
    printf("Average score for each course: ");
    print_averages(averages_course, N);
    max_pos = max_score(student_scores);
    printf("The maximum is in the position (%d, %d)\n", max_pos[0] + 1, max_pos[1] + 1);
    return 0;
}
