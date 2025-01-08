import os
import random
from datetime import datetime, timedelta

def makeCommitsRandomly(start_date: str, end_date: str, max_commits_per_day: int):
    """
    Crea commits aleatorios en un rango de fechas especificado.

    :param start_date: Fecha inicial en formato 'YYYY-MM-DD'.
    :param end_date: Fecha final en formato 'YYYY-MM-DD'.
    :param max_commits_per_day: Máximo número de commits por día.
    """
    # Convertir fechas de entrada a objetos datetime
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    delta_days = (end_date_obj - start_date_obj).days

    # Generar commits para cada día en el rango
    for i in range(delta_days + 1):
        current_date = start_date_obj + timedelta(days=i)
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

        # Número aleatorio de commits para el día
        commits_today = random.randint(1, max_commits_per_day)
        print(f"Generating {commits_today} commits for {formatted_date.split(' ')[0]}")

        for _ in range(commits_today):
            # Generar una hora aleatoria dentro del día
            random_time = datetime.combine(current_date.date(), datetime.min.time()) + timedelta(
                seconds=random.randint(0, 86400)
            )
            random_formatted_date = random_time.strftime('%Y-%m-%d %H:%M:%S')

            # Escribir en el archivo
            with open('data.txt', 'a') as file:
                file.write(f'{random_formatted_date} <- this was a random commit!!\n')

            # Agregar y commitear con la fecha aleatoria
            os.system('git add data.txt')
            os.system(
                f'set GIT_AUTHOR_DATE="{random_formatted_date}" && '
                f'set GIT_COMMITTER_DATE="{random_formatted_date}" && '
                f'git commit -m "Random commit for {random_formatted_date}"'
            )

    # Hacer push al repositorio
    os.system('git push')

# Llama a la función con el rango de fechas y el máximo de commits por día
makeCommitsRandomly('2025-01-01', '2025-01-08', 12)
