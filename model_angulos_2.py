import math

angle = math.radians(float(input("Digite o valor do ângulo em graus: ")))
seno = math.sin(angle)
cosseno = math.cos(angle)
if cosseno == 0:
	print("O cosseno é zero, a tangente não pode ser calculada.")
else:
	tangente = math.tan(angle)
	print(f"Seno: {seno:.2f}")
	print(f"Cosseno: {cosseno:.2f}")
	print(f"Tangente: {tangente:.2f}")
