# memtrace2npz

This project is a utility for converting the output of DynamoRIO's memtrace-x86 client to an npz file. The output can be compressed into a zip file as well. 

## Installation

```
pip3 install memtrace2npz
```

## Usage

```
memtrace2npz < -i inputfile > [ -o outfile ] [ -h ] [ -f ]
```

You must specifiy the input file with `-i`. You may optionally specify an outputfile -- if you don't, the output file will be in the current directory with the basename of your input file, and with the extension changed to `.npz`.

You may skip the check for the existence of the outfile with `-f`. 

## Testing

```
pytest
```
