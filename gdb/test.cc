#include <iostream>
#include <vector>

#include "head1.h"
#include "head2.h"

using namespace std;

void fun2(vector<int> &nums);

vector<int> fun1()
{
    vector<int> nums;
    for (int i = 0; i < 10; i++)
        nums.push_back(i);
    fun2(nums);
    return nums;
}

void fun2(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
        nums[i] *= 2;
}

int global = 0;

void addGlobal()
{
    cout << "invoke addGlobal function\n";
    global++;
}

int main()
{
    vector<int> res = fun1();
    for (auto t : res)
        cout << t << endl;
    cout << "\n-------------\n";

    vector<int> v1 = getArray(10);
    vector<int> v2 = doubleArray(v1);

    for (auto t : v2)
        cout << t << " ";

    cout << endl;

    cout << "times of invoke addGlobal():" << global << endl;

    return 0;
}