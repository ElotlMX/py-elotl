import pytest
import unittest
from elotl.otomi.orthography import Normalizer

INPUT_OTOMI_SENT = [
    "Ra ngaho ra tso̱ y'o̱te:",
    "k'a mäistória dáté porke dósuphré",
    "bu̱ rané rabadi",
    "por ehemplo dáphu̱ ná ra sapahtá pe lo prinsipal dáphu̱ ná ra ágila",
    "Ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra Sahagún, mi b'e̱tsi ha ra ndäxjua k'oi ra thuhu ra Códice Florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
    "Ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, Ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
    "Ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
    "gíRaya náya'wi",
    "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hjua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. Ge'bu̱ go min pu̱n doja 'na. ",
    "phăwi hi ndimá na madé",
    "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
    "Gatho ya hyoyajä'i mi b'u̱i ha ra hnini bi handi.",
]

OTS_OUTPUTS = [
    "ra ngajo ra tso̱ y'o̱te:",
    "k'a mäistória dáté porke dósufré",
    "bu̱ rané rabadi",
    "por ejemplo dáfu̱ ná ra sapajtá pe lo prinsipal dáfu̱ ná ra ágila",
    "ra b'ist'ofo gi nu̱tiju̱ ya jmä ya r'atsa noya ya mu̱dimejai ra sajagún, mi b'e̱tsi ja ra ndäxkjua k'oi ra tjuju ra tsóditse florentino, pede yojo ya b'ede mi mä ne juts'i xajño.",
    "nduntji bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, ngu mañä ra ñ'udi mi tjanda n'a ra ts'otjogi.",
    "ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ja ya mäts'a bi mu̱di ra ntujni.",
    "gíraya náya'wi",
    "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro jkjua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. ge'bu̱ go min pu̱n dokja 'na.",
    "făwi ji ndimá na madé",
    "nuje da fats'ije da umbabije ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
    "gatjo ya jyoyakjä'i mi b'u̱i ja ra jnini bi jandi.",
]


@pytest.mark.parametrize(
    "input_sent, ots_norm_sent",
    list(zip(INPUT_OTOMI_SENT, OTS_OUTPUTS)),
)
def test_ots_normalizer(input_sent: str, ots_norm_sent: str):
    assert Normalizer("ots").normalize(input_sent) == ots_norm_sent


class TestOrthographicNormalization(unittest.TestCase):
    test_inputs = [
        "Ra ngaho ra tso̱ y'o̱te:",
        "k'a mäistória dáté porke dósuphré",
        "bu̱ rané rabadi",
        "por ehemplo dáphu̱ ná ra sapahtá pe lo prinsipal dáphu̱ ná ra ágila",
        "Ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra Sahagún, mi b'e̱tsi ha ra ndäxjua k'oi ra thuhu ra Códice Florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
        "Ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, Ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
        "Ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
        "gíRaya náya'wi",
        "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hjua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. Ge'bu̱ go min pu̱n doja 'na. ",
        "phăwi hi ndimá na madé",
        "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
        "Gatho ya hyoyajä'i mi b'u̱i ha ra hnini bi handi.",
    ]

    otq_outputs = [
        "ra ngaho ra tso̱ y'o̱te:",
        "k'a mäistória dáté porke dósufré",
        "bu̱ rané rabadi",
        "por ehemplo dáfu̱ ná ra sapahtá pe lo prinsipal dáfu̱ ná ra ágila",
        "ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra sahagún, mi b'e̱tsi ha ra ndäxkhua k'oi ra thuhu ra tsóditse florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
        "ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
        "ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
        "gíraya náya'wi",
        "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hkhua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. ge'bu̱ go min pu̱n dokha 'na.",
        "făwi hi ndimá na madé",
        "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
        "gatho ya hyoyakhä'i mi b'u̱i ha ra hnini bi handi.",
    ]

    inali_outputs = [
        "ra ngaho ra tso̱ y'o̱te:",
        "k'a mäistória dáté porke dósufré",
        "bu̱ rané rabadi",
        "por ehemplo dáfu̱ ná ra sapahtá pe lo prinsipal dáfu̱ ná ra ágila",
        "ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra sahagún, mi b'e̱tsi ha ra ndäxkhua k'oi ra thuhu ra tsóditse florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
        "ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
        "ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
        "gíraya náya'wi",
        "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hkhua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. ge'bu̱ go min pu̱n dokha 'na.",
        "făwi hi ndimá na madé",
        "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
        "gatho ya hyoyakhä'i mi b'u̱i ha ra hnini bi handi.",
    ]

    rfe_outputs = [
        "ra ngaho ra cɔ yʔɔte:",
        "kʔa mᶏistória dáté porke dósuphré",
        "bɨ rané rabadi",
        "por ehemplo dáphɨ ná ra sapahtá pe lo prinsipal dáphɨ ná ra ágila",
        "ra bʔistʔopho gi nɨtihɨ ya hmᶏ ya rʔaca noya ya mɨdimehai ra sahagún, mi bʔɛci ha ra ndᶏškhua kʔoi ra thuhu ra códice phlorentino, pede yoho ya bʔede mi mᶏ ne hucʔi šahño.",
        "ndunthi bi ncu nuya ñᶏmphɔ bi ñucʔi ya ndoyʔo ra ncu, ngu mañᶏ ra ñʔudi mi thanda nʔa ra cʔothogi.",
        "ebɨ ba penga ya ñᶏmphɔ ne ya ñʔemabagi ha ya mᶏcʔa bi mɨdi ra ntuhni.",
        "gíraya náyaʔwi",
        "bi bošro ši ʔbɛcʔina, bidoʔɨ ro ʔyɨni ʔna, ši bi bɔš ro hkhua ʔna, bidoʔɨ ro cʔii ʔna, ši bɔšro cʔᶏre ʔna. geʔbɨ go min pɨn dokha ʔna.",
        "phăwi hi ndimá na madé",
        "nuhe da phacʔihe da umbabihe ya za ya ngi ya tɨdi pa da ɔtʔa ya mᶏca ya ñᶏmphɔ",
        "gatho ya hyoyakhᶏʔi mi bʔɨi ha ra hnini bi handi.",
    ]

    otq_normalizer = Normalizer("otq")
    inali_normalizer = Normalizer("inali")
    rfe_normalizer = Normalizer("rfe")

    def test_normalize_otq(self):
        for i, inp in enumerate(self.test_inputs):
            normed = self.otq_normalizer.normalize(inp)
            self.assertEqual(normed, self.otq_outputs[i])

    def test_normalize_inali(self):
        for i, inp in enumerate(self.test_inputs):
            normed = self.inali_normalizer.normalize(inp)
            self.assertEqual(normed, self.inali_outputs[i])

    def test_normalize_rfe(self):
        for i, inp in enumerate(self.test_inputs):
            normed = self.rfe_normalizer.normalize(inp)
            self.assertEqual(normed, self.rfe_outputs[i])


if __name__ == "__main__":
    unittest.main()
