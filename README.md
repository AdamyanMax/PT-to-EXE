# PT-to-EXE
Convert python files to .exe and run them from the cmd

1. First install pyinstaller:
```pip install pyinstaller```

2. Convert .py to .exe
```pyinstaller --onefile py_to_exe.py```

3. After it has been compiled run by typing this command: ```../dist/py_to_exe.exe --function_name args```

Currently, there are only 3 functions: hello_world(--hw); list_sum(--ls); input_asker(--ia);

Example:
Input: ../dist/py_to_exe.exe --hw Sam
Output: Hello Sam

Input: ../dist/py_to_exe.exe --ls 1 2 3 4
Output: 10

Input: ../dist/py_to_exe.exe --ia
Output: What's your name?
Input: Test/\
Output: Test/\
