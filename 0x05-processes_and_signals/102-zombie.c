#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define NUM_ZOMBIES 5

void create_zombie(void)
{
    pid_t pid;

    pid = fork();
    if (pid < 0)
    {
        perror("fork");
        exit(EXIT_FAILURE);
    }
    else if (pid == 0)
    {
        /* Child process */
        exit(EXIT_SUCCESS);
    }
    else
    {
        /* Parent process */
        printf("Zombie process created, PID: %d\n", pid);
    }
}

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    int i;

    for (i = 0; i < NUM_ZOMBIES; i++)
    {
        create_zombie();
    }

    infinite_while();

    return (0);
}
