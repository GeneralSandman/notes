#include "head1.h"

#include <vector>

std::vector<int> getArray(int n)
{
    std::vector<int> res;
    for (int i = 0; i < n; i++)
        res.push_back(i);
    return res;
}