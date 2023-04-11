# initialize ROMs
ROM = ["0" for _ in range(0x2000)] # Create Rom with 0x2000 zeros

indx=0
def shift():
    # a shifter function shifts 1 each time it is called
    # ex:
    #   1 10 100 1000 10000
    global indx
    if indx ==0:
        indx=1
    else:
        indx *=2
    return indx
add_indx = 0
def add_instruction(value, counter, flags= None):
    global add_indx
    if counter > 1:
        add_indx -=1
    if flags == None:
        ROM[counter*2**10 + add_indx*2**2 + 0b00] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b01] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b10] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b11] = st(value)

    else:
        ROM[counter*2**10 + add_indx*2**2 + flags] = st(value)
    print("Instruction added: {:08b}, {:02x}".format(add_indx,add_indx))
    add_indx +=1
# ALU CONTROLL
Z_A         = shift()
CPL_A       = shift()
Z_D         = shift()
CPL_D       = shift()
AND_A_D     = shift()
CPL_OUT     = shift()
CATCH_FLAGS = shift()

# Registers and Pointers
ALU_2_A     = shift()
A_2_DB      = shift()

ALU_2_X     = shift()
X_2_DB      = shift()

ALU_2_SP    = shift()
SP_2_AB      = shift()

IP_SEL      = shift()
IP_INP      = shift()
IP_2_AB     = shift()

ALU_2_AL    = shift()
ALU_2_AH    = shift()
A_2_AB      = shift()

# RAM / IO control
R_STR       = shift()
INP_OUT     = shift()
R_2_DB      = shift()

# Additional
CONST_OUT   = shift()
IR_RESET    = shift()
ALU_S0      = shift()
ALU_S1      = shift()
def st(instruction):
    return str(hex(instruction))[2:]

print(f"{len(str(bin(indx))[2:])} Micro Instruction has been added")