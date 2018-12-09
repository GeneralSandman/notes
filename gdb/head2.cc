#include "head2.h"

#include <vector>

std::vector<int> doubleArray(std::vector<int> &nums)
{
    std::vector<int> res;

    for (auto t : nums)
    {
        res.push_back(t * 2);
    }

    return res;
}