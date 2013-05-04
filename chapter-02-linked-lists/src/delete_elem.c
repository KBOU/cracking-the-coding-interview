#include <stdio.h>
#include <stdlib.h>


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
  Node *tmp, *n;
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

int node_delete_elem(Node *elem) {
  Node *next;
  next = elem->next;
  elem->data = next->data;
  elem->next = next->next;
  free(next);
}

int node_print(Node *head) {
  Node *tmp;
  tmp = head;
  
  while (tmp != NULL) {
    printf("e=%d\n", tmp->data);
    tmp = tmp->next;
  }
}

int main(int argc, char *argv[]) {
  Node *head;
  node_create(&head, 3);
  node_append(head, 2);
  node_append(head, 4);
  node_append(head, 5);

  printf("BEFORE\n");
  node_print(head);

  node_delete_elem(head->next->next);

  printf("AFTER\n");
  node_print(head);

  return 0;
}
