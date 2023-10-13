import glob

modelName = ''.join(glob.glob('*.gguf'))
print("Current Model: ", modelName, "\n")