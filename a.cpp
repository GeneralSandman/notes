#include <iostream>
#include <string>
#include <execinfo.h>

using namespace std;

class Basic
{
  protected:
    virtual void m_fF1(void)
    {
    }
    virtual void m_fF2(void)
    {
    }
    virtual void m_fF3(void)
    {
    }

  public:
    void f1() { m_fF1(); }
    void f2() { m_fF3(); }
    void f3() { m_fF3(); }
};

class Drive : public Basic
{
  protected:
    virtual void m_fF1(void)
    {
    }
    virtual void m_fF2(void)
    {
    }
    virtual void m_fF3(void)
    {
    }
};

int main()
{
    return 0;
}