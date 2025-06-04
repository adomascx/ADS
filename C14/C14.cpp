#include "C14.h"

int main(int argc, char *argv[])
{
    srand(time(NULL));

    // Taškų skaičiaus nuskaitymas
    int n;
    if (argc > 1)
    {
        n = atoi(argv[1]);
    }
    else
    {
        cout << "Enter the number of points: ";
        cin >> n;
    }

    // Sugeneruoti n atsitiktinių taškų koordinates
    vector<Point> points(n);
    for (int i = 0; i < n; i++)
    {
        randCoord(points[i].x);
        randCoord(points[i].y);
    }

    // coordTest(points.data(), n);

    // Rasti taškus, esančius apskritime
    int inCircleCnt = 0;
    for (int i = 0; i < n; i++)
    {
        if (isInCircle(points[i]))
            inCircleCnt++;
    }

    cout << "pi = " << 4 * ((double)inCircleCnt / n) << '\n';

    return 0;
}
