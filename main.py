import os
from datetime import datetime, timedelta

def makeCommits(days: int, start_date: str):
    """
    Crea commits retroactivos desde una fecha específica en sistemas Windows.
    
    :param days: Número de días hacia atrás para los commits.
    :param start_date: Fecha inicial en formato 'YYYY-MM-DD'.
    """
    if days < 1:
        os.system('git push')
    else:
        # Convertimos la fecha inicial a un objeto datetime
        current_date = datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=days - 1)
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Escribimos en el archivo
        with open('data.txt', 'a') as file:
            file.write(f'{formatted_date} <- this was the commit for the day!!\n')
        
        # Agregamos el archivo al índice
        os.system('git add data.txt')
        
        # Usamos `set` para definir las variables de entorno antes del commit
        os.system(
            f'set GIT_AUTHOR_DATE="{formatted_date}" && '
            f'set GIT_COMMITTER_DATE="{formatted_date}" && '
            f'git commit -m "Commit for {formatted_date}"'
        )
        
        # Recursión
        makeCommits(days - 1, start_date)

# Llama a la función con los días y la fecha inicial
makeCommits(30, '2024-12-29')
