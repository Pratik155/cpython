"""Python abstract syntax node definitions

This file is automatically generated by Tools/compiler/astgen.py
"""
from consts import CO_VARARGS, CO_VARKEYWORDS

def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l

def flatten_nodes(seq):
    return [n for n in flatten(seq) if isinstance(n, Node)]

nodes = {}

class Node:
    """Abstract base class for ast nodes."""
    def getChildren(self):
        pass # implemented by subclasses
    def __iter__(self):
        for n in self.getChildren():
            yield n
    def asList(self): # for backwards compatibility
        return self.getChildren()
    def getChildNodes(self):
        pass # implemented by subclasses

class EmptyNode(Node):
    pass

class Expression(Node):
    # Expression is an artificial node class to support "eval"
    nodes["expression"] = "Expression"
    def __init__(self, node):
        self.node = node

    def getChildren(self):
        return self.node,

    def getChildNodes(self):
        return self.node,

    def __repr__(self):
        return "Expression(%s)" % (repr(self.node))

class Add(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Add((%s, %s))" % (repr(self.left), repr(self.right))

class And(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "And(%s)" % (repr(self.nodes),)

class AssAttr(Node):
    def __init__(self, expr, attrname, flags, lineno=None):
        self.expr = expr
        self.attrname = attrname
        self.flags = flags
        self.lineno = lineno

    def getChildren(self):
        return self.expr, self.attrname, self.flags

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "AssAttr(%s, %s, %s)" % (repr(self.expr), repr(self.attrname), repr(self.flags))

class AssList(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "AssList(%s)" % (repr(self.nodes),)

class AssName(Node):
    def __init__(self, name, flags, lineno=None):
        self.name = name
        self.flags = flags
        self.lineno = lineno

    def getChildren(self):
        return self.name, self.flags

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "AssName(%s, %s)" % (repr(self.name), repr(self.flags))

class AssTuple(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "AssTuple(%s)" % (repr(self.nodes),)

class Assert(Node):
    def __init__(self, test, fail, lineno=None):
        self.test = test
        self.fail = fail
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.test)
        children.append(self.fail)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.test)
        if self.fail is not None:
            nodelist.append(self.fail)
        return tuple(nodelist)

    def __repr__(self):
        return "Assert(%s, %s)" % (repr(self.test), repr(self.fail))

class Assign(Node):
    def __init__(self, nodes, expr, lineno=None):
        self.nodes = nodes
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.extend(flatten(self.nodes))
        children.append(self.expr)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        nodelist.append(self.expr)
        return tuple(nodelist)

    def __repr__(self):
        return "Assign(%s, %s)" % (repr(self.nodes), repr(self.expr))

class AugAssign(Node):
    def __init__(self, node, op, expr, lineno=None):
        self.node = node
        self.op = op
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.node, self.op, self.expr

    def getChildNodes(self):
        return self.node, self.expr

    def __repr__(self):
        return "AugAssign(%s, %s, %s)" % (repr(self.node), repr(self.op), repr(self.expr))

class Backquote(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Backquote(%s)" % (repr(self.expr),)

class Bitand(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Bitand(%s)" % (repr(self.nodes),)

class Bitor(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Bitor(%s)" % (repr(self.nodes),)

class Bitxor(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Bitxor(%s)" % (repr(self.nodes),)

class Break(Node):
    def __init__(self, lineno=None):
        self.lineno = lineno

    def getChildren(self):
        return ()

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Break()"

class CallFunc(Node):
    def __init__(self, node, args, star_args = None, dstar_args = None, lineno=None):
        self.node = node
        self.args = args
        self.star_args = star_args
        self.dstar_args = dstar_args
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.node)
        children.extend(flatten(self.args))
        children.append(self.star_args)
        children.append(self.dstar_args)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.node)
        nodelist.extend(flatten_nodes(self.args))
        if self.star_args is not None:
            nodelist.append(self.star_args)
        if self.dstar_args is not None:
            nodelist.append(self.dstar_args)
        return tuple(nodelist)

    def __repr__(self):
        return "CallFunc(%s, %s, %s, %s)" % (repr(self.node), repr(self.args), repr(self.star_args), repr(self.dstar_args))

class Class(Node):
    def __init__(self, name, bases, doc, code, lineno=None):
        self.name = name
        self.bases = bases
        self.doc = doc
        self.code = code
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.name)
        children.extend(flatten(self.bases))
        children.append(self.doc)
        children.append(self.code)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.bases))
        nodelist.append(self.code)
        return tuple(nodelist)

    def __repr__(self):
        return "Class(%s, %s, %s, %s)" % (repr(self.name), repr(self.bases), repr(self.doc), repr(self.code))

class Compare(Node):
    def __init__(self, expr, ops, lineno=None):
        self.expr = expr
        self.ops = ops
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.extend(flatten(self.ops))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        nodelist.extend(flatten_nodes(self.ops))
        return tuple(nodelist)

    def __repr__(self):
        return "Compare(%s, %s)" % (repr(self.expr), repr(self.ops))

class Const(Node):
    def __init__(self, value, lineno=None):
        self.value = value
        self.lineno = lineno

    def getChildren(self):
        return self.value,

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Const(%s)" % (repr(self.value),)

class Continue(Node):
    def __init__(self, lineno=None):
        self.lineno = lineno

    def getChildren(self):
        return ()

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Continue()"

class Decorators(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Decorators(%s)" % (repr(self.nodes),)

class Dict(Node):
    def __init__(self, items, lineno=None):
        self.items = items
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.items))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.items))
        return tuple(nodelist)

    def __repr__(self):
        return "Dict(%s)" % (repr(self.items),)

class Discard(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Discard(%s)" % (repr(self.expr),)

class Div(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Div((%s, %s))" % (repr(self.left), repr(self.right))

class Ellipsis(Node):
    def __init__(self, lineno=None):
        self.lineno = lineno

    def getChildren(self):
        return ()

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Ellipsis()"

class Exec(Node):
    def __init__(self, expr, locals, globals, lineno=None):
        self.expr = expr
        self.locals = locals
        self.globals = globals
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.append(self.locals)
        children.append(self.globals)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        if self.locals is not None:
            nodelist.append(self.locals)
        if self.globals is not None:
            nodelist.append(self.globals)
        return tuple(nodelist)

    def __repr__(self):
        return "Exec(%s, %s, %s)" % (repr(self.expr), repr(self.locals), repr(self.globals))

class FloorDiv(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "FloorDiv((%s, %s))" % (repr(self.left), repr(self.right))

class For(Node):
    def __init__(self, assign, list, body, else_, lineno=None):
        self.assign = assign
        self.list = list
        self.body = body
        self.else_ = else_
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.assign)
        children.append(self.list)
        children.append(self.body)
        children.append(self.else_)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.assign)
        nodelist.append(self.list)
        nodelist.append(self.body)
        if self.else_ is not None:
            nodelist.append(self.else_)
        return tuple(nodelist)

    def __repr__(self):
        return "For(%s, %s, %s, %s)" % (repr(self.assign), repr(self.list), repr(self.body), repr(self.else_))

class From(Node):
    def __init__(self, modname, names, lineno=None):
        self.modname = modname
        self.names = names
        self.lineno = lineno

    def getChildren(self):
        return self.modname, self.names

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "From(%s, %s)" % (repr(self.modname), repr(self.names))

class Function(Node):
    def __init__(self, decorators, name, argnames, defaults, flags, doc, code, lineno=None):
        self.decorators = decorators
        self.name = name
        self.argnames = argnames
        self.defaults = defaults
        self.flags = flags
        self.doc = doc
        self.code = code
        self.lineno = lineno
        self.varargs = self.kwargs = None
        if flags & CO_VARARGS:
            self.varargs = 1
        if flags & CO_VARKEYWORDS:
            self.kwargs = 1



    def getChildren(self):
        children = []
        children.append(self.decorators)
        children.append(self.name)
        children.append(self.argnames)
        children.extend(flatten(self.defaults))
        children.append(self.flags)
        children.append(self.doc)
        children.append(self.code)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        if self.decorators is not None:
            nodelist.append(self.decorators)
        nodelist.extend(flatten_nodes(self.defaults))
        nodelist.append(self.code)
        return tuple(nodelist)

    def __repr__(self):
        return "Function(%s, %s, %s, %s, %s, %s, %s)" % (repr(self.decorators), repr(self.name), repr(self.argnames), repr(self.defaults), repr(self.flags), repr(self.doc), repr(self.code))

class GenExpr(Node):
    def __init__(self, code, lineno=None):
        self.code = code
        self.lineno = lineno
        self.argnames = ['[outmost-iterable]']
        self.varargs = self.kwargs = None



    def getChildren(self):
        return self.code,

    def getChildNodes(self):
        return self.code,

    def __repr__(self):
        return "GenExpr(%s)" % (repr(self.code),)

class GenExprFor(Node):
    def __init__(self, assign, iter, ifs, lineno=None):
        self.assign = assign
        self.iter = iter
        self.ifs = ifs
        self.lineno = lineno
        self.is_outmost = False


    def getChildren(self):
        children = []
        children.append(self.assign)
        children.append(self.iter)
        children.extend(flatten(self.ifs))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.assign)
        nodelist.append(self.iter)
        nodelist.extend(flatten_nodes(self.ifs))
        return tuple(nodelist)

    def __repr__(self):
        return "GenExprFor(%s, %s, %s)" % (repr(self.assign), repr(self.iter), repr(self.ifs))

class GenExprIf(Node):
    def __init__(self, test, lineno=None):
        self.test = test
        self.lineno = lineno

    def getChildren(self):
        return self.test,

    def getChildNodes(self):
        return self.test,

    def __repr__(self):
        return "GenExprIf(%s)" % (repr(self.test),)

class GenExprInner(Node):
    def __init__(self, expr, quals, lineno=None):
        self.expr = expr
        self.quals = quals
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.extend(flatten(self.quals))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        nodelist.extend(flatten_nodes(self.quals))
        return tuple(nodelist)

    def __repr__(self):
        return "GenExprInner(%s, %s)" % (repr(self.expr), repr(self.quals))

class Getattr(Node):
    def __init__(self, expr, attrname, lineno=None):
        self.expr = expr
        self.attrname = attrname
        self.lineno = lineno

    def getChildren(self):
        return self.expr, self.attrname

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Getattr(%s, %s)" % (repr(self.expr), repr(self.attrname))

class Global(Node):
    def __init__(self, names, lineno=None):
        self.names = names
        self.lineno = lineno

    def getChildren(self):
        return self.names,

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Global(%s)" % (repr(self.names),)

class If(Node):
    def __init__(self, tests, else_, lineno=None):
        self.tests = tests
        self.else_ = else_
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.extend(flatten(self.tests))
        children.append(self.else_)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.tests))
        if self.else_ is not None:
            nodelist.append(self.else_)
        return tuple(nodelist)

    def __repr__(self):
        return "If(%s, %s)" % (repr(self.tests), repr(self.else_))

class Import(Node):
    def __init__(self, names, lineno=None):
        self.names = names
        self.lineno = lineno

    def getChildren(self):
        return self.names,

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Import(%s)" % (repr(self.names),)

class Invert(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Invert(%s)" % (repr(self.expr),)

class Keyword(Node):
    def __init__(self, name, expr, lineno=None):
        self.name = name
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.name, self.expr

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Keyword(%s, %s)" % (repr(self.name), repr(self.expr))

class Lambda(Node):
    def __init__(self, argnames, defaults, flags, code, lineno=None):
        self.argnames = argnames
        self.defaults = defaults
        self.flags = flags
        self.code = code
        self.lineno = lineno
        self.varargs = self.kwargs = None
        if flags & CO_VARARGS:
            self.varargs = 1
        if flags & CO_VARKEYWORDS:
            self.kwargs = 1



    def getChildren(self):
        children = []
        children.append(self.argnames)
        children.extend(flatten(self.defaults))
        children.append(self.flags)
        children.append(self.code)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.defaults))
        nodelist.append(self.code)
        return tuple(nodelist)

    def __repr__(self):
        return "Lambda(%s, %s, %s, %s)" % (repr(self.argnames), repr(self.defaults), repr(self.flags), repr(self.code))

class LeftShift(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "LeftShift((%s, %s))" % (repr(self.left), repr(self.right))

class List(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "List(%s)" % (repr(self.nodes),)

class ListComp(Node):
    def __init__(self, expr, quals, lineno=None):
        self.expr = expr
        self.quals = quals
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.extend(flatten(self.quals))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        nodelist.extend(flatten_nodes(self.quals))
        return tuple(nodelist)

    def __repr__(self):
        return "ListComp(%s, %s)" % (repr(self.expr), repr(self.quals))

class ListCompFor(Node):
    def __init__(self, assign, list, ifs, lineno=None):
        self.assign = assign
        self.list = list
        self.ifs = ifs
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.assign)
        children.append(self.list)
        children.extend(flatten(self.ifs))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.assign)
        nodelist.append(self.list)
        nodelist.extend(flatten_nodes(self.ifs))
        return tuple(nodelist)

    def __repr__(self):
        return "ListCompFor(%s, %s, %s)" % (repr(self.assign), repr(self.list), repr(self.ifs))

class ListCompIf(Node):
    def __init__(self, test, lineno=None):
        self.test = test
        self.lineno = lineno

    def getChildren(self):
        return self.test,

    def getChildNodes(self):
        return self.test,

    def __repr__(self):
        return "ListCompIf(%s)" % (repr(self.test),)

class Mod(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Mod((%s, %s))" % (repr(self.left), repr(self.right))

class Module(Node):
    def __init__(self, doc, node, lineno=None):
        self.doc = doc
        self.node = node
        self.lineno = lineno

    def getChildren(self):
        return self.doc, self.node

    def getChildNodes(self):
        return self.node,

    def __repr__(self):
        return "Module(%s, %s)" % (repr(self.doc), repr(self.node))

class Mul(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Mul((%s, %s))" % (repr(self.left), repr(self.right))

class Name(Node):
    def __init__(self, name, lineno=None):
        self.name = name
        self.lineno = lineno

    def getChildren(self):
        return self.name,

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Name(%s)" % (repr(self.name),)

class Not(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "Not(%s)" % (repr(self.expr),)

class Or(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Or(%s)" % (repr(self.nodes),)

class Pass(Node):
    def __init__(self, lineno=None):
        self.lineno = lineno

    def getChildren(self):
        return ()

    def getChildNodes(self):
        return ()

    def __repr__(self):
        return "Pass()"

class Power(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Power((%s, %s))" % (repr(self.left), repr(self.right))

class Print(Node):
    def __init__(self, nodes, dest, lineno=None):
        self.nodes = nodes
        self.dest = dest
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.extend(flatten(self.nodes))
        children.append(self.dest)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        if self.dest is not None:
            nodelist.append(self.dest)
        return tuple(nodelist)

    def __repr__(self):
        return "Print(%s, %s)" % (repr(self.nodes), repr(self.dest))

class Printnl(Node):
    def __init__(self, nodes, dest, lineno=None):
        self.nodes = nodes
        self.dest = dest
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.extend(flatten(self.nodes))
        children.append(self.dest)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        if self.dest is not None:
            nodelist.append(self.dest)
        return tuple(nodelist)

    def __repr__(self):
        return "Printnl(%s, %s)" % (repr(self.nodes), repr(self.dest))

class Raise(Node):
    def __init__(self, expr1, expr2, expr3, lineno=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr1)
        children.append(self.expr2)
        children.append(self.expr3)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        if self.expr1 is not None:
            nodelist.append(self.expr1)
        if self.expr2 is not None:
            nodelist.append(self.expr2)
        if self.expr3 is not None:
            nodelist.append(self.expr3)
        return tuple(nodelist)

    def __repr__(self):
        return "Raise(%s, %s, %s)" % (repr(self.expr1), repr(self.expr2), repr(self.expr3))

class Return(Node):
    def __init__(self, value, lineno=None):
        self.value = value
        self.lineno = lineno

    def getChildren(self):
        return self.value,

    def getChildNodes(self):
        return self.value,

    def __repr__(self):
        return "Return(%s)" % (repr(self.value),)

class RightShift(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "RightShift((%s, %s))" % (repr(self.left), repr(self.right))

class Slice(Node):
    def __init__(self, expr, flags, lower, upper, lineno=None):
        self.expr = expr
        self.flags = flags
        self.lower = lower
        self.upper = upper
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.append(self.flags)
        children.append(self.lower)
        children.append(self.upper)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        if self.lower is not None:
            nodelist.append(self.lower)
        if self.upper is not None:
            nodelist.append(self.upper)
        return tuple(nodelist)

    def __repr__(self):
        return "Slice(%s, %s, %s, %s)" % (repr(self.expr), repr(self.flags), repr(self.lower), repr(self.upper))

class Sliceobj(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Sliceobj(%s)" % (repr(self.nodes),)

class Stmt(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Stmt(%s)" % (repr(self.nodes),)

class Sub(Node):
    def __init__(self, (left, right), lineno=None):
        self.left = left
        self.right = right
        self.lineno = lineno

    def getChildren(self):
        return self.left, self.right

    def getChildNodes(self):
        return self.left, self.right

    def __repr__(self):
        return "Sub((%s, %s))" % (repr(self.left), repr(self.right))

class Subscript(Node):
    def __init__(self, expr, flags, subs, lineno=None):
        self.expr = expr
        self.flags = flags
        self.subs = subs
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.expr)
        children.append(self.flags)
        children.extend(flatten(self.subs))
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.expr)
        nodelist.extend(flatten_nodes(self.subs))
        return tuple(nodelist)

    def __repr__(self):
        return "Subscript(%s, %s, %s)" % (repr(self.expr), repr(self.flags), repr(self.subs))

class TryExcept(Node):
    def __init__(self, body, handlers, else_, lineno=None):
        self.body = body
        self.handlers = handlers
        self.else_ = else_
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.body)
        children.extend(flatten(self.handlers))
        children.append(self.else_)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.body)
        nodelist.extend(flatten_nodes(self.handlers))
        if self.else_ is not None:
            nodelist.append(self.else_)
        return tuple(nodelist)

    def __repr__(self):
        return "TryExcept(%s, %s, %s)" % (repr(self.body), repr(self.handlers), repr(self.else_))

class TryFinally(Node):
    def __init__(self, body, final, lineno=None):
        self.body = body
        self.final = final
        self.lineno = lineno

    def getChildren(self):
        return self.body, self.final

    def getChildNodes(self):
        return self.body, self.final

    def __repr__(self):
        return "TryFinally(%s, %s)" % (repr(self.body), repr(self.final))

class Tuple(Node):
    def __init__(self, nodes, lineno=None):
        self.nodes = nodes
        self.lineno = lineno

    def getChildren(self):
        return tuple(flatten(self.nodes))

    def getChildNodes(self):
        nodelist = []
        nodelist.extend(flatten_nodes(self.nodes))
        return tuple(nodelist)

    def __repr__(self):
        return "Tuple(%s)" % (repr(self.nodes),)

class UnaryAdd(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "UnaryAdd(%s)" % (repr(self.expr),)

class UnarySub(Node):
    def __init__(self, expr, lineno=None):
        self.expr = expr
        self.lineno = lineno

    def getChildren(self):
        return self.expr,

    def getChildNodes(self):
        return self.expr,

    def __repr__(self):
        return "UnarySub(%s)" % (repr(self.expr),)

class While(Node):
    def __init__(self, test, body, else_, lineno=None):
        self.test = test
        self.body = body
        self.else_ = else_
        self.lineno = lineno

    def getChildren(self):
        children = []
        children.append(self.test)
        children.append(self.body)
        children.append(self.else_)
        return tuple(children)

    def getChildNodes(self):
        nodelist = []
        nodelist.append(self.test)
        nodelist.append(self.body)
        if self.else_ is not None:
            nodelist.append(self.else_)
        return tuple(nodelist)

    def __repr__(self):
        return "While(%s, %s, %s)" % (repr(self.test), repr(self.body), repr(self.else_))

class Yield(Node):
    def __init__(self, value, lineno=None):
        self.value = value
        self.lineno = lineno

    def getChildren(self):
        return self.value,

    def getChildNodes(self):
        return self.value,

    def __repr__(self):
        return "Yield(%s)" % (repr(self.value),)

for name, obj in globals().items():
    if isinstance(obj, type) and issubclass(obj, Node):
        nodes[name.lower()] = obj
