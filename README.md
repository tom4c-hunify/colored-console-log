# Colored console logs for Python 3(>=3.6)

The project is aimed to give specific handlers and log formatters to users for coloring stream logs in multiple ways.  
Among the main features some utilities are also provided in order to make use easier.

## Outputs

Output of the logger is defaulted to stdout but can be changed just in case as normal logger.

## Formats

All default formatting styles are supported (`%(levelname)s`, `{levelname}` and `${levelname}`).

## Modes

There are four different modes at the moment for coloring:

* Mode 0 - NO_COLOR  
  No coloring (output formatting) is done, everything remains the same as in normal cases
* Mode 1 - LEVEL  
  Only `levelname` is colored according to the setup
* Mode 2 - MESSAGE  
  Only `message` is colored according to the setup
* Mode 3 - ALL  
  The whole output is colored according to the setup

## Colors

Colors are stored in an enum and represent standard terminal formatting escapes such as ```\x1b[0m```.  
The following colors could be used (and represent the following formatting):

``` 
NO_COLOR = "\x1b[0m"  
BLACK = "\x1b[30m"  
RED = "\x1b[31m"  
GREEN = "\x1b[32m"  
YELLOW = "\x1b[33m"  
BLUE = "\x1b[34m"  
MAGENTA = "\x1b[35m"  
CYAN = "\x1b[36m"  
LIGHT_GRAY = "\x1b[37m"  
DARK_GRAY = "\x1b[90m"  
LIGHT_RED = "\x1b[91m"  
LIGHT_GREEN = "\x1b[92m"  
LIGHT_YELLOW = "\x1b[93m"  
LIGHT_BLUE = "\x1b[94m"  
LIGHT_MAGENTA = "\x1b[95m"  
LIGHT_CYAN = "\x1b[96m"  
WHITE = "\x1b[97m"  
```

## Levels

The level can be set through the Handler and Formatter objects as well.  
The defaults are the following:

```
logging.NOTSET: TerminalColors.NO_COLOR,
logging.DEBUG: TerminalColors.BLUE,
logging.INFO: TerminalColors.GREEN,
logging.WARNING: TerminalColors.YELLOW,
logging.ERROR: TerminalColors.RED,
logging.CRITICAL: TerminalColors.MAGENTA
```

## Install

```
pip3 install cclogs
```

## Basic usage

See examples attached