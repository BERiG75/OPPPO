from enum import StrEnum
import logging


class PencilColors(StrEnum):
    RED = "красный"
    BLUE = "синий"
    ORANGE = "оранжевый"
    VIOLET = "фиолетовый"
    YELLOW = "желтый"
    GREEN = "зеленый"
    LIGHT_BLUE = "голубой"

class PenTypes(StrEnum):
    BALL = "шариковая"
    GEL = "гелевая"

class StationeryParams(StrEnum):
    TYPE = "type"

class PencilParams(StrEnum):
    TYPE = "type"
    LEAD_DENCITY = "lead_density"
    COLOR = "color"
    PHONE_NUMBER = "phone_number"
    PRICE = "price"

class PenParams(StrEnum):
    ROD_DIAMETER = "rod_diameter"
    PEN_TYPE = "pen_type"
    PHONE_NUMBER = "phone_number"
    PRICE = "price"

class PaperParams(StrEnum):
    HEIGHT = "height"
    WIDTH = "width"
    WEIGHT = "weight"
    PHONE_NUMBER = "phone_number"
    PRICE = "price"

class Stationery:
    def __init__(self, price: float, phone_number: str):
        self.price = price
        self.phone_number = phone_number
        
    @staticmethod
    def _is_valid_str_param_of_child_enum(param: str, child_enum: StrEnum) -> bool:
        return isinstance(param, str) and param in child_enum
    
    @staticmethod
    def _is_positive_int_param_of_child(param: int):
        return isinstance(param, int) and param > 0
    
    @staticmethod
    def _is_positive_float_param_of_child(param: float):
        return isinstance(param, float) and param > 0.0
    
    @staticmethod
    def _is_valid_phone_number(phone_number: str):
        return isinstance(phone_number, str) and phone_number.startswith("+7") and len(phone_number) == 12



class Pencil(Stationery):
    def __new__(cls, *args, **kwargs):
        if args:
            kwargs["lead_density"] = args[0]
            kwargs["color"] = args[1]

        if not (cls._is_valid_initial_parameters(kwargs)):
            logging.error(f"Неверные данные для инициализации! Объект с данными {kwargs} не был создан из-за ошибки!")
            return None

        return super().__new__(cls)
    
    def __init__(self, color : str, lead_density: int, price: float, phone_number: str):
        self.lead_density = lead_density
        self.color = color
        super().__init__(price, phone_number)
    

    @classmethod
    def _is_valid_initial_parameters(cls, parameters: dict) -> bool:
        if not (super()._is_valid_str_param_of_child_enum(parameters.get("color"), PencilColors)):
            logging.error(f"Параметр цвета (color) задан неверно. Допустимые значения: {list(PencilColors)}. Переданное значение: {parameters.get("color")}")
            return False
        
        if not (super()._is_positive_int_param_of_child(parameters.get("lead_density"))):
            logging.error("Параметр плотности грифеля (lead_density) задан неверно. Плотность грифеля (lead_density) должна быть целым положительным числом")
            return False
        
        if not (super()._is_positive_float_param_of_child(parameters.get("price"))):
            logging.error("Параметр цены (price) задан неверно. Цена должна быть вещественным положительным числом")
            return False
        
        if not super()._is_valid_phone_number(parameters.get("phone_number")):
            logging.error("Номер телефона (phone_number) указан неверно. Он должен начинаться с +7 и составлять 12 символов (включая знак +)")
            return False
        
        return True

    def __str__(self):
        return f"Объект pencil. Параметры --> lead_density: {self.lead_density}, color: {self.color}, price: {self.price}, phone_number: {self.phone_number}\n"

class Pen(Stationery):
    available_pen_types = ("шариковая", "гелевая")

    def __new__(cls, *args, **kwargs):
        if not (cls._is_valid_initial_parameters(kwargs)):
            logging.error(f"Неверные данные для инициализации! Объект с данными {kwargs} не был создан из-за ошибки!")
            return None

        return super().__new__(cls)
    
    def __init__(self, pen_type : str, rod_diameter: float, price: float, phone_number: str):
        self.rod_diameter = rod_diameter
        self.pen_type = pen_type
        super().__init__(price, phone_number)

    
    @classmethod
    def _is_valid_initial_parameters(cls, parameters: dict) -> bool:
        if not (super()._is_valid_str_param_of_child_enum(parameters.get("pen_type"), cls.available_pen_types)):
            logging.error(f"Параметр типа ручки (pen_type) задан неверно. Допустимые значения: {cls.available_pen_types}. Переданное значение: {parameters.get("pen_type")}")
            return False
        
        if not (super()._is_positive_float_param_of_child(parameters.get("rod_diameter"))):
            logging.error("Параметр диаметра (rod_diameter) стержня задан неверно. Диаметр должен быть вещественным положительным числом")
            return False
        
        if not (super()._is_positive_float_param_of_child(parameters.get("price"))):
            logging.error("Параметр цены (price) задан неверно. Цена должна быть вещественным положительным числом")
            return False
        
        if not super()._is_valid_phone_number(parameters.get("phone_number")):
            logging.error("Номер телефона (phone_number) указан неверно. Он должен начинаться с +7 и составлять 12 символов (включая знак +)")
            return False
        
        return True
    
    def __str__(self):
        return f"Объект Pen. Параметры --> rod_diameter: {self.rod_diameter}, pen_type: {self.pen_type}, price: {self.price}, phone_number: {self.phone_number}\n"

class Paper(Stationery):
    def __new__(cls, *args, **kwargs):
        if not (cls._is_valid_initial_parameters(kwargs)):
            logging.error(f"Неверные данные для инициализации! Объект с данными {kwargs} не был создан из-за ошибки!")
            return None

        return super().__new__(cls)
    
    def __init__(self, weight: int, height: int, width: int, price: float, phone_number: str):
        self.weight = weight
        self.height = height
        self.width = width
        super().__init__(price, phone_number)

    @classmethod
    def _is_valid_initial_parameters(cls, parameters: dict) -> bool:
        if not (super()._is_positive_int_param_of_child(parameters.get("weight"))):
            logging.error("Параметр плотности бумаги (weight) указан неверно. Плотность должна быть целым положительным числом")
            return False
        
        if not (super()._is_positive_int_param_of_child(parameters.get("height"))):
            logging.error("Параметр высоты бумаги (height) указан неверно. Высота должна быть целым положительным числом")
            return False

        if not (super()._is_positive_int_param_of_child(parameters.get("width"))):
            logging.error("Параметр ширины бумаги (width) указан неверно. Ширина должна быть целым положительным числом")
            return False
        
        if not (super()._is_positive_float_param_of_child(parameters.get("price"))):
            logging.error("Параметр цены (price) задан неверно. Цена должна быть вещественным положительным числом")
            return False
        
        if not super()._is_valid_phone_number(parameters.get("phone_number")):
            logging.error("Номер телефона (phone_number) указан неверно. Он должен начинаться с +7 и составлять 12 символов (включая знак +)")
            return False

        return True

    def __str__(self):
        return f"Объект Paper. Параметры --> weight: {self.weight}, height: {self.height}, width: {self.width}, price: {self.price}, phone_number: {self.phone_number}\n"
