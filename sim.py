class Curso:
    def __init__(self, id, nombre, creditos, anos_de_estudio):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def mostrar_ficha(self):
        print(f"\n--- Ficha del Curso ---\nID: {self.id}, Nombre: {self.nombre}, Créditos: {self.creditos}, Años de Estudio: {self.anos_de_estudio}\n")


class Alumno:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"\n--- Ficha del Alumno ---\nID: {self.id}, Nombre: {self.nombre}, Email: {self.email}\n")


class Matricula:
    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso

    def mostrar_datos(self):
        print(f"\n--- Datos de Matrícula ---\nID: {self.id_matricula}, Fecha: {self.fecha_matricula}, ID Alumno: {self.id_alumno}, ID Curso: {self.id_curso}\n")


class CentroEducacional:
    def __init__(self):
        self.matriculas = []

    def matricular_alumno(self, id_alumno, id_curso, fecha_matricula):
        id_matricula = len(self.matriculas) + 1
        matricula = Matricula(id_matricula, fecha_matricula, id_alumno, id_curso)
        self.matriculas.append(matricula)

    def mostrar_matriculas(self):
        print("\n--- Datos de Matrículas en el centro ---")
        for matricula in self.matriculas:
            matricula.mostrar_datos()

    def mostrar_alumnos_matriculados(self):
        alumnos_matriculados = set()
        print("\n--- Alumnos matriculados en el centro ---")
        for matricula in self.matriculas:
            alumno_id = matricula.id_alumno
            alumnos_matriculados.add(alumno_id)

        for alumno_id in alumnos_matriculados:
            alumno = self.obtener_alumno_por_id(alumno_id)
            alumno.mostrar_ficha()

    def obtener_alumno_por_id(self, alumno_id):
        for alumno in [alumno1, alumno2]:  # Asumiendo que tienes una lista de alumnos
            if alumno.id == alumno_id:
                return alumno
        return None


# Ejemplo de uso
curso1 = Curso(1, "Programación en Python", 4, 2)
curso2 = Curso(2, "Introducción a la Inteligencia Artificial", 3, 1)

alumno1 = Alumno(1, "Juan Pérez", "juan@email.com")
alumno2 = Alumno(2, "Ana García", "ana@email.com")

centro = CentroEducacional()

# Alumno1 se matricula en un curso
centro.matricular_alumno(alumno1.id, curso1.id, "2023-01-01")

# Alumno2 se matricula en dos cursos
centro.matricular_alumno(alumno2.id, curso1.id, "2023-02-01")
centro.matricular_alumno(alumno2.id, curso2.id, "2023-02-15")

# Mostrar ficha del curso y de todos los alumnos
curso1.mostrar_ficha()
curso2.mostrar_ficha()

for alumno in [alumno1, alumno2]:
    alumno.mostrar_ficha()

# Mostrar datos de matrícula
centro.mostrar_matriculas()
