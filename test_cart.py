"""Unit Tests für den Warenkorb."""
import pytest

from cart import ShoppingCart


@pytest.fixture(name='cart')
def fixture_cart():
    """Ein leerer Warenkorb."""
    return ShoppingCart()


# ---------------------------------------------------------------------------
# Teil 1: Die Methoden add_item und total sind fertig programmiert.
# ---------------------------------------------------------------------------

def test_add_item(cart):
    """Ein Artikel wird mit Preis und Menge abgelegt."""
    cart.add_item('Apfel', 0.80, 3)
    assert cart.items['Apfel'] == {'price': 0.80, 'quantity': 3}


def test_add_item_twice(cart):
    """Derselbe Artikel erhöht nur die Menge."""
    cart.add_item('Apfel', 0.80)
    cart.add_item('Apfel', 0.80, 2)
    assert len(cart.items) == 1
    assert cart.items['Apfel']['quantity'] == 3


def test_total(cart):
    """Das Total summiert Preis mal Menge."""
    cart.add_item('Apfel', 0.80, 3)
    cart.add_item('Brot', 4.35)
    assert cart.total() == pytest.approx(6.75)


def test_add_item_negative_price(cart):
    """Ein negativer Preis wird abgelehnt."""
    with pytest.raises(ValueError):
        cart.add_item('Apfel', -0.80)


# ---------------------------------------------------------------------------
# Teil 2: remove_item und apply_discount sind erst Stubs.
# ---------------------------------------------------------------------------

def test_remove_item(cart):
    """Ein Artikel wird vollständig entfernt."""
    cart.add_item('Apfel', 0.80, 3)
    cart.add_item('Brot', 4.35)
    cart.remove_item('Apfel')
    assert list(cart.items) == ['Brot']


def test_remove_unknown_item(cart):
    """Ein unbekannter Artikel löst einen KeyError aus."""
    with pytest.raises(KeyError):
        cart.remove_item('Banane')


def test_apply_discount(cart):
    """Der Rabatt wird vom Total abgezogen."""
    cart.add_item('Buch', 80.00)
    cart.apply_discount(25)
    assert cart.total() == pytest.approx(60.00)


@pytest.mark.parametrize('percent', [-1, 51])
def test_apply_discount_invalid(cart, percent):
    """Rabatte ausserhalb von 0 bis 50 werden abgelehnt."""
    with pytest.raises(ValueError):
        cart.apply_discount(percent)
