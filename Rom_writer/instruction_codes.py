from controll_constants import *

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_OUT | IP_SEL | IP_OUT)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
"""
add_instruction(R_OUT | A_IN | IR_RESET | IP_SEL| IP_OUT, 0b001) # LDA
add_instruction(R_OUT | X_IN | IR_RESET | IP_SEL | Z_A| OUT_LOW, 0b001) #LDX

with open("ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))


print("ROM WRITER DONE..")