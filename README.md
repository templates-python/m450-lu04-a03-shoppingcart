# M450 LU04.A03 - Erwartete Fehler

Schreiben Sie Tests für Code, der noch nicht fertig ist. Markieren Sie diese
Tests mit `xfail`, programmieren Sie danach die fehlenden Methoden und
beobachten Sie, wie PyTest reagiert.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu04/aufgaben/xfail>

## Ausgangslage

`cart.py` enthält die Klasse `ShoppingCart`, einen Warenkorb für einen kleinen
Onlineshop.

| Methode | Stand |
| --- | --- |
| `add_item(name, price, quantity=1)` | fertig |
| `total()` | fertig |
| `remove_item(name)` | Stub: löst `NotImplementedError` aus |
| `apply_discount(percent)` | Stub: löst `NotImplementedError` aus |

Die Docstrings in `cart.py` beschreiben, wie sich jede Methode verhalten soll.

## Auftrag

### Teil 1: Fertigen Code testen

Ergänzen Sie in `test_cart.py` die Tests für `add_item` und `total`
gemäss den Kommentaren `# TODO ...`.

### Teil 2: Tests für unfertigen Code

Schreiben Sie die Tests für `remove_item` und `apply_discount` vollständig,
so als wären die Methoden schon programmiert. Markieren Sie jeden dieser Tests mit

```python
@pytest.mark.xfail(raises=NotImplementedError, strict=True, reason='...')
```

Führen Sie `pytest -v -rxX` aus. Die Tests aus Teil 1 sind grün, die Tests aus
Teil 2 erscheinen als `XFAIL`.

### Teil 3: Stubs durch Code ersetzen

Programmieren Sie `remove_item` und `apply_discount` in `cart.py`. Führen Sie
die Tests nach jeder Methode erneut aus und beobachten Sie die Ausgabe.

- Was meldet PyTest, sobald eine Methode funktioniert?
- Warum wird der Test wegen `strict=True` rot?

Entfernen Sie danach die `xfail`-Markierungen, bis alle Tests grün sind.

## Tipp

Wenn Sie eine Fixture `cart` definieren und den Parameter ebenfalls `cart`
nennen, meldet pylint `redefined-outer-name`. Geben Sie der Fixture deshalb
einen Namen:

```python
@pytest.fixture(name='cart')
def fixture_cart():
    return ShoppingCart()
```

## Lokal testen

```bash
pip install -r requirements.txt
pytest -v -rxX
python _run_pylint.py
```

## Bewertung

Bewertet wird der Stand nach Teil 3: Alle Methoden sind programmiert und alle
Tests laufen ohne `xfail`-Markierung.

| Teil | Punkte |
| --- | --- |
| Tests Teil 1 (`test_add_item`, `test_add_item_twice`, `test_total`, `test_add_item_negative_price`) | 4 |
| Tests Teil 2 (`test_remove_item`, `test_remove_unknown_item`, `test_apply_discount`, `test_apply_discount_invalid`) | 4 |
| Linting von `test_cart.py` und `cart.py` | 3 |
| **Total** | **11** |

## Abgabe

Die Abgabe erfolgt durch den Push ins GitHub-Repository. Jeder Push wird
automatisch bewertet.
