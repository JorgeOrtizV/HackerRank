/*
Considering a tree has an initial height of 1, and it increases each height by double each spring and
1 m each summer. Given a number of cases t, identify which will be the final height of the tree after
all the given cycles.

https://www.hackerrank.com/challenges/utopian-tree/problem

Sample input:
3  // t
0  // N cycles test 1
1  // N cycles test 2
4

Sample output.
1   // Result test1
2
7
*/

#include <iostream>

void height_calculator(int cycles){
    int height {1};
    for(int i {1}; i<=cycles; i++){
        if(i%2 == 0){
            height += 1;
        }else{
            height *= 2;
        }
    }
    std::cout << height << std::endl;
}

int main(){
    int tests;
    int cycles;
    std::cin >> tests;

    for(int i {0}; i<tests; i++){
        std::cin>>cycles;
        height_calculator(cycles);
    }
}