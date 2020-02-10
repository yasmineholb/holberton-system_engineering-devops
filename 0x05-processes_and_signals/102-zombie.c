#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
/**
*infinite_while - fn infinite
*Return: int
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
*main - fn int
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
infinite_while();
}
}
}
