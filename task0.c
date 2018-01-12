#include <api.h>
#include <stdlib.h>
#include "syn_std.h"
Message msg;
int main()
{
 int i, j,t;
 int valoresON[SYNTHETIC_ITERATIONS] = {60,60,60,120,180,60};
 int valoresOFF[SYNTHETIC_ITERATIONS] = {60,60,60,90,150,60};
 Echo("synthetic task 0 started.");
 Echo(itoa(GetTick()));
 for(i=0;i<SYNTHETIC_ITERATIONS;i++){
     for(t=0;t<valoresOFF[i];t++){
     }
     msg.length = 30;
     for(j=0;j<30;j++) msg.msg[j]=i;
     for(b=0;b<valoresON[i];b++){
         Send(&msg,task1);
     }
}
Echo(itoa(GetTick()));
Echo("synthetic task 0 finished.");
exit();
}
