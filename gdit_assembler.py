def gdit_assembler(assembly_code):
    # Split the code into lines
    lines = assembly_code.strip().split("\n")
    
    # First pass: Collect labels and their addresses
    labels = {}
    address = 0
    for line in lines:
        # Remove comments
        line = line.split(';')[0].strip()
        if not line:
            continue  # Skip empty lines

        if line.endswith(":"):  # It's a label
            label = line[:-1]
            labels[label] = address
        else:
            # If it's data storage, increment the address counter
            if not any(op in line for op in ["ADD", "SUB", "STA", "LDI", "LDA", "BRA", "BRP", "BRZ", "INP", "OUT", "HLT"]):
                address += 1
            elif line in ["INP", "OUT", "HLT"]:
                address += 1  # One byte for opcode
            else:
                address += 2  # One byte for opcode and one byte for operand
    
    machine_code = []
    address = 0
    for line in lines:
        # Remove comments
        comment = None
        if ';' in line:
            line, comment = line.split(';', 1)
            line = line.strip()

        if line.endswith(":"):  # Skip labels in the second pass
            continue

        parts = line.split()
        if not parts:
            continue  # Skip empty lines

        instruction = parts[0]
        
        # Check if it's an instruction or data
        if any(op == instruction for op in ["ADD", "SUB", "STA", "LDI", "LDA", "BRA", "BRP", "BRZ", "INP", "OUT", "HLT"]):
            # Append opcode with assembly comment and operand
            opcode = {
                "ADD": "01",
                "SUB": "02",
                "STA": "03",
                "LDI": "04",
                "LDA": "05",
                "BRA": "06",
                "BRP": "07",
                "BRZ": "08",
                "INP": "09",
                "OUT": "0A",
                "HLT": "00"
            }.get(instruction, None)
            
            machine_code_line = f"{format(address, '02X')}: {opcode}"
            if comment:
                machine_code_line += f" ; {comment.strip()}"
            machine_code.append(machine_code_line)
            address += 1
            
            # Append operand if present
            if instruction not in ["INP", "OUT", "HLT"]:
                # Check if the operand is a label or an integer
                operand_value = labels.get(parts[1], None)
                if operand_value is None:  # Operand is not a label
                    operand_value = int(parts[1])
                operand = format(operand_value, '02X')
                machine_code.append(f"{format(address, '02X')}: {operand}")
                address += 1
        else:  # If it's data storage
            machine_code.append(f"{format(address, '02X')}: {format(int(parts[0]), '02X')}")
            address += 1
    
    return "\n".join(machine_code)
