Module(Stmt([Printnl([BoolExp(Const(1),and,BoolExp(Const(3),and,Const(2),None),None)])]))
Module(Stmt([Printnl([Tag(BoolExp(ConvertToInt(Tag(Const(1), int)),and,ConvertToInt(Tag(BoolExp(ConvertToInt(Tag(Const(3), int)),and,ConvertToInt(Tag(Const(2), int)),None), int)),None), int)])]))
%.6
Assign(AssName(%.6), Const(1))
%.6
Assign(AssName(%.6), Const(3))
None
None
Assign(AssName(%.11), Tag(Const(1), int))
Assign(AssName(%.9), ConvertToInt(Name(%.11)))
Assign(AssName(%.12), Tag(Const(0), int))
Assign(AssName(%.10), ConvertToInt(Name(%.12)))
Assign(AssName(%.8), BoolExp(Name(%.9),!=,Name(%.10),check))
Assign(AssName(%.7), Tag(Name(%.8), bool))
IfNode(%.7,GoTo(F0),GoTo(T1))
Label(T1)
Assign(AssName(%.17), Tag(Const(3), int))
Assign(AssName(%.15), ConvertToInt(Name(%.17)))
Assign(AssName(%.18), Tag(Const(0), int))
Assign(AssName(%.16), ConvertToInt(Name(%.18)))
Assign(AssName(%.14), BoolExp(Name(%.15),!=,Name(%.16),check))
Assign(AssName(%.13), Tag(Name(%.14), bool))
IfNode(%.13,GoTo(F2),GoTo(T3))
Label(T3)
Assign(AssName(%.6), Const(2))
GoTo(END)
Label(F2)
Assign(AssName(%.6), Const(3))
GoTo(END)
Label(END)
GoTo(END4)
Label(F0)
Assign(AssName(%.6), Const(1))
GoTo(END4)
Label(END4)
Assign(AssName(%.4), Tag(Name(%.6), int))
Assign(AssName(%.5), Printnl([Name(%.4)]))
declare i32 @input() nounwind uwtable ssp 
declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp 
define i32 @main() nounwind uwtable ssp {
	 %.11 = alloca i32, align 4
	 %.9 = alloca i32, align 4
	 %.12 = alloca i32, align 4
	 %.10 = alloca i32, align 4
	 %.8 = alloca i32, align 4
	 %.7 = alloca i32, align 4
	 %.17 = alloca i32, align 4
	 %.15 = alloca i32, align 4
	 %.18 = alloca i32, align 4
	 %.16 = alloca i32, align 4
	 %.14 = alloca i32, align 4
	 %.13 = alloca i32, align 4
	 %.6 = alloca i32, align 4
	 %.4 = alloca i32, align 4
	 %.5 = alloca i32, align 4

 ; Tagging  %.11 

  store i32 1, i32* %.11, align 4
	 %.20 = alloca i32, align 4
  store i32 2, i32* %.20, align 4

 ; generating code for binry op ,   LeftShift(Name(%.11), Name(%.20))  

	 %.21 = load i32* %.11, align 4
	 %.22 = load i32* %.20, align 4
	 %.23 = shl i32 %.21, %.22
  store i32 %.23, i32* %.11, align 4

 ; Untagging,   Name(%.11)  

 
	 %.24 = alloca i32, align 4
  store i32 2, i32* %.24, align 4

 ; generating code for binry op ,   RightShift(Name(%.11), Name(%.24))  

	 %.27 = load i32* %.11, align 4
	 %.28 = load i32* %.24, align 4
	 %.29 = ashr i32 %.27, %.28
  store i32 %.29, i32* %.9, align 4

 ; Tagging  %.12 

  store i32 0, i32* %.12, align 4
	 %.31 = alloca i32, align 4
  store i32 2, i32* %.31, align 4

 ; generating code for binry op ,   LeftShift(Name(%.12), Name(%.31))  

	 %.32 = load i32* %.12, align 4
	 %.33 = load i32* %.31, align 4
	 %.34 = shl i32 %.32, %.33
  store i32 %.34, i32* %.12, align 4

 ; Untagging,   Name(%.12)  

 
	 %.35 = alloca i32, align 4
  store i32 2, i32* %.35, align 4

 ; generating code for binry op ,   RightShift(Name(%.12), Name(%.35))  

	 %.38 = load i32* %.12, align 4
	 %.39 = load i32* %.35, align 4
	 %.40 = ashr i32 %.38, %.39
  store i32 %.40, i32* %.10, align 4

 ; generating code for boolean expression,   BoolExp(Name(%.9),!=,Name(%.10),check)  

	 %.41 = load i32* %.9, align 4
	 %.42 = load i32* %.10, align 4
   %.43 = icmp ne i32 %.41, %.42

 ; Tagging  %.7 

	 %.46 = alloca i32, align 4
  store i32 2, i32* %.46, align 4

 ; generating code for binry op ,   LeftShift(Name(%.8), Name(%.46))  

	 %.47 = load i32* %.8, align 4
	 %.48 = load i32* %.46, align 4
	 %.49 = shl i32 %.47, %.48
  store i32 %.49, i32* %.7, align 4
	 %.50 = alloca i32, align 4
  store i32 1, i32* %.50, align 4

 ; generating code for binry op ,   Bitor(Name(%.7), Name(%.50))  

	 %.51 = load i32* %.7, align 4
	 %.52 = load i32* %.50, align 4
	 %.53 = or i32 %.51, %.52
  store i32 %.53, i32* %.7, align 4

 ; generating code for ,   IfNode(%.7,GoTo(F0),GoTo(T1))  

   br i1 %.43, label %T1, label %F0
 
 
T1:
 

 ; Tagging  %.17 

  store i32 3, i32* %.17, align 4
	 %.56 = alloca i32, align 4
  store i32 2, i32* %.56, align 4

 ; generating code for binry op ,   LeftShift(Name(%.17), Name(%.56))  

	 %.57 = load i32* %.17, align 4
	 %.58 = load i32* %.56, align 4
	 %.59 = shl i32 %.57, %.58
  store i32 %.59, i32* %.17, align 4

 ; Untagging,   Name(%.17)  

 
	 %.60 = alloca i32, align 4
  store i32 2, i32* %.60, align 4

 ; generating code for binry op ,   RightShift(Name(%.17), Name(%.60))  

	 %.63 = load i32* %.17, align 4
	 %.64 = load i32* %.60, align 4
	 %.65 = ashr i32 %.63, %.64
  store i32 %.65, i32* %.15, align 4

 ; Tagging  %.18 

  store i32 0, i32* %.18, align 4
	 %.67 = alloca i32, align 4
  store i32 2, i32* %.67, align 4

 ; generating code for binry op ,   LeftShift(Name(%.18), Name(%.67))  

	 %.68 = load i32* %.18, align 4
	 %.69 = load i32* %.67, align 4
	 %.70 = shl i32 %.68, %.69
  store i32 %.70, i32* %.18, align 4

 ; Untagging,   Name(%.18)  

 
	 %.71 = alloca i32, align 4
  store i32 2, i32* %.71, align 4

 ; generating code for binry op ,   RightShift(Name(%.18), Name(%.71))  

	 %.74 = load i32* %.18, align 4
	 %.75 = load i32* %.71, align 4
	 %.76 = ashr i32 %.74, %.75
  store i32 %.76, i32* %.16, align 4

 ; generating code for boolean expression,   BoolExp(Name(%.15),!=,Name(%.16),check)  

	 %.77 = load i32* %.15, align 4
	 %.78 = load i32* %.16, align 4
   %.79 = icmp ne i32 %.77, %.78

 ; Tagging  %.13 

	 %.82 = alloca i32, align 4
  store i32 2, i32* %.82, align 4

 ; generating code for binry op ,   LeftShift(Name(%.14), Name(%.82))  

	 %.83 = load i32* %.14, align 4
	 %.84 = load i32* %.82, align 4
	 %.85 = shl i32 %.83, %.84
  store i32 %.85, i32* %.13, align 4
	 %.86 = alloca i32, align 4
  store i32 1, i32* %.86, align 4

 ; generating code for binry op ,   Bitor(Name(%.13), Name(%.86))  

	 %.87 = load i32* %.13, align 4
	 %.88 = load i32* %.86, align 4
	 %.89 = or i32 %.87, %.88
  store i32 %.89, i32* %.13, align 4

 ; generating code for ,   IfNode(%.13,GoTo(F2),GoTo(T3))  

   br i1 %.79, label %T3, label %F2
 
 
T3:
 

 ; storing  2  in  %.6 

  store i32 2, i32* %.6, align 4
     br label %END
 
F2:
 

 ; storing  3  in  %.6 

  store i32 3, i32* %.6, align 4
     br label %END
 
END:
 
     br label %END4
 
F0:
 

 ; storing  1  in  %.6 

  store i32 1, i32* %.6, align 4
     br label %END4
 
END4:
 

 ; Tagging  %.4 

	 %.92 = alloca i32, align 4
  store i32 2, i32* %.92, align 4

 ; generating code for binry op ,   LeftShift(Name(%.6), Name(%.92))  

	 %.93 = load i32* %.6, align 4
	 %.94 = load i32* %.92, align 4
	 %.95 = shl i32 %.93, %.94
  store i32 %.95, i32* %.4, align 4

 ; generating code to print,   %.5  

	 %.96 = load i32* %.4, align 4
	 %.97 = call i32 @print_int_nl(i32%.96) 
	 ret i32 0
}
declare double @floor(double) nounwind readnone
declare double @llvm.pow.f64(double, double) nounwind readonly
