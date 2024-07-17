minhas_fruta = ("banana", "maçã", "laranja")
print(minhas_fruta)
meus_legumes = ("tomate", "cenoura", "batata")
print(meus_legumes)
mercado = (minhas_fruta + meus_legumes)
print(mercado)
if "laranja" in mercado:
    print("sim!")
else:
    print("Não!")

if "alface" in mercado:
    print("Sim!")
else:
    print("Não!")
    
print(mercado[5])