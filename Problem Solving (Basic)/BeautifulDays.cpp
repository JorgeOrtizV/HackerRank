/*
Given a range of days [i, j], obtain the diference between each day number and its inverse.
If the difference is evenly divisible by k, it is considered a beautiful day.

Determine how many beatiful days are on the range.

Sample input:

20 23 6   //-> i j k

Sample output:

2  // (20-2)/6 = 3 and (22-22)/6 = 0

*/

#include <string>
#include <iostream>
#include <cmath>

float num_inverser(int x){
    float inverse {0};
    while(x != 0){
        inverse = inverse*10 + (x%10);
        x /= 10;
    }
    return inverse;
}

int main(){
    int low_lim;
    int up_lim;
    int divider;
    float inverse;
    float calculation;
    int beatiful_days {0};
    std::cin >> low_lim;
    std::cin >> up_lim;
    std::cin >> divider;

    for(int i = low_lim; i<=up_lim; i++){
        inverse = num_inverser(i);
        calculation = (i-inverse);
        if(fmod(calculation, divider) == 0){
            beatiful_days++;
        }
    }
    std::cout << beatiful_days << std::endl;
}