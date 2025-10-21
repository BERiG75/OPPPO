import json
from enum import StrEnum

from stationery_classes import Paper, PaperParams, Pen, Pencil, PencilParams, PenParams


class Commands(StrEnum):
	ADD = "ADD"
	PRINT = "PRINT"
	REM = "REM"


def read_commands_from_file(path: str):
	with open(path) as commands_file:
		line = commands_file.readline()
		while line:
			print(f"Команда на входе: {line}")
			parse_command_line(line)
			line = commands_file.readline()


def is_valid_command(command: str):
	return command in Commands


def is_all_params_in_enum(params: dict, enum) -> bool:
	for parameter in params.keys():
		if parameter not in enum:
			return False

	return True


def is_valid_parameters_for_stationery(
	params: dict, stationery_type: str, stationery_enum: StrEnum
):
	if params["type"] == stationery_type:
		params.pop("type")
		if is_all_params_in_enum(params, stationery_enum):
			print(f"Объект {stationery_type} успешно считан!")
			return True
		else:
			print(f"""Ошибка, неверные параметры для объекта {stationery_type}.
                  Допустимые параметры: {[param.value for param in stationery_enum]}""")
			return False


def add_command_handler(parameters):
	params_decoded: dict = json.loads(parameters)

	if is_valid_parameters_for_stationery(params_decoded, "pencil", PencilParams):
		new_obj = Pencil(**params_decoded)
		if new_obj:
			all_stationeries.append(new_obj)
			print("Объект pencil успешно добавлен в коллекцию!\n")

		return

	if is_valid_parameters_for_stationery(params_decoded, "pen", PenParams):
		all_stationeries.append(Pen(**params_decoded))

		print("Объект pen успешно добавлен в коллекцию!\n")

		return

	if is_valid_parameters_for_stationery(params_decoded, "paper", PaperParams):
		all_stationeries.append(Paper(**params_decoded))

		print("Объект paper успешно добавлен в коллекцию!\n")

		return


def print_command_handler():
	print(f"Содержимое коллекции: {'пусто' if len(all_stationeries) == 0 else ''}")
	for st in all_stationeries:
		print(st)


def rem_command_handler(parameters: str):
	splitted_params = parameters.split()

	if len(splitted_params) != 3:
		print("Неверные данные для условия")

	left_op, condition, right_op = splitted_params
	all_st = all_stationeries[:]
	for st in all_st:
		try:
			left_op, condition, right_op = splitted_params
			left_op = getattr(st, left_op)
			right_op = getattr(st, right_op)

			if not (isinstance(left_op, (int, float)) and isinstance(right_op, (int, float))):
				print(f"""ОШИБКА! Операнды должны быть целыми числами.
                      Сейчас сравниваются -> {left_op} и {right_op}""")
				return

			if eval(left_op + condition + right_op):
				all_stationeries.remove(st)
				print(f"УДАЛЕНО -> {st}")

		except AttributeError:
			if eval(str(left_op) + str(condition) + str(right_op)):
				all_stationeries.remove(st)
				print(f"УДАЛЕНО -> {st}")


def parse_command_line(command_line: str):
	splitted_line = command_line.split(" ", 1)
	command, parameters = "", ""

	if len(splitted_line) == 2:
		command = splitted_line[0].removesuffix("\n")
		parameters = splitted_line[1]
	elif len(splitted_line) == 1:
		command = splitted_line[0].removesuffix("\n")
	else:
		print("Неверная команда!")

	if not is_valid_command(command):
		print("Неверная команда!")

	if command == Commands.ADD:
		add_command_handler(parameters)
	if command == Commands.PRINT:
		print_command_handler()
	if command == Commands.REM:
		rem_command_handler(parameters)


all_stationeries = list()

if __name__ == "__main__":
	read_commands_from_file("commands.txt")
