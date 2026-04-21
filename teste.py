def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def main() -> None:
    entrada = input("Digite a temperatura em Celsius: ")
    celsius = float(entrada)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius:.1f}°C equivale a {fahrenheit:.1f}°F")


if __name__ == "__main__":
    main()
