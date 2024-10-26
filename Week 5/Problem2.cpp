#include <iostream>
#include <vector>
using namespace std;

main() 
{
    vector<int> vec;
    for (int x = 0; x < 100; x++) 
    {
        vec.push_back(x);
        cout << "Inserted: " << x ;
        cout << " | Size: " << vec.size() ;
        cout << " | Capacity: " << vec.capacity() ;
        cout << endl;
    }
}
