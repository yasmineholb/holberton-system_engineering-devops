#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
/**
*main - fn
*Return: int
*/
int main(void)
{
int i;
for (i = 0; i < 5; i++)
{
if (fork() == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
exit(0);
}
}
int infinite_while(void);
}
