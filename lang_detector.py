from langdetect import detect

text = input("Enter a text :")

language = detect(text)

print("Detected language :", language)