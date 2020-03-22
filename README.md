# proto-python

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/proto-python

## About

Using Protobuf with Python

## Setup software

1. Setup the Python version
pipenv --python $(which python3)

2. Install libraries manually
pipenv install protobuf

3. Download the protocol compiler from  https://github.com/protocolbuffers/protobuf/releases
mkdir protobuf
pushd protobuf
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.11.4/protoc-3.11.4-linux-x86_64.zip
unzip protoc-3.11.4-linux-x86_64.zip
popd

4. Display the version of the protocol compiler
./protobuf/bin/protoc --version

## Protobuf Python example1

1. Generate python code for protobuf example1
make protoc_exmaple1

2. Run the example
python example1/proto-python-example1

## Links

* [Protocol buffers][1000] documentation

[1000]: https://developers.google.com/protocol-buffers/

* [Python protobuf][1010] project

[1010]: https://github.com/protocolbuffers/protobuf/tree/master/python

* Using [Protobuf from Python][1020]

[1020]: https://developers.google.com/protocol-buffers/docs/pythontutorial

* [Comments from a proto][1030] file

[1030]: https://stackoverflow.com/questions/32742601/reading-comments-from-proto-files-using-a-protocol-buffers-descriptor-object


