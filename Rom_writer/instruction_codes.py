from controll_constants import *

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_2_DB | IP_SEL | IP_2_AB)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
""" 
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_A | IR_RESET | IP_SEL, 0b001) # LDA
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_X | IR_RESET | IP_SEL, 0b001) # LDX

add_instruction(X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, 0b001) # A = A + X
add_instruction(X_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET, 0b001) # X = A + X

add_instruction(CPL_A | CPL_OUT | X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, 0b001) # A = A - X
add_instruction(CPL_D | CPL_OUT | X_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET, 0b001) # X = X - A

add_instruction(IP_2_AB | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_SEL, 0b001) # A = A + NUM
add_instruction(IP_2_AB | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_SEL | ALU_S0, 0b001) # X = X + NUM

add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_SEL, 0b001) # A = A - NUM
add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_SEL | ALU_S0, 0b001) # X = X - NUM

add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_SEL, 0b001)
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH, 0b010)
add_instruction(A_2_AB | IP_INP | IP_SEL | IR_RESET, 0b011)

add_instruction(IR_RESET, 0b001) # NOP

with open("ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))


print("ROM WRITER DONE..")