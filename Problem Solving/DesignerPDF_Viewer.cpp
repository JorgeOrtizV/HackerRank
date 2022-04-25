/*
Having an array of length 26, where each element represents a letter form a to z
Given a word, calculate the area that a text box containing that word should have.

https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

Obtain the maximum height of a letter, and obtain the area by: max_height*width, where width is the number of letters.

Sample input:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample output:
9
*/

#include <iostream>
#include <string>
#include <sstream>

int max_height(int range, std::string word, int values[]){
    int index;
    int max {0};
    for(int i {0}; i<range; i++){
        index = (int)word[i]-97; // Obtain char index in values, based on ascii code. As a is 97 in ascii, it is maped to be 0 (index 0)
        if(values[index] > max)
            max=values[index];
    }
    return max;
}

int main(){

    std::string word;
    std::string value_str;
    int i {0};
    int values [26];
    int height;
    int width;
    int result;

    std::getline(std::cin, value_str);
    std::getline(std::cin, word);
    
    std::stringstream ss {value_str};

    while(ss >> values[i]){
        i++;
    }
    width = word.length();
    height = max_height(width, word, values);
    result = height*width;
    std::cout<<result;

    return 0;
}