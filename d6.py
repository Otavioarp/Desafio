def gera_frequencia_nota(semitons):

    from decimal import  Decimal, getcontext
    notas , semi = [ [  'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#' ] , [ 'Bb', 'B','C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A' ] ]  , semitons
    if abs(semitons) >= 12:
            semi = semi % 12
    a2 = notas[0][semi] if semi >= 0 else notas[1][ semi + 11]
    a1 = 440 * 2 ** (semitons / 12)
    y = 4 if a1 % 1 != 0 else 0
    x = len(str(round(a1)))
    getcontext().prec=x+y
    a1 = getcontext().create_decimal_from_float(a1)
    return [str(a1),   a2 ]