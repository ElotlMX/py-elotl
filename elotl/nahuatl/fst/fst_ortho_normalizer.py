from typing import List, Callable
from pathlib import Path
from string import punctuation
import attapply


#class TextoNahuatl(object):
#    def __init__(self, texto, ortografia="sep_u_j"):


class Normalizador(object):
    def __init__(self, ortografia, tokenize: Callable = lambda s: s.split()):
        path_to_hfst = Path("att", f"{ortografia}.att")
        self.tokenize = tokenize
        self.fst = attapply.ATTFST(path_to_hfst)

    def norm(self, s):
        secuencia_normalizada = [self.norm_palabra(p) for p in self.tokenize(s)]
        return " ".join(secuencia_normalizada)

    def norm_palabra(self, palabra):
        palabra = palabra.strip(punctuation)
        formas = self.fst.apply(palabra)
        if not formas:
            return palabra
        else:
            return formas[0]
