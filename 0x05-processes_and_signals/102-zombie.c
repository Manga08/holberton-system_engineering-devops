#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - Creates an infinite loop to make the program infinite.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
}
/**
 * main - Creates zombie(zmb) processes.
 */
int main(void)
{
	int ct;
	pid_t zmb;

	for (ct = 0; ct < 5; ct++)
	{
		zmb = fork();
		if (zmb == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", zmb);
	}

	infinite_while();
	return (0);
}
