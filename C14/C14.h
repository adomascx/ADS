#include <iostream>
#include <iomanip>
#include <vector>
#include <ctime>

using namespace std;

struct Point {
    double x, y;
};

void randCoord(double &x)
{
    x = (double)rand() / RAND_MAX;
}

bool isInCircle(Point &point)
{
    return point.x * point.x + point.y * point.y <= 1;
}

void coordTest(Point *points, int n)
{
    for (int i = 0; i < n; i ++){
        cout << i << ". (" << points[i].x << "," << points[i].y << ")\n"; 
    }
}