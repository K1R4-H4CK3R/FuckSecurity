senhas_comuns = [
    "123456", "password", "qwerty", "123456789", "abc123",
    "admin", "letmein", "welcome", "monkey", "12345",
    "12345678", "1234567", "sunshine", "iloveyou", "1234567890",
    "password1", "password123", "123456a", "football", "baseball",
    "qwertyuiop", "superman", "trustno1", "dragon", "michael",
    "123123", "shadow", "master", "hello", "killer",
    "1234", "123456789a", "hannah", "password2", "welcome1"
    "ana123", "123456" , "david123", "Dylan_2791", "lucas_123", "eleven_070","kira123", "1736207"
]

# Criando e escrevendo as senhas no arquivo
with open("wordlist.txt", "w") as arquivo:
    for senha in senhas_comuns:
        arquivo.write(senha + "\n")

print("Senhas comuns foram escritas no arquivo 'wordlist.txt'.")