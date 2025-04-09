# Text Encoder/Decoder
This project provides a hybrid encoding/decoding utility that handles both ASCII and Unicode characters. 

# Features
- Encodes ASCII characters (< 128) as "1" + ASCII code.
- Encodes non-ASCII (Unicode) characters as "2" + UTF-8 byte values (joined by '-').
- Returns encoded strings as space-separated values.
- Reconstructs the original string accurately using hybrid_decode.

# Run the script
`python main.py`

# Example
```
text = "Hello, दोस्तों!"
encoded = encoder(text)
print("Encoded:", encoded)

decoded = decoder(encoded)
print("Decoded:", decoded)
```