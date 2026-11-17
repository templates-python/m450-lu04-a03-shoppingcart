"""Unit Tests für den Warenkorb."""
import pytest

from cart import ShoppingCart


# ---------------------------------------------------------------------------
# Teil 1: Die Methoden add_item und total sind fertig programmiert.
# ---------------------------------------------------------------------------

def test_add_item():
    # TODO: Legen Sie einen Artikel in einen neuen Warenkorb
    # TODO: Prüfen Sie Preis und Menge in cart.items
    assert False


def test_add_item_twice():
    # TODO: Legen Sie denselben Artikel zweimal in den Warenkorb (Menge 1 und 2)
    # TODO: Prüfen Sie, dass der Artikel nur einmal vorhanden ist, mit Menge 3
    assert False


def test_total():
    # TODO: Legen Sie zwei verschiedene Artikel mit Fliesskomma-Preisen in den Warenkorb
    # TODO: Prüfen Sie das Total mit pytest.approx
    assert False


def test_add_item_negative_price():
    # TODO: Prüfen Sie mit pytest.raises, dass ein negativer Preis einen ValueError auslöst
    assert False


# ---------------------------------------------------------------------------
# Teil 2: remove_item und apply_discount sind erst Stubs.
# Schreiben Sie die Tests trotzdem fertig, so als wäre der Code schon da.
# Markieren Sie jeden Test mit
#     @pytest.mark.xfail(raises=NotImplementedError, strict=True, reason='...')
# ---------------------------------------------------------------------------

def test_remove_item():
    # TODO: Legen Sie zwei Artikel in den Warenkorb und entfernen Sie einen davon
    # TODO: Prüfen Sie, dass nur noch der andere Artikel im Warenkorb ist
    assert False


def test_remove_unknown_item():
    # TODO: Prüfen Sie mit pytest.raises, dass das Entfernen eines unbekannten Artikels
    #       einen KeyError auslöst
    assert False


def test_apply_discount():
    # TODO: Legen Sie Artikel für CHF 80.00 in den Warenkorb und gewähren Sie 25 % Rabatt
    # TODO: Prüfen Sie, dass das Total CHF 60.00 beträgt
    assert False


@pytest.mark.parametrize('percent', [-1, 51])
def test_apply_discount_invalid(percent):
    # TODO: Prüfen Sie mit pytest.raises, dass ein Rabatt ausserhalb von 0 bis 50
    #       einen ValueError auslöst
    assert False


# ---------------------------------------------------------------------------
# Teil 3: Programmieren Sie remove_item und apply_discount in cart.py.
# Führen Sie die Tests aus und beobachten Sie die Ausgabe (XPASS).
# Entfernen Sie danach die xfail-Markierungen, bis alle Tests grün sind.
# ---------------------------------------------------------------------------
