"""
El escritura del Náhuatl siempre ha contenido una gran diversidad ortográfica.
Para facilitar el uso de textos de fuentes distintos, que probablemente utilizan
diferentes sistemas ortográficas, este script hace disponible la normalización
ortográfica basada en el conocimiento de los diversos sistemas de escritura 
Náhuatl tanto en los tiempos coloniales como en la actualidad.

Por el momento se ofrecen dos ortografías comunes que se pueden ocupar como la
"ortografía normalizada":

    * SEP: Ortografía utilizada por la Secretería de Educación Pública de México
           a veces llamada de "ortografía moderna". Consiste en las siguentes
           equivalencias entre fonemas y grafemas: /k/='k', /w/='u', /s/='s' y
           el saltillo se escribe con 'j'.
    * ACK: Ortografía nombrado por tres académicos estadounidenses 
           (Richard Andrews, Joseph Campbell, y Frances Karttunen). Ésta tiene
           muchos de los rasgos de sistemas de escritura del llamado "Náhuatl
           Clásico", como el uso de 'qu/c' para el fonéma /k/ y 'hu/uh' para el
           fonéma /w/. El saltillo en esta ortografía se representa con 'h'.

En ambas ortografías, la duración vocálica se omite.

Para realizar la normalización, usamos un par de transductores de estado finito
(FST). Éstos están definidos en los archivos ".lexc" (elotl/nahuatl/fst/lexc/)
y compilado a un formato ".att" (elotl/nahuatl/fst/att/). Primero, convertimos
el texto de entrada a una ortografía fonética con el FST "orig-fon". Luego, 
esta forma se convierte en la ortografía normalizada con el FST "fon-sep" o 
"fon-ack".

Artículo sobre los diferentes sistemas ortográficos actuales del Nahuatl:
- https://www.academia.edu/42858002/La_escritura_n%C3%A1huatl_y_los_procesos_de_su_revitalizaci%C3%B3n

Información acerca de la ortografía SEP ("moderna"):
- https://nawatl.com/articulos/ortografia-moderna/

Ejemplos de unas publicaciones de la SEP utilizando la ortografía SEP:
- https://www.gob.mx/cms/uploads/attachment/file/3050/vocabulario_nahuatl_WEB.pdf
- https://www.gob.mx/cms/uploads/attachment/file/3040/LibroMaestroNahuatl1-14.pdf
- https://educacionbasica.sep.gob.mx/multimedia/RSC/BASICA/Documento/201611/201611-3-RSC-EN6CTWPkgG-libro_del_maestro_-_na_huatl-cicloii.pdf



###############################################################################
Para usarlo desde la línea de comandos:
    $ python elotl/nahuatl/orthography.py "<texto>" -ort [sep|ack]

O, desde otro programa de Python:

    >>> from elotl.nahuatl.orthography import Normalizer
    >>> normalizer = Normalizer("sep")  # o "ack"
    >>> normalizer.normalize("<texto>")
################################################################################
"""
import argparse
from pathlib import Path

from elotl.nahuatl.fst.attapply import ATTFST

path_to_att_dir = Path("elotl", "nahuatl", "fst", "att")
path_to_orig_fon = path_to_att_dir /  "orig-fon.att"
ORIG_FON_FST = ATTFST(path_to_orig_fon)


class Normalizer(object):
    def __init__(self, normalized_ort: str = "sep"):
        self.norm_fst = ATTFST(
            path_to_att_dir / f"fon-{normalized_ort}.att"
        )

    def _convert(self, w: str, fst: ATTFST) -> str:
        """
        Convert an input word form to an output form using the provided ATTFST
        object. In this implementation, we assume high weights are preferred,
        so we select the last of the generated candidates.

        Parameters
        ----------
        w: str
            Input word.
        
        fst: ATTFST
            FST object created with attapply. This object has an `apply` command
            used to apply the fst to an input.
        
        Returns
        -------
        str
            The generated string with the highest weight.

        """
        w = w.lower()
        forms = list(fst.apply(w))
        if forms:
            return forms[-1][0]

    def _g2p(self, w):
        """
        Converts an input word to a sequence of phonemes using an FST defined
        in elotl/nahuatl/fst/lexc/orig-fon.lexc.
        """
        return self._convert(w, ORIG_FON_FST)
        
    def _normalize_word(self, original_word: str) -> tuple[str, str]:
        """
        Convert an input word from 'any' orthography into a normalized 
        orthography (currently only either SEP or ACK). Since this process
        requires first converting the input to a pseudo-phonemic representation,
        we return both the phonemic and normalized forms.

        Parameters
        ----------
        original_word: str
            Input word form, in theory in any mixture of common Nahuatl 
            orthographies.
        
        Returns
        -------
        Tuple
            Phonemic, Normalized forms of the string.

        """
        w = original_word.lower()

        fon = self._g2p(w)
        if fon is None:
            # TODO: log this as a warning instead of printing to stdout.
            print("Unable to convert word '{}' to phonemes."
                  .format(w))
            return w, w
            
        normed = self._convert(fon, self.norm_fst)
        if normed is None:
            print("Unable to convert word '{}'.from phonemes to "
                             "normalized orthography.".format(fon))
            # TODO: log this as a warning instead of printing to stdout.
            return fon, w

        return fon, normed

    @staticmethod
    def _tokenize(s):
        return s.split()

    def to_phones(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Nahuatl text into approximate/pseudo IPA. 
        Conversion happens at the word-level after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Nahuatl
            orthographies (the system attempts to handle many of the graphic 
            variations observed in diverse Nahuatl texts).
        
        overrides: dict
            A dictionary of hard-coded normalizations. If an input word 
            (lowered) is contained in the dictionary, we will use the form it 
            maps to instead of applying the FST on it.
        
        Returns
        -------
        str
            Whitespace-joined words converted to approximate phonemic
            representation.

        """
        overrides = overrides if overrides is not None else {}
        fon = []
        for token in self._tokenize(text):
            if token in overrides:
                t_fon = overrides[token.lower()]
            t_fon = self._g2p(token)
            fon.append(t_fon)

        return " ".join(fon)

    def normalize(self, text: str, overrides: dict[str, str] = None) -> str:
        """
        Convert a non-normalized Nahuatl text into normalized orthography. 
        Depending on the value used when initializing this class, the normalized
        orthography is either SEP or ACK. Conversion happens at the word-level 
        after tokenizing on whitespace.

        Parameters
        ----------
        text: str
            Input text. It can be from any of a number of possible Nahuatl
            orthographies (the system attempts to handle many of the graphic 
            variations observed in diverse Nahuatl texts).
        
        overrides: dict
            A dictionary of hard-coded normalizations. If an input word 
            (lowered) is contained in the dictionary, we will use the form it 
            maps to instead of applying the FST on it.
        
        Returns
        -------
        str
            Whitespace-joined words converted to normalized orthography.

        """
        overrides = overrides if overrides is not None else {}

        norm = []
        for token in self._tokenize(text):
            if token in overrides:
                norm.append(overrides[token])
            _, t_norm = self._normalize_word(token)

            norm.append(t_norm)

        return " ".join(norm)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("texto")
    argparser.add_argument("--ortografia_preferida", "-ort", 
                           choices=["sep", "ack"], default="sep")

    args = argparser.parse_args()
    n = Normalizer(output_ort=args.ortografia_preferida)
    print(n.normalize(args.texto))
    
