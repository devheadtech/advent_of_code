/**
 * @author: DevHeadTech
 * 
 * Advent of Code - Day 03
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <errno.h>
#include <stdint.h>

#define CAP_A   65
#define CAP_Z   90
#define LOW_A   97
#define LOW_Z   122

bool open_file(const char *path, FILE** file)
{
    errno = 0;
    *file = fopen(path,"r");

    if (NULL == *file || errno != 0 )
    {
        perror("fopen");
        return false;
    }

    return true;
}

uint8_t convert(char c)
{
    if (c >= LOW_A && c <= LOW_Z)
    {
        return (c - LOW_A + 1);
    }
    else if (c >= CAP_A && c <= CAP_Z)
    {
        return (c - CAP_A + 1 + 26);
    }
    printf("Bad Char\n");
    return 0;
}

uint8_t find_priority(char* buf, int len)
{
    if(len%2 != 0) 
        printf("Bad Input\n");

    char* lower = buf;
    char* upper = buf+(len/2);

    for(int i=0; i < len/2; i++)
    {
        for(int j=0; j < len/2; j++)
        {
            if(lower[i] == upper[j])
            {
                //printf("len: %d i: %d, j: %d, c: %c\n",len,i,j,lower[i]);
                return convert(lower[i]);
            }
        }
    }

    return 0;
}

void process_file(FILE* file)
{
    char buf[128] = {0};
    char c = 0;
    int sum = 0;

    while (NULL != fgets(buf, 128, file))
    {
        int len = strcspn(buf, "\n");
        sum += find_priority(buf, len);
    } 

    printf("Sum of Priorities: %d\n", sum);

}

int main(int argc, char** argv)
{
    FILE* file = NULL;

    // only one input allowed
    if (argc < 2 || argc > 2)
    {
        fprintf(stderr, "Bad Parameters\n");
        // todo: print usage
        return EXIT_FAILURE;
    }

    if (open_file(argv[1], &file))
    {
        process_file(file);
        fclose(file);
        return EXIT_SUCCESS;
    }

    return EXIT_FAILURE;
}

