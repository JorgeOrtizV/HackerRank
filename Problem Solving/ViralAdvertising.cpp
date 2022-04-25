/*
An advertisement is shared to 5 people.
Each day floor(recipients/2) like the advertisement and will share it with 3 friends.

Determine how many people have liked the ad by the end of given day d.

Sample input:
d  // Day d
*/

#include <iostream>
#include <cmath>

int days_calculator(int day){
    int people {5};
    int likes = floor(people/2);  // 2
    int interactions {likes};  //2
    day--;
    while(day != 0){
        people = likes*3;  // 6
        likes = floor(people/2);
        interactions += likes; // 3->5
        //people = interactions * 3;
        day--;
    }
    return interactions;
}

int main(){
    int day;
    int interactions;
    std::cin >> day;
    interactions = days_calculator(day);
    std::cout<<interactions<<std::endl;
    return 0;
}