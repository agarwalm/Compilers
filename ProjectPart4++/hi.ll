;  Module(Stmt([IfNode(BoolExp(Not(Const(3)),==,Const(4),check),[Printnl([Const(2)])],[],)]))
 
;  Module(Stmt([IfNode(Tag(BoolExp(ConvertToInt(Tag(Not(ConvertToBool(Tag(Const(3), int))), bool)),==,ConvertToInt(Tag(Const(4), int)),check), bool),[Printnl([Tag(Const(2), int)])],[],)]))
 
; don't print end!

;  Assign(AssName(%.11), Tag(Const(3), int))
;  Assign(AssName(%.10), ConvertToBool(Name(%.11)))
;  Assign(AssName(%.9), Not(%.10))
;  Assign(AssName(%.8), Tag(Name(%.9), bool))
;  Assign(AssName(%.6), ConvertToInt(Name(%.8)))
;  Assign(AssName(%.12), Tag(Const(4), int))
;  Assign(AssName(%.7), ConvertToInt(Name(%.12)))
;  Assign(AssName(%.5), BoolExp(Name(%.6),==,Name(%.7),check))
;  Assign(AssName(%.4), Tag(Name(%.5), bool))
;  IfNode(%.4,GoTo(END),GoTo(T1),)
;  Label(T1)
;  Assign(AssName(%.13), Tag(Const(2), int))
;  Assign(AssName(%.14), Printnl([Name(%.13)]))
;  GoTo(END)
;  Label(END)
 
declare i32 @input() nounwind uwtable ssp 
declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp 
define i32 @main() nounwind uwtable ssp {
	 %.11 = alloca i32, align 4
	 %.10 = alloca i32, align 4
	 %.9 = alloca i32, align 4
	 %.8 = alloca i32, align 4
	 %.6 = alloca i32, align 4
	 %.12 = alloca i32, align 4
	 %.7 = alloca i32, align 4
	 %.5 = alloca i32, align 4
	 %.4 = alloca i32, align 4
	 %.13 = alloca i32, align 4
	 %.14 = alloca i32, align 4

 ; Tagging  %.11 

  store i32 3, i32* %.11, align 4
	 %.16 = alloca i32, align 4
  store i32 2, i32* %.16, align 4

 ; generating code for binry op ,   LeftShift(Name(%.11), Name(%.16))  

	 %.17 = load i32* %.11, align 4
	 %.18 = load i32* %.16, align 4
	 %.19 = shl i32 %.17, %.18
  store i32 %.19, i32* %.11, align 4
 
	 %.20 = alloca i32, align 4
  store i32 2, i32* %.20, align 4

 ; generating code for binry op ,   RightShift(Name(%.11), Name(%.20))  

	 %.23 = load i32* %.11, align 4
	 %.24 = load i32* %.20, align 4
	 %.25 = ashr i32 %.23, %.24
  store i32 %.25, i32* %.10, align 4
