; Hello.j

; Generated by ClassFileAnalyzer (Can)
; Analyzer and Disassembler for Java class files
; (Jasmin syntax 2, http://jasmin.sourceforge.net)
;
; ClassFileAnalyzer, version 0.7.0 


.bytecode 52.0
.source Hello.java
.class public Hello
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 1
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 1
  .line 3
  0: getstatic java/lang/System/out Ljava/io/PrintStream;
  3: ldc "Hello mom"
  5: invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
  .line 4
  8: return
.end method

