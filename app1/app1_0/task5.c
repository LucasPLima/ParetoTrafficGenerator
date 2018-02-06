#include <api.h>
#include <stdlib.h>
#include "syn_std.h"
Message msg;
int main()
{
	int i, j,t;
	Echo("synthetic task 5 started.");
	Echo(itoa(GetTick()));
for(i=0;i<SYNTHETIC_ITERATIONS;i++)
{
	msg.length = 30;
	for(j=0;j<30;j++) msg.msg[j]=i;
Receive(&msg,task0);
Receive(&msg,task1);
Receive(&msg,task2);
Receive(&msg,task3);
Receive(&msg,task4);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task8);
}
    Echo(itoa(GetTick()));
    Echo("synthetic task 5 finished.");
	exit();
}
