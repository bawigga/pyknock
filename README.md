## About

A simple port scanner to get used to working with Python's threading and socket libraries.

## Usage

Checkout the command line help using the `-h` flag.
	python pyknock.py -h

## How it works

### pyknock.py

This handles processing all the command line flags. It then creates a new `Scanner` instance

### scanner.py

When `scanner.py` initialized it creates a `Queue` of hosts and a `list` of `ScannerThread` objects. Each `ScannerThread` is started, and in a continuous loop dequeues a host from the Scanner class. If it can successfully open a TCP connection to that host's port then it reports it back to the user.