/**
 * @author: DevHeadTech
 * 
 * Advent of Code - Day 01
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <errno.h>

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

void process_file(FILE* file)
{
    int ret = 0;
    int val = 0;
    char buf[32] = {0};
    int water_mark = 0;
    int temp = 0;
    int cnt = 0;

    while (NULL != fgets(buf, 32, file))
    {
        ret = sscanf(buf, "%d", &val);
        if (ret == 0 || ret == EOF)
        {
            //printf("Elf #%d total: %d\n", ++cnt, temp);
            if (water_mark < temp)
            {
                water_mark = temp;
            }
            temp = 0;
        }
        else
        {
            temp+=val;
        }
    } 

    printf("Most Calories: %d\n", water_mark);

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

