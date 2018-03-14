# Project Title

PySetBan: this python scripts will issue a geetpeerinfo with a given wallet, and ban (setban) all the clients that don't use a specific wallet subversion.

## Getting Started

Download the file. Ensure you have Python 2.7 at minimum. It should work with Python 3.6 as well.

### Prerequisites

Wallet as to support standard "setban" command.

### Example

./PySetBan.py -s 86400 -c numusd --subver '/Rhizocarpon:1.0.1.1/'

Where s in the number of seconds to ban, c is the wallet command line client and subver is the string that identifies the version to retain.

## Authors

* **Denis Roy** - *Initial work*

## License

This project is licensed under the GNU General Public License, version 2

## Acknowledgments

* Hat tip to anyone who found this.