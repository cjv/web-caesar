def alphabet_position(letter):
	#find ordinal, and return letter position a0-z25
	#does not need to be case sensitive
	x = ord(letter.lower())
	return (x - 97)	

def rotate_character(char, rot): 
  y = alphabet_position(char)
  rotated = 0
  newchar = ''
  cap_check = ord(char)
  
  if ord(char) < 65 or ord(char) > 122:
    return char
  elif ord(char) >= 91 and ord(char) <= 96:
    return char
  else:
    if y + rot >= 26:
      rotated = ((y + rot) % 26)
    else:
      rotated = y + rot     
    if cap_check >= 65 and cap_check <= 90:
      newchar = chr(rotated + 65) #make upper
    else:
      newchar = chr(rotated + 97) #make lower
  return newchar #return the single rotated character

def encrypt(text, rot):
  """Take the text and iterate over each letter using rotate_char, then return"""
  encrypted = ''
  for char in text:
    encrypt_char = rotate_character(char, rot)
    encrypted = encrypted + encrypt_char
  return encrypted