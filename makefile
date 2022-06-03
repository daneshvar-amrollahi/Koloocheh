peer_proto: protos/koloocheh.proto
	python3 -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/koloocheh.proto
