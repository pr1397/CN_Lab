#include<iostream>
#include<time.h>
using namespace std;
const int QS= 10;
const int MaxPackets= 20;
const double minP=0.3,maxP =0.7;
double rand_double(double min, double max){
    return min +(max - min) * (double)rand() /(RAND_MAX-1);
}

int main()
{
    srand(time(0));
    int qs = 0;
    double dp = minP;
    for (int i = 0; i < MaxPackets; i++){
        if (qs == QS){
            cout<<"\nDropped.Queue Full";
            dp = minP;
        }
        else if (rand_double(0,1) < dp){
            cout<<"\nDropped.Random";
            dp += (maxP-minP)/(MaxPackets-1);
        }
        else {
            cout<<"\nAccepted";
            dp = minP;
            qs++;
        }
    }
    return 0;
}