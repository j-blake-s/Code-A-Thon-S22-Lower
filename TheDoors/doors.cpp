/* Copyright 2021
 * Vincent Kolb-Lugo
 * 9/5/21
 *
 * Locked Doors
 */
#include <iostream>
#include <vector>
#include <stdlib.h>
using std::cin;
using std::cout;
using std::endl;
using std::vector;

int main(int argc, char *argv[]) {
  // Get the number of doors/passes
  int n, passes, pass_count;
  char *arg1 = argv[1];
  char *arg2 = argv[2];
  n = atoi(arg1);
  passes = atoi(arg2);

  // vector doors represents the number of lockers in the hallway
  // lockers initialized to 0 for "closed"; 1 signals an "open" door
  vector<int> doors(n, 0);
  pass_count = 1;

  while (pass_count <= passes) {
    for (size_t i = 0; i < doors.size(); ++i) {
      if ((i+1) % pass_count == 0) {
        if (doors[i] == 1)
          doors[i] = 0;
        else
          doors[i] = 1;
      }
    }
    ++pass_count;
  }

  // display the number of open lockers and identify each locker
  // also display the number of closed lockers and identify each
  int open = 0;
  int closed = 0;
  for (size_t i =0; i < doors.size(); ++i) {
    if (doors[i] == 1)
      ++open;
    else
      ++closed;
  }
  cout << "Number of OPEN DOORS: " << open << endl;
  cout << "Opened doors: ";
  for (size_t i = 0; i < doors.size(); ++i) {
    if (doors[i] == 1)
      cout << (i + 1) << " ";
  }
  cout << endl;

  cout << "Number of CLOSED DOORS: " << closed << endl;
  cout << "Closed doors: ";
  for (size_t i = 0; i < doors.size(); ++i) {
    if (doors[i] == 1)
      cout << (i + 1) << " ";
  }
  cout << endl;

  return 0;
}
