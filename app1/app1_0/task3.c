#include <api.h>
#include <stdlib.h>
#include "syn_std.h"
Message msg;
int main()
{
	int i, j,t;
	Echo("synthetic task 3 started.");
	Echo(itoa(GetTick()));
for(i=0;i<SYNTHETIC_ITERATIONS;i++)
{
	msg.length = 30;
	for(j=0;j<30;j++) msg.msg[j]=i;
Receive(&msg,task0);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task4);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task5);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task6);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task7);
}
    Echo(itoa(GetTick()));
    Echo("synthetic task 3 finished.");
	exit();
}
