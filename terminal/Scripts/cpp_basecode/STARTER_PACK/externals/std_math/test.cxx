#include <math.h>
#include <iostream>
#include "test.hpp"

int some_really_hard_math(int x, int y)
{
    using std::cout;
    using std::endl;
    cout << pow(x, y) << endl;
    return pow(x,y);
}
