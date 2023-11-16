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
+ Some instructions requiere an argument and are 2 bytes long (1 byte Opcode + 1 byte argument)
+ Some instructions don't requiere an argument and are 1 byte long (1 byte opcode)
+ ADD, SUB, STA, LDA requiere a byte as argument which represents a memory address
+ LDI requires a byte as argument which represents an immediate value (a number)
+ BRA, BRP, BRZ requiere a text label as argument which represents a location in the code
+ HLT, INP, OUT require no arguments 

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
