	.text
	addi	$a0, $a0, 10
	li	$t1, 0x41a40000
	mtc1	$t1, $f1
	add.s	$f12, $f12, $f1
	li	$t1, 0x41ec0000
	mtc1	$t1, $f1
	add.s	$f12, $f12, $f1
	mtc1	$a0, $f1
	cvt.s.w	$f1, $f1
	add.s	$f12, $f12, $f1
	li	$v0, 2
	syscall
