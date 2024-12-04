def iniciales(cadena: str) -> str:
    """Recibe una cadena devuelve la cadena con la frase en mayusculas

    Args:
        cadena (str): Recibe una cadena

    Returns:
        str: Las mayusculas iniciales
        >>> iniciales ("Hola que tal")
        'HQT'
        >>> iniciales ()
         ''
        >>> iniciales ("Hola)
        'H'
    """
    lista = cadena.split()
    resultado=""
    for palabra in lista:
        resultado += palabra[0]
    return resultado