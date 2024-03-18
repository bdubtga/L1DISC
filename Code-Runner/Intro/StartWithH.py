while True:
  word = input("Give a word that starts with H: ")
  if word[0].lower() == "h":
      print(f"Yes, {word} starts with H!")
  else:
      print(f"No, {word} doesn't start with H!")
      break
