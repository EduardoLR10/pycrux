
# Pycrux

Pycrux is a simple python program created with the intent of applying different types of errors into a sequence of bytes contained in a text file and sending it via the serial port. The main goal is to have a convenient way of testing the behaviour of a second piece of software, i.e., see how it behaves error handling.

## Error Types

There are 4 different types of errors available in the current version of the software:

- Burst Error: it changes an existing bytes randomly. It will always change 2 or more bytes in sequence
- Byte Error: it changes one existing byte randomly.
- Bit Error: it changes a random bit in a randomly chosen byte.
- Removal Error: it removes one existing byte randomly.

## How to Use

To execute the software, being in the correct directory, use something like:

``` python pycrux.py data.txt -x ```

In the example `x` needs to be one of the following:

- -u for Burst Error
- -y for Byte Error
- -b for Bit Error
- -r for Removal Error

There is a bonus flag, `--report`, which adds more granular information of the process, in addition to the general information system.

## Observations

- It is always necessary to provide a file with data to work with
- It is always necessary to provide a valid error introduction flag
- The baudrate and port are fixed **for now** (baudrate = 19200 and port = COM6)
