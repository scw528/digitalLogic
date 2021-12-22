
# Digital Logic

Python Implementation of digital logic gates and some of their applications.

### Applications:
The following applications can be computed for bit strings of length n. You can find diagrams for the implemented circuits under diagrams.
- Addition
- Subtraction
- Multiplication


## Getting Started
1. Ensure Python is installed
   - https://wiki.python.org/moin/BeginnersGuide/Download
2. Clone this repository
   - ``` git clone https://github.com/scw528/digitalLogic.git```
3. Navigate to location of project on local machine
   - ```cd digitalLogic ```
4. Start python interpreter
   - ``` python ```

## Usage
Once the interpreter is started, import required modules

``` >>> from main import add, subtract, multiply ```

Now, you can use these functions. The values of the gates will be printed to the console as they are evaluated.

```
>>> add('01','01')
FA0-Cin set to 0
FA0-A set to 1
FA0-B set to 1
FA0-S set to 0
FA0-Cout set to 1
FA1-Cin set to 1
FA1-A set to 0
FA1-Cout set to 0
FA1-B set to 0
FA1-S set to 1
'10'
```

```
>>> subtract('1101', '0011')
FA0-Cin set to 0
FA0-A set to 0
FA0-Cout set to 0
FA1-Cin set to 0
FA0-B set to 1
FA0-S set to 1
FA1-A set to 0
FA1-Cout set to 0
FA2-Cin set to 0
FA1-B set to 0
FA1-S set to 0
FA2-A set to 1
FA2-B set to 0
FA2-S set to 1
FA2-Cout set to 0
FA3-Cin set to 0
FA3-A set to 1
FA3-B set to 0
FA3-S set to 1
FA3-Cout set to 0
FA0-Cin set to 0
FA0-A set to 1
FA0-B set to 1
FA0-S set to 0
FA0-Cout set to 1
FA1-Cin set to 1
FA1-A set to 0
FA1-Cout set to 0
FA2-Cin set to 0
FA1-B set to 0
FA1-S set to 1
FA2-A set to 1
FA2-B set to 1
FA2-S set to 0
FA2-Cout set to 1
FA3-Cin set to 1
FA3-A set to 1
FA3-B set to 1
FA3-S set to 1
FA3-Cout set to 1
'1010'
```

**NOTE:** If input bit string length > 2, gates will sometimes not be re-evaluated and therefore not set.
If you see 'None' in the output string, please uncomment lines 21,22 in logic.py. This will result 
in much slower computation, but will yield the correct value. 