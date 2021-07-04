import argparse
from pathlib import Path
from string import punctuation
import attapply

path_to_orig_fon = Path("att", "orig-fon.att")
ORIG_FON_FST = attapply.ATTFST(path_to_orig_fon)


class Normalizador(object):
    def __init__(self, input_ort=None, output_ort="sep-u-j"):
        self.norm_fst = attapply.ATTFST(Path("att", f"fon-{output_ort}.att"))

    def _convert_word(self, original_word):
        w = original_word.lower()
        fon = list(ORIG_FON_FST.apply(w))
        if not fon:
            raise ValueError("Unable to convert word '{}' to phonemes".format(w))
        else:
            fon = fon[-1][0]
            out_token = list(self.norm_fst.apply(fon))
            if not out_token:
                raise ValueError("Unable to convert phoneme sequence '{}' to normalized orthgraphy.".format(fon))
            else:
                return fon, out_token[-1][0]

    def normalize(self, s):
        orig, fon, norm = [], [], []
        for t in s.split():
            t_fon, t_norm = self._convert_word(t)
            orig.append(t)
            fon.append(t_fon)
            norm.append(t_norm)

        return " ".join(orig), " ".join(fon), " ".join(norm)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("texto")
    argparser.add_argument("--ortografia_preferida", "-ort", choices=["sep-u-j", "sep-w-h", "ack"], default="sep-u-j")

    args = argparser.parse_args()
    n = Normalizador(output_ort=args.ortografia_preferida)
    print(n.normalize(args.texto))
    
