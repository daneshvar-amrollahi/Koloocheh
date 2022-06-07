# Koloocheh

![Koloocheh](assets/koloocheh.jpg)

**Koloocheh** is a decentralized peer-to-peer file sharing system implemented with the [gRPC](https://grpc.io/) framework in Python.

## Installation

To run Koloocheh, follow the following steps:

1. Make sure you have ```python3``` and ```pip``` installed on your machine. 

2. Clone the repository:
    ```shell
    $ git clone git@github.com:daneshvar-amrollahi/Koloocheh.git
    $ cd Koloocheh
    ```

3. Create a virtual environment in the ```.venv``` directory:
    ```shell
    $ pip install --user virtualenv
    $ python -m venv .venv
    ```

3. Activate the virtual environment:
    ```shell
    $ source .venv/bin/activate
    ```

4. Install the required dependencies:
    ```shell
    $ pip install -r requirements.txt
    ```

## How to run?

### Master
The master should be created exactly once (in the very beginning):
```shell
$ python Koloocheh.py master
```

### Peer
A new peer can join the network using the following command:
```shell
$ python Koloocheh.py peer <ip> <port>
```

### Supported Commands for Peer

A peer can upload a file using the following command:
```shell
$ upload <file_name> <file_data>
```

A peer can view its own files using the following command:
```shell
$ get_files
```

A peer can request a file using the following command:

```shell
$ download <file_name>
```

### Supported Commands for Master

The graph representing the whole network can be viewed using the following command:
```shell
$ show
```

## Documentation

Please refer to our wiki at https://github.com/daneshvar-amrollahi/Koloocheh/wiki for further details on how this system works. 

## Contributors
* [Daneshvar Amrollahi](https://daneshvar-amrollahi.github.io/)
* [Mahyar Karimi](https://github.com/moyarka)