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

int node_append_node(Node *head, Node *tail) {
  Node *tmp;
  tmp = head;
  while (tmp->next != NULL) {
    tmp = tmp->next;
  }

  tmp->next = tail;
  
  return 0;
}

int node_partition(Node **head, int x) {
  int data;
  Node *less, *greater, *start;

  start = *head;
  less = NULL;
  greater = NULL;

  while (start != NULL) {
    data = start->data;
    if (data < x) {
      if (less == NULL) {
        if (node_create(&less, data)) {
          return 1;
        }
      } else {
        node_append(less, data);
      }
    } else {
      if (greater == NULL) {
        if (node_create(&greater, data)) {
          return 1;
        }
      } else {
        node_append(greater, data);
      }
    }
    start = start->next;
  }

  node_append_node(less, greater);

  *head = less;
  return 0;
}

int node_print(Node *head) {
  Node *tmp;
  tmp = head;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }
  return 0;
}

int main(int argc, char *argv[]) {
  Node *head;
  node_create(&head, 3);

  node_append(head, 2);
  node_append(head, 5);
  node_append(head, 1);
  node_append(head, 4);
  node_append(head, 9);

  printf("BEFORE\n");
  node_print(head);

  node_partition(&head, 4);
  printf("\nAFTER\n");
  node_print(head);
  return 0;
}
