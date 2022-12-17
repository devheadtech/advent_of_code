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

// a bit lazy coding
char elf1[128] = {0};
char elf2[128] = {0};
char elf3[128] = {0};
char* elf_buf[] = {elf1, elf2, elf3};

char* elf_grp[3] = {0};
int elf_cnt = 0;
int elf_len[3] = {0};

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

void clear_elfs(void)
{
    elf_cnt = 0;
    for(int i=0; i < 3; i++)
    {
        elf_len[i] = 0;
    }
}

void add_elf(char* buf, int len)
{
    elf_grp[0] = buf;
    elf_len[0] = len;
    elf_cnt++;

    for (int i=1; i < 3; i++)
    {
        if(elf_len[i-1] <= elf_len[i])
            return;
        
        // bubble up
        char* tmp = elf_grp[i];
        int ltmp = elf_len[i];
        elf_grp[i] = elf_grp[i-1];
        elf_len[i] = elf_len[i-1];
        elf_grp[i-1] = tmp;
        elf_len[i-1] = ltmp;
    }
}
    
uint8_t find_badge(char* buf, int len)
{
    char badge = 0;
    if(len%2 != 0) 
        printf("Bad Input\n");

    add_elf(buf, len);

    if(elf_cnt != 3)
        return 0;

    // Brute force - becuase... well why not
    for(int i=0; i < elf_len[0]; i++)
    { 
        for(int j=0; j < elf_len[1]; j++)
        {   // Found one match, see if its in the third
            if(elf_grp[0][i] == elf_grp[1][j])
            {
                for(int k=0; k < elf_len[2]; k++)
                {
                    if(elf_grp[0][i] == elf_grp[2][k])
                    {
                        badge = convert(elf_grp[0][i]);
                    }
                }
            }
        }
    }

    clear_elfs();
    return badge;
}

void process_file(FILE* file)
{
    char c = 0;
    int sum = 0;

    while (NULL != fgets(elf_buf[elf_cnt], 128, file))
    {
        int len = strcspn(elf_buf[elf_cnt], "\n");
        sum += find_badge(elf_buf[elf_cnt], len);
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

