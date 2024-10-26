#include <iostream>
#include <vector>
#include <conio.h>
using namespace std;
void displaySize_Capacity(const vector<string> &vec);

main()
{
    vector<string> vec;
    int choice;
    string input;

    while (true)
    {
        system("cls");
        cout << "1. Add a string" << endl;
        cout << "2. Remove a string" << endl;
        cout << "3. Display size and capacity" << endl;
        cout << "4. Exit" << endl;
        cout << "Choose an option: ";
        cin >> choice;

        if (choice == 1)
        {
            cout << "Enter a string to add: ";
            cin.ignore();
            getline(cin, input);
            vec.push_back(input);
            displaySize_Capacity(vec);
            getch(); 
        }
        else if (choice == 2)
        {
            if (vec.empty())
            {
                cout << "Vector is empty. Cannot remove a string.";
                getch(); 
            }
            else
            {
                cout << "Enter index of the string to remove (0 to " << vec.size() - 1 << "): ";
                int index;
                cin >> index;
                if (index >= 0 && index < vec.size())
                {
                    vec.erase(vec.begin() + index);
                    cout << "String removed.";
                    getch(); 
                }
                else
                {
                    cout << "Invalid index.";
                    getch(); 
                }
                displaySize_Capacity(vec);
            }
        }
        else if (choice == 3)
        {
            displaySize_Capacity(vec);
            getch(); 
        }
        else if (choice == 4)
        {
            return 0;
        }
        else
        {
            cout << "Invalid choice." << endl;
            getch(); 
        }
    }
}
void displaySize_Capacity(const vector<string> &vec)
{
    cout << "Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
}
