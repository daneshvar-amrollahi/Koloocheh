# NutellaMD

**NutellaMD** is a decentralized peer-to-peer file sharing system implemented with the [gRPC](https://grpc.io/) framework in Python.

## Installation

To run NutellaMD, follow the following steps:

1. Make sure you have ```python3``` and ```pip``` installed on your machine. 

2. Clone the repository:
    ```
    $ git clone git@github.com:daneshvar-amrollahi/NutellaMD.git
    $ cd NutellaMD
    ```

3. Create a virtual environment in the ```.venv``` directory:
    ```
    $ pip install --user virtualenv
    $ python -m venv .venv
    ```

3. Activate the virtual environment:
    ```
    $ source .venv/bin/activate
    ```

4. Install the required dependencies:
    ```
    $ pip install -r requirements.txt
    ```

## How to run?

### Master
The master is created exactly once (in the very beginning):
```
$ python NutellaMD.py master
```

### Peer
A new peer can join the network using the following command:
```
$ python NutellaMD.py peer <ip> <port>
```