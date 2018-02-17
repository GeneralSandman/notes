#include <iostream>
#include <string>
#include <execinfo.h>
#include <memory>
#include <vector>
#include <boost/ptr_container/ptr_vector.hpp>

using namespace std;

int constructor = 0;
int destructor = 0;

class A
{
public:
  A()
  {
    constructor++;
    std::cout << "constructor\n";
  }
  A(const A &a)
  {
    constructor++;
    std::cout << "constructor\n";
  }
  A &operator=(const A &a)
  {
    if (this == &a)
      return *this;
    constructor++;
    std::cout << "constructor\n";
    return *this;
  }
  ~A()
  {
    destructor++;
    cout << "destructor\n";
  }
};

int main()
{
  {
    boost::ptr_vector<string> vect;
    vect.reserve(50);
    int tmp = vect.capacity();
    for (int i = 0; i < 50; i++)
    {
      string *a = new string("li");
      vect.push_back(a);

      if (vect.capacity() != tmp)
      {
        std::cout << vect.capacity() << endl;
        tmp = vect.capacity();
      }
    }
  }

  cout << constructor << endl;
  cout << destructor << endl;
  return 0;
}