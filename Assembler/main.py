from utiles import *
from instructions import *
import os, sys

CODE = """
mov a, #12
mov x, #34

push x
push a
ret

halt:
    jmp $halt
"""
file_path= os.path.dirname(__file__)+"\\"
os.chdir(file_path)
if len(sys.argv)==2:
    with open(sys.argv[1], "r") as file:
        CODE = file.read()
    
CODE = CODE.strip()
preprocessed_ops = preprocessing_commenting_and_cleaning(CODE.split("\n"))
preprocessed_ops = preprcessing_labels_and_constants(preprocessed_ops)
# print(preprocessed_ops)
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
    
    elif line[0] == "PUSH":
        if line[1] == "A":
            line_code += inst2hex(PUSH_A)
            instruction_pointer+=1
        elif line[1] == "X":
            line_code += inst2hex(PUSH_X)
            instruction_pointer+=1
    elif line[0] == "PULL":
        if line[1] == "A":
            line_code += inst2hex(PULL_A)
            instruction_pointer+=1
        elif line[1] == "X":
            line_code += inst2hex(PULL_X)
            instruction_pointer+=1

    str_line = " ".join(line)
    print("{:<{}}".format(str_line, 15),"-->", line_code)
    binary_code+=line_code

print("hex code:")
print("  ",binary_code[9:])

with open("output", "w") as file: # Writing to the file
    file.write(binary_code)
