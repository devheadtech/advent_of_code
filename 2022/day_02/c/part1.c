/**
 * @author: DevHeadTech
 * 
 * Advent of Code - Day 02
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <errno.h>

#define NORM_A     64
#define NORM_X     87

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
    int opp_move = 0;
    int my_move = 0;
    char buf[16] = {0};
    uint opp_score = 0;
    uint my_score = 0;

    while (NULL != fgets(buf, 16, file))
    {
        if (EOF != sscanf(buf, "%c %c", &opp_move, &my_move))
        {   // normalize
            opp_move -= NORM_A;
            opp_score += opp_move;

            my_move -= NORM_X;
            my_score += my_move;

            int delta = my_move - opp_move;

            if (0 == delta)
            {   // tie
                my_score += 3;
                opp_score += 3;
            }
            else if(-1 == delta || 2 == delta)
            {   // lost
                opp_score += 6;
            }
            else
            {   // won
                my_score += 6;
            }
        }
    } 

    printf("My Score: %d\n", my_score);
    printf("Opponent Score: %d\n", opp_score);

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

