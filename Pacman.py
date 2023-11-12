# Fabiana
# Sebastian

import keyboard
# ________________________________________________________bibliotecas_________________________________________________________________
from tkinter import *  # Bibliotecas utilizadas para el funcionamiento
import tkinter as tk
import os
import pygame
import random
from itertools import cycle
from collections import deque
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font
import time
from PIL import Image



# _____________________________________________________pantallaPrincipal_________________________________________________________
presentacion = Tk()  # Crea la ventana principal
presentacion.geometry("900x506")  # Tamaño de la ventana
presentacion.title("Remake del juego PAC-MAN")  # Titulo de la ventana
presentacion.resizable(width=NO, height=NO)  # indica que no se puede modificar el tamaño de la ventana
pygame.init()  # inicia pygame
pygame.mixer.music.load('pacman.mp3')  # carga el sonido de fondo
pygame.mixer.music.set_volume(0.08)  # define el volumen de la musica
pygame.mixer.music.play(-1)  # pone la musica en bucle
musica_pausada = False  # define la musica como no pausada


# __________________________________________________cargarImagen__________________________________________________________________
def cargarImagen(nombre):  # Función para cargar imágenes
    ruta = os.path.join('imagenes', nombre)  # Obtiene la ruta completa del archivo de imagen
    global imagen  # Declara que la variable imagen es global
    imagen = PhotoImage(file=ruta)  # Carga la imagen desde la ruta y actualiza la variable global imagen
    return imagen  # Devuelve el objeto de imagen cargado


# ____________________________________________________ventanaJugar_________________________________________________________________
def menuDificultad():  # Funcion que crea la ventana "menuDificultad" donde selecciona la dificultad que desea
    menuDif = Toplevel(presentacion, bg="Black")
    menuDif.minsize(600, 300)  # Tamaño de la ventana
    menuDif.resizable(width=NO, height=NO)  # Hace que no se pueda modificar el tamaño de a ventana
    menuDif.title("Dificultad")
    titulo = Label(menuDif, text="Seleccione la dificultad:", fg="deep sky blue", bg="black", font=("Impact", 14))
    titulo.place(x=210, y=40)
    btnNivel1 = Button(menuDif, text="        Nivel 1        ", bg="deep sky blue", fg="black",
                       command= 0)  # boton que muestra la ventana "nivel_1"
    btnNivel1.place(x=150, y=140)
    btnNivel2 = Button(menuDif, text="        Nivel 2        ", bg="deep sky blue", fg="black",
                       command=0)  # boton que muestra la ventana "nivel_2"
    btnNivel2.place(x=350, y=140)
    btnNivel2.place(x=350, y=140)
    btnSalir = Button(menuDif, text=" X ", bg="red", font=("Arial", 12), fg="black",
                      command=menuDif.destroy)  # boton que realiza la opcion de salir
    btnSalir.place(x=568, y=0)
    btnSonido = Button(menuDif, text="🔉", bg="gray", fg="black", font=("Arial", 12),
                       command=toggle_musica)
    btnSonido.place(x=568.5, y=30.5)



#_______________________________________________Juego_________________________________________________________________

#
# class PacMan:
#     def __init__(self, canvas, matriz):
#         self.canvas = canvas
#         self.matriz = matriz
#         self.posicion = (0, 0)
#         self.filas = len(matriz)
#         self.columnas = len(matriz[0])
#         self.estado = "vivo"
#         self.pos_x = 1
#         self.pos_y = 1
#         self.velocidad = 1
#         self.juego = None
#
#     def terminar_juego(self):
#         # Lógica para terminar el juego
#         print("Juego terminado")
#         if self.juego:
#             self.juego.terminar_juego()
#
#
#
#     def mover_izquierda(self):
#         if self.pos_y > 0:
#             self.actualizar_posicion(self.pos_x, self.pos_y - 1)
#
#     def mover_derecha(self):
#         if self.pos_y < self.columnas - 1:
#             self.actualizar_posicion(self.pos_x, self.pos_y + 1)
#
#     def mover_arriba(self):
#         if self.pos_x > 0:
#             self.actualizar_posicion(self.pos_x - 1, self.pos_y)
#
#     def mover_abajo(self):
#         if self.pos_x < self.filas - 1:
#             self.actualizar_posicion(self.pos_x + 1, self.pos_y)
#
#     def obtener_posicion(self):
#         return self.posicion
#
#
#     def actualizar_posicion(self, nueva_x, nueva_y):
#         # Verificar si la nueva posición es válida
#         if 0 <= nueva_x < self.filas and 0 <= nueva_y < self.columnas:
#             contenido_nueva_posicion = self.matriz[nueva_x][nueva_y]
#
#             if contenido_nueva_posicion == "1":  # Alimento (punto)
#                 self.comer_punto(nueva_x, nueva_y)
#             elif contenido_nueva_posicion == "2":  # Cápsula
#                 self.comer_capsula(nueva_x, nueva_y)
#             elif contenido_nueva_posicion == "3":  # Alimento comida
#                 self.comer_alimento_comida(nueva_x, nueva_y)
#             elif contenido_nueva_posicion == "0":  # Pared
#                 # No se puede mover a una pared
#                 pass
#             else:
#                 # Mover a una posición vacía
#                 self.limpiar_posicion(self.pos_x, self.pos_y)
#                 self.pos_x = nueva_x
#                 self.pos_y = nueva_y
#                 self.dibujar_pacman()
#
#     def comer_punto(self, x, y):
#         if self.matriz[x][y] == "1":
#             self.limpiar_posicion(x, y)
#
#     def comer_capsula(self, x, y):
#         if self.matriz[x][y] == "2":
#             self.limpiar_posicion(x, y)
#
#     def comer_alimento_comida(self, x, y):
#         if self.matriz[x][y] == "3":
#             self.limpiar_posicion(x, y)
#
#     def limpiar_posicion(self, x, y):
#         self.matriz[x][y] = "0"  # Limpiar la posición en la matriz
#         self.canvas.delete("pacman")  # Limpiar el dibujo de PacMan
#         self.dibujar_pacman()  # Volver a dibujar PacMan en la nueva posición
#
#     def cargar_imagen_pacman(self):
#         # Carga la imagen de PacMan
#         imagen = Image.open("pacman.png")  # Reemplaza "pacman.png" con el nombre de tu imagen
#         imagen = imagen.resize((20, 20), Image.ANTIALIAS)
#         imagen_pacman = Image.PhotoImage(imagen)
#
#         return imagen_pacman
#
#     def dibujar_pacman(self):
#         # Calcula las coordenadas en píxeles del canvas
#         x_pixel = self.pos_y * 20
#         y_pixel = self.pos_x * 20
#
#         # Carga la imagen de PacMan en el canvas
#         self.imagen_pacman = self.cargar_imagen_pacman()
#         self.canvas.create_image(x_pixel, y_pixel, anchor="nw", image=self.imagen_pacman, tags="pacman")
#
#
#
#
# class PacmanGame:
#     def __init__(self, root, matriz):
#         self.root = root
#         self.numero_juego = 0
#         self.matriz = matriz
#         self.canvas = tk.Canvas(root, width=800, height=600)
#         self.canvas.pack()
#         self.pacman = PacMan(self.canvas, self.matriz)
#         self.inicializar_tablero()
#
#     def inicializar_tablero(self):
#         self.canvas.delete("all")  # Limpiar el tablero antes de la inicialización
#
#         for fila in range(len(self.matriz)):
#             for columna in range(len(self.matriz[0])):
#                 valor = self.matriz[fila][columna]
#                 x1, y1 = columna * 30, fila * 30
#                 x2, y2 = x1 + 30, y1 + 30
#
#                 # Dibujar el contenido del tablero según el valor en la matriz
#                 if valor == "0":
#                     color = "black"  # Espacio vacío
#                 elif valor == "1":
#                     color = "blue"  # Pared
#                 elif valor == "2":
#                     color = "white"  # Punto
#                     self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=color)
#                 else:
#                     color = "yellow"  # Otros valores (por ejemplo, Pac-Man)
#
#                 self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
#
#     def dibujar_tablero(self):
#         self.canvas.delete("pacman")  # Elimina cualquier representación anterior de Pac-Man
#
#         # Obtiene la posición actual de Pac-Man y dibuja una representación visual
#         pacman_posicion = self.pacman.obtener_posicion()
#         x, y = pacman_posicion
#         x1, y1 = x * 15, y * 15
#         x2, y2 = x1 + 15, y1 + 15
#
#         self.canvas.create_oval(x1, y1, x2, y2, fill="yellow", tags="pacman")
#
#     def terminar_juego(self):
#         # Lógica para terminar el juego
#         print("Juego terminado")
#         self.root.destroy()
#
#
#     def iniciar_juego(self):
#         self.numero_juego += 1
#         self.inicializar_tablero()
#         self.dibujar_tablero()
#         self.pacman.juego = self
#
#         keyboard.add_hotkey('d', self.pacman.mover_derecha)
#         keyboard.add_hotkey('a', self.pacman.mover_izquierda)
#         keyboard.add_hotkey('s', self.pacman.mover_abajo)
#         keyboard.add_hotkey('w', self.pacman.mover_arriba)
#         keyboard.add_hotkey('esc', self.terminar_juego)
#
#         keyboard.wait()
#
# if __name__ == "__Pacman__":
#     root = Tk()
#     matriz = [
#         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "2", "1", "1", "1", "1", "2", "1", "1", "1", "0"],
#         ["0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0"],
#         ["0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0"],
#         ["0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0"],
#         ["0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "2", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0","0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0","0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "1", "0", "1", "1", "1", "1", "0", "0", "0", "0", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
#         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
#     ]



#     pacman_game = PacmanGame(root, matriz)  # Solo pasa la matriz como argumento
#
#
#


# _________________________________________________infoComplementaria_____________________________________________________
def infoComplementaria():  # Funcion que crea la ventana "Infomarción Complementaria"
    global imagen2
    a = Toplevel(presentacion, bg="Black")
    a.minsize(900, 500)  # Tamaño de la ventana
    a.resizable(width=NO, height=NO)  # Hace que no se pueda modificar el tamaño de a ventana
    a.title("Información Complementaria")
    titulo = Label(a, text="Autores: ", fg="white", bg="black")
    titulo.place(x=40, y=50)
    infoComple = Label(a, text="Sebastian Herrera Solis - 2023066458.", fg="white", bg="black")
    infoComple.place(x=40, y=70)
    infoComple = Label(a, text="Fabiana Moreno Castrillo - 2023153700. ", fg="white", bg="black")
    infoComple.place(x=40, y=90)
    infoComple = Label(a, text="Instituto Tecnológico de Costa Rica.", fg="white", bg="black")
    infoComple.place(x=40, y=110)
    infoComple = Label(a, text="Asignatura: Introducción a la Programación.", fg="white", bg="black")
    infoComple.place(x=40, y=130)
    infoComple = Label(a, text="Carrera: Computer Engineering.", fg="white", bg="black")
    infoComple.place(x=40, y=150)
    infoComple = Label(a, text="Profesor:  Jeff Schmidt Peralta.", fg="white", bg="black")
    infoComple.place(x=40, y=170)
    infoComple = Label(a, text="País de producción: Costa Rica.", fg="white", bg="black")
    infoComple.place(x=40, y=210)
    infoComple = Label(a, text="Versión del programador 1.0.", fg="white", bg="black")
    infoComple.place(x=40, y=230)
    infoComple = Label(a, text="Información de ayuda", fg="white", bg="black")
    infoComple.place(x=40, y=270)
    infoComple = Label(a, text="1. Los controles para moverse son W,A,S,D.   ", fg="white", bg="black")
    infoComple.place(x=40, y=290)
    infoComple = Label(a, text="2. No toques los fantasmas.   ", fg="white", bg="black")
    infoComple.place(x=40, y=310)
    infoComple = Label(a, text="3. El tiempo corre.   ", fg="white", bg="black")
    infoComple.place(x=40, y=330)
    infoComple = Label(a, text="Foto de los autores del remake del juego original", fg="white", bg="black")
    infoComple.place(x=460, y=320)
    imagen2 = cargarImagen("autorSebas.png")
    Labelmovie = Label(a, image=imagen2)
    Labelmovie.place(x=420, y=90)
    imagen3 = cargarImagen("autorFabi.png")
    Labelmovie = Label(a, image=imagen3)
    Labelmovie.place(x=650, y=45)
    btnSalir = Button(a, text=" X ", bg="red", font=("Arial", 12), fg="black",
                      command=a.destroy)  # boton que realiza la opcion de salir
    btnSalir.place(x=850, y=22)
    btnSonido = Button(a, text="🔉", bg="gray", fg="black", font=("Arial", 12), command=toggle_musica)
    btnSonido.place(x=850, y=53.8)


# ____________________________________________________ventanaAyuda_______________________________________________________
def menuAyuda():  # Función que crea la ventana "menuAyuda" donde se muestra la ayuda del juego
    ayuda = Toplevel(presentacion, bg="Black")
    ayuda.minsize(850, 400)  # Tamaño de la ventana
    ayuda.resizable(width=NO, height=NO)  # Hace que no se pueda modificar el tamaño de la ventana
    ayuda.title("Ayuda")

    titulo = Label(ayuda, text="Historia:", fg="hotpink1", bg="black", font=("Impact", 14))
    titulo.place(x=30, y=218)

    historia_pacman = """
    Pac-Man es un juego arcade icónico de 1980.
    Controlas a Pac-Man, un per7onaje amarillo, que come píldoras en un laberinto mientras evita fantasmas.
    El objetivo es completar niveles, comiendo píldoras y frutas. Pac-Man puede consumir "superpíldoras" para comer a los fantasmas.
    El juego es un ícono de la cultura pop y los videojuegos.
    """
    # Etiqueta con la historia de Pac-Man en fuente más pequeña
    historia_label = Label(ayuda, text=historia_pacman, fg="white", bg="black", justify="left", font=("Arial", 8))
    historia_label.place(x=40, y=250)

    # Título de la lista de controles
    titulo = Label(ayuda, text="Controles:", fg="orange", bg="black", font=("Impact", 14))
    titulo.place(x=30, y=45)

    btnSalir = Button(ayuda, text=" X ", bg="red", font=("Arial", 12), fg="black",
                      command=ayuda.destroy)  # boton que realiza la opcion de salir
    btnSalir.place(x=810, y=22)
    btnSonido = Button(ayuda, text="🔉", bg="gray", fg="black", font=("Arial", 12), command=toggle_musica)
    btnSonido.place(x=810, y=53.8)

    # Imagen del teclado de juego
    imagen1 = cargarImagen("tecladoJuego.png")
    Labelmovie = Label(ayuda, image=imagen1)
    Labelmovie.place(x=400, y=50)
    # Controles del juego
    controles_label = Label(ayuda, text="Arriba: W\nAbajo: S\nDerecha: D\nIzquierda: A\n", fg="white", bg="black")
    controles_label.place(x=40, y=80)


# ____________________________________________________ventanaPuntajes_______________________________________________________
def ventanaPuntajes():
    global venPuntaje, boton_mostrar

    venPuntaje = tk.Toplevel(presentacion, bg="Black")
    venPuntaje.minsize(300, 100)
    venPuntaje.resizable(width=tk.NO, height=tk.NO)
    venPuntaje.title("Dificultad")
    txt = Label(venPuntaje, text="¡Mejores puntajes!", fg="deep sky blue", font=("Impact", 17), bg="black")
    txt.place(x=70, y=40)
    boton_mostrar = tk.Button(venPuntaje, text="      Mostrar      ", bg="deep sky blue", fg="black",
                              command=lambda: mostrar_puntajes(venPuntaje))
    boton_mostrar.place(x=115, y=100)
    boton_mostrar = tk.Button(venPuntaje, text="      Salir        ", bg="deep sky blue", fg="black",
                              command=venPuntaje.destroy)
    boton_mostrar.place(x=120, y=140)


def mostrar_puntajes(ventana_principal):
    # Mostrar los puntajes en una ventana
    venMostrarPuntajes = tk.Toplevel(ventana_principal)
    venMostrarPuntajes.title("Puntajes más altos")
    # Crear una lista para almacenar los puntajes como tuplas (nombre, puntaje)
    puntajes = []
    # Leer los nombres y puntajes desde el archivo y almacenarlos en la lista puntajes
    with open('puntajes.txt', 'r') as f:  # Abrir el archivo en modo lectura
        lineas = f.readlines()  # Leer todas las líneas del archivo
        for linea in lineas:  # Recorrer las líneas del archivo
            partes = linea.strip().split(': ')  # Separar el nombre del puntaje
            if len(partes) == 2:  # Asegurarse de que haya dos partes: nombre y puntaje
                nombre = partes[0]
                puntaje = partes[1]
                puntajes.append((nombre, int(puntaje)))  # Convertir puntaje a entero
    # Ordenar los puntajes de mayor a menor
    puntajes.sort(key=lambda x: x[1], reverse=True)  # Ordenar la lista de puntajes de mayor a menor
    # Crear una etiqueta con los puntajes
    etiquetas_puntajes = [tk.Label(venMostrarPuntajes, text=f"{i + 1}. {nombre}: {puntaje}") for i, (nombre, puntaje) in
                          enumerate(puntajes[:5])]
    # Mostrar todas las etiquetas de puntajes al mismo tiempo
    for label in etiquetas_puntajes:  # Recorrer todas las etiquetas
        label.pack()  # Mostrar la etiqueta


def guardar_numeros(nombre_jugador, puntuacion):  # Cambiamos el nombre de la función a guardar_numeros
    # Obtener el número ingresado en la ventana
    numero = puntuacion
    jugador = nombre_jugador
    # Abrir el archivo en modo append (añadir al final del archivo)
    with open('puntajes.txt', 'a') as f:
        # Escribir el nombre del jugador, la puntuación y un separador en una nueva línea
        f.write(f"{jugador}: {numero}\n")


# ____________________________________________________________musica___________________________________________________________
def toggle_musica():  # Funcion que crea la ventana "menuAyuda" donde se muestra la ayuda del juego
    global musica_pausada
    if musica_pausada:  # Si la música está pausada,
        pygame.mixer.music.unpause()  # Reanudar la música
        musica_pausada = False
    else:
        pygame.mixer.music.pause()  # Pausar la música
        musica_pausada = True


# __________________________________________________ventanaPrincipal_____________________________________________________

imagen1 = cargarImagen("fondoPrincipal.png")  # carga la imagen del fondo
LabelFondo = Label(presentacion, image=imagen1)  # define la imagen del fondo
LabelFondo.place(x=0, y=0)  # coloca la imagen del fondo

btnJugar = Button(presentacion, text="                        Jugar                         ", bg="red1", fg="black",
                  command=menuDificultad)  # Muestra el boton para seleccionar dificultad y jugar
btnJugar.place(x=350, y=170)
btnPuntajes = Button(presentacion, text="             Salón de la fama                ", bg="deep sky blue", fg="black",
                     command=ventanaPuntajes)  # boton que muestra los mejores puntajes
btnPuntajes.place(x=350, y=215)
btnInfoC = Button(presentacion, text="   Información Complementaria  ", bg="orange", fg="black",
                  command=infoComplementaria)  # Muestra el boton para mostrar la infocomplementaria
btnInfoC.place(x=350, y=260)
btnComoJugar = Button(presentacion, text="                     Ayuda                        ", bg="hotpink1",
                      fg="black", command=menuAyuda)  # boton que realiza la opcion de salir
btnComoJugar.place(x=350, y=305)
btnSalir = Button(presentacion, text=" X ", bg="red", font=("Arial", 12), fg="black",
                  command=presentacion.destroy)  # boton que realiza la opcion de salir
btnSalir.place(x=853.5, y=22)
btnSonido = Button(presentacion, text="🔉", bg="gray", fg="black", font=("Arial", 12), command=toggle_musica)
btnSonido.place(x=853.6, y=53.8)



presentacion.mainloop()  # cierro la ventana






