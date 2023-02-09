#include<iostream>
#include<string.h>
using namespace std;
int crc (char* ip, char* op, char* poly, int mode){
    strcpy(op,ip);
    if (mode == 1){
        for (int i = 1; i < strlen(poly); i++)
            strcat(op,"0");
    }
    for (int i = 0; i < strlen(ip); i++){
        if (op[i] == '1'){
            for (int j = 0; j < strlen(poly); j++){
                if (op[i+j] == poly[j])
                    op[i+j] = '0';
                else 
                    op[i+j] = '1';
            }
        }
    }
    for (int i = 0; i < strlen(op); i++){
        if (op[i] == '1')
            return 1;
    }
    return 0;
}

int main()
{
    char ip[20],op[20],recv[20];
    char poly[] = "1001";
    cout<<"\nEnter string ";
    cin>>ip;
    crc(ip,op,poly,1);
    cout<<"\nTransmitted\n"<<ip<<op+strlen(ip);
    cout<<"\nEnter recieved\n";
    cin>>recv;
    if (crc(recv,op,poly,0) == 1)
        cout<<"Error";
    else
        cout<<"No Error";
    return 0;
}