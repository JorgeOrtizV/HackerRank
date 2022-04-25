#include <iostream>

long long min_cost(int black_items, int white_items, int bc, int wc, int z){
    if((wc+z)<bc)
        bc = wc+z;
    if((bc+z)<wc)
        wc = bc+z;
    return((long)black_items*bc)+((long)white_items*wc);
}

int main(){
    int black_items;
    int white_items;
    int bc;
    int wc;
    int z;
    int tests;
    long long result;
    std::cin>>tests;
    for(int i {0}; i<tests; i++){
        std::cin>>black_items>>white_items;
        std::cin>>bc>>wc>>z;
        result = min_cost(black_items, white_items, bc, wc, z);
        std::cout<<result<<std::endl;
    }
}