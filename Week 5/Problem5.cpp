#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> addRow(vector<vector<int>> mat, vector<int> row); 
vector<vector<int>> addColumn(vector<vector<int>> mat, vector<int> column); 
void display(vector<vector<int>> mat); 
vector<vector<int>> transpose(vector<vector<int>> mat); 

main()
{
    vector<vector<int>> matrix;
    matrix = addRow(matrix, {1, 2, 3});
    matrix = addRow(matrix, {4, 5, 6});
    matrix = addRow(matrix, {7, 8, 9});
    cout << "Original Matrix: " << endl;
    display(matrix);
    matrix = addColumn(matrix, {10, 11, 12});
    cout << endl << "Matrix after adding a column: " << endl;
    display(matrix);
    vector<vector<int>> transposedMatrix = transpose(matrix);
    cout << endl <<"Transposed Matrix: " << endl;
    display(transposedMatrix);
}

vector<vector<int>> addRow(vector<vector<int>> mat, vector<int> row)
{
    mat.push_back(row);
    return mat; 
}

vector<vector<int>> addColumn(vector<vector<int>> mat, vector<int> column) 
{
    if (mat.empty()) 
    { 
        for (int x = 0; x < column.size(); x++) 
        {
            mat.push_back({column[x]});
        }
    } 
    else 
    {
        for (int x = 0; x < mat.size(); x++) 
        {
            if (x < column.size()) 
            {
                mat[x].push_back(column[x]);
            } 
            else 
            {
                mat[x].push_back(0); 
            }
        }
    }
    return mat; 
}

void display(vector<vector<int>> mat) 
{
   for (int x = 0; x < mat.size(); x++) 
   {
        for (int y = 0; y < mat[x].size(); y++) 
        { 
            cout << mat[x][y] << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> transpose(vector<vector<int>> mat) 
{
    vector<vector<int>> transposed;
    int rows = mat.size();
    if (rows == 0) return transposed; 
    int cols = mat[0].size();

    for (int y = 0; y < cols; y++)
    {
        vector<int> newRow;
        for (int x = 0; x < rows; x++) {
            newRow.push_back(mat[x][y]);
        }
        transposed.push_back(newRow);
    }
    return transposed;
}
