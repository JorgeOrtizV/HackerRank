/*
Given the arrival time of a group of students, where if the arrival time is negative
or cero they are on time and if it is positive they are late.
And also given a threshold (required absences to cancel the class), determine if the 
class should be or not cancelled.

Input format:
2               // Test cases
4 3             // n k -> Number of students and k, cancellation threshold.
-1 -3 4 2       // Students arrival times
4 2
0 -1 2 1

*/

#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

std::string class_cancellation(std::vector <int> values, int thresh){
    int on_time;

    on_time = std::count_if(values.begin(), values.end(), [](int x){return x<=0;});
    
    if(on_time >= thresh){
        return "NO";
    }
    else{
        return "YES";
    }
}


int main(){

    int tests;
    int size;
    int thresh;
    int value;
    std::stringstream s;
    std::string values_str;
    std::vector <int> values;
    std::string result;

    std::cin>>tests;
    for(int i {0}; i<tests;i++){
        //std::fflush(stdin);
        std::cin>>size;
        std::cin>>thresh;
        std::fflush(stdin);
        std::cin.ignore();
        std::getline(std::cin, values_str);
        std::fflush(stdin);
        s << values_str;
        //std::cout<<s.str();
        while(s >> value){
            values.push_back(value);
        }
        s.clear();
        result = class_cancellation(values, thresh);
        std::cout << result << std::endl;
        values.clear();
    }

    return 0;
}