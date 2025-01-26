import os
import random
from datetime import datetime, timedelta

def makeCommitsRandomly(start_date: str, end_date: str, min_commits_per_day: int, max_commits_per_day: int):
    """
    Crea commits aleatorios en un rango de fechas especificado con mensajes realistas.
    
    :param start_date: Fecha inicial en formato 'YYYY-MM-DD'.
    :param end_date: Fecha final en formato 'YYYY-MM-DD'.
    :param min_commits_per_day: Mínimo número de commits por día.
    :param max_commits_per_day: Máximo número de commits por día.
    """
    # Lista de mensajes de commit realistas
    commit_messages = [
        "fix: resolver error de validación en formulario de contacto",
        "feat: añadir nueva funcionalidad de exportación a CSV",
        "refactor: optimizar algoritmo de ordenación de productos",
        "docs: actualizar documentación de la API v2",
        "style: corregir formato en componentes de React",
        "perf: mejorar rendimiento en carga de imágenes",
        "test: añadir casos de prueba para módulo de autenticación",
        "chore: actualizar dependencias de seguridad",
        "fix: corregir error de tiempo de zona horaria en dashboard",
        "feat: implementar sistema de caché para consultas frecuentes",
        "refactor: reorganizar estructura de directorios del proyecto",
        "docs: añadir guía de instalación para Windows",
        "fix: reparar enlaces rotos en la navegación principal",
        "feat: agregar soporte para temas oscuros en la UI",
        "perf: reducir tamaño de bundles de JavaScript"
    ]

    # Convertir fechas de entrada a objetos datetime
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    delta_days = (end_date_obj - start_date_obj).days

    # Generar commits para cada día en el rango
    for i in range(delta_days + 1):
        current_date = start_date_obj + timedelta(days=i)
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

        # Número aleatorio de commits para el día
        commits_today = random.randint(min_commits_per_day, max_commits_per_day)
        print(f"Generando {commits_today} commits para {formatted_date.split(' ')[0]}")

        for _ in range(commits_today):
            # Generar una hora aleatoria dentro del día
            random_time = datetime.combine(current_date.date(), datetime.min.time()) + timedelta(
                seconds=random.randint(0, 86400)
            )
            random_formatted_date = random_time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Seleccionar mensaje aleatorio
            commit_message = random.choice(commit_messages)
            
            # Modificar algunos mensajes con información específica
            if "feat" in commit_message:
                commit_message += f" ({random.choice(['UI', 'API', 'backend'])})"
            elif "fix" in commit_message:
                commit_message += f" (#{random.randint(100, 999)})"

            # Escribir en el archivo
            with open('data.txt', 'a') as file:
                file.write(f'{random_formatted_date} <- Actualización del proyecto\n')

            # Agregar y commitear con la fecha aleatoria
            os.system('git add data.txt')
            os.system(
                f'set GIT_AUTHOR_DATE="{random_formatted_date}" && '
                f'set GIT_COMMITTER_DATE="{random_formatted_date}" && '
                f'git commit -m "{commit_message}"'
            )

    # Hacer push al repositorio
    os.system('git push')

# Configuración mejorada con más commits y mensajes realistas
makeCommitsRandomly(
    start_date='2024-01-01',
    end_date='2024-12-31',
    min_commits_per_day=5,
    max_commits_per_day=10
)
