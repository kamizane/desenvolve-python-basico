import emoji
print(emoji.emojize("Emojis disponíveis:\n:thumbs_up: - :thumbs_up:\n:red_heart: - :red_heart:\n:partying_face: - :partying_face:\n:thinking_face: - :thinking_face:"))
print("digite uma frase e ela será emojizada:")
frase = str(input())
print(emoji.emojize("Frase emojizada:\n %s" % (frase)))