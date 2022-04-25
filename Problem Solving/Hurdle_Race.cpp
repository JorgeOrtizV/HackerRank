#include <sstream>
#include <iostream>
#include <string>
#include <vector>

int main(){

    std::string constraints;
    std::string hurdles;
    std::vector <int> values;
    int k; // jumping natural ability
    int n; // number of values
    int number;
    int max_height {0};

    std::getline(std::cin, constraints);
    std::getline(std::cin, hurdles);

    // splitting data
    std::stringstream parameters {constraints};
    parameters >> n;
    parameters >> k;

    std::stringstream ss {hurdles};

    while(ss >> number){
        values.push_back(number);
        if(number>max_height){
            max_height=number;
        }
    }

    // Number of potions to drink

    int potions = max_height - k;
    if(potions < 0)
        potions=0;

    std::cout << potions << std::endl;


    return 0;
}