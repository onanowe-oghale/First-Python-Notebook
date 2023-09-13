

sample_text = "Hello, 你好, مرحبا"
encoded_text = sample_text.encode("utf-16", "little")

print(encoded_text, "\n <===>", sample_text)
