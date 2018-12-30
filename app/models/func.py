class Func:
    def update_from_dict(self, data):
        for key in data:
            if not hasattr(self, key):
                raise ValueError(f"{self.__tablename__} has no such attribute "
                                 f"'{key}'")

        for key, val in data.items():
            setattr(self, key, val)
