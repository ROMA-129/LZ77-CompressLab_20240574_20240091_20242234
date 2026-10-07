def decompress(tags):
    output = []

    for position, length, next_symbol in tags:
        if length > 0:
            if position <= 0 or position > len(output):
                raise ValueError("Invalid position in tag")

            start = len(output) - position

            for k in range(length):
                output.append(output[start + k])

        if next_symbol is not None:
            output.append(next_symbol)

    return "".join(output)

def verify(original_text, tags):
    result = decompress(tags)

    if result == original_text:
        print("Original Text     :", original_text)
        print("Decompressed Text :", result)
        print("Verification      : PASSED")
        return True

    print("Original Text     :", original_text)
    print("Decompressed Text :", result)
    print("Verification      : FAILED")
    return False
