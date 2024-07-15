from typing import NamedTuple
from enum import Enum
import sys
import ast

class KindEnum(Enum):
    TEXT = 0 #  [a-z][A-Z][0-9]
    HASH = 1 # #
    UNDERSCORE = 2 # _
    STAR = 3 # *
    NEWLINE = 4 # \n
    DASH = 5 # -
    STRAIGHTBRACEOPEN = 6 # [
    STRAIGHTBRACECLOSE = 7 # ]
    PARENOPEN = 8 # (
    PARENCLOSE = 9 # )
    BACKTICK = 10 # `
    GREATERTHAN = 11 # >
    BANG = 12 # !
    TILDE = 13 # ~

TOKEN_DICT ={
    "TEXT":KindEnum(0), # [a-z][A-Z][0-9]
    "HASH":KindEnum(1), # #
    "UNDERSCORE":KindEnum(2), # _
    "STAR":KindEnum(3), # *
    "NEWLINE":KindEnum(4), # \n
    "DASH":KindEnum(5),# -
    "STRAIGHTBRACEOPEN":KindEnum(6), # [
    "STRAIGHTBRACECLOSE":KindEnum(7), # ]
    "PARENOPEN":KindEnum(8),# (
    "PARENCLOSE":KindEnum(9), # )
    "BACKTICK":KindEnum(10),# `
    "GREATERTHAN":KindEnum(11), # >
    "BANG":KindEnum(12), # !
    "TILDE":KindEnum(13) # ~
}

class Token(NamedTuple):
    pos:int 
    kind:KindEnum 
    line:int 
    value:str

class MarkdownCompiler:
        def __init__(self,f):
            try:
                with open(f,'r') as file:
                    self.data = file.read()
            except FileNotFoundError:
                self.data = ""
        
        def tokenize(self):
            pos = 0
            line = 0
            self.tokens= []
            while pos < len(self.data):
                if self.data[pos] == "\n":
                    self.tokens.append(Token(pos,TOKEN_DICT["NEWLINE"],line,""))
                    line += 1
                elif self.data[pos] == "#":
                    self.tokens.append(Token(pos,TOKEN_DICT["HASH"],line,""))
                elif self.data[pos] == "_":
                    self.tokens.append(Token(pos,TOKEN_DICT["UNDERSCORE"],line,""))
                elif self.data[pos] == "*":
                    self.tokens.append(Token(pos,TOKEN_DICT["STAR"],line,""))
                elif self.data[pos] == "[":
                    self.tokens.append(Token(pos,TOKEN_DICT["STRAIGHTBRACEOPEN"],line,""))
                elif self.data[pos] == "]":
                    self.tokens.append(Token(pos,TOKEN_DICT["STRAIGHTBRACECLOSE"],line,""))
                elif self.data[pos] == "(":
                    self.tokens.append(Token(pos,TOKEN_DICT["PARENOPEN"],line,""))
                elif self.data[pos] == ")":
                    self.tokens.append(Token(pos,TOKEN_DICT["PARENCLOSE"],line,""))
                elif self.data[pos] == "`":
                    self.tokens.append(Token(pos,TOKEN_DICT["BACKTICK"],line,""))
                elif self.data[pos] == ">":
                    self.tokens.append(Token(pos,TOKEN_DICT["GREATERTHAN"],line,""))
                elif self.data[pos] == "!":
                    self.tokens.append(Token(pos,TOKEN_DICT["BANG"],line,""))
                elif self.data[pos] == "~":
                    self.tokens.append(Token(pos,TOKEN_DICT["TILDE"],line,""))
                else:
                    temp = ""
                    while pos < len(self.data) and self.data[pos] not in ['\n', '!', '#', '_', '*', '-', '[', ']', '(', ')', '`', '>','~']:
                        temp += self.data[pos]
                        pos += 1
                    if temp:  # Add the accumulated text if it's not empty
                        start_pos = pos - len(temp)
                        self.tokens.append(Token(start_pos, TOKEN_DICT["TEXT"], line, temp))
                    continue  # Skip pos increment at the end of the loop
                pos+=1
        
        def parse(self):
                ast = {
                    "root" : [
                    ]
                }
                for i in self.tokens:
                    if i.kind == KindEnum.HASH:
                        ast["root"].append("")
file = sys.argv[1]
a = MarkdownCompiler(file)
a.tokenize()

b = Token(0,TOKEN_DICT["HASH"],0,"")
print(b.kind)
for i in a.tokens:
    print(i)
