import sys


class LittleBenComputer:
    """
    Implementation of the Little Man Computer.
    """

    def run(self):
        """
        Begins executing the program.
        """
        self.running = True
        self.accumulator = 0
        self.program_counter = 0
        while self.running:
            next_instruction = self.instructions[self.program_counter]
            self.program_counter += 1
            self.exec_instruction(next_instruction)

    def load_file(self, source):
        """
        Loads and preprocesses the source file.
        """
        with open(source, "r") as infile:
            self.lines = infile.readlines()
        self.instructions = []
        self.memory = {}
        num_dats = 0
        for i in range(len(self.lines)):
            components = self.lines[i].split(" ")
            components[-1] = components[-1][:-1]
            if len(components) == 3:
                if components[1] == "DAT":
                    self.memory[components[0]] = int(components[2])
                    num_dats += 1
                    continue
                else:
                    self.links[components[0]] = i - num_dats
                    self.instructions.append([components[1], components[2]])
            elif len(components) == 2:
                self.instructions.append([components[0], components[1]])
            elif len(components) == 1:
                self.instructions.append([components[0], None])

    def add(self, address):
        """
        The LMC `ADD` instruction.

        Adds the value in the passed memory address to the accumulator.
        """
        self.accumulator += self.memory[address]

    def sub(self, address):
        """
        The LMC `SUB` instruction.

        Subtracts the value in the passed memory address from the accumulator.
        """
        self.accumulator -= self.memory[address]

    def dat(self, address, value):
        """
        The LMC `DAT` instruction.

        Marks the address as data and stores the passed value in it.
        """
        self.memory[address] = value

    def bra(self, pc):
        """
        The LMC `BRA` instruction.

        Sets the program counter to the passed line.
        """
        self.program_counter = pc

    def brp(self, pc):
        """
        The LMC `BRP` instruction.

        Branches to the passed line if the accumulator is positive or zero.
        """
        if not self.accumulator < 0:
            self.program_counter = pc

    def brz(self, pc):
        """
        The LMC `BRZ` instruction.

        Branches to the passed line if the accumulator contains zero.
        """
        if self.accumulator == 0:
            self.program_counter = pc

    def lda(self, address):
        """
        The LMC `LDA` instruction.

        Loads the value in the passed memory address into the accumulator.
        """
        self.accumulator = self.memory[address]

    def sta(self, address):
        """
        The LMC `STA` instruction.

        Stores the accumulator value in the passed memory address.
        """
        self.memory[address] = self.accumulator

    def inp(self):
        """
        The LMC `INP` instruction.

        Gets user input and stores the result in the accumulator.
        """
        self.accumulator = int(input("Enter a number: "))

    def out(self):
        """
        The LMC `OUT` instruction.

        Outputs the value in the accumulator.
        """
        print(self.accumulator)

    def hlt(self):
        """
        The LMC `HLT` instruction.

        Terminates the program.
        """
        self.running = False
        print("HALT")

    def exec_instruction(self, instruction):
        """
        Finds and executes the correct method for the passed instruction.
        """
        opcode, operand = instruction[0], instruction[1]
        if opcode == "ADD":
            self.add(operand)
        elif opcode == "SUB":
            self.sub(operand)
        elif opcode == "BRA":
            self.bra(operand)
        elif opcode == "BRZ":
            self.brz(operand)
        elif opcode == "BRP":
            self.brp(operand)
        elif opcode == "HLT":
            self.hlt()
        elif opcode == "LDA":
            self.lda(operand)
        elif opcode == "STA":
            self.sta(operand)
        elif opcode == "OUT":
            self.out()
        elif opcode == "INP":
            self.inp()


def main():
    source = sys.argv[1]
    lbc = LittleBenComputer()
    lbc.load_file(source)
    lbc.run()


if __name__ == "__main__":
    main()
