from controll_constants import *

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_2_DB | IP_INC | IP_2_AB)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
"""
add_instruction(IR_RESET, "NOP")
# MOVE INSTRUCTION
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_A | IR_RESET | IP_INC, "mov a, #num")
add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_X | IR_RESET | IP_INC, "mov x, #num")

add_instruction(A_2_DB | Z_A | ALU_2_X | IR_RESET , "mov x, a")
add_instruction(X_2_DB | Z_A | ALU_2_A | IR_RESET , "mov a, x")

add_relative_instruction(R_STR | A_2_DB, "mov $addr, a")

add_relative_instruction(R_STR | X_2_DB, "mov $addr, x")


add_relative_instruction(R_2_DB | Z_A | ALU_2_A, "mov a, $addr")

add_relative_instruction(R_2_DB | Z_A | ALU_2_X, "mov x, $addr")

add_instruction(IP_2_AB | R_2_DB | ALU_S0 | CATCH_FLAGS | ALU_2_AL | IP_INC, "mov a, $addr + x")
add_conditional_carry_instruction(IP_2_AB | R_2_DB | Z_A | CPL_A | CPL_D | CPL_OUT | ALU_2_AH | IP_INC, IP_2_AB | R_2_DB | Z_A | ALU_2_AH | IP_INC, "mov a, $addr + x") # if inc db+1->ah, else db ->ah
add_instruction(ADDR_2_AB | R_2_DB | Z_A | ALU_2_A | IR_RESET, "mov a, $addr + x")


add_instruction(IP_2_AB | R_2_DB | ALU_S0 | CATCH_FLAGS | ALU_2_AL | IP_INC, "mov $addr + x, a")
add_conditional_carry_instruction(IP_2_AB | R_2_DB | Z_A | CPL_A | CPL_D | CPL_OUT | ALU_2_AH | IP_INC, IP_2_AB | R_2_DB | Z_A | ALU_2_AH | IP_INC, "mov $addr + x, a") # if inc db+1->ah, else db ->ah
add_instruction(ADDR_2_AB | A_2_DB | R_STR | IR_RESET, "mov $addr + x, a")

# ADD INSTRUCTION
add_instruction(X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, "add a, x")
add_instruction(X_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET, "add x, a")

add_instruction(IP_2_AB | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_INC,"add a, #num")
add_instruction(IP_2_AB | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0, "add x, #num")

add_relative_instruction(R_2_DB | ALU_2_A |  CATCH_FLAGS, "add a, $addr")

add_relative_instruction(R_2_DB | ALU_S0 | ALU_2_X |  CATCH_FLAGS, "add x, $addr")

# SUB INSTRUCTION
add_instruction(CPL_A | CPL_OUT | X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, "sub a, x")
add_instruction(CPL_A | CPL_OUT | A_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | ALU_S0, "sub x, a")

add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_INC, "sub a, #num")
add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0, "sub x, #num")

add_relative_instruction(CPL_A | CPL_OUT  | R_2_DB | ALU_2_A | CATCH_FLAGS, "sub a, $addr")

add_relative_instruction(CPL_A | CPL_OUT  | R_2_DB | ALU_2_X | CATCH_FLAGS | ALU_S0, "sub x, $addr")

add_relative_instruction(IP_INP, "jmp $addr")

add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, "jsr $addr")
add_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, "jsr $addr")
add_instruction(SP_2_AB | IPL_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT, "jsr $addr")
add_instruction(SP_2_AB | IPH_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT, "jsr $addr")
add_instruction(ADDR_2_AB | IP_INP | IR_RESET, "jsr $addr")

add_instruction(SP_2_AB | ALU_2_AH | Z_A | R_2_DB, "ret")
add_instruction(Z_D | CPL_D | ALU_2_SP | SP_2_AB | ALU_S1, "ret")
add_instruction(SP_2_AB | R_2_DB | ALU_2_AL | Z_A, "ret")
add_instruction(Z_D | CPL_D | ALU_2_SP | ALU_S1 | ADDR_2_AB | IP_INP | IR_RESET, "ret")

add_conditional_carry_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, IP_INC, "jc $addr")
add_conditional_carry_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, IP_INC | IR_RESET, "jc $addr")
add_conditional_carry_instruction(ADDR_2_AB | IP_INP | IR_RESET, 0, "jc $addr")

add_conditional_zero_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AL | IP_INC, IP_INC, "jz $addr")
add_conditional_zero_instruction(IP_2_AB | R_2_DB  | Z_A | ALU_2_AH | IP_INC, IP_INC | IR_RESET, "jz $addr")
add_conditional_zero_instruction(ADDR_2_AB | IP_INP | IR_RESET, 0, "jz $addr")

add_instruction(CPL_A | CPL_OUT | X_2_DB | CATCH_FLAGS | IR_RESET, "cmp a, x")
add_instruction(CPL_A | CPL_OUT | A_2_DB | CATCH_FLAGS | IR_RESET | ALU_S0, "cmp x, a")

add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | CATCH_FLAGS | IR_RESET | IP_INC, "cmp a, #num")
add_instruction(IP_2_AB | CPL_A | CPL_OUT | R_2_DB | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0, "cmp x, #num")

add_relative_instruction(CPL_A | CPL_OUT  | R_2_DB | CATCH_FLAGS, "cmp a, $addr")

add_relative_instruction(CPL_A | CPL_OUT  | R_2_DB | ALU_S0 | CATCH_FLAGS, "cmp x, $addr")

add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AL | IP_INC, "out a, $2bit_addr")
add_instruction(ADDR_2_AB | A_2_DB | INP_OUT | IR_RESET, "out a, $2bit_addr")

add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AL | IP_INC, "out a, $2bit_addr")
add_instruction(ADDR_2_AB | X_2_DB | INP_OUT | IR_RESET, "out x, $2bit_addr")

add_instruction(SP_2_AB | A_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT | IR_RESET, "push a") # inc sp
add_instruction(SP_2_AB | X_2_DB | ALU_S1 | ALU_2_SP | R_STR | CPL_A | Z_D | CPL_D | CPL_OUT | IR_RESET, "push x") # inc sp

add_instruction(SP_2_AB | R_2_DB | Z_A | ALU_2_A, "pull a")
add_instruction(ALU_S1 | Z_D | CPL_D | ALU_2_SP | SP_2_AB | IR_RESET, "pull a")

add_instruction(SP_2_AB | R_2_DB | Z_A | ALU_2_X, "pull x")
add_instruction(ALU_S1 | Z_D | CPL_D | ALU_2_SP | SP_2_AB | IR_RESET, "pull x")

add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AL | IP_INC,     "in a, $2bit_addr")
add_instruction(ADDR_2_AB | ALU_2_A | Z_A | INP_OUT | IR_RESET, "in a, $2bit_addr")

add_instruction(IP_2_AB | R_2_DB | Z_A | ALU_2_AL | IP_INC,     "in x, $2bit_addr")
add_instruction(ADDR_2_AB | ALU_2_A | Z_A | INP_OUT | IR_RESET, "in x, $2bit_addr")

add_instruction(X_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | AND_A_D, "and a, x")
add_instruction(X_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | AND_A_D, "and x, a")

add_instruction(IP_2_AB | R_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET | IP_INC | AND_A_D,"and a, #num")
add_instruction(IP_2_AB | R_2_DB | ALU_2_X | CATCH_FLAGS | IR_RESET | IP_INC | ALU_S0 | AND_A_D, "and x, #num")


add_relative_instruction(R_2_DB | ALU_2_A |  CATCH_FLAGS | AND_A_D, "and a, $addr")

add_relative_instruction(R_2_DB | ALU_S0 | ALU_2_X |  CATCH_FLAGS | AND_A_D, "and x, $addr")


add_instruction(A_2_DB | ALU_2_A | CATCH_FLAGS | IR_RESET, "rol a")
add_instruction(X_2_DB | ALU_2_X | CATCH_FLAGS | ALU_S0 | IR_RESET, "rol x")

with open("Rom_writer//ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))


print("ROM WRITER DONE..")