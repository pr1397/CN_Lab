#include<iostream>
using namespace std;
const int rate = 50;
const int capacity = 100;
int main(){
    int tokens = 0;
    int i = 0;
    while(i<15){
        tokens+=rate;
        if (tokens > capacity)
            tokens = capacity;
        int tokens_needed = 60;
        if (tokens > tokens_needed){
            tokens-=tokens_needed;
            cout<<"\nPerformed Operation.Tokens left "<<tokens;
        }
        else{
            cout<<"\nNot enough tokens.Waiting";
            continue;
        }
        i+=3;
    }
    return 0;
}
