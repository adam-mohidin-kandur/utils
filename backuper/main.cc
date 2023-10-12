#include <iostream>

#include "backuper.cc"


int main(int argc, char* argv[]) {
  Backuper backuper(argv[1]);

  backuper.backup();

  return 0;
}

