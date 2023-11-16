## Introduction
Simple assembler for the course "Grundlagen der Informationstechnologie", Hochschule Kempten

In this course we introduce a very simple CPU with a Von Neumann architecture.
The CPU supports the following Instruction Set:

| Opcode (HEX)      | Assembler | Explanation |
| :----------------: | :------ | :---- |
| 00  | HLT   | Stop the machine, no further instructions will be executed |
| 01  | ADD M   | Add the number taken from memory at address M to the content of the accumulator and place the result in the accumulator |
| 02  | SUB M   | Subtract the number taken from memory at address M from the content of the accumulator and place the result in the accumulator |
| 03  | STA M   | Copy the number from the accumulator into memory at address M |
| 04  | LDI I   | Copy the number I (immediate) into the accumulator |
| 05  | LDA M   | Copy the number from memory at address M into the accumulator |
| 06  | BRA Lbl   | Branch unconditionally to the code line marked 'Lbl' (Label) |
| 07  | BRP Lbl   | Branch to the code line marked 'Lbl' if the value in the accumulator is greater or equal to 0, $\text{Akk} \geq 0$ |
| 08  | BRZ Lbl   | Branch to the code line marked 'Lbl' if the value in the accumulator is equal to 0, $\text{Akk} == 0$  |
| 09  | INP   | Copy the value from the input port into the accumulator |
| 0A  | OUT   | Copy the value from the accumulator into the output port |

**Notes**
+ Every Opcode is 1 byte long
+ Some instructions requiere an operand and are 2 bytes long (1 byte opcode + 1 byte operand)
+ Some instructions don't requiere an operand and are 1 byte long (1 byte opcode)
+ ADD, SUB, STA, LDA requiere a byte as operand which represents a memory address
+ LDI requires a byte as operand which represents an immediate value (a number)
+ BRA, BRP, BRZ requiere a text label as operand which represents a location in the code
+ HLT, INP, OUT require no operands 

With this assembler language you can write simple programms such as the following:

```
Start:
INP
BRZ Output
ADD Sum
STA Sum
BRA Start
Output:
LDA Sum
OUT
HLT
Sum:
0
```

Taking into account the definition of the instruction set and the lengths of the different instructions (1 or 2 bytes), you can convert assembler code into machine code (this is called *to assemble*). For this you need to replace the aseembler mnemonics with the appropriate opcodes and calculate the memory adresses corresponding to the labels. The assembler code above translates into the following machine code:
```
00 09
01 08
02 09
03 01
04 0D
05 03
06 0D
07 06
08 00
09 05
0A 0D
0B 0A
0C 00
0D 00
```
In this representation, the first column gives the memory location and the second column is the content. The content of a memory location will be either an opcode, an argument or data.

## This Project
This project implements a simple two-pass assembler written in python for the above given Instruction Set.

### First Pass: Label Resolution
- **Purpose**: The first pass is primarily for handling labels. Labels are symbolic names for memory addresses and are used in branching and data storage.
- **Process**:
  1. **Splitting the Code**: The assembly code is split into individual lines.
  2. **Label Collection**: As the assembler goes through each line, it checks for labels (lines ending with `:`). When a label is found, it's stored in a dictionary (`labels`) with its corresponding memory address.
  3. **Address Calculation**: The memory address for each label is calculated based on the size of the instructions and data encountered so far. This is crucial for correctly resolving the addresses in the second pass.

### Second Pass: Code Generation
- **Purpose**: The second pass generates the actual machine code by translating each assembly instruction into its binary or hexadecimal equivalent.
- **Process**:
  1. **Iterating Over Lines**: The assembler again iterates over each line of the assembly code.
  2. **Skipping Labels**: Labels are skipped in this pass as their addresses have already been resolved.
  3. **Instruction Translation**:
     - Each line is split into parts (operation and operand).
     - The assembler translates each operation into its corresponding opcode.
     - For operations that require an operand, the assembler checks if the operand is a label or a numeric value. If it's a label, its address (resolved in the first pass) is used; otherwise, the numeric value is used.
  4. **Machine Code Generation**: For each instruction, the corresponding machine code (opcode and operand) is generated and stored.
  5. **Data Handling**: If a line contains data (not an instruction), the assembler treats it accordingly, storing the data value at the correct memory address.

### Output
- The final output is a sequence of machine code instructions, each associated with a memory address. This output can be loaded into memory for execution by a machine (or emulator) that understands the defined instruction set.

### Key Points
- **Two-Pass Nature**: This approach ensures that all labels are correctly resolved before the actual machine code generation, allowing for forward and backward jumps and data references.
- **Flexibility**: The assembler can handle various instructions and is adaptable to different assembly language syntaxes, as long as the instruction set is predefined.
- **Error Handling**: While not explicitly detailed in our discussion, a robust assembler would also include error handling to manage undefined labels, syntax errors, and other anomalies in the assembly code.
- 
