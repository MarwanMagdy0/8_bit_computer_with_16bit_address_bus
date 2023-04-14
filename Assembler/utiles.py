def preprocessing_commenting_and_cleaning(each_line):
    each_line = [ line for line in each_line if len(line)>0 and not line.startswith(";")]
    operations = [[] for line in each_line if len(line)>0]
    for idx, line in enumerate(each_line):
        if len(line)==0:
             continue
        c = ""
        for char in line:
            if char != "" and char !=" " and char != "," and char != ";" and char !="+" and char !=":" and char !="=":
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
    return operations

def preprcessing_labels_and_constants(each_line_no_comments):
    variables = {}
    operations_no_labels = []
    instruction_pointer = 0
    for line in each_line_no_comments:
        if line[0]=="=":
            # print(line[2][0] + "{:02x}".format(line[2][0:]))
            variables[line[1]] = line[2][0] + "{:02x}".format(int(line[2][1:]))
            continue
        
        if line[0] == ":":
            # instruction_pointer+=1
            variables[line[1]] = "${:04x}".format(instruction_pointer)
            continue
        if line[0] == "MOV":
            if line[1] == "A":
                if line[2] == "X":
                    instruction_pointer+=1

                elif line[2].startswith("#"):
                    instruction_pointer+=2
                
                elif line[2].startswith("$"):
                    instruction_pointer+=3
                
                elif line[2].startswith("%"):
                    instruction_pointer+=2
            
            elif line[1] == "X":
                if line[2] == "A":
                    instruction_pointer+=1

                elif line[2].startswith("#"):
                    instruction_pointer+=2
                
                elif line[2].startswith("$"):
                    instruction_pointer+=3
                
                elif line[2].startswith("%"):
                    instruction_pointer+=2


            elif line[1].startswith("$"):
                if line[2] == "A":
                    instruction_pointer+=3

                if line[2] == "X":
                    instruction_pointer+=3
        
        elif line[0]=="JMP":
                instruction_pointer+=3

        elif line[0]=="JSR":
                instruction_pointer+=3
            
        elif line[0]=="JC":
                instruction_pointer+=3

        elif line[0]=="JZ":
                instruction_pointer+=3

        elif line[0]=="RET":
            instruction_pointer+=1
    
        operations_no_labels.append(line)
    for i, line in enumerate(operations_no_labels):
        for j, op in enumerate(line):
            if variables.get(op, False):
                operations_no_labels[i][j] = variables.get(op)
    print(variables)
    return operations_no_labels
