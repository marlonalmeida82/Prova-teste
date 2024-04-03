#defina as três variáves
nome_maquina=input("Digite o nome da máquina:")
tempo_uso=int(input("Digite o tempode uso(em anos):"))
ligado=bool(input("Amáquinaestá ligada?(True/false):"))


#Exibindo os valores lidos e seus tipos
print(f"Nome da máquina:{nome_maquina}(Tipo:{type(nome_maquina)})")
print(f"Tempo de uso:{tempo_uso}anos(Tipo:{type(tempo_uso)})")
print(f"ligado:{ligado}(Tipo:{type(ligado)})")

