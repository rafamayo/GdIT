# GdIT_Assembler
Simple assembler for the course "Grundlagen der Informationstechnologie", Hochschule Kempten

In this course we introduce a very simple CPU with a Von Neumann architecture.
The CPU supports the following Instruction Set:

| Opcode (HEX)      | Assembler | Explanation |
| :----------------: | :------ | :---- |
| 00  | HLT   | Stop the machine, no further instructions will be executed |
| 01  | ADD M   | Add the number taken from memory at address M to the content of the accumulator and place the result in the accumulator |
| 02  | SUB M   | Subtract the number taken from memory at address M from the content of the accumulator and place the result in the accumulator |
| 03  | STA M   | Copy the number from the accumulator into memory at address M |
