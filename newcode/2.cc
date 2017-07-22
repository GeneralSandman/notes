#include <iostream>
#include <vector>
using namespace std;

int f(int number)
{
    int result = 0;
    int key = 10;

    while (number)
    {
        result += number % key;
        number /= key;
    }

    return result;
}

int g(int number)
{

    int result = 0;
    int key = 2;

    while (number)
    {
        result += number % key;
        number /= key;
    }

    return result;
}

int main()
{
    int result=0,n=0;
    cin>>n;
    for(int i=1;i<=n;i++){
        if(f(i)==g(i))
            result++;
    }

    cout<<result<<endl;
    return 0;
}