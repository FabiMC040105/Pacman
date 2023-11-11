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
                       command=nivel1)  # boton que muestra la ventana "nivel_1"
    btnNivel1.place(x=150, y=140)
    btnNivel2 = Button(menuDif, text="        Nivel 2        ", bg="deep sky blue", fg="black",
                       command=nivel2)  # boton que muestra la ventana "nivel_2"
    btnNivel2.place(x=350, y=140)
    btnSalir = Button(menuDif, text="                   Salir                    ", bg="deep sky blue", fg="black",
                      command=menuDif.destroy)  # boton que realiza la opcion de salir
    btnSalir.place(x=430, y=250)
    btnSonido = Button(menuDif, text="           Sonido              ", bg="deep sky blue", fg="black",
                       command=0)  # boton que realiza la opcion de salir
    btnSonido.place(x=457, y=210)


#_______________________________________________NivelUno_________________________________________________________________


def nivel1():
    niv1 = Toplevel(bg="Black")
    niv1.minsize(800, 500)
    niv1.resizable(width=NO, height=NO)
    niv1.title("Nivel 1")




#_______________________________________________NivelDos_________________________________________________________________


def nivel2():
    niv2 = Toplevel(bg="Black")
    niv2.minsize(800, 500)
    niv2.resizable(width=NO, height=NO)
    niv2.title("Nivel 2")



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








matriz = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"],
    ["0", "1", "2", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "2", "1", "1", "1", "1", "2", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "2", "1", "0", "1", "1", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "3", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "2", "0", "0", "0", "0", "0", "0", "3", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "2", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "0", "0","1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0","0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0","1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0","0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "1", "1", "0","0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0","0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "2", "0", "1", "0", "0","1", "1", "0", "3", "0", "0", "0", "0", "1", "0", "1", "1", "1"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0","0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "0", "0", "0", "0","1", "1", "1", "1", "1", "1", "0", "0", "2", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0","0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1", "1", "1", "0","0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0","0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
]


matriz_inicial = [fila.copy() for fila in matriz]



posx = 0  #posicion en x del jugador e indices de la matriz
posy = 0 #posicion en y del jugador e indices de la matriz



#actualiza la matriz, cuando llega a los indices iguales a posx y pos
#actualiza la posicion del jugador
def actualizar_matriz():
    for n in range(len(matriz)):
        for x in range(len(matriz[0])):
            if n == posy and x == posx:
                matriz[n][x] = "👾"
            elif matriz[n][x] == "👾":
                matriz[n][x] = matriz_inicial[n][x]
            else:
                matriz[n][x] = f"{matriz[n][x]}"

def imprimir_matriz():
    actualizar_matriz()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-------------------------------------------------------------------------")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()
    print(f"posx:{posx}, posy: {posy}")
    print("-------------------------------")

#aumenta la posicion posx y verifica que no salga de la matriz
def mover_derecha():
    global posx
    if posx + 1 < len(matriz[0]):
        posx += 1
#disminuye la posicion posx y verifica que no salga de la matriz
def mover_izquierda():
    global posx
    if posx - 1 >= 0:
        posx -= 1

#aumenta la posicion posy y verifica que no salga de la matriz
def mover_abajo():
    global posy
    if posy + 1 < len(matriz):
        posy += 1

#disminuye la posicion posy y verifica que no salga de la matriz
def mover_arriba():
    global posy
    if posy - 1 >= 0:
        posy -= 1

#lista de teclas funcionales
teclas = ['k', 'a', 's', 'd', 'w']

for tecla in teclas:
    if tecla == 'd': #verifica la tecla que se toco
        keyboard.add_hotkey(tecla, mover_derecha)  #ejecuta la funcion segun la tecla
    elif tecla == 's': #verifica la tecla que se toco
        keyboard.add_hotkey(tecla, mover_abajo) #ejecuta la funcion segun la tecla
    elif tecla == 'w': #verifica la tecla que se toco
        keyboard.add_hotkey(tecla, mover_arriba) #ejecuta la funcion segun la tecla
    elif tecla == 'a': #verifica la tecla que se toco
        keyboard.add_hotkey(tecla, mover_izquierda) #ejecuta la funcion segun la tecla
    else:
        keyboard.add_hotkey(tecla, imprimir_matriz) #ejecuta la funcion segun la tecla

keyboard.wait('esc') #para salir del bucle



