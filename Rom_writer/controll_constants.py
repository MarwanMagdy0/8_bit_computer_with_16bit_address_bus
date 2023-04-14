# initialize ROMs
ROM = ["0" for _ in range(0x2000)] # Create Rom with 0x2000 zeros
instructions = []
_indx=0
def shift():
    # a shifter function shifts 1 each time it is called
    # ex:
    #   1 10 100 1000 10000
    global _indx
    if _indx ==0:
        _indx=1
    else:
        _indx *=2
    return _indx
_instructions_indx = -1
_local_counter = 1
def add_instruction(value, name):
    global _instructions_indx, _local_counter
    if name not in instructions:
        _local_counter=1
        _instructions_indx+=1
        instructions.append(name)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b00] = st(value)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b01] = st(value)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b10] = st(value)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b11] = st(value)
    if _local_counter==1:
        print("Instruction added: 0x{:02x}".format(_instructions_indx), f"--> {name}")
    _local_counter+=1

def add_conditional_carry_instruction(if_carry, if_not_carry, name):
    global _instructions_indx, _local_counter
    if name not in instructions:
        _local_counter=1
        _instructions_indx+=1
        instructions.append(name)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b00] = st(if_not_carry)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b01] = st(if_not_carry)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b10] = st(if_carry)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b11] = st(if_carry)
    if _local_counter==1:
        print("Instruction added: 0x{:02x}".format(_instructions_indx), f"--> {name}")
    _local_counter+=1

def add_conditional_zero_instruction(if_zero, if_not_zero, name):
    global _instructions_indx, _local_counter
    if name not in instructions:
        _local_counter=1
        _instructions_indx+=1
        instructions.append(name)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b00] = st(if_not_zero)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b01] = st(if_zero)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b10] = st(if_not_zero)
    ROM[_local_counter*2**10 + _instructions_indx*2**2 + 0b11] = st(if_zero)
    if _local_counter==1:
        print("Instruction added: 0x{:02x}".format(_instructions_indx), f"--> {name}")
    _local_counter+=1
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

IP_INC      = shift()
IP_INP      = shift() | IP_INC
IP_2_AB     = shift()
IPL_2_DB    = shift()
IPH_2_DB    = shift()

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

print(f"{len(str(bin(_indx))[2:])} Micro Instruction has been added")