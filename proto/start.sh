#!/bin/bash
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. investment.proto

echo copying the generated files to the server folder
cp investment_pb2_grpc.py ../server
cp investment_pb2.py ../server
echo copying the generated files to the client folder
cp investment_pb2_grpc.py ../client
cp investment_pb2.py ../client