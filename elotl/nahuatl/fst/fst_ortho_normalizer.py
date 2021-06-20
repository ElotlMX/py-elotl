import argparse
from pathlib import Path
from string import punctuation
import attapply

path_to_orig_fon = Path("att", "orig-fon.att")
orig_fon_fst = attapply.ATTFST(path_to_orig_fon)


class TextoNormalizado:
    def __init__(self, s, ortografia_normalizada="sep-u-j"):
        self.norm_fst = attapply.ATTFST(Path("att", f"fon-{ortografia_normalizada}.att"))
        self.original = s
        self.fonemica = self._convertir(self.original, orig_fon_fst)
        self.normalizada = self._convertir(self.fonemico, self.norm_fst)

    def _convertir(self, s, fst):
        tokens_convertidos = []
        for token in s.split():
            token = token.strip(punctuation).lower()
            formas = list(fst.apply(token))
            if not formas:
                tokens_convertidos.append(token)
            else:
                tokens_convertidos.append(formas[-1][0])
        return " ".join(tokens_convertidos)

    def __repr__(self):
        return "Original: {}\nFonemica: {}\nNormalizada:{}".format(self.original, self.fonemico, self.normalizado)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("texto")
    argparser.add_argument("--ortografia_preferida", "-ort", choices=["sep-u-j", "sep-w-h", "ack"], default="sep-u-j")

    args = argparser.parse_args()
    texto = TextoNormalizado(args.texto, args.ortografia_preferida)
    print(texto)
