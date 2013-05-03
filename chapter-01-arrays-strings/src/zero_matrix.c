#include <stdio.h>

#define M 4
#define N 5

int prepare_mask(int matrix[M][N], int mask[M][N]) {
  int i, j;
  for (i = 0; i < M; i++) {
    for (j = 0; j < N; j++) {
      mask[i][j] = ~0;
    }
  }
  return 0;
}

int find_zero(int matrix[M][N], int mask[M][N]) {
  int i, j, ti, tj;
  for (i = 0; i < M; i++) {
    for (j = 0; j < N; j++) {
      if (matrix[i][j] == 0) {
        for (tj = 0; tj < N; tj++) {
          mask[i][tj] = 0;
        }
        for (ti = 0; ti < M; ti++) {
          mask[ti][j] = 0;
        }
      }
    }
  }
  return 0;
}

int set_mask(int matrix[M][N], int mask[M][N]) {
  int i, j;
  for (i = 0; i < M; i++) {
    for (j = 0; j < N; j++) {
      matrix[i][j] &= mask[i][j];
    }
  }
  return 0;
}

int print_matrix(int matrix[M][N]) {
  int i, j;
  for (i = 0; i < M; i++) {
    for (j = 0; j < N; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }
  return 0;
}


int main(int argc, char *argv[]) {
  int matrix[M][N] = {
    {3, 2, 1, 0, 4},
    {1, 0, 1, 0, 4},
    {1, 1, 3, 1, 3},
    {1, 1, 2, 3, 2}
  };

  int mask[M][N];
  prepare_mask(matrix, mask);
  find_zero(matrix, mask);

  printf("BEFORE\n");
  print_matrix(matrix);
  set_mask(matrix, mask);
  /*
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
    {1, 0, 3, 0, 3},
    {1, 0, 2, 0, 2}
  */
  printf("AFTER\n");
  print_matrix(matrix);
  return 0;
}

/*
2. MxN行列をいてレートし0の要素を探す。
3. 0の要素があった場合は、その要素の行、列のマスクを0にする。
4. 元の行列とマスクを&演算する。
*/
