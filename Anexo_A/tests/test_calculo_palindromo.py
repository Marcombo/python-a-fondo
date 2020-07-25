from palindromo import es_palindromo


def test_ana():
    assert es_palindromo('ana') is True


def test_diferente_tamano():
    assert es_palindromo('Maria') is False


def test_varias_palabras():
    assert es_palindromo('amor roma') is True


def test_numero_par_caracteres():
    assert es_palindromo('anna') is True
