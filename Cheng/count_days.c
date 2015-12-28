/**********************************************
 * count_days.c
 * Libao Jin
 * Dec 28, 2015
 * imthomasking@gmail.com
 *
 * Copyright (c) 2015 Libao Jin
 * All rights reserved
 * MIT LICENSE
 **********************************************/

#include <stdio.h>

int is_leap(int year)
{
    if(year % 400 == 0)
    {
        return 1;
    }
    else if(year % 100 != 0 && year % 4 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int days_of_month(int year, int month)
{
    int days;
    switch(month)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            days = 31;
            break;
        case 2:
            {
                if(is_leap(year))
                {
                    days = 29;
                }
                else
                {
                    days = 28;
                }
            }
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            days = 30;
            break;
    }
    return days;
}

int count_days(int year, int month, int day)
{
    int all_days = 0;
    for(int i = 1; i < month; i++)
    {
        all_days += days_of_month(year, i);
    }

    all_days += day;
    return all_days;
}

int main()
{

    int year, month, day, all_days;
    scanf("%d%d%d", &year, &month, &day);
    all_days = count_days(year, month, day);
    printf("Date(YYYY/MM/DD): %d, %d, %d is the %d(th) day of year %d.\n", year, month, day, all_days, year);
    return 0;
}
