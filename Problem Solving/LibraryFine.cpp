#include <iostream>
#include <string>
#include <sstream>

int fine_calculator(int d1, int m1, int y1, int d2, int m2, int y2){
    if(y1 != y2)
        return 10000;
    else if(m1 != m2)
        return 500*(m2-m1);
    else
        return 15*(d2-d1);
}

int main(){
    int d1;
    int m1;
    int y1;
    int d2;
    int m2;
    int y2;
    int result;
    
    std::cin >> d2 >> m2 >> y2 >> d1 >> m1 >> y1;

    result = fine_calculator(d1, m1, y1, d2, m2, y2);
    std::cout<<result<<std::endl;

}