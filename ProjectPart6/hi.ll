

;  Module(Stmt([Assign(AssName(a), List([Add(Const(1), Const(2))])), Assign(AssName(b), Subscript(a,Const(0)))]))
 


; converted ast:  Module(Stmt([Assign(AssName(a), List([Add(Const(1), Const(2))])), Assign(AssName(b), Subscript(a,Const(0)))])) 






; tagged dict:  {}


; THE TAGGED AST:  Module(Stmt([Assign(AssName(a), Tag(List([Add(ConvertToInt(Tag(
;  Assign(AssName(%.7), Tag(Const(1), int))
;  Assign(AssName(%.5), ConvertToInt(Name(%.7)))
;  Assign(AssName(%.8), Tag(Const(2), int))
;  Assign(AssName(%.6), ConvertToInt(Name(%.8)))
;  Assign(AssName(%.4), Add(Name(%.5), Name(%.6)))
;  Assign(AssName(%.a), Tag(List([Name(%.4)]), list))
;  Assign(AssName(%.9), Tag(Const(0), int))
 
; the flattened dict:  {}
 
%struct.Hashtable = type {}
%struct.function = type { i8*}
declare i32 @input() nounwind uwtable ssp 
declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp 
declare i32 @htGet(%struct.Hashtable*, i8*)
declare %struct.function* @make_closure(i8*, i32)
declare i32 @insertFreeVar(%struct.function*, i8*, i32*)
declare %struct.Hashtable* @get_free_vars(%struct.function*)
declare i32 @createList(i32)
declare i32 @insertList(i32,i32,i32*)

;declaring strings for all of the free variables

; defining all of the functions
define i32 @main() nounwind uwtable ssp {
	 %.7 = alloca i32, align 4
	 %.5 = alloca i32, align 4
	 %.8 = alloca i32, align 4
	 %.6 = alloca i32, align 4
	 %.4 = alloca i32, align 4
	 %.a = alloca i32, align 4
	 %.9 = alloca i32, align 4

 ; Tagging  %.7 

  store i32 1, i32* %.7, align 4
	 %.11 = alloca i32, align 4
  store i32 2, i32* %.11, align 4

 ; generating code for binry op ,   LeftShift(Name(%.7), Name(%.11))  

	 %.12 = load i32* %.7, align 4
	 %.13 = load i32* %.11, align 4
	 %.14 = shl i32 %.12, %.13
  store i32 %.14, i32* %.7, align 4

 ; Untagging,   Name(%.7)  

 
	 %.15 = alloca i32, align 4
  store i32 2, i32* %.15, align 4

 ; generating code for binry op ,   RightShift(Name(%.7), Name(%.15))  

	 %.18 = load i32* %.7, align 4
	 %.19 = load i32* %.15, align 4
	 %.20 = ashr i32 %.18, %.19
  store i32 %.20, i32* %.5, align 4

 ; Tagging  %.8 

  store i32 2, i32* %.8, align 4
	 %.22 = alloca i32, align 4
  store i32 2, i32* %.22, align 4

 ; generating code for binry op ,   LeftShift(Name(%.8), Name(%.22))  

	 %.23 = load i32* %.8, align 4
	 %.24 = load i32* %.22, align 4
	 %.25 = shl i32 %.23, %.24
  store i32 %.25, i32* %.8, align 4

 ; Untagging,   Name(%.8)  

 
	 %.26 = alloca i32, align 4
  store i32 2, i32* %.26, align 4

 ; generating code for binry op ,   RightShift(Name(%.8), Name(%.26))  

	 %.29 = load i32* %.8, align 4
	 %.30 = load i32* %.26, align 4
	 %.31 = ashr i32 %.29, %.30
  store i32 %.31, i32* %.6, align 4

 ; generating code for binry op ,   Add(Name(%.5), Name(%.6))  

	 %.32 = load i32* %.5, align 4
	 %.33 = load i32* %.6, align 4
	 %.34 = add i32 %.32, %.33
  store i32 %.34, i32* %.4, align 4
	 %.35 = call i32 @createList(i32 1)
	 %.37 = call i32 @insertList(i32 %.35, i32 0, i32* %.4)
  store i32 %.35, i32* %.a, align 4

 ; Tagging  %.9 

  store i32 0, i32* %.9, align 4
	 %.39 = alloca i32, align 4
  store i32 2, i32* %.39, align 4

 ; generating code for binry op ,   LeftShift(Name(%.9), Name(%.39))  

	 %.40 = load i32* %.9, align 4
	 %.41 = load i32* %.39, align 4
	 %.42 = shl i32 %.40, %.41
  store i32 %.42, i32* %.9, align 4
	 ret i32 0
}
declare double @floor(double) nounwind readnone
declare double @llvm.pow.f64(double, double) nounwind readonly
