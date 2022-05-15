#update: 02/04/2022
from abc import ABC
from dataclasses import dataclass
from AST import *

class Kind(ABC):
    pass

class Class(Kind):
    def __str__(self):
        return "Class"

class Method(Kind):
    def __str__(self):
        return "Method"

class SpecialMethod(Kind):
    def __str__(self):
        return "Special Method"

class Attribute(Kind):
    def __str__(self):
        return "Attribute"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Constant(Kind):
    def __str__(self):
        return "Constant"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass

"""
    An identifier must be declared before used.
    Declaration must be unique in it's scope.
    An attribute/method is redeclared if there is a member with the same name.
"""
@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

"""
    When an identifier is used but it's declaration cannot be found.
    Because this is OOP so we must check in super class for identifier.
"""
@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str # name of identifier
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n

"""
    If error appear in assignment for a foreach statement,
    just the assignment part is printed out.
"""
@dataclass
class CannotAssignToConstant(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Cannot Assign To Constant: "+ str(self.stmt)

"""
    1. Scalar var, expr1 and expr2 in ForEach must be integer.
    2. Assignment: Left must not be void, right must be compatible with left
        (equal or can be coerced to). Array can also be coerced.
    3. Call statement: Must be Class that call method, callee must return void. 
        Parameter = Argument.
    4. Return: something = return_value
"""
@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

"""
    1. ArrayType[Integer]
    2. Binary & Unary
    3. Class.(non-void-returning-method).
    4. Class.Identifier.
"""
@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr
    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

"""
    Must be compatible
"""
@dataclass
class TypeMismatchInConstant(StaticError):
    constdecl:ConstDecl
    def __str__(self):
        return "Type Mismatch In Constant Declaration: "+ str(self.constdecl)

"""
    Break/Continue must be in a loop
"""
@dataclass
class MustInLoop(StaticError):
    stmt:Stmt
    def __str__(self):
        return str(self.stmt) + " Not In Loop"

"""
    Must be statically evaluated (composed of constants/literals)
"""
@dataclass
class IllegalConstantExpression(StaticError):
    expr:Expr
    def __str__(self):
        return "Illegal Constant Expression: "+ str(self.expr)

"""
    All member of an array literal must be of same type
"""
@dataclass
class IllegalArrayLiteral(StaticError):
    arr:ArrayLiteral
    def __str__(self):
        return "Illegal Array Literal: "+ str(self.arr)

"""
    Self-explanatory. Cannot E::InstanceAttr or E.StaticAttr
"""
@dataclass
class IllegalMemberAccess(StaticError):
    expr:Expr
    def __str__(self):
        return "Illegal Member Access: " + str(self.expr)

"""
    No main function
"""
@dataclass
class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
