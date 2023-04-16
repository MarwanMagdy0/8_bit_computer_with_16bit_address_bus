from utiles import *
from instructions import *
import os, sys

CODE = """
porta = $0000
portb = $0001
mov x, #00
loop:
    mov a, $frame1+x
    out a, porta
    mov a, #01
    out a, portb
    mov a, #00
    out a, portb
    add x, #1
    cmp x, #2d
    mov a, #02
    out a, portb
    jz $reset
    jmp $loop    

reset:
    mov x, #00
    jmp $loop


frame1:
    db 0 0 8 24 4 24 8 0 24 24 7c 20 0 50 50 7c 0 74 54 7c 0 4 4 7c 0 5c 54 74 0 7c 24 6c 0 7c 54 5c 0 7c 14 1c 0 7c 54 7c 0

"""
file_path= os.path.dirname(__file__)+"\\"
os.chdir(file_path)
if len(sys.argv)==2:
    with open(sys.argv[1], "r") as file:
        CODE = file.read()
    
CODE = CODE.strip()
preprocessed_ops = preprocessing_commenting_and_cleaning(CODE.split("\n"))
preprocessed_ops = preprcessing_labels_and_constants(preprocessed_ops)
binary_code = "v2.0 raw\n"
instruction_pointer = 0
for line in preprocessed_ops:
    print("{:04x}".format(instruction_pointer), end=": ")
    line_code = ""
    if line[0] == "MOV":
        line_code +=handle_multi_operand(line, MOV_A_X, MOV_A_NUM, MOV_A_ADDR, MOV_X_A, MOV_X_NUM, MOV_X_ADDR, MOV_A_ADDR_X)
        instruction_pointer+=instruction_pointer_for_multi_op_instruction(line)
    
    elif line[0] == "ADD":
        line_code +=handle_multi_operand(line, ADD_A_X, ADD_A_NUM, ADD_A_ADDR, ADD_X_A, ADD_X_NUM, ADD_X_ADDR)
        instruction_pointer+=instruction_pointer_for_multi_op_instruction(line)

    
    elif line[0] == "SUB":
        line_code +=handle_multi_operand(line, SUB_A_X, SUB_A_NUM, SUB_A_ADDR, SUB_X_A, SUB_X_NUM, SUB_X_ADDR)
        instruction_pointer+=instruction_pointer_for_multi_op_instruction(line)
    
    elif line[0] == "CMP":
        line_code +=handle_multi_operand(line, CMP_A_X, CMP_A_NUM, CMP_A_ADDR, CMP_X_A, CMP_X_NUM, CMP_X_ADDR)
        instruction_pointer+=instruction_pointer_for_multi_op_instruction(line)
    
    elif line[0] == "OUT":
        if line[1] == "A":
            line_code += inst2hex(OUT_A_ADDR) + address2hex(line[2])[0:2] + " "
            instruction_pointer+=2
    elif line[0]=="JMP":
        instruction_pointer+=3
        if line[1].startswith("$"):
            line_code += inst2hex(JMP) + address2hex(line[1])
        else:
            error_print(line, f"{line[1]} is not defined")
    elif line[0]=="JSR":
        instruction_pointer+=3
        if line[1].startswith("$"):
            line_code += inst2hex(JSR) + address2hex(line[1])
        else:
            error_print(line, f"{line[1]} is not defined")
    elif line[0]=="JC":
        instruction_pointer+=3
        if line[1].startswith("$"):
            line_code += inst2hex(JC) + address2hex(line[1])
        else:
            error_print(line, f"{line[1]} is not defined")
    elif line[0]=="JZ":
        instruction_pointer+=3
        if line[1].startswith("$"):
            line_code += inst2hex(JZ) + address2hex(line[1])
        else:
            error_print(line, f"{line[1]} is not defined")

    elif line[0]=="RET":
        instruction_pointer+=1
        line_code += inst2hex(RET)

    elif line[0]=="DB":
        for hex_byte in line[1:]:
            line_code += hex_byte.lower() + " "
            instruction_pointer+=1

    str_line = " ".join(line)
    print("{:<{}}".format(str_line, 15),"-->", line_code)
    binary_code+=line_code

print("hex code:")
print("  ",binary_code[9:])

with open("output", "w") as file: # Writing to the file
    file.write(binary_code)
