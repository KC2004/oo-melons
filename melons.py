"""This file should have our order classes in it."""
class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5
        christmas_melon == base_price * 1.5
                
        if self.species == "Christmas_melon":
            total = (1 + self.tax) * self.qty * christmas_melon 
        else:
            total = (1 + self.tax) * self.qty * base_price 
        return total



    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        flat_fee = 3
        self.country_code = country_code 
    
    def get_total(self):
            
            total = super(InternationalMelonOrder, self).get_total()

            if self.qty < 10:
                total += flat_fee
            return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """GovernmentMelonOrder without tax"""
        
    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0.00)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
