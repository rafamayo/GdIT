# Simple Computer Emulator User Manual

## Overview
The Simple Computer Emulator is a Python-based tool designed to emulate a basic computer system. It interprets and executes machine code written for a predefined instruction set. This emulator supports both normal and step-by-step execution modes, allowing users to inspect the execution process in detail.

This simple computer model is used as part of the course "Fundamentals of information technology" at the Kempten University of Applied Sciences (https://www.hs-kempten.de/).

## Features
- **256 Memory Locations**: The emulator has 256 memory locations, each capable of storing a byte.
- **Step-by-Step Execution**: Users can choose to execute programs step-by-step, inspecting the state of the emulator at each step.
- **Memory Inspection**: During step-by-step execution, users can inspect individual memory locations or dump the entire memory content.
- **Input and Output Operations**: Supports basic input and output operations.

## Instruction Set
The emulator supports the following instructions:
- `ADD <M>`: Add the value at memory location M to the accumulator.
- `SUB <M>`: Subtract the value at memory location M from the accumulator.
- `STA <M>`: Store the accumulator's value into memory location M.
- `LDI I`: Load immediate value I into the accumulator.
- `LDA <M>`: Load the value from memory location M into the accumulator.
- `BRA Lbl`: Unconditional branch to the instruction at memory location Lbl.
- `BRP Lbl`: Branch to Lbl if the accumulator is positive or zero.
- `BRZ Lbl`: Branch to Lbl if the accumulator is zero.
- `INP`: Read an input value into the accumulator.
- `OUT`: Output the value in the accumulator.
- `HLT`: Halt the execution.

## Usage

### Loading a Program
- The `load_program` method is used to load machine code into the emulator's memory.
- Machine code should be in the format `address: value`, with each line representing a memory location and its corresponding byte value.

### Running a Program
- The `run` method starts the execution of the loaded program.
- Users can choose between normal execution and step-by-step execution.
- In step-by-step mode, the current state (instruction pointer and accumulator value) is displayed after each instruction. Users can:
  - Press `'n'` to execute the next instruction.
  - Press `'m'` to inspect a specific memory location.
  - Press `'d'` to dump the entire memory content.
  - Press `'c'` to continue running the program normally.

### Memory Inspection
- The `inspect_memory` method allows users to view the value stored at a specific memory address.
- The `dump_memory` method displays the content of all memory locations in a formatted manner.

### Halting Execution
- The program halts when the `HLT` instruction is executed.
- Upon halting, the emulator displays a message and allows only memory inspection.

## Example
Here's an example of loading and running a simple program:

```python
machine_code = """
00: 09 ; Read input
01: 08 ; Check if zero
02: 09
03: 01 ; Add to sum
04: 0D
05: 03 ; Store sum
06: 0D
07: 06 ; Loop back
08: 00
09: 05 ; Load sum
0A: 0D
0B: 0A ; Output sum
0C: 00 ; Halt
0D: 00 ; Sum storage
"""

emulator = SimpleComputerEmulator()
emulator.load_program(machine_code)
emulator.run()
```

---

This manual provides a comprehensive guide to using the Simple Computer Emulator, covering its features, instruction set, and basic usage instructions.
