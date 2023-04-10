class MediaAritmetica:

    @staticmethod
    def calcula(numeros: list[float]) -> float:

        tamanho = len(numeros)

        total = 0.0
        for numero in numeros:
            total += numero

        media = total / tamanho

        return media
