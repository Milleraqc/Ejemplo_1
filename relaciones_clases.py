# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 10:54:16 2025

@author: ingmi
"""




# %%

# %%

# %%
class Colegio:
    nombre = ""
    ubicacion = ""
    
    def __init__(self,nombreCol,ubicacionCol):
        self.nombre = nombreCol
        self.ubicacion = ubicacionCol
        self.estudiantes = []
    
    
    def adicionar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        
    def eliminar_estudiante(self,estudiante):
        for e in self.estudiantes:
            if (e == estudiante):
                self.estudiantes.remove(estudiante)
    
    def mostrar_estudiantes(self):
       print("Los estudiantes son:")
       for estudiante in self.estudiantes:
           print(f' - {estudiante}')
    
    
class Estudiante:
     def __init__(self,nombreEstudiante,edadEstudiante,gradoEstudiante):
         self.nombre: str = nombreEstudiante
         self.edad: int= edadEstudiante
         self.grado: str = gradoEstudiante
         self.promedio: float = 0.0

     def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.grado}"
         
     def promedio(self,notas):
         suma = 0 
         for i in notas:
             self.suma += i
         self.promedio = self.suma / len(notas)
     def informacion_estudiante(self):
         print(f"El estudiante es {self.nombre} con edad {self.edad}, del grado {self.grado} tiene es siguiente promedio: {self.promedio}")

     
         
        
san_pablo = Colegio("San Pablo", "Victoria-Caldas")
e1 = Estudiante("Roger Villa", 27,"pregrado")
e2 = Estudiante("Wilfredo Calderon", 21,"pregrado")
e3 = Estudiante("Nicolas Cortes", 18,"pregrado") 
e4 = Estudiante("Felipe Choconta", 21,"pregrado")
e5 = Estudiante("Miller Quiroga", 45,"pregrado")
san_pablo.adicionar_estudiante(e1)
san_pablo.adicionar_estudiante(e2)
san_pablo.adicionar_estudiante(e3)
san_pablo.adicionar_estudiante(e4)
san_pablo.adicionar_estudiante(e5)
san_pablo.mostrar_estudiantes()


# %%

class Colegio:
    nombre = ""
    ubicacion = ""
    
    
    def __init__(self,nombreCol,ubicacionCol):
        self.nombre = nombreCol
        self.ubicacion = ubicacionCol
        self.estudiantes = []
    
    
    def adicionar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        
    def eliminar_estudiante(self,estudiante):
        for e in self.estudiantes:
            if (e == estudiante):
                self.estudiantes.remove(estudiante)
    
    def mostrar_estudiantes(self):
       print("Los estudiantes son:")
       for estudiante in self.estudiantes:
           print(f' - {estudiante}')

    
class Estudiante:
     def __init__(self,nombreEstudiante,edadEstudiante,gradoEstudiante):
         self.nombre: str = nombreEstudiante
         self.edad: int= edadEstudiante
         self.grado: str = gradoEstudiante
         self.promedio: float = 0.0
         
     def promedio(self,notas):
         suma = 0 
         for i in notas:
             self.suma += i
         self.promedio = self.suma / len(notas)
     def informacion_estudiante(self):
         print(f"El estudiante es {self.nombre} con edad {self.edad}, del grado {self.grado} tiene es siguiente promedio: {self.promedio}")

     
         
        
san_pablo = Colegio("San Pablo", "Victoria-Caldas")
e1 = Estudiante("Roger Villa", 27,"pregrado")
e2 = Estudiante("Wilfredo Calderon", 21,"pregrado")
e3 = Estudiante("Nicolas Cortes", 18,"pregrado") 
e4 = Estudiante("Felipe Choconta", 21,"pregrado")
e5 = Estudiante("Miller Quiroga", 45,"pregrado")
san_pablo.adicionar_estudiante(e1)
san_pablo.adicionar_estudiante(e2)
san_pablo.adicionar_estudiante(e3)
san_pablo.adicionar_estudiante(e4)
san_pablo.adicionar_estudiante(e5)
san_pablo.mostrar_estudiantes()



# %% OOP - Relación Composición

class Solicitud:
    estudiante = ""
    profesor = ""
    hora = ""
    
    def __init__(self, nombre_estudiante:str, nombre_profesor:str, hora:str):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora
        
class Agenda:
    def __init__(self):
        self.turnos: list[Solicitud] = []
    
    def agregar_turno(self, estudiante:str, profesor:str, hora:str) -> bool:
        if (self.disponibilidad(profesor, hora)):
            self.turnos.append(Solicitud(estudiante, profesor, hora))
            return True
        return False
        
    def eliminar_turno(self, profesor:str, hora:str) -> bool:
        for profe, turno in enumerate(self.turnos):
            if (turno.profesor == profesor) and (turno.hora == hora):
                # self.turnos.remove(profe)
                del self.turnos[profe]
                return True
        print("No hay ningun tutoria agendada en esta hora para el profesor")
        return False    
      
    def disponibilidad(self, profesor:str, hora:str) -> bool:
        for turno in self.turnos:
            if (turno.profesor == profesor) and (turno.hora == hora):
                print("El profesor no está disponible en esta hora")
                return False
        print("El profesor se encuentra disponible en el horario")
        return True
    
    def mostrar_turno(self):
        if(not self.turnos):
            print("La agenda se encuentra vacía")
            return
        
        print("------------ Tutorias -----------")
        for turno in self.turnos:
            print(f"- {turno.hora}\t {turno.profesor}\t {turno.estudiante}")

# %%
agenda = Agenda()
agenda.mostrar_turno()
agenda.agregar_turno("Felipe", "Jorge", "14:00")
agenda.mostrar_turno()
agenda.agregar_turno("Nicolas", "Miller", "8:00")
agenda.mostrar_turno()
agenda.disponibilidad("Jorge", "8:00")
agenda.disponibilidad("Jorge", "14:00")
agenda.mostrar_turno()
agenda.eliminar_turno("Miller", "9:00")
agenda.eliminar_turno("Miller", "8:00")
agenda.mostrar_turno()

# %%

"""
Ejercicio de Agenda de tickes para Tutorías en la facultad de Matemáticas Aplicadas.

Elaborar un algoritmo en OOP, para solicitar un ticket para tutoría con algún docente del programa de
Matematicas Aplicadas.

# %% OOP - Relación Composición
"""
class Ticket:
    estudiante = ""
    profesor = ""
    hora = ""
    
    def __init__(self, nombre_estudiante:str, nombre_profesor:str, hora:str):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora

class Agenda:
    def __init__(self):
        self.tickets: list[Ticket] = []
    
    def disponibilidad(self, profesor:str, hora:str) -> bool:
        for ticket in self.tickets:
            if (ticket.profesor == profesor) and (ticket.hora == hora):
                print("El profesor no está disponible en esta hora")
                return False
        print("El profesor se encuentra disponible en el horario")
        return True
    
    def agregar_ticket(self, estudiante:str, profesor:str, hora:str) -> bool:
        if (self.disponibilidad(profesor, hora) == True):
            self.tickets.append(Ticket(estudiante, profesor, hora))
            return True
        return False
        
    def eliminar_ticket(self, profesor:str, hora:str) -> bool:
        for profe, ticket in enumerate(self.tickets):
            if (ticket.profesor == profesor) and (ticket.hora == hora):
                # self.ticket.remove(ticket) - No funciona
                del self.tickets[profe]
                return True
        print("No hay ningun tutoria agendada en esta hora para el profesor")
        return False
        
    def mostrar_ticket(self):
        if(not self.tickets):
            print("La agenda se encuentra vacía")
            return
        
        print("------------ Tutorias -----------")
        for ticket in self.tickets:
            print(f"- {ticket.hora}\t | {ticket.profesor}\t  -->{ticket.estudiante}")
# %% CREAR MENÚ



# %%



tutoria = Agenda()
tutoria.mostrar_ticket()
tutoria.agregar_ticket("Felipe", "Jorge", "14:00")
tutoria.agregar_ticket("Nicolas", "Miller","9:00")
tutoria.mostrar_ticket()
tutoria.disponibilidad("Jorge", "8:00")
tutoria.disponibilidad("Jorge", "14:00")
tutoria.mostrar_ticket()
tutoria.eliminar_ticket("Miller", "9:00")
tutoria.eliminar_ticket("Miller", "8:00")
tutoria.mostrar_ticket()
