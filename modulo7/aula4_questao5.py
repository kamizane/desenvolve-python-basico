import csv

livros = [
    ["A Revolução dos Bichos", "George Orwell", 1945, 144],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
    ["1984", "George Orwell", 1949, 328],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 863],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 432],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 574]
]


with open('meus_livros.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])

    escritor.writerows(livros)
