/**
 * @author: DevHeadTech
 * 
 * Advent of Code - Day 02
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <errno.h>
#include <math.h>

#define LOSE    0
#define TIE     3
#define WIN     6

#define NORM_MOVE      64
#define NORM_ROUND     89

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
    int outcome = 0;
    // Scissors, Rock, Paper
    int move[] = {3,1,2};

    while (NULL != fgets(buf, 16, file))
    {   // scanf doesn't clear the whole int
        opp_move = 0;
        outcome = 0;
        if (EOF != sscanf(buf, "%c %c", &opp_move, &outcome))
        {   // normalize
            outcome -= NORM_ROUND;
            opp_move -= NORM_MOVE;
            opp_score += opp_move;
            my_move = move[(opp_move+outcome)%3];
            my_score += my_move;

            if (0 == outcome)
            {   // tie
                my_score += 3;
                opp_score += 3;
            }
            else if(-1 == outcome)
            {   // lose
                opp_score += 6;
            }
            else
            {   // win
                my_score += 6;
            }

            //printf("opp: %d my: %d\n", opp_move, my_move);
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

