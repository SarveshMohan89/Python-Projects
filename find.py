#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extra
text = "X-DSPAM-Confidence:    0.8475";
x=text.find(':')
y=text[x+1:]
z=float(y)
print(z)
