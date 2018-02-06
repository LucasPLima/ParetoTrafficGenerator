#include <api.h>
#include <stdlib.h>
#include "syn_std.h"
Message msg;
int main()
{
	int i, j,t;
	Echo("synthetic task 7 started.");
	Echo(itoa(GetTick()));
for(i=0;i<SYNTHETIC_ITERATIONS;i++)
{
	msg.length = 30;
	for(j=0;j<30;j++) msg.msg[j]=i;
Receive(&msg,task3);
Receive(&msg,task4);
Receive(&msg,task6);
Receive(&msg,task2);
}
    Echo(itoa(GetTick()));
    Echo("synthetic task 7 finished.");
	exit();
}
