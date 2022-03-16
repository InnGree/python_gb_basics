from office_equipments import Printers, Scanners, Copiers
from stock_class import Stock, ItemMissedException, NotEnoughVolumeException, LackOfItemException
from items_validation import EquipmentsTypesCheck

# создаем оргтехнику
printer1 = Printers("EPSON L805", 25000, 2000, ["A4", "A3"], 30000)
printer2 = Printers("HP M102A", 45000, 3000, ["A4", "A3"], 50000)
scanner1 = Scanners("Canon CanoScan LiDE 400", 15000, 1500, ["A4", "A3"], 300)
scanner2 = Scanners("Epson Perfection V850 Pro", 35000, 2500, ["A4", "A3"], 500)
copier1 = Copiers("HP COLOR LaserJet Pro M254dw", 40000, 3000, ["A4", "A3"], 400)
copier2 = Copiers("HP LaserJet MFP M436n", 30000, 2500, ["A4", "A3"], 200)

# создаем склад
company_stock = Stock(30)

# поместить созданную технику на склад в указанном количестве
try:
    company_stock.arrive(printer1, 5)
    company_stock.arrive(printer2, 5)
    company_stock.arrive(scanner1, 5)
    company_stock.arrive(scanner2, 7)
    company_stock.arrive(copier1, 5)
    company_stock.arrive(copier2, 5)
except NotEnoughVolumeException as exception:
    print(exception)

# отобразить остатки на складе
print("Added on Stock:")
for x in company_stock.storage:
    print(x)
print(f"\n")

# передать со склада в подразделения
try:
    company_stock.transfer("Printer", "EPSON L805", "Sales department", 3)
    company_stock.transfer("Scanner", "Canon CanoScan LiDE 400", "Support", 7)
except LackOfItemException as exception:
    print(exception)
except ItemMissedException as exception:
    print(exception)

# отобразить, что передано
print("Transferred from Stock:")
for x in company_stock.transfer_book:
    print(x)
print(f"\n")

# отобразить остатки на складе после передачи
print("Stock:")
for x in company_stock.storage:
    print(x)
print(f"\n")


# проверка названия модели
new_printer = Printers(EquipmentsTypesCheck.model_check("HP LaserJet Toooooooooo long naaaaaaaaaaaaaaaaame"),
                       25000, 2000, ["A4", "A3"], 30000)

