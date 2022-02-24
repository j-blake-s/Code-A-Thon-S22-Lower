/**
 * Even Odd Sort
 * 
 * Brute force approach to sorting an integer array into a partioned
 * array of acsending even and odd numbers.
 */
 #include <algorithm>
 #include <iostream>
 #include <vector>
 #include <cstddef>
 #include <stdlib.h>
 using std::cin;
 using std::cout;
 using std::endl;
 using std:: vector;
 using std::size_t;

// sorts random integer array into a partioned array of acsending
// even then odd integers
vector<int> EOSort(vector<int> arr) {
  vector<int> return_array;
  vector<int> evens;
  vector<int> odds;

  for (size_t i = 0; i < arr.size(); ++i) {
    if (arr[i] % 2 == 0) evens.push_back(arr[i]);
    else odds.push_back(arr[i]);
  }
  for (size_t i = 0; i < evens.size(); ++i) {
    return_array.push_back(evens[i]);
  }
  for (size_t i =0; i < odds.size(); ++i) {
    return_array.push_back(odds[i]);
  }
  return return_array;
}

// generate random integers between a set value
int RandomIntGen(size_t size) {
  //const long HIGH = 10000;
  const long LOW = 10000;
  srand (time(NULL));
  int ret;
  ret = rand() % LOW + 1;
  return ret;
}


int main() {
  // write shit here
  vector<int> t1;
  int NUM = 100;
  for (size_t i = 0; i < NUM; ++i) {
    int rando;
    rando = RandomIntGen(500);
    t1.push_back(rando);
  }  

  // show that test populates
  for (size_t i = 0; i < t1.size();++i) 
    cout << t1[i] << endl;

  return 0;
}
