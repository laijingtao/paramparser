# Parameter Parser

## Why I need this

In scientific computation, I often have problem with model parameters. Sometimes there are too many parameters in a model and I lose track of them. Sometimes I want to do a sensitivity test and change several parameters, but I don't want to mess up my code.

A good practice to manage parameters or options for your model is to use [argparser](https://docs.python.org/2/library/argparse.html#module-argparse). It supports command-line options and arguments. Another good way is to read values for parameter from a file. A model I used - [Landlab](http://landlab.github.io/#/) supports this method. I found this is better than argparser because I can save a copy of the parameter file with the results and next time I can use the exact same parameters to reproduce all the results.

Therefore, I write this paramparser module to support reading parameter values or options in my other models.

## Usage
Write your parameter file like this:
```
keyword:
value
another_keyword:
another_value
```
For example:
```
height:
1.8
width:
1
switch:
True
```
Please note the colon symbol ":" behind keyword.

Read from file:
```python
from paramparser import ParamParser

parser = ParamParser()
height = parser.read(key='height', param_type='float')
width = parser.read(key='width', param_type='int')
switch = parser.read(key='switch', param_type='bool')
```