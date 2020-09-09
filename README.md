# SeqTools
Simple app for basic nucleotide sequence manipulation.\
This includes **Reverse**, **Complement**, **Reversed complement** and **Translation** options.

## Installation
App was tested on python 3.7.9 and does not support 3.8.X+ versions.

Clone repository to your local machine and install requirements with `pip install -r requirements.txt`.

### Linux
Install `xclip` package, which is needed to control clipboard.\
On ubuntu-like systems do the following command: `sudo apt install xclip`.

### Windows
Everything should work out of the box.


## Usage
App may be packaged with pyinstaller.

App works with nucleotide sequences, which are in clipboard.

3 steps of usage:
1. Copy your sequence into clipboard (digits and spaces play no part).
2. Press on button with action, that you like to perform.
3. Clipboard content changes on needed one, so you can paste it anywhere you want.

