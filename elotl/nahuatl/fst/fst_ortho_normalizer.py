import argparse
from typing import Callable
from pathlib import Path
from string import punctuation
import attapply


class Normalizador(object):
    def __init__(self, ortografia, tokenize: Callable = lambda s: s.split()):
        path_to_orig_fon = Path("att", "orig-fon.att")
        path_to_hfst = Path("att", f"fon-{ortografia}.att")
        self.tokenize = tokenize
        self.fon_fst = attapply.ATTFST(path_to_orig_fon)
        self.fst = attapply.ATTFST(path_to_hfst)

    def norm(self, s):
        secuencia_normalizada = [self.norm_palabra(p) for p in self.tokenize(s.lower())]
        return " ".join(secuencia_normalizada)

    def norm_palabra(self, palabra):
        palabra = palabra.strip(punctuation)
        formas_fonemicas = list(self.fon_fst.apply(palabra))
        if not formas_fonemicas:
            return palabra
        formas = list(self.fst.apply(formas_fonemicas[-1][0]))
        if not formas:
            return palabra
        else:
            return formas[-1][0]


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("texto")
    argparser.add_argument("--ortografia_preferida", "-ort", choices=["sep-u-j", "sep-w-h", "ack"], default="sep-u-j")

    args = argparser.parse_args()

    normalizador = Normalizador(args.ortografia_preferida)
    print(normalizador.norm(args.texto))
