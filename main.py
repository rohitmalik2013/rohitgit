name: Python Hello World

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  run-hello-world:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip

    - name: Run hello.py
      id: run_hello
      run: python hello.py

    - name: Verify output
      run: |
        echo "${{ steps.run_hello.outputs.stdout }}" | grep "Hello, World!" || exit 1
