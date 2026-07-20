# PRODIGY_CS_01
A Python command-line tool that encrypts and decrypts text using the Caesar cipher. Supports custom shift values, preserves letter case, and leaves non-alphabetic characters untouched. Built to demonstrate core cryptographic and Python fundamentals.

## Caesar Cipher Tool
A simple command-line tool to encrypt and decrypt messages using the classic Caesar cipher — a substitution cipher where each letter is shifted a fixed number of places in the alphabet.

## Features
Encrypt or decrypt any text message
Custom shift value (supports negative shifts and shifts greater than 26)
Preserves letter case
Leaves spaces, punctuation, and numbers unchanged
Pure Python, no external dependencies

## How it works
Each letter in the message is shifted forward (encryption) or backward (decryption) through the alphabet by the shift value. For example, with a shift of 3:

A → D
Hello → Khoor
