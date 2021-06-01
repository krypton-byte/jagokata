# Install Library

```bash
$ pip install jagokata
# Github
$ pip install git+https://github.com/krypton-byte/jagokata
```
# Mencari Peribahasa

```python
from jagokata import cari_peribahasa
peribahasa = cari_peribahasa("biasa")
for i in peribahasa:
    print(f"peribahasa: {i.text}\nArti: {i.arti}")
```

# Mencari Kata Bijak

```python
from jagokata import cari_katabijak
katabijak = cari_katabijak("biasa")
for i in katabijak:
    print(i.text)
```