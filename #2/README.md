# RE #2

### Task:
- Figure out what the code does.
 
### Procedure: 

We load in a 64 bit word and, do a byte reversal on it, and then perform a series on bitwise operations with a pattern of and, shift, or with a mask being applied.
I chose to translate the assembly code into a python script to get an idea of the operations being performed. The python code is provided in the git repo.
The output after each operation is as follows:

1) 00000000000000000010101111110110 < input
2) 11110110001010110000000000000000 < byte reversal
3) 01101111101100100000000000000000 < operation 1
4) 10011111111010000000000000000000 < operation 2
5) 01101111110101000000000000000000 < operation 3 and output

So, it seems like the code is reversing the bits of the data provided as input. 

Googling the values for the mask brough up results for a bit reversal algorithm so I will take that as confirmation that the code is intended to reverse the bits. 
