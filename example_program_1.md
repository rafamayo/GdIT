## Example program 1

```
Start:
INP          ; Read number from input
BRZ Output   ; If read number is a zero, go to output 
ADD Sum      ; Add the read number to the current sum value
STA Sum      ; Store the current sum value in Sum
BRA Start    ; Branch back to start to read a new number
Output:
LDA Sum      ; Load the current value of the sum
OUT          ; Copy the accumulator value to output
HLT          ; Stop the machine
Sum:
0            ; Current value of sum (start value is 0)
```

### Program Analysis

1. **Start:**
   - **INP**: Reads a number from the input and stores it in the accumulator.

2. **BRZ Output**:
   - Checks if the number just read (now in the accumulator) is zero.
   - If it is zero, the program branches to the `Output` label; otherwise, it continues to the next instruction.

3. **ADD Sum**:
   - Adds the value stored at the memory location labeled `Sum` to the accumulator. Initially, `Sum` is 0, so this effectively starts accumulating the sum of the input numbers.

4. **STA Sum**:
   - Stores the current value of the accumulator (which now holds the sum) back into the memory location labeled `Sum`.

5. **BRA Start**:
   - Unconditionally branches back to the `Start` label, causing the program to read the next input number.

6. **Output:**
   - This section is reached only when a zero is input (due to the `BRZ Output` instruction).
   
7. **LDA Sum**:
   - Loads the current value of `Sum` (the accumulated sum) into the accumulator.

8. **OUT**:
   - Outputs the value in the accumulator (the total sum) to the output.

9. **HLT**:
   - Halts the machine, stopping the program execution.

10. **Sum:**
    - A memory location labeled `Sum` initialized with 0. This is used to store the running total of the input numbers.

### Program Functionality
- The program continuously reads numbers from the input and adds them to a running total.
- When the user inputs zero, the program outputs the total sum of all previously entered numbers.
- After outputting the sum, the program halts.

### Example execution
- If a user inputs `3`, `5`, `2`, and then `0`, the program will output `10` (since `3 + 5 + 2 = 10`) and then halt.
