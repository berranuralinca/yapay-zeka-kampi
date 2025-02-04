# ozel hata sinifi

class Negativenumbererror(ValueError):
    def __init__(self, message="Negatif sayi girildi!"):
        self.message = message
        super().__init__(self.message)