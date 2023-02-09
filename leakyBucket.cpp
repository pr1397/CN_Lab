#include <iostream>
using namespace std;
int main() {
    int rem,st = 0, ip =4,op=1,bs=10;
    for (int i = 0; i < 5; i++){
        rem = bs-st;
        if (ip <= rem)
            st+=ip;
        else
            cout<<"\nPacket Dropped\n";
        cout<<"\nBuffer Size "<< rem << " of bucket size "<<bs;
        st-=op;
    }
}