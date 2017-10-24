#include<iostream>>
using namespace std;
int main()
{
int a=0,b=1,c,n=10;
cout<<b;
for(int i=1;i<=n;i++)

{
c=a+b;
a=b;
b=c;
cout<<c<<"\t"<<endl;
}
return 0;
}
