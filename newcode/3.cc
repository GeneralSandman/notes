#include<iostream>
#include<vector>
#include<algorithm>

int main(){

    using namespace std;

    int m=0,n=0;
    cin>>m>>n;
    vector<int> res;
    res.reserve(m+n);

    for(int i=0;i<m+n;i++){
        int tmp;
        cin>>tmp;
        res.push_back(tmp);
    }


    sort(res.begin(),res.end());
    auto p=unique(res.begin(),res.end());
    res.erase(p,res.end());
    
    
    for(int i=0;i<res.size();i++){
        cout<<res[i];
        if(i<res.size()-1)
            cout<<" ";        
    }
    cout<<endl;

}