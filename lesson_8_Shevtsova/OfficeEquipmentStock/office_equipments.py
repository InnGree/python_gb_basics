class OfficeEquipment:
    def __init__(self, model, price: float, speed: int, supported_formats: list):
        self.name = "Office Equipment"
        self.model = model
        self.price = price
        self.speed = speed
        self.supported_formats = supported_formats


class Printers(OfficeEquipment):
    def __init__(self, model, price: float, speed: int, supported_formats: list, cartridge_resource: int):
        super().__init__(model, price, speed, supported_formats)
        self.cartridge_resource = cartridge_resource
        self.name = "Printer"


class Scanners(OfficeEquipment):
    def __init__(self, model, price: float, speed: int, supported_formats: list, optical_density: int):
        super().__init__(model, price, speed, supported_formats)
        self.optical_density = optical_density
        self.name = "Scanner"


class Copiers(OfficeEquipment):
    def __init__(self, model, price: float, speed: int, supported_formats: list, copies_per_cycle: int):
        super().__init__(model, price, speed, supported_formats)
        self.copies_per_cycle = copies_per_cycle
        self.name = "Copier"
