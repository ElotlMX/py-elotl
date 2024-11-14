# Orthographic Normalization

Coming soon: orthographic normalization for other languages!

For now, see the following sections for the existing support of Nahuatl and Otomi orthographies.

### Normalizing nahuatl orthographies

Import the orthography module and Load the axolot nahuatl corpus.

```python
import elotl.corpus
import elotl.nahuatl.orthography
a = elotl.corpus.load("axolotl")
```

Creates a normalizer object, passing as parameter the normalization to be used.

The following normalizations are currently available:

- sep
  - Alphabet often seen in use by the Secretaría de Educación Pública (SEP) and the Instituto Nacional para la Educación de los Adultos (INEA). important characteristics of this alphabet are the use of "u" for the phoneme /w/, "k" for /k/, and "j" for /h/.
- inali
  - Alphabet in use by the Instituto Nacional de Lenguas Indígenas. Uses "w" for /w/, "k" for /k/, and "h" for /h/.
- ack
  - Alphabet initially used by Richard Andrews and subsequently by a number of other Nahuatl scholars. Named after Andrews, Campbell, and Karttunen. Uses "hu" for /w/, "c" and "qu" for /k/, and "h" for /h/.

If an unsupported normalization is specified, sep will be used by default.

You can use the `normalize` method to normalize a text to the selected orthography. And the `to_phones` method to get
the phonemes.

```python
>>> n = elotl.nahuatl.orthography.Normalizer("sep")
>>> n.normalize(a[1][1])
'au in ye yujki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokaua.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```

```python
>>> n = elotl.nahuatl.orthography.Normalizer("inali")
>>> n.normalize(a[1][1])
'aw in ye yuhki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokawa.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```

```python
>>> n = elotl.nahuatl.orthography.Normalizer("ack")
>>> n.normalize(a[1][1])
'auh in ye yuhqui in on tlenamacac niman ye ic teixpan on motlalia ce tlacatl itech mocahua.'
>>> n.to_phones(a[1][1])
'aw in ye yuʔki in on ƛenamakak niman ye ik teiʃpan on moƛalia se ƛakaƛ itet͡ʃ mokawa.'
```


### Normalizing otomi orthographies

Import the orthography module and Load the tsunkua otomi corpus.

```python
import elotl.corpus
import elotl.otomi.orthography
a = elotl.corpus.load("tsunkua")
```
Creates a normalizer object, passing as parameter the normalization to be used.

The following normalizations are currently available:

- **inali**
  - Norm proposed by INALI in 2014. Published in:
    - INALI (2014). *Njaua nt’ot’i ra Hñähñü*. Norma de escritura de la lengua Hñähñü. SEP-INALI.

- **rfe**
  - Standard used for the phonetic transcription of texts, utilized in the works of Yolanda Lastra, based on the phonetic alphabet proposed by the *Revista de Filología Española*:
    - Lastra, Y. (1992). *El otomí de Toluca*. IIA, UNAM
    - Lastra, Y. (1989). *Otomí de San Andrés Cuexcontitlán, Estado de México*. *Archivo de Lenguas Indígenas de México*, COLMEX.

- **ots**
  - Standard used in some written texts in variants from the State of Mexico.
    - De la Vega Lázaro, M. (2017). *Aprendiendo Otomí (Hñähñü)*. CDI

- **otq**
  - Standard proposed for the writing of Otomí, mainly in some variants from the Querétaro region.
    - Hekking, E., & de Jesús, A. (1989). *Diccionario español-otomí de Santiago Mexquititlán*. Universidad Autónoma de Querétaro.
    - Hekking, E., & de Jesús, A. (1984). *Gramática otomí*. Universidad Autónoma de Querétaro.

If an unsupported normalization is specified, inali will be used by default.

You can use the `normalize` method to normalize a text to the selected orthography. And the `to_phones` method to get
the phonemes.

```python
>>> n = elotl.otomi.orthography.Normalizer("ots")
>>> n.normalize(a[1][1])
"ebu̱ ba eje man'aki ba te̱nga ra t'o̱jo̱ ra tjuju ra tsitlaltépets. tlatsopan, nubia ba o̱t'ra b'u̱i ja ra ndo̱m'ijmu."
>>> n.to_phones(a[1][1])
"ebɨ ba ehe manʔaki ba tɛnga ra tʔɔhɔ ra thuhu ra t͡sitlaltépet͡s. tlat͡sopan, nubia ba ɔtʔɾa bʔɨi ha ra ndɔmʔihmu."
```

```python
>>> n = elotl.otomi.orthography.Normalizer("otq")
>>> n.normalize(a[1][1])
"ebu̱ ba ehe man'aki ba te̱nga ra t'o̱ho̱ ra thuhu ra tsitlaltépets. tlatsopan, nubia ba o̱t'ra b'u̱i ha ra ndo̱m'ihmu."
>>> n.to_phones(a[1][1])
'ebɨ ba ehe manʔaki ba tɛnga ra tʔɔhɔ ra thuhu ra t͡sitlaltépet͡s. tlat͡sopan, nubia ba ɔtʔɾa bʔɨi ha ra ndɔmʔihmu.'
```

```python
>>> n = elotl.otomi.orthography.Normalizer("inali")
>>> n.normalize(a[1][1])
"ebu̱ ba ehe man'aki ba te̱nga ra t'o̱ho̱ ra thuhu ra tsitlaltépets. tlatsopan, nubia ba o̱t'ra b'u̱i ha ra ndo̱m'ihmu."
>>> n.to_phones(a[1][1])
'ebɨ ba ehe manʔaki ba tɛnga ra tʔɔhɔ ra thuhu ra t͡sitlaltépet͡s. tlat͡sopan, nubia ba ɔtʔɾa bʔɨi ha ra ndɔmʔihmu.'
```

```python
>>> n = elotl.otomi.orthography.Normalizer("rfe")
>>> n.normalize(a[1][1])
'ebɨ ba ehe manʔaki ba tɛnga ra tʔɔhɔ ra thuhu ra citlaltépec. tlacopan, nubia ba ɔtʔra bʔɨi ha ra ndɔmʔihmu.'
>>> n.to_phones(a[1][1])
'ebɨ ba ehe manʔaki ba tɛnga ra tʔɔhɔ ra thuhu ra t͡sitlaltépet͡s. tlat͡sopan, nubia ba ɔtʔɾa bʔɨi ha ra ndɔmʔihmu.'
```
