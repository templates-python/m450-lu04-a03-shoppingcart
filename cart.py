"""Warenkorb für einen kleinen Onlineshop."""


class ShoppingCart:
    """Ein Warenkorb mit Artikeln, Preisen und Mengen."""

    def __init__(self):
        self.items = {}
        self.discount = 0

    def add_item(self, name, price, quantity=1):
        """
        Legt einen Artikel in den Warenkorb.
        Ist der Artikel schon vorhanden, wird nur die Menge erhöht.
        :param name: Bezeichnung des Artikels
        :param price: Preis pro Stück in CHF
        :param quantity: Anzahl Stück
        :raises ValueError: wenn der Preis negativ oder die Menge kleiner als 1 ist
        """
        if price < 0:
            raise ValueError('Der Preis darf nicht negativ sein')
        if quantity < 1:
            raise ValueError('Die Menge muss mindestens 1 sein')
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def total(self):
        """
        Berechnet das Total aller Artikel nach Abzug des Rabatts.
        :return: Total in CHF, auf Rappen gerundet
        """
        subtotal = 0
        for item in self.items.values():
            subtotal += item['price'] * item['quantity']
        return round(subtotal * (100 - self.discount) / 100, 2)

    def remove_item(self, name):
        """
        Entfernt einen Artikel vollständig aus dem Warenkorb.
        :param name: Bezeichnung des Artikels
        :raises KeyError: wenn der Artikel nicht im Warenkorb ist
        """
        # TODO Teil 3: Ersetzen Sie diesen Stub durch Code
        raise NotImplementedError('remove_item ist noch nicht umgesetzt')

    def apply_discount(self, percent):
        """
        Gewährt einen Rabatt in Prozent auf das Total.
        :param percent: Rabatt in Prozent, erlaubt sind 0 bis 50
        :raises ValueError: wenn der Rabatt kleiner als 0 oder grösser als 50 ist
        """
        # TODO Teil 3: Ersetzen Sie diesen Stub durch Code
        raise NotImplementedError('apply_discount ist noch nicht umgesetzt')
