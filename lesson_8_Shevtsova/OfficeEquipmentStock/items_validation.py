class EquipmentsTypesCheck:
    @staticmethod
    def type_check(type_name: str):
        if len(type_name) > 30:
            return f"Incorrect entity_type"

    @staticmethod
    def model_check(type_name: str):
        if len(type_name) > 40:
            print(f"Too long model name")



