/*
 * File: 102-zombie.c
 * Auth: SALIM ABDESSAMAD
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - --
 *
 * Return: Always 0.
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
 * main - --
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pd;
	char add = 0;

	while (add < 5)
	{
		pd = fork();
		if (pd > 0)
		{
			printf("Zombie process created, PID: %d\n", pd);
			sleep(1);
			add++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
