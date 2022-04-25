# This program receive a number n, which means the size of an array of positive unsigend integers it will receive.
# The goal is to obtain the maxium number and return how many times this number repeats.

# C++ implementation:
# Actually decided to submit C++ version, because of faster runtime. The comparison can be made element by elemente.
# In python we would need to read all the line, split it, make it int, run iterator max and then run iterator to count
# how many times this max number repeats itself

# #include <iostream>
#
# int n {0};
# int max {0};
# int temporary {0};
# int counter {0};
#
# int main (){
#     std::cin>>n;
#     for(int i {0}; i<n; i++){
#         std::cin>>temporary;
#         if(temporary>max){
#             max = temporary;
#             counter = 1;
#         }else if(temporary == max){
#             counter++;
#         }
#     }
#     std::cout<<counter<<std::endl;
#     return 0;
# }

# Python implementtion

n = int(input())
max_num = 0
numbers = input()
numbers = numbers.split(" ")
numbers = list(map(int, numbers))
max_num = max(numbers)
print(numbers.count(max_num))