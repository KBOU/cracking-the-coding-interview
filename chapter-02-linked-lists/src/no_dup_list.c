#include <stdlib.h>
#include <stdio.h>

typedef struct node {
  int data;
  struct node *next;
} Node;

int node_create(Node **elem, int data) {
  Node *n;

  if (!(n = (Node *)malloc(sizeof(Node)))) {
    return 1;
  }
  n->data = data;
  n->next = NULL;

  *elem = n;

  return 0;
}

int node_append(Node *head, int data) {
  Node *n, *next;
  node_create(&n, data);

  next = head;
  while (next->next != NULL) {
    next = next->next;
  }
  next->next = n;
  return 0;
}

int node_delete_all(Node **head) {
  Node *tmp;
  while (*head != NULL) {
    tmp = (*head)->next;
    free(*head);
    *head = tmp;
  }
}

int node_rm_dup(Node *head) {
  Node *tmp1, *tmp2, *prev;
  tmp1 = head;

  while (tmp1 != NULL) {
    tmp2 = tmp1->next;
    prev = tmp1;
    while (tmp2 != NULL) {
      printf("tmp1=%d tmp2=%d\n", tmp1->data, tmp2->data);
      if (tmp1->data == tmp2->data) {
        prev->next = tmp2->next;
        free(tmp2);
        tmp2 = prev;
      } else {
        prev = prev->next;
      }
      tmp2 = tmp2->next;
    }
    tmp1 = tmp1->next;
  }
}


int main(int argc, char *argv[]) {
  Node *head, *tmp;
  node_create(&head, 3);
  node_append(head, 1);
  node_append(head, 2);
  node_append(head, 4);
  node_append(head, 1);
  node_append(head, 1);
  node_append(head, 2);

  printf("BEFORE\n");
  tmp = head;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }

  node_rm_dup(head);

  printf("AFTER\n");
  tmp = head;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }

  node_delete_all(&head);
  if (head == NULL) {
    printf("delete succeeded\n");
  }

  return 0;
}
