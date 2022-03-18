# Checks for url strings and runs a whois query
#@author Sophie Boyle https://github.com/sophieboyle
#@category Strings
#@keybinding
#@menupath Window.Who_Is
#@toolbar

from ghidra.program.util import DefinedDataIterator
import subprocess

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

def get_domains(strings):
    domains = []
    for s in strings:
        url_str = urlparse(s)
        if url_str.hostname:
            domains.append(url_str.hostname)
    return domains

def main():
    strings = [s.getDefaultValueRepresentation()[1:-1] \
               for s in DefinedDataIterator.definedStrings(currentProgram)]
    domains = get_domains(strings)
    for domain in domains:
        print('-'*100)
        print(subprocess.check_output(["whois", ".".join(domain.split(".")[1:])]))
    
if __name__ == "__main__":
    main()
