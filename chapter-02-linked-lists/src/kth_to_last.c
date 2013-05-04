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
  Node *tmp, *elem;
  if (node_create(&elem, data)) {
    return 1;
  }

  tmp = head;
  while (tmp->next != NULL) {
    tmp = tmp->next;
  }
  
  tmp->next = elem;
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

int get_data_at_kth_to_last(Node *head, int index, Node **elem) {
  Node *runner1, *runner2;
  int i = 0;
  runner1 = head;
  runner2 = head;
  while (runner1 != NULL) {
    runner1 = runner1->next;
    i++;
    if (i >= index) {
      break;
    }
  }

  if (i < index) {
    *elem = NULL;
    return 1;
  }

  while (runner1 != NULL) {
    runner1 = runner1->next;
    runner2 = runner2->next;
  }

  *elem = runner2;
  return 0;
}

int main(int argc, char *argv[]) {
  Node *head, *tmp, *elem;
  node_create(&head, 2);
  node_append(head, 3);
  node_append(head, 4);
  node_append(head, 6);
  node_append(head, 7);
  node_append(head, 8);
  node_append(head, 20);

  tmp = head;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }
  get_data_at_kth_to_last(head, 8, &elem);
  if (elem != NULL) {
    printf("kth to last=%d\n", elem->data);
  } else {
    printf("index out of linkedlist size\n");
  }

  node_delete_all(&head);

  if (head == NULL) {
    printf("delete succeeded\n");
  }
  return 0;
}
