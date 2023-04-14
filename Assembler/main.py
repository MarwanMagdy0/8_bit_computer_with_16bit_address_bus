from utiles import *
CODE = """
f = #6
mov a f
""".strip()
preprocessed_ops = preprocessing_commenting_and_cleaning(CODE.split("\n"))
preprcessing_labels_and_constants(preprocessed_ops)

binary_code = "v2.0 raw\n"

for line in preprocessed_ops:
    if line[0] == "MOV":
        if line[1] == "A":
            if line[2] == "X":
                assert False, "MOV A, X ; Not implemented"

            elif line[2].startswith("#"):
                assert False,  "MOV A, #54 ; Imediat Not implemented"
            
            elif line[2].startswith("$"):
                assert False,  "MOV A, $1054 ; Indirect Not implemented"
                if len(line) ==4:
                    if line[3] == "X":
                        assert False,  "MOV A, $1054+X ; register plus address Not implemented"
                    else:
                        assert False, f"({' '.join(line)}) --> {line[3]} is not a register"
            
            elif line[2].startswith("%"):
                assert False,  "MOV A, %10010101 ; Imediat Not implemented"
        
        elif line[1] == "X":
            if line[2] == "A":
                assert False,  "MOV X, A ; Not implemented"

            elif line[2].startswith("#"):
                assert False,  "MOV X, #54 ; Imediat Not implemented"
            
            elif line[2].startswith("$"):
                assert False,  "MOV X, $1054 ; Indirect Not implemented"
            
            elif line[2].startswith("%"):
                assert False,  "MOV X, %10010101 ; Imediat Not implemented"

        elif line[1].startswith("$"):
            if line[2] == "A":
                assert False,  "MOV $6402, A ; Not implemented"

            if line[2] == "X":
                assert False,  "MOV $6402, X ; Not implemented"
    
    elif line[0]=="JMP":
        if line[1].startswith("$"):
            assert False,  "JMP $6402 ; JMP is Not implemented"

    elif line[0]=="JSR":
        if line[1].startswith("$"):
            assert False,  "JSR $6402 ; JMP is Not implemented"
    
    elif line[0]=="JC":
        if line[1].startswith("$"):
            assert False,  "JC $6402 ; JMP is Not implemented"
        
    elif line[0]=="JZ":
        if line[1].startswith("$"):
            assert False,  "JZ $6402 ; JMP is Not implemented"

    elif line[0]=="RET":
        assert False, "RET is not implemented"

            

with open("output", "w") as file: # Writing to the file
    file.write(binary_code)
