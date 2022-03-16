from office_equipments import OfficeEquipment


class NotEnoughVolumeException(Exception):
    def __init__(self, item, requested_volume, free_volume):
        self.item = item
        self.requested_volume = requested_volume
        self.free_volume = free_volume

    def __str__(self):
        return f"Not enough volume for {self.item}: requested is {self.requested_volume}, free is {self.free_volume}"


class ItemMissedException(Exception):
    def __init__(self, request_type, item):
        self.request_type = request_type
        self.item = item

    def __str__(self):
        return f"{self.request_type} {self.item} doesn't exist"


class LackOfItemException(Exception):
    def __init__(self, item, requested_count, free_count):
        self.item = item
        self.requested_count = requested_count
        self.free_count = free_count

    def __str__(self):
        return f"Lack of {self.item}: requested {self.requested_count}, free is {self.free_count}"


class Stock:
    def __init__(self, volume: int):
        self.volume = volume
        self.storage = []
        self.transfer_book = []
        self.id = 1

    def arrive(self, entity: OfficeEquipment, count: int):
        if self.volume < count:
            raise NotEnoughVolumeException(entity.name + "" + entity.model, count, self.volume)

        item = {"Entity_type": entity.name, "Model": entity.model, "Count": count, "ID": self.id}
        self.storage.append(item)
        self.volume -= count
        self.id += 1

    def transfer(self, request_type, request_model, department, count: int):
        search_failed = True
        for item in self.storage:
            if item["Entity_type"] == request_type and item["Model"] == request_model:
                transferred_item = {"Entity_type": item["Entity_type"],
                                    "Model": item["Model"],
                                    "Count": count,
                                    "ID": item["ID"],
                                    "Department": department
                                    }
                search_failed = False

                if item["Count"] < count:
                    raise LackOfItemException(request_model, count, item["Count"])

                item["Count"] -= count
                self.transfer_book.append(transferred_item)
                break
        if search_failed:
            raise ItemMissedException(request_type, request_model)