def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))


fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")