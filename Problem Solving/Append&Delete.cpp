#include <iostream>
#include <string>
#include <cmath>

std::string text_transformation(std::string word1, std::string word2, int operations){
    int length1 = word1.length();
    int length2 = word2.length();
    int index = 0;
    int required_operations = 0;
    auto mispair = std::mismatch(word1.begin(), word1.end(), word2.begin(), word2.end(), [&](char a, char b){
        index++;
        return(a==b);
    });
    //std::cout<<index<<std::endl;
    required_operations = abs(index - length1) + abs(index - length2);
    //std::cout<<required_operations<<std::endl;
    if(required_operations == operations){
        return "Yes";
    }else if ((required_operations < operations) && ((((required_operations-operations)%2)==0) || (abs(required_operations-operations)>=2*std::min(length1,index)))){
        return "Yes";
    }else{
        return "No";
    }
}

int main(){

    std::string word1;
    std::string word2;
    int operations;
    std::string result;
    std::cin >> word1 >> word2 >> operations;
    
    result = text_transformation(word1, word2, operations);
    std::cout<<result<<std::endl;

    return 0;
}