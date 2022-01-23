import unittest
from elotl.nahuatl.orthography import Normalizer


class TestOrthographicNormalization(unittest.TestCase):
    test_inputs = [
        'teocuitlatl plata yn icruzyo; yc niman conmotoquilitia ce '
        'Crucifixo cenca tlaçotli mahuiztic, cenca miec indulgencias '
        'ytetzinco mocnopilhuia.',
        'Ypan yn tlahtohuani Michhuacan yn itoca Camacoyahuac, yquac '
        'pehualloque.',
        'Amo uejkapania.',
        'tazohmahuiz tepixcatzin Jesucristo,',
        'Mah amo timiquican de mayan,',
        'mochinin axcan mochipa ye huel tiquihtozqueh ahmo zan momachtihqueh '
        'tlacemmelahuazqueh itechpa in tomomoztlanemiliz no iuhqui inin huel '
        'ticchihuazquiani ahquihuan techtlamachtiah ahnozo techteopoah '
        'tonemiliz',
        'Ome axoxtlantli',
        "xikita ninke ixnesyohme wan ixpowa yen tlanonotsal",
        "Wilis tikekuilos tlen nika timitstlatlanilia itich nin amatl",
    ]

    sep_outputs = [
        'teokuitlatl plata in ikrusyo; ik niman konmotokilitia se krusifixo '
        'senka tlasotli mauistik, senka miek indulgensias itetsinko '
        'moknopiluia.',
        'ipan in tlajtouani michuakan in itoka kamakoyauak, ikuak peualoke.',
        'amo uejkapania.',
        'tasojmauis tepixkatsin jesukristo,',
        'maj amo timikikan de mayan,',
        'mochinin axkan mochipa ye uel tikijtoskej ajmo san momachtijkej '
        'tlasemmelauaskej itechpa in tomomostlanemilis no iuki inin uel '
        'tikchiuaskiani ajkiuan techtlamachtiaj ajnoso techteopoaj tonemilis',
        'ome axoxtlantli',
        'xikita ninke ixnesyojme uan ixpoua yen tlanonotsal',
        'uilis tikekuilos tlen nika timitstlatlanilia itich nin amatl'
    ]

    ack_outputs = [
        'teocuitlatl plata in icruzyo; ic niman conmotoquilitia ce crucifixo '
        'cenca tlazotli mahuiztic, cenca miec indulgenciaz itetzinco '
        'mocnopilhuia.',
        'ipan in tlahtohuani michhuacan in itoca camacoyahuac, icuac '
        'pehualloque.',
        'amo huehcapania.',
        'tazohmahuiz tepixcatzin hezucrizto,',
        'mah amo timiquican de mayan,',
        'mochinin axcan mochipa ye huel tiquihtozqueh ahmo zan momachtihqueh '
        'tlacemmelahuazqueh itechpa in tomomoztlanemiliz no iuhqui inin huel '
        'ticchihuazquiani ahquihuan techtlamachtiah ahnozo techteopoah '
        'tonemiliz',
        'ome axoxtlantli',
        'xiquita ninque ixnezyohme huan ixpohua yen tlanonotzal',
        'huiliz tiquecuiloz tlen nica timitztlatlanilia itich nin amatl'
    ]

    sep_normalizer_u_j = Normalizer("sep")
    sep_normalizer_w_h = Normalizer("inali")
    ack_normalizer = Normalizer("ack")

    def test_normalize_sep_u_j(self):
        for i, inp in enumerate(self.test_inputs):
            normed = self.sep_normalizer_u_j.normalize(inp)
            self.assertEqual(normed, self.sep_outputs[i])

    def test_normalize_ack(self):
        for i, inp in enumerate(self.test_inputs):
            normed = self.ack_normalizer.normalize(inp)
            self.assertEqual(normed, self.ack_outputs[i])

    def test_overrides(self):
        inp = "ce Crucifixo"
        outp = "se crucifixo"
        normed_w_override = (
            self.sep_normalizer_u_j.normalize(
                inp,
                overrides={'Crucifixo': 'crucifixo'}
            )
        )
        self.assertEqual(normed_w_override, outp)


if __name__ == '__main__':
    unittest.main()
