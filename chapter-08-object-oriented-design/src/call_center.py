#!/usr/bin/python
# coding: utf-8

import random

class Call:
  def __init__(self, val):
    self.val = val
  

""" Employee class
"""
class Employee:
    def __init__(self):
        self.next_employee = None

    def handle(self, call):
        if self.can_handle(call):
            self.do_handle(call)
        else:
            if self.next_employee is not None:
                self.next_employee.handle(call)

    def can_handle(self, call):
        pass

    def do_handle(self, call):
        pass

    def set_next(self, employee):
        self.next_employee = employee
        return employee


class Respondent(Employee):
    def do_handle(self, call):
        print 'Respondent handles %d' % call.val

    def can_handle(self, call):
        return True if call.val < 70 else False

class Manager(Employee):
    def do_handle(self, call):
        print 'Manager handles %d' % call.val

    def can_handle(self, call):
        return True if call.val < 90 else False

class Director(Employee):
    def do_handle(self, call):
        print 'Director handles %d' % call.val

    def can_handle(self, call):
        return True

if __name__ == '__main__':
    respondent = Respondent()
    manager = Manager()
    director = Director()
    respondent.set_next(manager).set_next(director)

    for i in range(0, 100):
        call = Call(random.randint(0, 100))
        respondent.handle(call)
