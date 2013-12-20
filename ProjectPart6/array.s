; ModuleID = 'array.c'
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.8.0"

@.str = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define i32* @createList(i32 %size) nounwind ssp uwtable {
  %1 = alloca i32, align 4
  %a = alloca i32*, align 8
  store i32 %size, i32* %1, align 4
  %2 = load i32* %1, align 4
  %3 = sext i32 %2 to i64
  %4 = mul i64 4, %3
  %5 = call i8* @malloc(i64 %4)
  %6 = bitcast i8* %5 to i32*
  store i32* %6, i32** %a, align 8
  %7 = load i32** %a, align 8
  ret i32* %7
}

declare i8* @malloc(i64)

define i32 @main() nounwind ssp uwtable {
  %1 = alloca i32, align 4
  %ptr = alloca i32*, align 8
  %iptr = alloca i32*, align 8
  store i32 0, i32* %1
  %2 = call i32* @createList(i32 3)
  store i32* %2, i32** %ptr, align 8
  %3 = call i32* @createList(i32 3)
  %4 = load i32** %ptr, align 8
  store i32* %4, i32** %iptr, align 8
  %5 = load i32** %ptr, align 8
  store i32 1, i32* %5, align 4
  %6 = load i32** %ptr, align 8
  %7 = getelementptr inbounds i32* %6, i64 1
  store i32 2, i32* %7, align 4
  %8 = load i32** %ptr, align 8
  %9 = getelementptr inbounds i32* %8, i64 2
  store i32 3, i32* %9, align 4
  %10 = load i32** %iptr, align 8
  %11 = load i32* %10, align 4
  %12 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str, i32 0, i32 0), i32 %11)
  %13 = load i32** %iptr, align 8
  %14 = getelementptr inbounds i32* %13, i64 1
  %15 = load i32* %14, align 4
  %16 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str, i32 0, i32 0), i32 %15)
  %17 = load i32** %iptr, align 8
  %18 = getelementptr inbounds i32* %17, i64 3
  %19 = load i32* %18, align 4
  %20 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str, i32 0, i32 0), i32 %19)
  ret i32 0
}

declare i32 @printf(i8*, ...)
