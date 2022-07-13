# Orthographic Normalization

Coming soon: orthographic normalization for other languages!

For now, see the following sections for the existing support of Nahuatl orthographies.

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
