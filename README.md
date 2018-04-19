# brutetGOT
when you have some functions  and  offsets, use this script to brute the consistent one-to-one match and then get the certain libc.so

## About
The script is due to solve a recent CTF pwn game about blind format string.As I have leaked some address belong to some functions.But I can't identify their one-to-one match.So a brute force script like this is needed

## Usage
The script enums the permutations of the address and functions,and then search in the libc database online.
Just fill in the list 'raw_list' and make the network accessable.
