#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *next;
} Node;


int node_create(Node **head, int data) {
  Node *n;
  if (!(n = (Node *)malloc(sizeof(Node)))) {
    return 1;
  }

  n->data = data;
  n->next = NULL;

  *head = n;
  return 0;
}

int node_append(Node *head, int data) {
  Node *n, *tmp;
  if (node_create(&n, data)) {
    return 1;
  }

  tmp = head;
  while (tmp->next != NULL) {
    tmp = tmp->next;
  }

  tmp->next = n;

  return 0;
}

int node_print(Node *head) {
  Node *n;
  n = head;
  while (n != NULL) {
    printf("el=%d\n", n->data);
    n = n->next;
  }
}


int circular(Node *head, Node **start) {
  Node *rn1;
  Node *rn2;
  int i1 = -1, i2 = -1, i = 0;
  int circular_length;

  rn1 = head;
  rn2 = head;
  while (rn1 != NULL && rn2 != NULL) {
    rn1 = rn1->next;
    rn2 = rn2->next->next;
    i++;
    if (rn1 == rn2) {
      if (i1 == -1) {
        i1 = i;
      } else {
        i2 = i;
        break;
      }
    }
  }

  circular_length = i2 - i1;
  for (i1++; i1 <= i2; i1++) {
    rn1 = head;
    rn2 = head;

    i = 0;
    while (i++ < i1) {
      rn2 = rn2->next;
    }

    i = 0;
    while (i++ < i1 - circular_length) {
      rn1 = rn1->next;
    }

    if (rn1 == rn2) {
      *start = rn1;
      break;
    }
  }
}

int main(int argc, char *argv[]) {
  Node *head;
  Node *start;
  node_create(&head, 1);
  node_append(head, 2);
  node_append(head, 3);
  node_append(head, 4);
  node_append(head, 5);

  head->next->next->next->next->next = head->next->next->next->next;

  circular(head, &start);
  printf("circular start is %d\n", start->data);

  return 0;
}
/*
4. STEP=1とSTEP=i1+1で1回イテレートする。出会えばそこが始点。
5. STEP=1とSTEP=i1+2で1回イテレートする。出会えばそこが始点。。。というのを出会うまでSTEP=i2まで繰り返す。
*/
