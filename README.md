# bun-ffi-bug

This is a small reproduction of a bug that occures when there are too many FFI functions.
It may not work on MacOS as this was made on WSL

To generate the files run `python main.py`
Then compile the shared library, if you are on Linux, you can run `gcc -c functions.c -fPIC -o functions.o && gcc -shared -o functions.so functions.o`
