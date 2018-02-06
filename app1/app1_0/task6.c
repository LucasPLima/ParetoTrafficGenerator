#include <api.h>
#include <stdlib.h>
#include "syn_std.h"
Message msg;
int main()
{
	int i, j,t;
	Echo("synthetic task 6 started.");
	Echo(itoa(GetTick()));
for(i=0;i<SYNTHETIC_ITERATIONS;i++)
{
	msg.length = 30;
	for(j=0;j<30;j++) msg.msg[j]=i;
Receive(&msg,task3);
	for(t=0;t<1000;t++)
	{
	}
	Send(&msg,task7);
}
    Echo(itoa(GetTick()));
    Echo("synthetic task 6 finished.");
	exit();
}
