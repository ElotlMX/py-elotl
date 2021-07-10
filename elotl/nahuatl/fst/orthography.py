import argparse
from pathlib import Path
from string import punctuation
import attapply

path_to_orig_fon = Path("att", "orig-fon.att")
ORIG_FON_FST = attapply.ATTFST(path_to_orig_fon)


class Normalizador(object):
    def __init__(self, input_ort=None, output_ort="sep", overrides=None):
        self.norm_fst = attapply.ATTFST(Path("att", f"fon-{output_ort}.att"))
        self.overrides = overrides if overrides is not None else {}

    def _convert(self, w, fst):
        w = w.lower()
        forms = list(fst.apply(w))
        if forms:
            return forms[-1][0]
        else:
            raise ValueError("Unable to convert word '{}'".format(w, fst))

    def _normalize_word(self, original_word):
        w = original_word.lower()
        fon = self._convert(w, ORIG_FON_FST)
        normed = self._convert(fon, self.norm_fst)
        return fon, normed

    def _tokenize(self, sent):
        return sent.split()

    def g2p(self, s, overrides=None):
        overrides = overrides if overrides is not None else {}
        return " ".join([self._convert(w, ORIG_FON_FST) if not w in overrides else overrides[w] 
                         for w in self._tokenize(s)])

    def normalize(self, s):
        norm = []
        for t in self._tokenize(s):
            if t in self.overrides:
                norm.append(t)
            _, t_norm = self._normalize_word(t)
            norm.append(t_norm)

        return " ".join(norm)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("texto")
    argparser.add_argument("--ortografia_preferida", "-ort", choices=["sep", "ack"], default="sep")

    args = argparser.parse_args()
    n = Normalizador(output_ort=args.ortografia_preferida)
    print(n.normalize(args.texto))
    
