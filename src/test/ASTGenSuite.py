import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_case0(self):
        input = """Var: x = 3;"""
        expect = Program([VarDecl(variable = Id('x'), varDimen = [], varInit = IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_case1(self):
        input = """Var: x;"""
        expect = Program([VarDecl(variable = Id("x"), varDimen = [],varInit = None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_case2(self):
        input = """Var: c, d = 6, e, f;"""
        expect = Program([VarDecl(variable = Id("c"), varDimen = [],varInit = None),VarDecl(variable = Id("d"),varDimen = [],varInit = IntLiteral(6)),VarDecl(variable = Id("e"),varDimen = [],varInit = None),VarDecl(variable = Id("f"),varDimen = [], varInit = None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_case3(self):
        input = """ Var: b[2][3]= { {1,2,3},{4,5,6} }; """
        expect = Program([VarDecl(Id('b'),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303)) 

    def test_case4(self):
        input = """ Var: m, n[10]; """
        expect = Program([VarDecl(variable = Id("m"),varDimen = [], varInit = None),VarDecl(variable = Id("n"),varDimen = [IntLiteral(10)],varInit = None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_case5(self):
        input = """ Var: c, d = 6, e;"""
        expect = Program([VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_case6(self):
        input = """ Var: m, n[10][12];"""
        expect = Program([VarDecl(Id('m'),[],None),VarDecl(Id('n'),[IntLiteral(10),IntLiteral(12)],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_case7(self):
        input = """ Function: fact
                Body:
                write(i);
                EndBody."""
        expect = Program([FuncDecl(name = Id('fact'),param = [],body = ([],[CallStmt(Id('write'),[Id('i')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_case8(self):
        input = """ Function: main
                    Body:
                    x = 10;
                    EndBody."""
        expect = Program([FuncDecl(name = Id('main'),param = [],body = ([],[Assign(Id('x'),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_case9(self):
        input = """ Var: x;
                    Function: foo
                    Parameter: a[5]
                    Body:
                    EndBody."""
        expect = Program([VarDecl(variable = Id('x'), varDimen = [], varInit = None),FuncDecl(name = Id('foo'),param = [VarDecl(Id('a'),[IntLiteral(5)],None)], body = ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_case10(self):
        input = """ Function: main
                    Parameter: a
                    Body:
                    EndBody."""
        expect = Program([FuncDecl(name = Id('main'),param =[VarDecl(variable = Id('a'),varDimen = [], varInit = None)],body = ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_case11(self):
        input = """ Function: main
                    Parameter: a
                    Body:
                    EndBody.
                    Function: main2
                    Body:
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[])),FuncDecl(Id('main2'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_case12(self):
        input = """ Function: main
                    Body:
                    a = 0x34 ;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(52))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_case13(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(name = Id('main'),param = [],body = ([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_case14(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 2) Do writeln(i);
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_case15(self):
        input = """ Function: main
                    Body:
                    For (i = 0 + 1, i + 10, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),BinaryOp('+',IntLiteral(0),IntLiteral(1)),BinaryOp('+',Id('i'),IntLiteral(10)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_case16(self):
        input = """ Function: main
                    Body:
                    Var: c;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(variable=Id(name='c'), varDimen=[], varInit=None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_case17(self):
        input = """ Function: main
                    Body:
                    If (x == 2) Then x = x + 1;
                    Else
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('x'),IntLiteral(2)),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_case18(self):
        input = """ Function: main
                    Body:
                    If (x == 2) Then x[foo(5)] = x + 1;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('x'),IntLiteral(2)),[],[Assign(ArrayCell(Id('x'),[CallExpr(Id('foo'),[IntLiteral(5)])]),BinaryOp('+',Id('x'),IntLiteral(1)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_case19(self):
        input = """ Function: main
                    Body:
                    Break;
                    Continue;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Break(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_case20(self):
        input = """ Function: main
                    Body:
                    Var: a;
                    a = { {1,2}, "abc"};
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id("a"),[],None)],[Assign(Id('a'),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),StringLiteral('abc')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_case21(self):
        input = """ Function: main
                    Body:
                    If (x == 2) Then
                    ElseIf (x == 4) Then
                    Else Break;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('x'),IntLiteral(2)),[],[]),(BinaryOp('==',Id('x'),IntLiteral(4)),[],[])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_case22(self):
        input = """ Function: foo
                    Body:
                    Continue;
                    
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_case23(self):
        input = """ Function: main
                    Body:
                    a[a+1] = 120000e-1 ;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp('+',Id('a'),IntLiteral(1))]),FloatLiteral(12000.0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_case24(self):
        input = """ Function: main
                    Body:
                    Return a[i*3];
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[BinaryOp('*',Id('i'),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_case25(self):
        input = """ Function: main
                    Body:
                    Continue;
                    (a+ foo(2))[i * 2 + 3] = { 1 };
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Continue(),Assign(ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[IntLiteral(2)])),[BinaryOp('+',BinaryOp('*',Id('i'),IntLiteral(2)),IntLiteral(3))]),ArrayLiteral([IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_case26(self):
        input = """ Function: main
                    Body:
                    While (x && y > 98) Do
                    x = 2;
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('>',BinaryOp('&&',Id('x'),Id('y')),IntLiteral(98)),([],[Assign(Id('x'),IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_case27(self):
        input = """ Function: main
                    Body:
                    If (x >= y) Then x = 2;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('>=',Id('x'),Id('y')),[],[Assign(Id('x'),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_case28(self):
        input = """ Var: b = 0O77; """
        expect = Program([VarDecl(Id('b'),[],IntLiteral(63))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_case29(self):
        input = """ Function: foo
                    Body:
                    f(f())[3] = 0X65;
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(CallExpr(Id('f'),[CallExpr(Id('f'),[])]),[IntLiteral(3)]),IntLiteral(101))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_case30(self):
        input = """ Function: foo
                    Body:
                    While (i =/= 5) Do
                    a[i] = b +. 1.0;
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[While(BinaryOp('=/=',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_case31(self):
        input = """ Function: main
                    Body:
                    Return a[foo(1.3)];
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[CallExpr(Id('foo'),[FloatLiteral(1.3)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_case32(self):
        input = """ Function: main
                    Body:
                    While True Do
                    x = 2;
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral('true'),([],[Assign(Id('x'),IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_case33(self):
        input = """ Function: main
                    Body:
                    Var: r = 1.3e1;
                    If (x) Then
                    v = 4 * r;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('r'),[],FloatLiteral('13.0'))],[If([(Id('x'),[],[Assign(Id('v'),BinaryOp('*',IntLiteral(4),Id('r')))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_case34(self):
        input = """ Function: main
                    Body:
                    While a[a[d]][2+2] Do
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(ArrayCell(ArrayCell(Id('a'),[ArrayCell(Id('a'),[Id('d')])]),[BinaryOp('+',IntLiteral(2),IntLiteral(2))]),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_case35(self):
        input = """ Function: main
                    Body:
                    Do While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_case36(self):
        input = """ Function: main
                    Body:
                    Do x = 13e1; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[Assign(Id('x'),FloatLiteral(130.0))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_case37(self):
        input = """ Function: main
                    Body:
                    Do x = 16; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[Assign(Id('x'),IntLiteral(16))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_case38(self):
        input = """ Function: foo
                    Parameter: a[2][4][6], b
                    Body:
                    EndBody. """
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[IntLiteral(2),IntLiteral(4),IntLiteral(6)],None),VarDecl(Id('b'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_case39(self):
        input = """ Function: main
                    Body:
                    a = b % 34.e3 > a[foo()] ;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp('>',BinaryOp('%',Id('b'),FloatLiteral(34000.0)),ArrayCell(Id('a'),[CallExpr(Id('foo'),[])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_case40(self):
        input =  """Function: main
                    Body:
                    a[3][foo()] = b % 34.e3 > a[foo()] ;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(ArrayCell(Id('a'),[IntLiteral(3)]),[CallExpr(Id('foo'),[])]),BinaryOp('>',BinaryOp('%',Id('b'),FloatLiteral(34000.0)),ArrayCell(Id('a'),[CallExpr(Id('foo'),[])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_case41(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_case42(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 2) Do
                    a = 4;
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[Assign(Id('a'),IntLiteral(4))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_case43(self):
        input = """ Function: main
                    Body:
                    While (a < 3 && (2 != 9)) Do EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('<',Id('a'),BinaryOp('&&',IntLiteral(3),BinaryOp('!=',IntLiteral(2),IntLiteral(9)))),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_case44(self):
        input = """ Function: main
                    Body:
                    func(a[x]);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[ArrayCell(Id('a'),[Id('x')])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_case45(self):
        input = """ Function: main
                    Body:
                    func(a[x]);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[ArrayCell(Id('a'),[Id('x')])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_case46(self):
        input = """ Function: main
                    Body:
                    func(a[x]);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[ArrayCell(Id('a'),[Id('x')])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_case47(self):
        input = """ Function: main
                    Body:
                    If 2 < 3 Then a = 1;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('<',IntLiteral(2),IntLiteral(3)),[],[Assign(Id('a'),IntLiteral(1))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_case48(self):
        input = """ Function: main
                    Body:
                    func(a[x]+12.3e3);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('func'),[BinaryOp('+',ArrayCell(Id('a'),[Id('x')]),FloatLiteral(12300.0))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_case49(self):
        input = """ Function: a
                    Body:
                    func(a + a[x]);
                    EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([],[CallStmt(Id('func'),[BinaryOp('+',Id('a'),ArrayCell(Id('a'),[Id('x')]))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_case50(self):
        input = """ Var: x = 0XABC;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(2748))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_case51(self):
        input = """ Function: main
                    Body:
                    a[3 + a(2)] = a[b[2][3]];
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('a'),[IntLiteral(2)]))]),ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_case52(self):
        input = """ Function: main
                    Body:
                    a[3 + a(2)] = a[b[2][3]] + 4;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('a'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_case53(self):
        input = """ Function: main
                    Body:
                    a[3 + (2)] = a[b[2][3]] + 4;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),IntLiteral(2))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_case54(self):
        input = """ Function: main 
                    Parameter: a[10]
                    Body: 
                    While func() Do EndWhile. 
                    EndBody. """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[IntLiteral(10)],None)],([],[While(CallExpr(Id('func'),[]),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_case55(self):
        input = """ Function: main
                    Body:
                    If (fup[3] == 2) Then EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',ArrayCell(Id('fup'),[IntLiteral(3)]),IntLiteral(2)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_case56(self):
        input = """ Function: main
                    Body:
                    a[3*a[2]] = a[b[2][3]] + 4;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('*',IntLiteral(3),ArrayCell(Id('a'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_case57(self):
        input = """ Function: main
                    Body:
                    While (a < 3 ) Do EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('<',Id('a'),IntLiteral(3)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_case58(self):
        input = """ Function: main
                    Body:
                    x = 10;
                    x = main(main(x));
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),Assign(Id('x'),CallExpr(Id('main'),[CallExpr(Id('main'),[Id('x')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_case59(self):
        input = """ Function: main
                    Body:
                    While (True) Do
                    x = x +. 1;
                    x(foo(x));
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral('true'),([],[Assign(Id('x'),BinaryOp('+.',Id('x'),IntLiteral(1))),CallStmt(Id('x'),[CallExpr(Id('foo'),[Id('x')])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_case60(self):
        input = """ Function: foo
                    Parameter: a[5], b
                    Body:
                    Var: i = 0;
                    While (i < 5) Do
                    a = b +. 1.0;
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[IntLiteral(5)],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(Id('a'),BinaryOp('+.',Id('b'),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_case61(self):
        input = """ Function: foo
                    Body:
                    For (x = 1, (f[2] + 1)[5], 12e1) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[For(Id('x'),IntLiteral(1),ArrayCell(BinaryOp('+',ArrayCell(Id('f'),[IntLiteral(2)]),IntLiteral(1)),[IntLiteral(5)]),FloatLiteral(120.0),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_case62(self):
        input = """ Function: main
                    Body:
                    While (a+3) Do x = x; EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('+',Id('a'),IntLiteral(3)),([],[Assign(Id('x'),Id('x'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_case63(self):
        input = """ Function: foo
                    Body:
                    For (x = 1, 4 , 3 ) Do
                    x = x *. 1;
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[For(Id('x'),IntLiteral(1),IntLiteral(4),IntLiteral(3),([],[Assign(Id('x'),BinaryOp('*.',Id('x'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_case64(self):
        input = """ Function: main
                    Body:
                    Return (2 <. 3);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('<.',IntLiteral(2),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_case65(self):
        input = """ Function: main
                    Body:
                    Return ak49(d);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(CallExpr(Id('ak49'),[Id('d')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_case66(self):
        input = """ Function: main
                    Body:
                    Return a[i(2) * 2 + 3];
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[BinaryOp('+',BinaryOp('*',CallExpr(Id('i'),[IntLiteral(2)]),IntLiteral(2)),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_case67(self):
        input = """ Function: main
                    Body:
                    Continue;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_case68(self):
        input = """ Function: main
                    Body:
                    While (a == 3) Do Var: a = 3; a = a + 3; EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('==',Id('a'),IntLiteral(3)),([VarDecl(Id('a'),[],IntLiteral(3))],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_case69(self):
        input = """ Function: main
                    Body:
                    While (x || y > 98) Do
                    If (x >=. y) Then x = 2; EndIf.
                    EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('>',BinaryOp('||',Id('x'),Id('y')),IntLiteral(98)),([],[If([(BinaryOp('>=.',Id('x'),Id('y')),[],[Assign(Id('x'),IntLiteral(2))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_case70(self):
        input = """ Function: main
                    Body:
                    While (True) Do
                    If (x >= y) Then x = 2; 
                    Else foo[foo()] = a[3];
                    EndIf.
                    EndWhile.
                    EndBody.
                    """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral('true'),([],[If([(BinaryOp('>=',Id('x'),Id('y')),[],[Assign(Id('x'),IntLiteral(2))])],([],[Assign(ArrayCell(Id('foo'),[CallExpr(Id('foo'),[])]),ArrayCell(Id('a'),[IntLiteral(3)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_case71(self):
        input = """ Function: main
                    Body:
                    While (a == 3) Do EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('==',Id('a'),IntLiteral(3)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_case72(self):
        input = """ Function: main
                    Body:
                    If (x >= y) Then
                    ElseIf (True) Then
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('>=',Id('x'),Id('y')),[],[]),(BooleanLiteral('true'),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_case73(self):
        input = """ Function: main
                    Body:
                    If (x == 2) Then x = 12.8e-12; EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('x'),IntLiteral(2)),[],[Assign(Id('x'),FloatLiteral(1.28e-11))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_case74(self):
        input = """ Function: main
                    Body:
                    funcion(78 + function(78));
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('funcion'),[BinaryOp('+',IntLiteral(78),CallExpr(Id('function'),[IntLiteral(78)]))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_case75(self):
        input = """ Function: main
                    Body:
                    While (a < 3 && 2 != 90) Do fucn(); EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('!=',BinaryOp('<',Id('a'),BinaryOp('&&',IntLiteral(3),IntLiteral(2))),IntLiteral(90)),([],[CallStmt(Id("fucn"),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_case76(self):
        input = """ Function: main
                    Body:
                    Return !a[i * 2 + 3];
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('!',ArrayCell(Id('a'),[BinaryOp('+',BinaryOp('*',Id('i'),IntLiteral(2)),IntLiteral(3))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_case77(self):
        input = """ Function: main
                    Body:
                    Do While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_case78(self):
        input = """ Function: main
                    Body:
                    While (x) Do  EndWhile.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(Id('x'),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_case79(self):
        input = """ Function: m
                    Body:
                    Do Var: x = {1,2}; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('m'),[],([],[Dowhile(([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_case80(self):
        input = """ Function: main
                    Body:
                    For (i = 12.3, i < 10, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),FloatLiteral(12.3),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_case81(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i > 0x34, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('>',Id('i'),IntLiteral(52)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_case82(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i == 10, 2) Do
                    x = x > 2;
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('==',Id('i'),IntLiteral(10)),IntLiteral(2),([],[Assign(Id('x'),BinaryOp('>',Id('x'),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_case83(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 2 =/= 3) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=/=',IntLiteral(2),IntLiteral(3)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_case84(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i < 10, 23) Do foo (2,4. \. 2);
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(23),([],[CallStmt(Id('foo'),[IntLiteral(2),BinaryOp('\.',FloatLiteral(4.0),IntLiteral(2))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_case85(self):
        input = """ Function: main
                    Body:
                    Do Var: x = 1; Continue; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('x'),[],IntLiteral(1))],[Continue()]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
        
    def test_case86(self):
        input = """ Function: main
                    Body:
                    Do Var: x = 1; While (x==2) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('x'),[],IntLiteral(1))],[]),BinaryOp("==",Id('x'),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_case87(self):
        input = """ Function: main
                    Body:
                    Do Var: x = 1; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('x'),[],IntLiteral(1))],[]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_case88(self):
        input = """ Function: main
                    Body:
                    Do Continue; While (1) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[Continue()]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_case89(self):
        input = """ Function: main
                    Body:
                    Do Var: x[3][4] = 2; While (5) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('x'),[IntLiteral(3),IntLiteral(4)],IntLiteral(2))],[]),IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_case90(self):
        input = """ Function: main
                    Parameter: x
                    Body:
                    x[foo(3)] = 3;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(ArrayCell(Id('x'),[CallExpr(Id('foo'),[IntLiteral(3)])]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_case91(self):
        input = """ Function: main
                    Body:
                    Do Break; Continue; While (False) EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[Break(),Continue()]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_case92(self):
        input = """ Function: main
                    Body:
                    For (i = 2, i[2] || 2, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(2),BinaryOp('||',ArrayCell(Id('i'),[IntLiteral(2)]),IntLiteral(2)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_case93(self):
        input = """ Function: main
                    Body:
                    For (i = 0, i == 10, 2) Do
                    EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('==',Id('i'),IntLiteral(10)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_case94(self):
        input = """ Var: c = "SAD", f;"""
        expect = Program([VarDecl(Id('c'),[],StringLiteral('SAD')),VarDecl(Id('f'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_case95(self):
        input = """ Function: main
                    Body:
                    x = 10;
                    fact(x);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_case96(self):
        input = """ Function: main
                    Parameter: e
                    Body:
                    x = "ABC" + { 1, 2, 3 };
                    fact(x);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('e'),[],None)],([],[Assign(Id("x"),BinaryOp('+',StringLiteral('ABC'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_case97(self):
        input = """ Function: m
                    Body:
                    x = 10 * 23 + 3 \. 4 % 3 >= 3 ;
                    EndBody."""
        expect = Program([FuncDecl(Id('m'),[],([],[Assign(Id('x'),BinaryOp('>=',BinaryOp('+',BinaryOp('*',IntLiteral(10),IntLiteral(23)),BinaryOp('%',BinaryOp('\.',IntLiteral(3),IntLiteral(4)),IntLiteral(3))),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_case98(self):
        input = """ Function: main
                    Parameter: a
                    Body:
                    x = function(x);
                    fact (x);
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(Id('x'),CallExpr(Id('function'),[Id('x')])),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_case99(self):
        input = """ Function: m
                    Body:
                    x = 10;
                    fact("x");
                    EndBody."""
        expect = Program([FuncDecl(Id('m'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[StringLiteral('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
   