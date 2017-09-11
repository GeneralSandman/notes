#include <iostream>
#include <string>
#include <cstring>
#include <map>

typedef void *(*CreatFun)(void);
using namespace std;

class Factory
{
  private:
    map<string, CreatFun> m_nMap;
    Factory();

  public:
    void *getClassByName(string name)
    {
        map<string, CreatFun>::iterator p;
        p = m_nMap.find(name);
        if (p == m_nMap.end())
        {
            return nullptr;
        }
        else
        {
            return p->second();
        }
    }
    void registClass(string name, CreatFun f)
    {
        m_nMap.insert(pair<string, CreatFun>(name, f));
    }
    static Factory &getInstance()
    {
        static Factory factory;
        return factory;
    }
};

void * createInstance(void){
    
}

void regit(void *className)
{
    className * f
    CreatFun f
    Factory::getInstance().registClass(name, f);
}

class A{
    public:
    void print(){cout<<"class A\n";}
};

int main()
{
}