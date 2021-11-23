#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse
from pymd5 import md5, padding, test


##########################
# Example URL parsing code:
res = urlparse(
    'https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]
    #print("Included URL: " + url)

    #################################
    # Your length extension code here

    # Parse given URL for real authenticated token, and length of commands (does not include first '&', does include following ones),
    res = urlparse(url)
    auth_token = res.query[6:38]
    #print("Auth token: " + auth_token)
    commands = res.query[39:]
    #print("Commands: " + commands)
    commands_length = len(commands)
    #print("Length of commands: " + str(commands_length))

    # Compute num of bits of original text used to generate token (8 byte password + length of commands) including padding bits!!
    # Know: bits = (length_of_m + len(padding(length_of_m*8)))*8
    password_length = 8
    m_length = password_length + commands_length
    bits = (m_length + len(padding(m_length*8)))*8

    # Generate new  md5 class from orignal token "state" and count of num of bits used from original
    extensionHashFunction = md5(state=bytes.fromhex(auth_token), count=bits)

    # Create new hash (update) token from md5 original state with our malicious command
    extensionHashFunction.update('&command=UnlockSafes')
    malicious_token = extensionHashFunction.hexdigest()
    # print(malicious_token)

    # Generate new url, add padding, add malicious command, replace auth token with malicious token
    pad = quote(padding((m_length * 8)))
    newUrl = url + pad + '&command=UnlockSafes'
    tokenStartIndex = newUrl.find('token') + 6
    tokenEndIndex = tokenStartIndex + 32
    # my auto linter wont let me have on same line...
    newUrl = newUrl[:tokenStartIndex] + \
        malicious_token + newUrl[tokenEndIndex:]  # cant change

    print(newUrl)
