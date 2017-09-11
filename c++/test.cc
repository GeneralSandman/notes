#include <iostream>
#include <cstdlib>
#include <vector>
#include <memory>
#include <string>
#include <cstring>

using namespace std;

void replace(string &str, char textFrom, const char *textTo)
{
    int sLen = strlen(textTo);
    size_t p = str.find(textFrom);
    while (p != string::npos)
    {
        str = str.substr(0, p) + textTo + str.substr(p + 1);
        p = str.find(textFrom, p + sLen);
    }
}
int main(int argv, char *argc[])
{
    char res[]="++++++";
    string a="abcdefghijk";
    replace(a,'b',res);
    cout<<a<<endl;
    return 0;
}