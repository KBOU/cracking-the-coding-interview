#include <stdio.h>

int draw_horizontal(const unsigned char *arr, const unsigned int length, int w, int x1, int x2, int y) {
  int i, j;
  int width = w  / 8;
  int index = y * width;
  int x1_index = x1 + index * 8;
  int x2_index = x2 + index * 8;

  for (i = 0; i < length; i++) {
    unsigned char e = arr[i];
    for (j = 7; j >= 0; j--) {
      char sign = '*';

      int byte_index = i * 8 + 7 - j;
      if (byte_index >= x1_index && byte_index <= x2_index) {
        sign = '-';
      }
      printf("%c", sign);
    }

    if ((i % width) == width - 1) {
      printf("\n");
    }
  }
}

int main(int argc, char *argv[]) {
  unsigned char arr[] = {
    0, 0,
    0, 0
  };
  int length = sizeof arr / sizeof arr[0];
  draw_horizontal(arr, length, 16, 3, 8, 1);
  return 0;
}
