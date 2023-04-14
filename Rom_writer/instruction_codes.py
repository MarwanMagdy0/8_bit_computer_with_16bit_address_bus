from controll_constants import *

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_2_DB | IP_INC | IP_2_AB)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
""" 
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_A | IR_RESET | IP_INC, "LDA")
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_X | IR_RESET | IP_INC, "LDX")

add_instruction(X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, "ADD_A_X")
add_instruction(X_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET, "ADD_X_A")

add_instruction(CPL_A | CPL_OUT | X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, "SUB_A_X")
add_instruction(CPL_A | CPL_OUT | A_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | ALU_S0, "SUB_X_A")

add_instruction(IP_2_AB | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_INC,"ADD_A_NUM")
add_instruction(IP_2_AB | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0, "ADD_X_NUM")

add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_INC, "SUB_A_NUM")
add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0, "SUB_X_NUM")

add_instruction(IR_RESET, "NOP")


add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, "JMP")
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH, "JMP")
add_instruction(A_2_AB | IP_INP | IR_RESET, "JMP")

add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC,"LDA_ADDR")
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC,"LDA_ADDR")
add_instruction(A_2_AB  | R_2_DB | Z_A | ALU_2_A | IR_RESET,"LDA_ADDR")

add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC,"LDX_ADDR")
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC,"LDX_ADDR")
add_instruction(A_2_AB  | R_2_DB | Z_A | ALU_2_X | IR_RESET,"LDX_ADDR")

add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, "JSR")
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, "JSR")
add_instruction(SP_2_AB | IPL_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT, "JSR")
add_instruction(SP_2_AB | IPH_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT, "JSR")
add_instruction(A_2_AB | IP_INP | IR_RESET, "JSR")

add_instruction(SP_2_AB | ALU_2_AH | Z_A | R_2_DB, "RET")
add_instruction(Z_D | CPL_D | ALU_2_SP | SP_2_AB | ALU_S1, "RET")
add_instruction(SP_2_AB | R_2_DB | ALU_2_AL | Z_A, "RET")
add_instruction(Z_D | CPL_D | ALU_2_SP | ALU_S1 | A_2_AB | IP_INP | IR_RESET, "RET")

add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AL | IP_INC, "STA_ADDR")
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AH | IP_INC, "STA_ADDR")
add_instruction(A_2_AB | A_2_DB | R_STR | IR_RESET, "STA_ADDR")

add_conditional_carry_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, IP_INC, "JC")
add_conditional_carry_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, IP_INC | IR_RESET, "JC")
add_conditional_carry_instruction(A_2_AB | IP_INP | IR_RESET, 0, "JC")

add_conditional_zero_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, IP_INC, "JZ")
add_conditional_zero_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, IP_INC | IR_RESET, "JZ")
add_conditional_zero_instruction(A_2_AB | IP_INP | IR_RESET, 0, "JZ")
with open("ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))


print("ROM WRITER DONE..")