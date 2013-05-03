#include <stdio.h>

int len(char *str) {
  int i = 0;
  while (str[i] != '\0') {
    i++;
  }
  return i;
}

void reverse(char *str) {
  char tmp;
  char *end;
  end = str;

  while (*end != '\0') {
    end++;
  }
  --end;


  while (str < end) {
    tmp = *str;
    *str++ = *end;
    *end-- = tmp;
  }

  printf("%s\n", str);
}

int main(int argc, char **argv) {
  char str[] = "hogehgoe";
  reverse(str);
}
