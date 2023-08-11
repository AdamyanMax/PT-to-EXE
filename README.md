# PT-to-EXE
Convert python files to .exe and run them from the cmd

1. First install pyinstaller: <br />
```pip install pyinstaller```

2. Convert .py to .exe: <br />
```pyinstaller --onefile py_to_exe.py```

3. After it has been compiled run by typing this command: <br />
 ```../dist/py_to_exe.exe --function_name args```

Currently, there are only 3 functions: hello_world(--hw); list_sum(--ls); input_asker(--ia);

Example: <br />
Input: ../dist/py_to_exe.exe --hw Sam <br />
Output: Hello Sam <br />

Input: ../dist/py_to_exe.exe --ls 1 2 3 4 <br />
Output: 10 <br />

Input: ../dist/py_to_exe.exe --ia <br />
Output: What's your name? <br />
Input: Test/\ <br />
Output: Test/\ <br />
