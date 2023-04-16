import os
def enum():
    count = 0
    while True:
        yield count
        count += 1
        
gen = enum()
NOP          = next(gen)

MOV_A_NUM    = next(gen)
MOV_X_NUM    = next(gen)

MOV_X_A      = next(gen)
MOV_A_X      = next(gen)

MOV_ADDR_A   = next(gen)
MOV_ADDR_X   = next(gen)

MOV_A_ADDR   = next(gen)
MOV_X_ADDR   = next(gen)

MOV_A_ADDR_X = next(gen)

ADD_A_X      = next(gen)
ADD_X_A      = next(gen)

ADD_A_NUM    = next(gen)
ADD_X_NUM    = next(gen)

ADD_A_ADDR   = next(gen)
ADD_X_ADDR   = next(gen)

SUB_A_X      = next(gen)
SUB_X_A      = next(gen)

SUB_A_NUM    = next(gen)
SUB_X_NUM    = next(gen)

SUB_A_ADDR   = next(gen)
SUB_X_ADDR   = next(gen)

JMP          = next(gen)
JSR          = next(gen)
RET          = next(gen)
JC           = next(gen)
JZ           = next(gen)

CMP_A_X      = next(gen)
CMP_X_A      = next(gen)
CMP_A_NUM    = next(gen)
CMP_X_NUM    = next(gen)
CMP_A_ADDR    = next(gen)
CMP_X_ADDR    = next(gen)

OUT_A_ADDR    = next(gen)
OUT_X_ADDR    = next(gen)
def bin2hex(text):
    return "{:02x} ".format(int(eval("0b"+text[1:])))

def byte2hex(text):
    return "{:02x} ".format(int(eval("0x"+text[1:])))

def inst2hex(instruction):
    return "{:02x}".format(instruction) + " "

def address2hex(address):
    address_ret = ""
    address_ret += address[1:][2:4]+ " "
    address_ret += address[1:][0:2]+ " "
    return address_ret

def error_print(line, error_msg):
    print(" ".join(line))
    print("    ",f"ERROR: {error_msg}")
    os._exit(0)

def handle_multi_operand(line, a_x, a_num, a_addr, x_a, x_num, x_addr, a_addr_x=None, addr_x=None, addr_a=None):
    binary_code = ""
    if line[1] == "A":
        if line[2] == "X":
            binary_code += inst2hex(a_x)

        elif line[2].startswith("#"):
            binary_code += inst2hex(a_num)
            binary_code += byte2hex(line[2])
        
        elif line[2].startswith("$"):
            if len(line)==4:
                binary_code += inst2hex(a_addr_x)
                binary_code += address2hex(line[2])
            else:
                binary_code += inst2hex(a_addr)
                binary_code += address2hex(line[2])
            

        
        elif line[2].startswith("%"):
            binary_code += inst2hex(a_num)
            binary_code += bin2hex(line[2])
        
    elif line[1] == "X":
        if line[2] == "A":
            binary_code += inst2hex(x_a)

        elif line[2].startswith("#"):
            binary_code += inst2hex(x_num)
            binary_code += byte2hex(line[2])
        
        elif line[2].startswith("$"):
            binary_code += inst2hex(x_addr)
            binary_code += address2hex(line[2])
        
        elif line[2].startswith("%"):
            binary_code += inst2hex(x_num)
            binary_code += bin2hex(line[2])
    
    elif line[1]=="$":
        pass

    return binary_code