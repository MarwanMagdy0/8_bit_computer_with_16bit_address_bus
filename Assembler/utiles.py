def preprocessing_commenting_and_cleaning(each_line):
    each_line = [ line for line in each_line if len(line)>0 and not line.startswith(";")]
    operations = [[] for line in each_line if len(line)>0]
    for idx, line in enumerate(each_line):
        if len(line)==0:
             continue
        c = ""
        for char in line:
            if char != "" and char !=" " and char != "," and char != ";" and char !="+" and char !=":" and char !="=" and char!='"':
                c+=char
            elif char == "=":
                operations[idx].insert(0,"=")
                if c !="":
                    operations[idx].append(c.upper())
                c=""
            elif char == ":":
                operations[idx].insert(0, ":")
                if c !="":
                    operations[idx].append(c.upper())
                c=""
            elif char==";":
                break
            else:
                if c !="":
                    operations[idx].append(c.upper())
                c = ""
        if c !="":
                operations[idx].append(c.upper())
    print(operations)
    return list(filter(None, operations))

def instruction_pointer_for_multi_op_instruction(line, constants={}, labels={}):
    instruction_pointer = 0
    if line[1] == "A":
        if constants.get(line[2], False):
            line[2] = constants.get(line[2], False)
        elif labels.get(line[2], False):
            line[2] = labels.get(line[2], False)
        if line[2] == "X":
            instruction_pointer+=1

        elif line[2].startswith("#"):
            instruction_pointer+=2
        
        elif line[2].startswith("$"):
            instruction_pointer+=3
        
        elif line[2].startswith("%"):
            instruction_pointer+=2
    
    elif line[1] == "X":
        if constants.get(line[2], False):
            line[2] = constants.get(line[2], False)
        elif labels.get(line[2], False):
            line[2] = labels.get(line[2], False)
        if line[2] == "A":
            instruction_pointer+=1

        elif line[2].startswith("#"):
            instruction_pointer+=2
        
        elif line[2].startswith("$"):
            instruction_pointer+=3
            if len(line) ==4:
                instruction_pointer+=1
        
        elif line[2].startswith("%"):
            instruction_pointer+=2


    elif line[1].startswith("$"):
        if constants.get(line[2], False):
            line[2] = constants.get(line[2], False)
        elif labels.get(line[2], False):
            line[2] = labels.get(line[2], False)
        if line[2] == "A":
            instruction_pointer+=3

        if line[2] == "X":
            instruction_pointer+=3
    
    return instruction_pointer


def preprcessing_labels_and_constants(each_line_no_comments):
    constants = {}
    labels    = {}
    operations_no_labels = []
    instruction_pointer = 0
    for line in each_line_no_comments:
        if line[0]=="=":
            if line[2][0]=="#":
                constants[line[1]] = line[2][0] + "{:02x}".format(int(eval("0x"+line[2][1:])))
            elif line[2][0]=="$":
                constants[line[1]] = line[2][0] + "{:04x}".format(int(eval("0x"+line[2][1:])))
                
    for i, line in enumerate(each_line_no_comments):
        for j, op in enumerate(line):
            if constants.get(op, False):
                each_line_no_comments[i][j] = constants.get(op)   
        
    for line in each_line_no_comments:
        if line[0] == ":":
            labels[line[1]] = "{:04x}".format(instruction_pointer)
            continue
        if line[0] == "MOV" or line[0]=="ADD" or line[0]=="SUB" or line[0]=="AND" or line[0]=="OR" or line[0]=="CMP":
            instruction_pointer+=instruction_pointer_for_multi_op_instruction(line, constants, labels)
        
        elif line[0]=="JMP":
            instruction_pointer+=3
        
        elif line[0]=="OUT":
            instruction_pointer+=2

        elif line[0]=="JSR":
            instruction_pointer+=3
            
        elif line[0]=="JC":
            instruction_pointer+=3

        elif line[0]=="JZ":
            instruction_pointer+=3

        elif line[0]=="RET":
            instruction_pointer+=1
        
        elif line[0]=="DB":
            for _ in line[1:]:
                instruction_pointer+=1
        else:
            continue
        operations_no_labels.append(line)
    for i, line in enumerate(operations_no_labels):
        for j, op in enumerate(line):
            if labels.get(op[1:], False):
                operations_no_labels[i][j] = "$" + labels.get(op[1:])
    print("code constants :", constants)
    print("code labels    :", labels)
    print(f"program takes {instruction_pointer} bytes\n")
    return operations_no_labels