# coding: utf-8

class Result
    def __init__(self, node, is_anc):
        self.node = node
        self.is_anc = is_anc

def common_anc(root, p, q):
    if root is None:
        return Result(None, False)
    if root is p and root is q:
        return Result(root, true)

    rx = common_anc(root.left, p, q)
    if rx.is_anc:
        return rx

    ry = common_anc(root.right, p, q)
    if ry.is_anc:
        return ry

    if rx.node is not None and ry.node is not None:
        return Result(root, True)
    elif root is p or root is q:
        is_anc = True if rx.node is not None or ry.node is not None else False
        return Result(root, is_anc)
    else:
        return Result(rx.node if rx.node is not None else ry.node, False)
