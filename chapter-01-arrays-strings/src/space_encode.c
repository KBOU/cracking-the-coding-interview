#include <stdio.h>

int convert_space(char *str) {
  char *non_space_end, *start;
  start = str;
  while (*str != '\0') {
    if (*str != ' ') {
      non_space_end = str;
    }
    str++;
  }
  str--;

  while (str >= start) {
    if (*non_space_end != ' ') {
      *str-- = *non_space_end--;
    } else {
      *str-- = '0';
      *str-- = '2';
      *str-- = '%';
      non_space_end--;
    }
  }
}

int main(int argc, char *argv[]) {
  char str[] = "Hello Wolrd and Japan!      ";
  convert_space(str);
  printf("%s\n", str);
  return 0;
}
