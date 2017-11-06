# GL BaseCamp

## Automation using Selenium

The `test.py` script uses Selenium to test the Calculator application (written in JavaScript) against some basic tests defined in the script.

### Prerequisites

1. The script uses Google Chrome for testing, so Google Chrome has to be installed. 
2. `chromedriver.exe` has to be downloaded
3. The system `PATH` variable has to be updated to include the directory with `chromedriver.exe`
4. `calc.html` should be in the folder specified in the script (here: `C:\Users\ada.melentyeva\Documents\BaseCamp\Automation\`). Feel free to change line 25 in the script for it to reflect actual file location.

### Summary

The script is written using `Python 2.7`. It runs `calc.html` calculator and tests whether it performs correct basic arithmetic operations on two-digit numbers.

Test cases are specified as a pair of strings where the first string is the sequence of keys needed to be pressed (such keys are guaranteed to be pressed: `0123456789.*/+-=C`). and the second string is the expected result of the calculation.
