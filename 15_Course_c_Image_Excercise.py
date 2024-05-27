# Image Exercise
# In the folder "Working with Images" (same folder this notebook is located in) 
# there are two images we will be working with:

# word_matrix.png
# mask.png
# The word_matrix is a .png image that contains a spreadsheet of words with a 
# hidden message in it.

# Your task is to use the mask.png image to reveal the hidden message inside the word
# _matrix.png. Keep in mind, you may need to make changes to the mask.png in order for 
# this to work. That is all we'll say for now, since we really want you to discover this 
# on your own!

from PIL import Image
words = Image.open('word_matrix.png')
print(type(words))
print(words)

mask=Image.open('mask.png')
print(mask)


print(mask.size)
print(words.size)

mask.putalpha(200)
print(mask)

words.paste(mask,(0,0),mask)
print(words.show())


