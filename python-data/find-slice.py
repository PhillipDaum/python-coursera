# Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
x = text.find("0")
y = len(text)
z = text[x : ]
fn = float(z)
print(fn)

otherText = [1, 2, 3, 4]

for item in otherText :
    print('hi')