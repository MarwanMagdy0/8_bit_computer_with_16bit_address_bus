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
    # print(str(bin(indx))[2:], len(str(bin(indx))[2:]))
    return indx
add_indx = 0
def add_instruction(value, counter, flags= None):
    global add_indx
    if flags == None:
        ROM[counter*2**10 + add_indx*2**2 + 0b00] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b01] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b10] = st(value)
        ROM[counter*2**10 + add_indx*2**2 + 0b11] = st(value)

    else:
        ROM[counter*2**10 + add_indx*2**2 + flags] = st(value)
    print("Instruction added: {:08b}".format(add_indx))
    add_indx +=1
# ALU CONTROLL
Z_A         = shift()
CPL_A       = shift()
Z_D         = shift()
CPL_D       = shift()
ADD_AND     = shift()
CPL_OUT     = shift()
OUT_LOW     = shift()
CATCH_FLAGS = shift()
OUT_HIGH    = shift()

# Registers and Pointers
A_IN        = shift()
X_OUT       = shift()
X_IN        = shift()
S0          = shift()
S1          = shift()
SP_OUT      = shift()
SP_IN       = shift()
IP_SEL      = shift()
IP_INP      = shift()
AL_OUT      = shift()
AL_IN       = shift()
AH_OUT      = shift()
AH_IN       = shift()
R_STR       = shift()
R_SEL       = shift()
R_OUT       = shift() | R_SEL
IR_RESET    = shift()
IP_OUT      = shift()
CONST_OUT   = shift()

def st(instruction):
    return str(hex(instruction))[2:]
