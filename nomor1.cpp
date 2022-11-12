#include <iostream>

using namespace std;

int main(){
    int N;
    cout << "Nilai N = ";
    cin >> N;

    int counter = 0;
    int number = 1;

    while(counter < N){
        if(number % 3 == 0 && number % 7 == 0){
            if(counter != N - 1){
                cout << "N, ";
            }else{
                cout << "N" ;
            }
            counter ++;
        }else if(number % 3 == 0 || number % 7 == 0){
            if(counter != N - 1){
                cout << number <<", ";
            }else{
                cout << number ;
            }
            counter ++;
        }
        number++;
    }


    return 0;
}