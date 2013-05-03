#include <stdio.h>
#include <string.h>

int compression(char *original, size_t org_len, char *compressed) {
  char *tmp, *tmp2, prev;
  int count = 0, i = 0;
  char buf[256];

  tmp = original;
  prev = '\0';
  while (*tmp != '\0') {
    if (prev == '\0') {
      prev = *tmp;
      count++;
      continue;
    }
    if (*tmp == prev) {
      count++;
    } else {
      compressed[i++] = prev;
      sprintf(buf, "%d", count);

      tmp2 = buf;
      while (*tmp2 != '\0') {
        compressed[i++] = *tmp2++;
      }
      count = 1;
      prev = *tmp;
    }
    tmp++;
  }

  compressed[i++] = prev;
  sprintf(buf, "%d", count);

  tmp2 = buf;
  while (*tmp2 != '\0') {
    compressed[i++] = *tmp2++;
  }

  compressed[i] = '\0';
  size_t len2 = strlen(compressed);
  if (len2 >= org_len) {
    strcpy(compressed, original);
  }
  return 0;
}

int main(int argc, char *argv[]) {
  char original[] = "abbbbbbbbbbbbbbbbbbbcde";
  size_t len = strlen(original);
  char compressed[len+1];
  compression(original, len, compressed);
  printf("%s\n", compressed);
  return 0;
}
