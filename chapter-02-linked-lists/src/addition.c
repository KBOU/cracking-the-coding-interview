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

int node_print(Node *elem) {
  Node *tmp;
  tmp = elem;
  while (tmp != NULL) {
    printf("elem=%d\n", tmp->data);
    tmp = tmp->next;
  }
  return 0;
}

int add(Node *x, Node *y, Node **res) {
  Node *tmp_x, *tmp_y, *carry, *carry2, *tmp_carry, *r;
  int n = 0;
  int diff = 0;
  node_create(&carry, 0);
  tmp_x = x;
  tmp_y = y;
  while (tmp_x != NULL || tmp_y != NULL) {
    if (tmp_x == NULL) {
      diff--;
    } else if (tmp_y == NULL) {
      diff++;
    }

    if (tmp_x != NULL) {
      tmp_x = tmp_x->next;
    }
    if (tmp_y != NULL) {
      tmp_y = tmp_y->next;
    }
    node_append(carry, 0);
  }


  tmp_x = x;
  tmp_y = y;
  while (diff > 0) {
    Node *tmp;
    node_create(&tmp, 0);
    tmp->next = tmp_y;
    tmp_y = tmp;
    diff--;
  }

  while (diff < 0) {
    Node *tmp;
    node_create(&tmp, 0);
    tmp->next = tmp_x;
    tmp_x = tmp;
    diff++;
  }

  tmp_carry = carry;
  r = tmp_x;
  *res = r;
  while (tmp_carry->next != NULL) {
    n = r->data + tmp_y->data;
    r->data = n % 10;

    if (n > 9) {
      tmp_carry->data = 1;
    }

    r = r->next;
    tmp_y = tmp_y->next;
    tmp_carry = tmp_carry->next;
  }

  while (is_carry_not_zero(carry)) {
    r = *res;
    tmp_carry = carry->next;
    carry2 = carry;
    while (tmp_carry != NULL) {
      n = r->data + tmp_carry->data;
      r->data = n % 10;
      if (n > 9) {
        carry2->data = 1;
      } else {
        carry2->data = 0;
      }
      r = r->next;
      tmp_carry = tmp_carry->next;
      carry2 = carry2->next;
    }
  }

  return 0;
}

int is_carry_not_zero(Node *carry) {
  Node *n;
  n = carry;
  while (n != NULL) {
    if (n->data != 0) {
      return 1;
    }
    n = n->next;
  }

  return 0;
}

int main(int argc, char *argv[]) {
  Node *x, *y, *res;
  // x = 3999
  // y = 123
  node_create(&x, 4);
  node_append(x, 8);
  node_append(x, 2);
  node_append(x, 3);

  node_create(&y, 9);
  node_append(y, 4);
  node_append(y, 5);

  add(x, y, &res);

  node_print(x);

  return 0;
}
