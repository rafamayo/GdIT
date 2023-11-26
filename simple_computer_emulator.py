class SimpleComputerEmulator:
    def __init__(self):
        self.memory = [0] * 256  # Assuming 256 memory locations
        self.accumulator = 0
        self.program_counter = 0
        self.halted = False
        self.step_by_step = False

    def load_program(self, machine_code):
        lines = machine_code.strip().split("\n")
        for line in lines:
            code_part = line.split(';')[0].strip()
            if not code_part:
                continue
            address, value = code_part.split(':')
            self.memory[int(address, 16)] = int(value.strip(), 16)

    def run(self):
        user_input = input("Run step-by-step? (y/n, default: y): ").lower()
        self.step_by_step = user_input != "n"

        if self.step_by_step:
            self.display_current_state()
            input("Press Enter to start execution...")

        while not self.halted:
            self.execute_instruction()
            self.display_current_state()  # Display current state after each instruction
            if self.step_by_step and not self.halted:
                self.step_execution()

        if self.halted:
            self.post_execution()

    def post_execution(self):
        while True:
            user_input = input("Execution halted. Press 'm' to inspect memory, 'd' to dump memory, or 'q' to quit: ").lower()
            if user_input == 'm':
                self.inspect_memory()
            elif user_input == 'd':
                self.dump_memory()
            elif user_input == 'q':
                break
            else:
                print("Invalid input. Please try again.")

    def execute_instruction(self):
        opcode = format(self.memory[self.program_counter], '02X')
        self.program_counter += 1

        if opcode == "00":  # HLT
            self.halted = True
            print("Execution halted. (HLT instruction encountered)")
        elif opcode in ["01", "02", "03", "05", "06", "07", "08"]:
            operand = self.memory[self.program_counter]
            self.program_counter += 1
            self.perform_operation(opcode, operand)
        elif opcode == "04":  # LDI
            self.accumulator = self.memory[self.program_counter]
            self.program_counter += 1
        elif opcode == "09":  # INP
            self.accumulator = int(input("Enter input value: "))
        elif opcode == "0A":  # OUT
            print("Output:", self.accumulator)

    def perform_operation(self, opcode, operand):
        if opcode == "01":  # ADD
            self.accumulator += self.memory[operand]
        elif opcode == "02":  # SUB
            self.accumulator -= self.memory[operand]
        elif opcode == "03":  # STA
            self.memory[operand] = self.accumulator
        elif opcode == "05":  # LDA
            self.accumulator = self.memory[operand]
        elif opcode == "06":  # BRA
            self.program_counter = operand
        elif opcode == "07":  # BRP
            if self.accumulator >= 0:
                self.program_counter = operand
        elif opcode == "08":  # BRZ
            if self.accumulator == 0:
                self.program_counter = operand

    def step_execution(self):
        while True:
            user_input = input("Press 'n' for next step, 'm' to inspect memory, or 'd' to dump memory: ").lower()
            if user_input == 'm':
                self.inspect_memory()
            elif user_input == 'd':
                self.dump_memory()
            elif user_input == 'n':
                break  # Proceed to next step only when 'n' is pressed
            else:
                print("Invalid input. Please try again.")
    
    def step_execution(self):
        while True:
            user_input = input("Press 'n' for next step, 'c' to continue running, 'm' to inspect memory, or 'd' to dump memory: ").lower()
            if user_input == 'm':
                self.inspect_memory()
            elif user_input == 'd':
                self.dump_memory()
            elif user_input == 'c':
                self.step_by_step = False  # Disable step-by-step mode
                break
            elif user_input == 'n':
                break  # Proceed to next step
            else:
                print("Invalid input. Please try again.")

    def display_current_state(self):
        print(f"Instruction Pointer: {format(self.program_counter, '02X')}, Memory Content: {format(self.memory[self.program_counter], '02X')}")


    def inspect_memory(self):
        address = input("Enter memory address to inspect (hex): ")
        try:
            value = self.memory[int(address, 16)]
            print(f"Memory at {address}: {format(value, '02X')}")
            print(f"Instruction Pointer: {format(self.program_counter, '02X')}, Accumulator: {self.accumulator}")
        except ValueError:
            print("Invalid address.")

    def dump_memory(self):
        for row in range(0, len(self.memory), 16):
            print(f"{format(row, '02X')}: ", end='')
            for col in range(16):
                if row + col < len(self.memory):
                    print(f"{format(self.memory[row + col], '02X')} ", end='')
            print()  # New line after each row

        print(f"Instruction Pointer: {format(self.program_counter, '02X')}, Accumulator: {self.accumulator}")
