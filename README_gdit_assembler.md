## Simple Computer Assembler User Manual

This is a simple two-pass assembler written in python for the Instruction Set specified below.

The simple computer model and its assembler are used as part of the course "Fundamentals of information technology" at the Kempten University of Applied Sciences (https://www.hs-kempten.de/).

### The Instruction Set:

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

## Features

- Converts assembly code into machine code, also handling comments within the assembly code.
- Takes as input a string containing the assembly code, which may include comments marked by semicolons (`;`).

#### First Pass: Label and Address Resolution with Comment Handling
- **Splitting the Code**: The assembly code is split into individual lines.
- **Comment Removal and Label Collection**:
  - Each line is processed to remove comments. This is done by splitting the line at the first semicolon (`;`) and keeping only the part before it.
  - If a line is empty or becomes empty after removing comments, it's skipped.
  - If a line ends with `:`, it's identified as a label. The label's name and its corresponding address are stored in the `labels` dictionary.
- **Address Calculation**:
  - The address counter (`address`) is incremented based on the size of the instructions and data, excluding comments.

#### Second Pass: Machine Code Generation with Comment Preservation
- **Iterating Over Lines with Comment Handling**: The assembler again goes through each line, removing comments and skipping empty lines.
- **Skipping Labels**: Labels are skipped as their addresses are already resolved.
- **Instruction Handling**:
  - Each line is split into parts (operation and operand), excluding the comment part.
  - The assembler checks if the line is an instruction or data.
  - For instructions, the corresponding opcode is appended to the machine code. If the original line had a comment, it's preserved alongside the machine code.
  - The address is incremented after appending the opcode.
- **Operand Handling**:
  - If the instruction requires an operand, the assembler checks if it's a label or an integer.
  - If it's a label, its resolved address is used; otherwise, the integer value is used.
  - The operand is formatted and appended to the machine code, and the address is incremented.
- **Data Handling**:
  - For data storage lines, the data value is formatted and appended to the machine code.
  - The address is incremented after appending the data.

#### Output
- The function returns the generated machine code as a string. Each line of the output represents a byte of machine code with its corresponding address. Comments from the assembly code are preserved in the output where applicable.

#### Key Features
- **Comment Handling**: The assembler strips comments from the code during processing, ensuring they don't interfere with the assembly process. Comments are preserved in the output for readability and reference.
- **Two-Pass Approach**: Ensures accurate address resolution for labels before generating machine code.
- **Flexibility and Robustness**: Handles various instructions, data storage formats, and comments, making it versatile and user-friendly.
