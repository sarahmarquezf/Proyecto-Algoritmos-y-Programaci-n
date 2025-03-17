import math
import re

def results_management(experiments, recipes, reagents): # menú de gestión de resultados
    option = input("\nGestión de resultados:\n\n1. Validar resultados. \n2. Salir.\n\n>> ")
    while not option.isnumeric() or int(option) not in range(1,3):
        option = input("\nGestión de resultados:\n\n1. Validar resultados. \n2. Salir.\n\n>> ")

    if option == "1": # validar resultados
        return find_experiment(experiments, recipes)
    else:
        return "\nNo hubo gestión de resultados."

def find_experiment(experiments, recipes): # búsqueda de experimento para validar resultados
    search_id = input("\nIngresa el ID del experimento que deseas validar: ")
    while not search_id.isnumeric():
        search_id = input("\nIngrese un ID válido para el reactivo a validar: ")

    for experiment in experiments:
        if int(search_id) == experiment.id:
            print(experiment.show())
            option = input("\n¿Es este el experimento que deseas validar?\n\n1. Si.\n2. No.\n3. Salir.\n\n>> ")
            while not option.isnumeric() or int(option) not in range(1,4):
                option = input("\n¿Es este el experimento que deseas validar?\n\n1. Si.\n2. No.\n3. Salir.\n\n>> ")
            if option == "1":
                return validate_results(experiment, recipes)
            elif option == "2":
                find_experiment(experiments, recipes)
            elif option == "3":
                return "\nNo hubo validación."

    return "\nNo se encontró resultado."

def validate_results(experiment, recipes): # valida el resultado
    for recipe in recipes:
        if recipe.id == experiment.recipe:
            result = recipe.valores_a_medir
            if result == None:
                return "\nHubo algún error en la fórmula."
            elif result >= recipe.values[0].minimum and result <= recipe.values[0].maximum:
                return f"\nEl resultado es {round(result, 3)} y se encuentra dentro de los parametros establecidos 'mínimo: {recipe.values[0].minimum}' - 'máximo: {recipe.values[0].maximum}'."
            else:
                return f"\nEl resultado es {round(result, 3)} y no se encuentra dentro de los parametros establecidos 'mínimo: {recipe.values[0].minimum}' - 'máximo: {recipe.values[0].maximum}'."