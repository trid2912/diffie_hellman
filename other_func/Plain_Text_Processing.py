def convert_to_binary(self, text):
    bin_text = np.array([[int(j) for j in '{0:05b}'.format((ord(i)-ord('A'))%32)] for i in text]).T

    return bin_text

def CharConvertAscii(self, s):
    nchars = len(s)
    x = sum(ord(s[byte])<<8*(nchars-byte-1) for byte in range(nchars)) # string to int or long. Type depends on nchars
    return x

def AsciiConvertChar(self, s):

    x = ''.join(chr((s>>8*(nchars-byte-1))&0xFF) for byte in range(nchars)) # int or long to string
    return x
