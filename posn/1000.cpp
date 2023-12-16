#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {
    int l, n, temp, count = 0;
    string in;
    vector<string> words;
    cin >> l >> n;
    for(int i = 0; i < n; i++){
        cin >> in;
        words.push_back(in);
    }
    /*sort(numbers.begin(), numbers.end()); 
    countzero = count(numbers.begin(), numbers.end(), 0);
    temp = numbers[countzero];
    numbers[countzero] = numbers[0];
    numbers[0] = temp;*/
    cout << words.at(n);
    for (string s : words) {
        cout << s << "";
    }
    return 0;
}
