#include <iostream>
using namespace std;
class circular_queue
{
private:
    int front, rear, size;
    int *arr;   
public:
    circular_queue(int s)
    {
        front = rear = -1;
        size = s;
        arr = new int[s];
    }
    void enQueue(int value);
    int deQueue();
    void displayQueue();
};     