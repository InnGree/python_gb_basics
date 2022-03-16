class Operations:
    """
    This is description for Operations class
    """
    class_name: str
    class_attr: int

    @staticmethod
    def lowerstring(content):
        return content.lower()

    @staticmethod
    def upperstring(content):
        return content.upper()

    @classmethod
    def normalize(cls, content):
        a = cls.lowerstring(content)
        return cls.upperstring(a)


temp_string = "Hello!"
print(Operations.lowerstring(temp_string))
print(Operations.normalize(temp_string))

print(Operations.__dict__)
print(Operations.__annotations__)
print(Operations.__doc__)