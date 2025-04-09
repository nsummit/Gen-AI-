def hybrid_encode(text: str) -> str:
    encoded = []
    for char in text:
        if ord(char) < 128:
            encoded.append("1" + str(ord(char)))
        else:
            utf8_bytes = char.encode('utf-8')
            encoded.append("2" + "-".join(str(b) for b in utf8_bytes))
    return " ".join(encoded)


def hybrid_decode(text: str) -> str:
    tokens = text.strip().split()
    decoded = ""
    for token in tokens:
        if token.startswith("1"):
            decoded += chr(int(token[1:]))
        elif token.startswith("2"):
            byte_array = bytes(int(b) for b in token[1:].split("-"))
            decoded += byte_array.decode('utf-8')
    return decoded


# Example usage
if __name__ == "__main__":
    original_text = "Hello, दोस्तों !"
    encoded = hybrid_encode(original_text)
    print("Encoded:", encoded)

    decoded = hybrid_decode(encoded)
    print("Decoded:", decoded)
