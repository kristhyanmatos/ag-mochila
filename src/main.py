from evolucao import Evolucao
from matplotlib import pyplot as plt

evolucao = Evolucao(
    geracoes=70,
    volume_maximo=3,
    taxa_mutacao=0.05,
    volumes_e_precos=[
        [0.635, 849],
        [0.527, 3999],
        [0.751, 999.9],
        [0.00350, 2499],
        [0.496, 199.90],
        [0.0319, 299.29],
        [0.400, 4346.99],
        [0.290, 3999.90],
        [0.200, 2999.90],
        [0.0424, 308.66],
        [0.0544, 429.90],
        [0.870, 1199.89],
        [0.498, 1999.90],
        [0.0000899, 2199.12],
    ],
    numero_de_cromossomos=112,
)

populacao = evolucao.criar_populacao()
historico_de_fitness = [evolucao.media_fitness(populacao)]

for i in range(70):
    populacao = evolucao.evoluir(
        populacao,
    )
    historico_de_fitness.append(evolucao.media_fitness(populacao))

print("\nSuguestões de boas soluções:")
for index in range(6):
    print(populacao[index])


plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.xlabel("Gerações")
plt.ylabel("Preços médios do caminhão")
plt.show()
