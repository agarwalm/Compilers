;  Module(Stmt([Assign(AssName(x), Bitand(Const(1), Const(0))), Assign(AssName(y), Bitand(Bitand(Bitand(Name(x), Const(3)), Const(2)), Const(5)))]))
 
;  Module(Stmt([Assign(AssName(x), Tag(Bitand(ConvertToInt(Tag(Const(1), int)), ConvertToInt(Tag(Const(0), int))), int)), Assign(AssName(y), Tag(Bitand(ConvertToInt(Tag(Bitand(ConvertToInt(Tag(Bitand(ConvertToInt(Name(x)), ConvertToInt(Tag(Const(3), int))), int)), ConvertToInt(Tag(Const(2), int))), int)), ConvertToInt(Tag(Const(5), int))), int))]))
 
;  Assign(AssName(%.7), Tag(Const(1), int))
;  Assign(AssName(%.5), ConvertToInt(Name(%.7)))
;  Assign(AssName(%.8), Tag(Const(0), int))
;  Assign(AssName(%.6), ConvertToInt(Name(%.8)))
;  Assign(AssName(%.4), Bitand(Name(%.5), Name(%.6)))
;  Assign(AssName(%.x), Tag(Name(%.4), int))
;  Assign(AssName(%.18), ConvertToInt(Name(%.x)))
;  Assign(AssName(%.21), Tag(Const(3), int))
;  Assign(AssName(%.19), ConvertToInt(Name(%.21)))
;  Assign(AssName(%.17), Bitand(Name(%.18), Name(%.19)))
;  Assign(AssName(%.16), Tag(Name(%.17), int))
;  Assign(AssName(%.14), ConvertToInt(Name(%.16)))
;  Assign(AssName(%.22), Tag(Const(2), int))
;  Assign(AssName(%.15), ConvertToInt(Name(%.22)))
;  Assign(AssName(%.13), Bitand(Name(%.14), Name(%.15)))
;  Assign(AssName(%.12), Tag(Name(%.13), int))
;  Assign(AssName(%.10), ConvertToInt(Name(%.12)))
;  Assign(AssName(%.23), Tag(Const(5), int))
;  Assign(AssName(%.11), ConvertToInt(Name(%.23)))
;  Assign(AssName(%.9), Bitand(Name(%.10), Name(%.11)))
;  Assign(AssName(%.y), Tag(Name(%.9), int))
 
declare i32 @input() nounwind uwtable ssp 
declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp 
define i32 @main() nounwind uwtable ssp {
	 %.7 = alloca i32, align 4
	 %.5 = alloca i32, align 4
	 %.8 = alloca i32, align 4
	 %.6 = alloca i32, align 4
	 %.4 = alloca i32, align 4
	 %.x = alloca i32, align 4
	 %.18 = alloca i32, align 4
	 %.21 = alloca i32, align 4
	 %.19 = alloca i32, align 4
	 %.17 = alloca i32, align 4
	 %.16 = alloca i32, align 4
	 %.14 = alloca i32, align 4
	 %.22 = alloca i32, align 4
	 %.15 = alloca i32, align 4
	 %.13 = alloca i32, align 4
	 %.12 = alloca i32, align 4
	 %.10 = alloca i32, align 4
	 %.23 = alloca i32, align 4
	 %.11 = alloca i32, align 4
	 %.9 = alloca i32, align 4
	 %.y = alloca i32, align 4

 ; Tagging  Tag(Const(1), int)  and assign to:  %.7 

  store i32 1, i32* %.7, align 4
	 %.25 = alloca i32, align 4
  store i32 2, i32* %.25, align 4

 ; generating code for binry op ,   LeftShift(Name(%.7), Name(%.25))  to assign to  %.7  

	 %.26 = load i32* %.7, align 4
	 %.27 = load i32* %.25, align 4
	 %.28 = shl i32 %.26, %.27
  store i32 %.28, i32* %.7, align 4
   

 ; Untagging,   ConvertToInt(Name(%.7))  and assign to  %.5  

 
	 %.29 = alloca i32, align 4
  store i32 2, i32* %.29, align 4

 ; generating code for binry op ,   RightShift(Name(%.7), Name(%.29))  to assign to  %.5  

	 %.32 = load i32* %.7, align 4
	 %.33 = load i32* %.29, align 4
	 %.34 = ashr i32 %.32, %.33
  store i32 %.34, i32* %.5, align 4
   

 ; Tagging  Tag(Const(0), int)  and assign to:  %.8 

  store i32 0, i32* %.8, align 4
	 %.36 = alloca i32, align 4
  store i32 2, i32* %.36, align 4

 ; generating code for binry op ,   LeftShift(Name(%.8), Name(%.36))  to assign to  %.8  

	 %.37 = load i32* %.8, align 4
	 %.38 = load i32* %.36, align 4
	 %.39 = shl i32 %.37, %.38
  store i32 %.39, i32* %.8, align 4
   

 ; Untagging,   ConvertToInt(Name(%.8))  and assign to  %.6  

 
	 %.40 = alloca i32, align 4
  store i32 2, i32* %.40, align 4

 ; generating code for binry op ,   RightShift(Name(%.8), Name(%.40))  to assign to  %.6  

	 %.43 = load i32* %.8, align 4
	 %.44 = load i32* %.40, align 4
	 %.45 = ashr i32 %.43, %.44
  store i32 %.45, i32* %.6, align 4
   

 ; generating code for binry op ,   Bitand(Name(%.5), Name(%.6))  to assign to  %.4  

	 %.46 = load i32* %.5, align 4
	 %.47 = load i32* %.6, align 4
	 %.48 = and i32 %.46, %.47
  store i32 %.48, i32* %.4, align 4
   

 ; Tagging  Tag(Name(%.4), int)  and assign to:  %.x 

	 %.50 = alloca i32, align 4
  store i32 2, i32* %.50, align 4

 ; generating code for binry op ,   LeftShift(Name(%.4), Name(%.50))  to assign to  %.x  

	 %.51 = load i32* %.4, align 4
	 %.52 = load i32* %.50, align 4
	 %.53 = shl i32 %.51, %.52
  store i32 %.53, i32* %.x, align 4
   

 ; Untagging,   ConvertToInt(Name(%.x))  and assign to  %.18  

 
	 %.54 = alloca i32, align 4
  store i32 2, i32* %.54, align 4

 ; generating code for binry op ,   RightShift(Name(%.x), Name(%.54))  to assign to  %.18  

	 %.57 = load i32* %.x, align 4
	 %.58 = load i32* %.54, align 4
	 %.59 = ashr i32 %.57, %.58
  store i32 %.59, i32* %.18, align 4
   

 ; Tagging  Tag(Const(3), int)  and assign to:  %.21 

  store i32 3, i32* %.21, align 4
	 %.61 = alloca i32, align 4
  store i32 2, i32* %.61, align 4

 ; generating code for binry op ,   LeftShift(Name(%.21), Name(%.61))  to assign to  %.21  

	 %.62 = load i32* %.21, align 4
	 %.63 = load i32* %.61, align 4
	 %.64 = shl i32 %.62, %.63
  store i32 %.64, i32* %.21, align 4
   

 ; Untagging,   ConvertToInt(Name(%.21))  and assign to  %.19  

 
	 %.65 = alloca i32, align 4
  store i32 2, i32* %.65, align 4

 ; generating code for binry op ,   RightShift(Name(%.21), Name(%.65))  to assign to  %.19  

	 %.68 = load i32* %.21, align 4
	 %.69 = load i32* %.65, align 4
	 %.70 = ashr i32 %.68, %.69
  store i32 %.70, i32* %.19, align 4
   

 ; generating code for binry op ,   Bitand(Name(%.18), Name(%.19))  to assign to  %.17  

	 %.71 = load i32* %.18, align 4
	 %.72 = load i32* %.19, align 4
	 %.73 = and i32 %.71, %.72
  store i32 %.73, i32* %.17, align 4
   

 ; Tagging  Tag(Name(%.17), int)  and assign to:  %.16 

	 %.75 = alloca i32, align 4
  store i32 2, i32* %.75, align 4

 ; generating code for binry op ,   LeftShift(Name(%.17), Name(%.75))  to assign to  %.16  

	 %.76 = load i32* %.17, align 4
	 %.77 = load i32* %.75, align 4
	 %.78 = shl i32 %.76, %.77
  store i32 %.78, i32* %.16, align 4
   

 ; Untagging,   ConvertToInt(Name(%.16))  and assign to  %.14  

 
	 %.79 = alloca i32, align 4
  store i32 2, i32* %.79, align 4

 ; generating code for binry op ,   RightShift(Name(%.16), Name(%.79))  to assign to  %.14  

	 %.82 = load i32* %.16, align 4
	 %.83 = load i32* %.79, align 4
	 %.84 = ashr i32 %.82, %.83
  store i32 %.84, i32* %.14, align 4
   

 ; Tagging  Tag(Const(2), int)  and assign to:  %.22 

  store i32 2, i32* %.22, align 4
	 %.86 = alloca i32, align 4
  store i32 2, i32* %.86, align 4

 ; generating code for binry op ,   LeftShift(Name(%.22), Name(%.86))  to assign to  %.22  

	 %.87 = load i32* %.22, align 4
	 %.88 = load i32* %.86, align 4
	 %.89 = shl i32 %.87, %.88
  store i32 %.89, i32* %.22, align 4
   

 ; Untagging,   ConvertToInt(Name(%.22))  and assign to  %.15  

 
	 %.90 = alloca i32, align 4
  store i32 2, i32* %.90, align 4

 ; generating code for binry op ,   RightShift(Name(%.22), Name(%.90))  to assign to  %.15  

	 %.93 = load i32* %.22, align 4
	 %.94 = load i32* %.90, align 4
	 %.95 = ashr i32 %.93, %.94
  store i32 %.95, i32* %.15, align 4
   

 ; generating code for binry op ,   Bitand(Name(%.14), Name(%.15))  to assign to  %.13  

	 %.96 = load i32* %.14, align 4
	 %.97 = load i32* %.15, align 4
	 %.98 = and i32 %.96, %.97
  store i32 %.98, i32* %.13, align 4
   

 ; Tagging  Tag(Name(%.13), int)  and assign to:  %.12 

	 %.100 = alloca i32, align 4
  store i32 2, i32* %.100, align 4

 ; generating code for binry op ,   LeftShift(Name(%.13), Name(%.100))  to assign to  %.12  

	 %.101 = load i32* %.13, align 4
	 %.102 = load i32* %.100, align 4
	 %.103 = shl i32 %.101, %.102
  store i32 %.103, i32* %.12, align 4
   

 ; Untagging,   ConvertToInt(Name(%.12))  and assign to  %.10  

 
	 %.104 = alloca i32, align 4
  store i32 2, i32* %.104, align 4

 ; generating code for binry op ,   RightShift(Name(%.12), Name(%.104))  to assign to  %.10  

	 %.107 = load i32* %.12, align 4
	 %.108 = load i32* %.104, align 4
	 %.109 = ashr i32 %.107, %.108
  store i32 %.109, i32* %.10, align 4
   

 ; Tagging  Tag(Const(5), int)  and assign to:  %.23 

  store i32 5, i32* %.23, align 4
	 %.111 = alloca i32, align 4
  store i32 2, i32* %.111, align 4

 ; generating code for binry op ,   LeftShift(Name(%.23), Name(%.111))  to assign to  %.23  

	 %.112 = load i32* %.23, align 4
	 %.113 = load i32* %.111, align 4
	 %.114 = shl i32 %.112, %.113
  store i32 %.114, i32* %.23, align 4
   

 ; Untagging,   ConvertToInt(Name(%.23))  and assign to  %.11  

 
	 %.115 = alloca i32, align 4
  store i32 2, i32* %.115, align 4

 ; generating code for binry op ,   RightShift(Name(%.23), Name(%.115))  to assign to  %.11  

	 %.118 = load i32* %.23, align 4
	 %.119 = load i32* %.115, align 4
	 %.120 = ashr i32 %.118, %.119
  store i32 %.120, i32* %.11, align 4
   

 ; generating code for binry op ,   Bitand(Name(%.10), Name(%.11))  to assign to  %.9  

	 %.121 = load i32* %.10, align 4
	 %.122 = load i32* %.11, align 4
	 %.123 = and i32 %.121, %.122
  store i32 %.123, i32* %.9, align 4
   

 ; Tagging  Tag(Name(%.9), int)  and assign to:  %.y 

	 %.125 = alloca i32, align 4
  store i32 2, i32* %.125, align 4

 ; generating code for binry op ,   LeftShift(Name(%.9), Name(%.125))  to assign to  %.y  

	 %.126 = load i32* %.9, align 4
	 %.127 = load i32* %.125, align 4
	 %.128 = shl i32 %.126, %.127
  store i32 %.128, i32* %.y, align 4
   
	 ret i32 0
}
declare double @floor(double) nounwind readnone
declare double @llvm.pow.f64(double, double) nounwind readonly
