#include <stdio.h>
#include <stdlib.h>

typedef int BOOL;
#define TRUE 1
#define FALSE 0

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

int node_print(Node *elem) {
  Node *tmp;
  tmp = elem;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }
  return 0;
}


BOOL node_is_palindrome(Node *head) {
  Node *reversed, *tmp, *rtmp;

  tmp = head;
  reversed = NULL;
  while (tmp != NULL) {
    if (reversed == NULL) {
      node_create(&reversed, tmp->data);
    } else {
      node_create(&rtmp, tmp->data);
      rtmp->next = reversed;
      reversed = rtmp;
    }
    tmp = tmp->next;
  }

  tmp = head;
  while (tmp != NULL) {
    if (tmp->data != reversed->data) {
      return FALSE;
    }
    tmp = tmp->next;
    reversed = reversed->next;
  }
  return TRUE;
}

int main(int argc, char *argv[]) {
  Node *head1, *head2;
  node_create(&head1, 1);
  node_append(head1, 2);
  node_append(head1, 4);
  node_append(head1, 2);
  node_append(head1, 1);
  printf("%d\n", node_is_palindrome(head1));

  node_create(&head2, 1);
  node_append(head2, 2);
  node_append(head2, 2);
  node_append(head2, 4);
  node_append(head2, 1);
  printf("%d\n", node_is_palindrome(head2));
  return 0;
}
