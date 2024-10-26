#include <iostream>
#include <vector>
using namespace std;
void printVector(const vector<int> vec);
vector<int> removeDuplicates(vector<int> vec);

main() 
{
    vector<int> vec = {5, 3, 8, 1, 5, 9, 3, 2, 8, 4, 6, 7};

    cout << "Original vector: ";
    printVector(vec);

    for (int x = 0; x < vec.size() / 2; x++) 
    {
        int temp = vec[x];
        vec[x] = vec[vec.size() - 1 - x]; 
        vec[vec.size() - 1 - x] = temp; 
    }
    cout << "Reversed vector: ";
    printVector(vec);

    for (int x = 0; x < vec.size(); x++) 
    {
        for (int y = 0; y < vec.size() - 1; y++)
        {
            if (vec[y] > vec[y + 1]) 
            {
                if (vec[y] > vec[y + 1])
                {
                    int temp = vec[y];      
                    vec[y] = vec[y + 1];
                    vec[y + 1] = temp;    
                }
            }
        }
    }
    cout << "Sorted vector: ";
    printVector(vec);

    vec = removeDuplicates(vec); 
    cout << "Vector after removing duplicates: ";
    printVector(vec);


}
void printVector(const vector<int> vec) 
{
    for (int x = 0; x < vec.size(); x++) 
    {
        cout << vec[x] << " ";
    }
    cout << endl;
}
vector<int> removeDuplicates(vector<int> vec) 
{ 
    vector<int> uniqueVec;
    for (int x = 0; x < vec.size(); x++) 
    {
        if (uniqueVec.empty() || uniqueVec.back() != vec[x]) 
        {
            uniqueVec.push_back(vec[x]);
        }
    }
    return uniqueVec;
}