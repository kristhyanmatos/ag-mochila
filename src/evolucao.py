from random import getrandbits, randint, random


class Evolucao:
    def __init__(
        self,
        volume_maximo,
        volumes_e_precos,
        numero_de_cromossomos,
        geracoes,
        taxa_mutacao,
    ) -> None:
        self.volume_maximo = volume_maximo
        self.volumes_e_precos = volumes_e_precos
        self.numero_de_cromossomos = numero_de_cromossomos
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao
        self.numero_de_itens = len(volumes_e_precos)

        self.__informacoes_iniciais()

    def evoluir(self, populacao):
        maes = []
        for individuo in populacao:
            preco_total_individuo = self.fitness(individuo)
            if preco_total_individuo >= 0:
                maes.append([preco_total_individuo, individuo])

        maes.sort(reverse=True)

        # Reprodução
        filhas = []
        while len(filhas) < self.numero_de_cromossomos:
            homem, mulher = self.__selecao_por_roleta(maes)
            meio = len(homem) // 2
            filha = homem[:meio] + mulher[meio:]
            filhas.append(filha)

        # Mutação
        for individuo in filhas:
            if self.taxa_mutacao > random():
                index_mutacao = randint(0, len(individuo) - 1)
                if individuo[index_mutacao] == 1:
                    individuo[index_mutacao] = 0
                else:
                    individuo[index_mutacao] = 1

        return filhas

    def media_fitness(self, populacao):
        precos_individuos_maiores_zero = []
        for individuo in populacao:
            preco_total_individuo = self.fitness(individuo)
            if preco_total_individuo >= 0:
                precos_individuos_maiores_zero.append(preco_total_individuo)

        soma = sum(precos_individuos_maiores_zero)
        return soma / (len(populacao) * 1.0)

    def fitness(self, individuo):
        preco_total = 0
        volumeo_total = 0
        for index, _ in enumerate(individuo):
            preco_total += individuo[index] * self.volumes_e_precos[index][1]
            volumeo_total += individuo[index] * self.volumes_e_precos[index][0]

        return -1 if (self.volume_maximo - volumeo_total) < 0 else preco_total

    def criar_populacao(self):
        populacao = []
        for _ in range(self.numero_de_cromossomos):
            populacao.append(self.__criar_individuo())

        return populacao

    def __criar_individuo(self):
        individuo = []
        for _ in range(self.numero_de_itens):
            individuo.append(getrandbits(1))

        return individuo

    def __selecao_por_roleta(self, maes):
        listas = list(zip(*maes))
        # listas[0] -> Preços
        # listas[1] -> Cromossomos

        fitness_total = sum(listas[0])

        index_pai = self.__sortear(fitness_total, listas[0])
        index_mae = self.__sortear(fitness_total, listas[0], index_pai)

        pai = listas[1][index_pai]
        mae = listas[1][index_mae]

        return pai, mae

    def __sortear(
        self,
        fitness_total,
        lista_precos,
        index_a_ignorar=-1,
    ):
        roleta = []
        acumulado = 0
        valor_sorteado = random()

        if index_a_ignorar != -1:
            fitness_total -= lista_precos[index_a_ignorar]

        for index, preco in enumerate(lista_precos):
            if index_a_ignorar != index:
                acumulado += preco
                roleta.append(acumulado / fitness_total)
                if roleta[-1] >= valor_sorteado:
                    return index

    def __informacoes_iniciais(self):
        for index, item in enumerate(self.volumes_e_precos):
            print("Item ", index + 1)
            print(item[0], "m³")
            print("R$", item[1],"\n")

        print("Volume máximo comportado:", self.volume_maximo, "m³")
