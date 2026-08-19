import math


def calcular_razoes(cateto_oposto: float, cateto_adjacente: float) -> tuple[float, float, float, float]:
	if not math.isfinite(cateto_oposto) or not math.isfinite(cateto_adjacente):
		raise ValueError('Os catetos devem ser números finitos.')

	if cateto_oposto <= 0 or cateto_adjacente <= 0:
		raise ValueError('Os catetos devem ser maiores que zero.')

	hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
	seno = cateto_oposto / hipotenusa
	cosseno = cateto_adjacente / hipotenusa
	tangente = cateto_oposto / cateto_adjacente

	return hipotenusa, seno, cosseno, tangente


def main() -> None:
	try:
		cateto_oposto = float(input('Digite o valor do cateto oposto: '))
		cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
		hipotenusa, seno, cosseno, tangente = calcular_razoes(
			cateto_oposto, cateto_adjacente
		)
	except ValueError as erro:
		print(f'Entrada inválida: {erro}')
		return

	print(f'Valor da hipotenusa: {hipotenusa:.4f}')
	print(f'Valor seno: {seno:.4f}')
	print(f'Valor cosseno: {cosseno:.4f}')
	print(f'Valor tangente: {tangente:.4f}')


if __name__ == '__main__':
	main()

