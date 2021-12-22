
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

**NOTE:** If input bit string length > 2, gates will sometimes not be re-evaluated and therefore not set.
If you see 'None' in the output string, please comment out lines 20,21 in logic.py. This will result 
in much slower computation, but will yield the correct value. 

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

```
>>> multiply('1111', '1111')
FA1-Cin set to 0
FA4-A set to 0
FA4-Cout set to 0
FA8-A set to 0
FA8-Cout set to 0
FA5-Cin set to 0
FA9-Cin set to 0
FA1-A set to 1
FA2-A set to 1
FA3-A set to 1
FA1-B set to 1
FA1-S set to 0
FA1-Cout set to 1
FA2-Cin set to 1
FA2-B set to 1
FA2-S set to 1
FA5-A set to 1
FA2-Cout set to 1
FA3-Cin set to 1
FA3-B set to 1
FA3-S set to 1
FA6-A set to 1
FA3-Cout set to 1
FA4-Cin set to 1
FA4-B set to 1
FA4-S set to 0
FA7-A set to 0
FA7-Cout set to 0
FA8-Cin set to 0
FA4-Cout set to 1
FA8-A set to 1
FA5-B set to 1
FA5-S set to 0
FA5-Cout set to 1
FA6-Cin set to 1
FA6-B set to 1
FA6-S set to 1
FA9-A set to 1
FA6-Cout set to 1
FA7-Cin set to 1
FA7-B set to 1
FA7-S set to 0
FA10-A set to 0
FA10-Cout set to 0
FA11-Cin set to 0
FA7-Cout set to 1
FA8-Cin set to 1
FA8-B set to 1
FA8-S set to 1
FA11-A set to 1
FA8-Cout set to 1
FA12-A set to 1
FA9-B set to 1
FA9-S set to 0
FA9-Cout set to 1
FA10-Cin set to 1
FA10-B set to 1
FA10-S set to 0
FA10-Cout set to 1
FA11-Cin set to 1
FA11-B set to 1
FA11-S set to 1
FA11-Cout set to 1
FA12-Cin set to 1
FA12-B set to 1
FA12-S set to 1
FA12-Cout set to 1
'11100001'
```