#########################
#	REVERSE STRING		#
#########################

		        .data
cArray:	    	.asciiz		"Teacher: Tran Thanh Binh"
cArray_size:	.word		24
eol:	    	.asciiz		"\n"
	        	.text
main:
	la	    	$a0, cArray				# print original string
	li	    	$v0, 4
	syscall
	la	    	$a0, eol				# println
	li	    	$v0, 4
	syscall
	la	    	$a0, cArray				# load array pointer
	lw	      	$a1, cArray_size		# load array size
	jal		    reverse					# function call
								        # $ra = PC + 4, PC = reverse
	li		    $v0, 4					# output string
	syscall
	li		    $v0, 10					
	syscall
# end main

reverse:
	move		$t2, $a0				# t2 -> a0
	move		$t3, $a0
	add		    $t3, $t3, $a1			
	addi		$t3, $t3, -1				# t3 -> a0 end
	for_loop:
		bge		$t2, $t3, exit_for_loop		# for_loop condition
		lbu		$t4, 0($t2)			        # t4 = cArray[i]
		lbu		$t5, 0($t3)			        # t5 = cArray[size - 1 - i]
		sb		$t4, 0($t3)			        # swap
		sb		$t5, 0($t2)
		addi		$t2, $t2, 1			    # increment pointer t2
		addi		$t3, $t3, -1			# decrement pointer t3
		j		for_loop
	exit_for_loop:
	jr		$ra
# end reverse	
	
	
	

