# LittleBenComputer
An implementation of Little Man Computer written in Python

## Why?
Because of who I am as a person

## Usage
To run LittleBenComputer, run the Python file from the command line. Pass the path to the LBC code as the first argument.
```
python lbc.py <filepath>
```

Example:
```
python lbc.py test.lbc
```

The `.lbc` extension is not required: anything should work.

## Opcodes
The opcodes available are as following:

`ADD x` - adds `x` to the value in the accumulator.

`SUB x` - subtracts `x` from the value in the accumulator.

`DAT x` - stores the value of `x` in the marked memory address.

`LDA` - reads an input and stores it in the accumulator.

`OUT` - outputs the value in the accumulator.

`STA x` - stores the value in the accumulator in address `x`.

`BRA x` - branches to `x`.

`BRP x` - branches to `x` if the value in the accumulator is zero or positive.

`BRZ x` - branches to `x` if the value in the accumulator is zero.

`HLT` - terminates the program.

To mark a line so that it can be referenced in the future, write the name of the pointer before the instruction. For example,

```
myLoop <opcode> <operand>
```

creates a reference to this line of code with the name `myLoop`, so that it can be branched to in the future:

```
BRA myLoop
```

will then branch to this line.

To use a variable, first allocate it using a `DAT` instruction and a default value. For example,

```
x DAT 12
...
OUT x
```

will output `12` provided that the value of `x` has not been updated in the meantime.