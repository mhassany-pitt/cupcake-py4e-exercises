data = 'X-DSPAM-Confidence: 0.8475'
colon_position = data.find(':')
number_str = data[colon_position + 1:].strip()
confidence = float(number_str)
print(confidence)
