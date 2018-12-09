#include <iostream>
#include <vector>

using namespace std;

void fun2(vector<int> &nums);

vector<int> fun1()
{
    cout << "function fun1\n";

    vector<int> nums;
    for (int i = 0; i < 10; i++)
    {
        nums.push_back(i);
    }

    fun2(nums);

    return nums;
}

void fun2(vector<int> &nums)
{
    cout << "function fun2\n";
    for (int i = 0; i < nums.size(); i++)
    {
        nums[i] = nums[i] * nums[i];
    }
}

int main()
{

    vector<int> res = fun1();

    cout << "res: ";
    for (auto t : res)
        cout << t << " ";
    cout << endl;

    return 0;
}