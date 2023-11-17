def transform_text(text, text_format):
    transformed_values = []

    for i in text:
        ascii_value = ord(i)
        if text_format == "Hex":
            hex_value = f"0x{ascii_value:X}"
            transformed_values.append(hex_value)
        elif text_format == "Binary":
            binary_value = f"0b{ascii_value:b}"
            transformed_values.append(binary_value)

    resulting_string = " ".join(transformed_values)
    return resulting_string


transformer_hex = transform_text("Hallo", "Hex")
transformer_bin = transform_text("Hallo", "Binary")
print(transformer_bin)
print(transformer_hex)
