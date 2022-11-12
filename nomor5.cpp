#include <iostream>

using namespace std;

int main(){
    int N;
    cout << "Input Nilai N = ";
    cin >> N;

    if(N % 2 == 0){
        cout << "Harus bilangan ganjil\n";
    }else{
        if(N == 1){
            cout << "X";
        }else{
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(i == 0 || j==0 || j == N-1 || i == N-1){
                        cout << "X";
                    }else{
                        if(i + j == N - 1){
                            cout << "X";
                        }else{
                            cout << "O";
                        }
                    }
                }
                cout<<"\n";
            }
        }
    }

    return 0;
}