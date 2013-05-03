#include <stdio.h>

#define N 5

int rotation(int matrix[N][N]) {
  int i, j, i0, j0, i1, j1, i2, j2, i3, j3, tmp;

  for (i = 0; i < N / 2; i++) {
    for (j = i; j < N - i - 1; j++) {
      i0 = i;
      j0 = j;
      i3 = N - 1 - j0;
      j3 = i0;
      i2 = N - 1 - j3;
      j2 = i3;
      i1 = N - 1 - j2;
      j1 = i2;

      tmp = matrix[i0][j0];
      matrix[i0][j0] = matrix[i1][j1];
      matrix[i1][j1] = matrix[i2][j2];
      matrix[i2][j2] = matrix[i3][j3];
      matrix[i3][j3] = tmp;
    }
  }

}

int print_matrix(int matrix[N][N]) {
  int i, j;
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      printf("%2d ", matrix[i][j]);
    }
    printf("\n");
  }
}

int main(int argc, char *argv[]) {
  int matrix[N][N] = {
    {1, 2, 3, 4, 5},
    {6, 7, 8, 9, 10},
    {11, 12, 13, 14, 15},
    {16, 17, 18, 19, 20},
    {21, 22, 23, 24, 25}
  };
  printf("BEFORE\n");
  print_matrix(matrix);
  rotation(matrix);
  printf("\nAFTER\n");
  print_matrix(matrix);

  return 0;
}
