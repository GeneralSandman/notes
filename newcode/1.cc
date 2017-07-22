#include <iostream>
#include <vector>
using namespace std;

int count_(int number, int key)
{
    int result = 0;

    while (number)
    {
        result += number % key;
        number /= key;
    }

    return result;
}

int count(int number)
{
    int result = 0;

    for (int i = 2; i < number; i++)
    {
        result += count_(number, i);
    }

    return result;
}

int main()
{

    int number;

    while (cin >> number)
    {
        int result = count(number);
        cout << result << "/" << number - 2 << endl;
    }

    return 0;
}