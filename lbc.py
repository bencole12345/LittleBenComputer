import sys


class LittleBenComputer:

    def run(self):
        self.running = True
        self.accumulator = 0
        self.program_counter = 0
        while self.running:
            next_instruction = self.instructions[self.program_counter]
            self.program_counter += 1
            self.exec_instruction(next_instruction)

    def load_file(self, source):
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
        self.accumulator += self.memory[address]

    def sub(self, address):
        self.accumulator -= self.memory[address]

    def dat(self, address, value):
        self.memory[address] = value

    def bra(self, pc):
        self.program_counter = pc

    def brp(self, pc):
        if not self.accumulator < 0:
            self.program_counter = pc

    def brz(self, pc):
        if self.accumulator == 0:
            self.program_counter = pc

    def hlt(self):
        self.running = False
        print("HALT")

    def lda(self, address):
        self.accumulator = self.memory[address]

    def sta(self, address):
        self.memory[address] = self.accumulator

    def inp(self):
        self.accumulator = int(input("Enter a number: "))

    def out(self):
        print(self.accumulator)

    def exec_instruction(self, instruction):
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