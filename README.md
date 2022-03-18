# Ghidra WhoIs

A script for Ghidra which checks for url strings, and runs a whois query. Requires whois to be installed.

## Limitations

Since Ghidra uses Jython 2.7, importing libraries that would help in parsing of domains etc like tldextract would require the installation of python 2.7 on user's desktops. To avoid subjecting users to the installation of deprecated software, only the basic libraries are used. Currently the script just removes the top level label (obviously this won't work for all domains though). The script should be expanded to pattern match for the root domain.
