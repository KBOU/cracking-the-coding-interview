# coding: utf-8

import random

class Server(object):
    __instance = None
    __machines = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Server, cls).__new__(cls)
            cls.__machines = {}
        return cls.__instance

    @classmethod
    def get_new_pid(cls, person):
        return random.randint()
    @classmethod
    def get_machine(cls, fid):
        return cls.__machines.get(fid)


class Machine(object):
    def __init__(self):
        self.__persons = {}
        pass

    def get_friend(self, fid):
        return self.__persons.get(fid)


class Person(object):
    def __init__(self):
        self.pid = Server.get_new_pid(self)
        self.friend_ids = []

    def find(self, friend):
        for fid in friend_ids:
            machine = Server.get_machine(fid)
            frd = machine.get_friend(fid)
            if frd.pid == friend.pid:
                return f
        for f in friends:
            machine = Server.get_machine(fid)
            frd = machine.get_friend(fid)
            fn = frd.find(friend)
            if fn is not None:
                return fn

