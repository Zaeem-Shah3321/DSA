#include <iostream>
#include <vector>
using namespace std;

main() 
{
    vector<int> vec = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    int target;
    cout << "Enter the integer to search for: ";
    cin >> target;
    bool flag = false;
    for (size_t x = 0; x < vec.size(); x++) 
    {
        if (vec[x] == target) 
        {
            cout << "Integer " << target << " found at index: " << x << endl;
            flag = true;
            break; 
        }
    }
    if (!flag) 
    {
        cout << "Integer " << target << " is not present in the vector." << endl;
    }
}
