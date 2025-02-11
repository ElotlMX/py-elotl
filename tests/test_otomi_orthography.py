import pytest
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


OTQ_OUTPUTS = [
    "ra ngaho ra tso̱ y'o̱te:",
    "k'a mäistória dáté porke dósufré",
    "bu̱ rané rabadi",
    "por ehemplo dáfu̱ ná ra sapahtá pe lo prinsipal dáfu̱ ná ra ágila",
    "ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra sahagún, mi b'e̱tsi ha ra ndäxjua k'oi ra thuhu ra tsóditse florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
    "ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
    "ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
    "gíraya náya'wi",
    "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hjua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. ge'bu̱ go min pu̱n doja 'na.",
    "făwi hi ndimá na madé",
    "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
    "gatho ya hyoyajä'i mi b'u̱i ha ra hnini bi handi.",
]


INALI_OUTPUTS = [
    "ra ngaho ra tso̱ y'o̱te:",
    "k'a mäistória dáté porke dósufré",
    "bu̱ rané rabadi",
    "por ehemplo dáfu̱ ná ra sapahtá pe lo prinsipal dáfu̱ ná ra ágila",
    "ra b'ist'ofo gi nu̱tihu̱ ya hmä ya r'atsa noya ya mu̱dimehai ra sahagún, mi b'e̱tsi ha ra ndäxjua k'oi ra thuhu ra tsóditse florentino, pede yoho ya b'ede mi mä ne huts'i xahño.",
    "ndunthi bi ntsu nuya ñämfo̱ bi ñuts'i ya ndoy'o ra ntsu, ngu mañä ra ñ'udi mi thanda n'a ra ts'othogi.",
    "ebu̱ ba penga ya ñämfo̱ ne ya ñ'emabagi ha ya mäts'a bi mu̱di ra ntuhni.",
    "gíraya náya'wi",
    "bi boxro xi 'be̱ts'ina, bido'u̱ ro 'yu̱ni 'na, xi bi bo̱x ro hjua 'na, bido'u̱ ro ts'ii 'na, xi bo̱xro ts'äre 'na. ge'bu̱ go min pu̱n doja 'na.",
    "făwi hi ndimá na madé",
    "nuhe da fats'ihe da umbabihe ya za ya ngi ya tu̱di pa da o̱t'a ya mätsa ya ñämfo̱",
    "gatho ya hyoyajä'i mi b'u̱i ha ra hnini bi handi.",
]


RFE_OUTPUTS = [
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


@pytest.mark.parametrize(
    "input_sent, ots_norm_sent",
    list(zip(INPUT_OTOMI_SENT, OTS_OUTPUTS)),
    ids=["[OTS]::" + sent.split()[0] for sent in OTS_OUTPUTS],
)
def test_ots_normalizer(input_sent: str, ots_norm_sent: str):
    # Arrange
    normalizer = Normalizer("ots")

    # Act
    result = normalizer.normalize(input_sent)

    # Assert
    assert result == ots_norm_sent


@pytest.mark.parametrize(
    "input_sent, otq_norm_sent",
    list(zip(INPUT_OTOMI_SENT, OTQ_OUTPUTS)),
    ids=["[OTQ]::" + sent.split()[0] for sent in OTQ_OUTPUTS],
)
def test_otq_normalizer(input_sent: str, otq_norm_sent: str):
    # Arrange
    normalizer = Normalizer("otq")

    # Act
    result = normalizer.normalize(input_sent)

    # Assert
    assert result == otq_norm_sent


@pytest.mark.parametrize(
    "input_sent, inali_norm_sent",
    list(zip(INPUT_OTOMI_SENT, INALI_OUTPUTS)),
    ids=["[INALI]::" + sent.split()[0] for sent in INALI_OUTPUTS],
)
def test_inali_normalizer(input_sent: str, inali_norm_sent: str):
    # Arrange
    normalizer = Normalizer("inali")

    # Act
    result = normalizer.normalize(input_sent)

    # Assert
    assert result == inali_norm_sent


@pytest.mark.parametrize(
    "input_sent, rfe_norm_sent",
    list(zip(INPUT_OTOMI_SENT, RFE_OUTPUTS)),
    ids=["[RFE]::" + sent.split()[0] for sent in RFE_OUTPUTS],
)
def test_rfe_normalizer(input_sent: str, rfe_norm_sent: str):
    # Arrange
    normalizer = Normalizer("rfe")

    # Act
    result = normalizer.normalize(input_sent)

    # Assert
    assert result == rfe_norm_sent
