;  Module(Stmt([Assign(AssName(x), Const(3)), Assign(AssName(y), Const(0)), WhileNode(BoolExp(Name(x),>,Name(y),check),[Printnl([Name(x)]), Assign(AssName(x), Sub(Name(x), Const(1)))])]))
 
;  Module(Stmt([Assign(AssName(x), Tag(Const(3), int)), Assign(AssName(y), Tag(Const(0), int)), WhileNode(Tag(BoolExp(ConvertToInt(Name(x)),>,ConvertToInt(Name(y)),check), bool),[Printnl([Name(x)]), Assign(AssName(x), Tag(Sub(ConvertToInt(Name(x)), ConvertToInt(Tag(Const(1), int))), int))])]))
 
;  Assign(AssName(%.x), Tag(Const(3), int))
;  Assign(AssName(%.y), Tag(Const(0), int))
;  GoTo(BOTTOM0)
;  Label(TOP2)
;  Assign(AssName(%.5), Printnl([Name(%.x)]))
;  Assign(AssName(%.7), ConvertToInt(Name(%.x)))
;  Assign(AssName(%.10), Tag(Const(1), int))
;  Assign(AssName(%.8), ConvertToInt(Name(%.10)))
;  Assign(AssName(%.6), Sub(Name(%.7), Name(%.8)))
;  Assign(AssName(%.x), Tag(Name(%.6), int))
;  GoTo(BOTTOM0)
;  Label(BOTTOM0)
;  Assign(AssName(%.13), ConvertToInt(Name(%.x)))
;  Assign(AssName(%.14), ConvertToInt(Name(%.y)))
;  Assign(AssName(%.12), BoolExp(Name(%.13),>,Name(%.14),check))
;  Assign(AssName(%.11), Tag(Name(%.12), bool))
;  IfNode(%.11,GoTo(END1),GoTo(TOP2),)
;  GoTo(END1)
;  Label(END1)
 
declare i32 @input() nounwind uwtable ssp 
declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp 
define i32 @main() nounwind uwtable ssp {
	 %.x = alloca i32, align 4
	 %.y = alloca i32, align 4
	 %.5 = alloca i32, align 4
	 %.7 = alloca i32, align 4
	 %.10 = alloca i32, align 4
	 %.8 = alloca i32, align 4
	 %.6 = alloca i32, align 4
	 %.13 = alloca i32, align 4
	 %.14 = alloca i32, align 4
	 %.12 = alloca i32, align 4
	 %.11 = alloca i32, align 4

 ; Tagging  Tag(Const(3), int)  and assign to:  %.x 

  store i32 3, i32* %.x, align 4
	 %.18 = alloca i32, align 4
  store i32 2, i32* %.18, align 4

 ; generating code for binry op ,   LeftShift(Name(%.x), Name(%.18))  to assign to  %.x  

	 %.19 = load i32* %.x, align 4
	 %.20 = load i32* %.18, align 4
	 %.21 = shl i32 %.19, %.20
  store i32 %.21, i32* %.x, align 4
   

 ; Tagging  Tag(Const(0), int)  and assign to:  %.y 

  store i32 0, i32* %.y, align 4
	 %.23 = alloca i32, align 4
  store i32 2, i32* %.23, align 4

 ; generating code for binry op ,   LeftShift(Name(%.y), Name(%.23))  to assign to  %.y  

	 %.24 = load i32* %.y, align 4
	 %.25 = load i32* %.23, align 4
	 %.26 = shl i32 %.24, %.25
  store i32 %.26, i32* %.y, align 4
   
     br label %BOTTOM0
 
TOP2:
 

 ; generating code to print,   Printnl([Name(%.x)])  

	 %.27 = load i32* %.x, align 4
	 %.28 = call i32 @print_int_nl(i32%.27) 

 ; Untagging,   ConvertToInt(Name(%.x))  and assign to  %.7  

 
	 %.29 = alloca i32, align 4
  store i32 2, i32* %.29, align 4

 ; generating code for binry op ,   RightShift(Name(%.x), Name(%.29))  to assign to  %.7  

	 %.32 = load i32* %.x, align 4
	 %.33 = load i32* %.29, align 4
	 %.34 = ashr i32 %.32, %.33
  store i32 %.34, i32* %.7, align 4
   

 ; Tagging  Tag(Const(1), int)  and assign to:  %.10 

  store i32 1, i32* %.10, align 4
	 %.36 = alloca i32, align 4
  store i32 2, i32* %.36, align 4

 ; generating code for binry op ,   LeftShift(Name(%.10), Name(%.36))  to assign to  %.10  

	 %.37 = load i32* %.10, align 4
	 %.38 = load i32* %.36, align 4
	 %.39 = shl i32 %.37, %.38
  store i32 %.39, i32* %.10, align 4
   

 ; Untagging,   ConvertToInt(Name(%.10))  and assign to  %.8  

 
	 %.40 = alloca i32, align 4
  store i32 2, i32* %.40, align 4

 ; generating code for binry op ,   RightShift(Name(%.10), Name(%.40))  to assign to  %.8  

	 %.43 = load i32* %.10, align 4
	 %.44 = load i32* %.40, align 4
	 %.45 = ashr i32 %.43, %.44
  store i32 %.45, i32* %.8, align 4
   

 ; generating code for binry op ,   Sub(Name(%.7), Name(%.8))  to assign to  %.6  

	 %.46 = load i32* %.7, align 4
	 %.47 = load i32* %.8, align 4
	 %.48 = sub i32 %.46, %.47
  store i32 %.48, i32* %.6, align 4
   

 ; Tagging  Tag(Name(%.6), int)  and assign to:  %.x 

	 %.50 = alloca i32, align 4
  store i32 2, i32* %.50, align 4

 ; generating code for binry op ,   LeftShift(Name(%.6), Name(%.50))  to assign to  %.x  

	 %.51 = load i32* %.6, align 4
	 %.52 = load i32* %.50, align 4
	 %.53 = shl i32 %.51, %.52
  store i32 %.53, i32* %.x, align 4
   
     br label %BOTTOM0
 
BOTTOM0:
 

 ; Untagging,   ConvertToInt(Name(%.x))  and assign to  %.13  

 
	 %.54 = alloca i32, align 4
  store i32 2, i32* %.54, align 4

 ; generating code for binry op ,   RightShift(Name(%.x), Name(%.54))  to assign to  %.13  

	 %.57 = load i32* %.x, align 4
	 %.58 = load i32* %.54, align 4
	 %.59 = ashr i32 %.57, %.58
  store i32 %.59, i32* %.13, align 4
   

 ; Untagging,   ConvertToInt(Name(%.y))  and assign to  %.14  

 
	 %.60 = alloca i32, align 4
  store i32 2, i32* %.60, align 4

 ; generating code for binry op ,   RightShift(Name(%.y), Name(%.60))  to assign to  %.14  

	 %.63 = load i32* %.y, align 4
	 %.64 = load i32* %.60, align 4
	 %.65 = ashr i32 %.63, %.64
  store i32 %.65, i32* %.14, align 4
   

 ; generating code for boolean expression,   BoolExp(Name(%.13),>,Name(%.14),check)  and assign to %.12 

	 %.66 = load i32* %.13, align 4
	 %.67 = load i32* %.14, align 4
  %.68 = icmp sgt i32 %.66, %.67
	 %.69 = zext i1 %.68 to i32
 
  store i32 %.69, i32* %.12, align 4

 ; Tagging  Tag(Name(%.12), bool)  and assign to:  %.11 

	 %.71 = alloca i32, align 4
  store i32 2, i32* %.71, align 4

 ; generating code for binry op ,   LeftShift(Name(%.12), Name(%.71))  to assign to  %.11  

	 %.72 = load i32* %.12, align 4
	 %.73 = load i32* %.71, align 4
	 %.74 = shl i32 %.72, %.73
  store i32 %.74, i32* %.11, align 4
   
	 %.75 = alloca i32, align 4
  store i32 1, i32* %.75, align 4

 ; generating code for binry op ,   Bitor(Name(%.11), Name(%.75))  to assign to  %.11  

	 %.76 = load i32* %.11, align 4
	 %.77 = load i32* %.75, align 4
	 %.78 = or i32 %.76, %.77
  store i32 %.78, i32* %.11, align 4
   

 ; generating code for ,   IfNode(%.11,GoTo(END1),GoTo(TOP2),)  where the x val is  %.79  

	 %.80 = load i32* %.11, align 4
    %.81  = alloca i32, align 4
  store i32 2, i32* %.81, align 4
	 %.82 = load i32* %.81, align 4
   %.83  = ashr i32  %.80 ,  %.82
  %.84  = trunc i32  %.83  to i1
       br i1 %.84, label %TOP2, label %END1
     br label %END1
 
END1:
 
	 ret i32 0
}
declare double @floor(double) nounwind readnone
declare double @llvm.pow.f64(double, double) nounwind readonly
