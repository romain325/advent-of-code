#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

  int cnt = 0;
  int val, previous;
  FILE *f = fopen("./input1", "r");

  fscanf(f, "%d", &previous);
  while(fscanf(f, "%d", &val) == 1){
    if(val > previous) { cnt++; }
    previous = val;
  }

  printf("CNT1: %d", cnt);

  // reset file pos
  fseek(f, 0, SEEK_SET);
  unsigned int arr[2048];
  int length = 0;

  while (fscanf(f, "%d", &val) == 1) {
    arr[length++] = val;
  }

    cnt = 0;
    for (int i = 1; i < length - 2; i++) {
      int prev = arr[i - 1] + arr[i] + arr[i + 1];
      int curr = arr[i] + arr[i + 1] + arr[i + 2];

      if (curr > prev) {
        cnt++;
      }
    }

    printf("\nCNT2: %d", cnt);
  

}
