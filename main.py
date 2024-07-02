from typing import NamedTuple
from enum import Enum
import sys

class KindEnum(Enum):
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
    TEXT = 13 # [a-z][A-Z]

TOKEN_DICT ={
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
    "BANG":KindEnum(12),# !
    "TEXT":KindEnum(13)
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
                    self.data = file.read().rstrip()
            except FileNotFoundError:
                self.data = ""
        
        def tokenize(self):
            pos = 0
            line = 0
            self.tokens= []
            while pos < len(self.data):
                if self.data[pos] == "\n":
                    line += 1
                    self.tokens.append(Token(pos,TOKEN_DICT["NEWLINE"],line,""))
                elif self.data[pos] == "#":
                    self.tokens.append(Token(pos,TOKEN_DICT["HASH"],line,""))
                elif self.data[pos] == "_":
                    self.tokens.append(Token(pos,TOKEN_DICT["UNDERSCORE"],line,""))
                elif self.data[pos] == "*":
                    self.tokens.append(Token(pos,TOKEN_DICT["STAR"],line,""))
                elif self.data[pos] == "[":
                    self.tokens.append(Token(pos,TOKEN_DICT["STRAIGHTBRACEOPEN"],line,""))
                elif self.data[pos] == "]":
                    self.tokens.append(Token(pos,TOKEN_DICT["UNDERSCORE"],line,""))
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
                else:
                    temp = ""
                    text = True
                    while text and pos<len(self.data):
                        if self.data[pos] == ['\n', '!',  '#', '_', '*', '-', '[', ']', '(', ')', '`', '>']:
                                text = False
                        else:
                            temp += self.data[pos]
                            pos+=1
                    self.tokens.append((Token(pos,TOKEN_DICT["TEXT"],line,temp)))
                    continue
                pos+=1
                


file = sys.argv[1]
a = MarkdownCompiler(file)
a.tokenize()
print(a.tokens)
