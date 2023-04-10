from src.media_aritmetica import MediaAritmetica


def test_calcula():
    numeros = [2, 2, 2]

    resultado = MediaAritmetica.calcula(numeros)

    assert resultado == 2.0
