# **PyGates**


PyGates is a library for using the logic gates as a conditions on Python.


#### Installation
____________________

PyGates can be installed using:

```sh
pip install pygates
```

Or if you have multiple versions of Python and pip on your machine, try:

```sh
pip3 install pygates
```

Alternatively, you can pull the library directly from GitHub:

```sh
git clone https://github.com/Baticaly/PyGates
cd PyGates
python setup.py install
```

#### Usage
____________________

You can just basicaly use the gates as a condition like:

    PyGates.Gates.AND('input1', 'input2')

Or just for calling the functions easily you can create a basic definition for library:


    import pygates
    lg = pygates.Gates

And you can easily call it by using:


    lg.AND('input1', 'input2')

#### Gates
____________________


| Gate | Function | 
| ------ | ------ | 
| AND | ```PyGates.Gates.AND( 'A' , 'B' )``` | 
| NAND | ```PyGates.Gates.NAND( 'A' , 'B' )``` | 
| OR | ```PyGates.Gates.OR( 'A' , 'B' )``` |  
| NOR | ```PyGates.Gates.NOR( 'A' , 'B' )``` |
| XOR | ```PyGates.Gates.XOR( 'A' , 'B' )``` | 
| XNOR | ```PyGates.Gates.XNOR( 'A' , 'B' )``` | 

License
----

MIT License

Copyright (c) 2020 Batuhan Ergün

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


