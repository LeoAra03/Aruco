import numpy as np
import cv2
import cv2.aruco as aruco
import tkinter as tk
from tkinter import ttk, Scale, messagebox, filedialog
from PIL import Image, ImageTk, ImageOps
import threading
import random
import time
import os



class VentanaCrearAruco:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Crear ArUco")
        self.ventana.geometry("400x250")
        self.ventana.resizable(False, False)

        # Variables
        self.var_diccionario = tk.StringVar(value="DICT_4X4_100")
        self.var_tamano = tk.IntVar(value=200)
        self.var_id = tk.IntVar(value=0)

        self.resultado = None  # Para almacenar los datos

        self.crear_interfaz()

    # =========================================================================
    # MÉTODOS DE CREACIÓN DE INTERFAZ - VENTANA CREAR ARUCO
    # =========================================================================

    def crear_interfaz(self):
        frame = ttk.Frame(self.ventana, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Diccionario:").grid(row=0, column=0, sticky=tk.W)
        dicc_combo = ttk.Combobox(frame, textvariable=self.var_diccionario,
            values=["DICT_ARUCO_ORIGINAL", "DICT_4X4_100", "DICT_5X5_100", "DICT_6X6_100", "DICT_7X7_100"], width=20)
        dicc_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Tamaño (px):").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.var_tamano, width=10).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="ID del marcador:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.var_id, width=10).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Generar", command=self.generar_aruco).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Cancelar", command=self.cancelar).grid(row=4, column=0, columnspan=2, pady=5)

    # =========================================================================
    # MÉTODOS DE FUNCIONALIDAD - VENTANA CREAR ARUCO
    # =========================================================================

    def generar_aruco(self):
        # Almacena los datos y cierra la ventana
        self.resultado = {
            "diccionario": self.var_diccionario.get(),
            "tamano": self.var_tamano.get(),
            "id": self.var_id.get()
        }
        self.ventana.destroy()

    def cancelar(self):
        self.resultado = None
        self.ventana.destroy()

def crear_aruco(root):
    ventana = VentanaCrearAruco(root)
    root.wait_window(ventana.ventana)
    return ventana.resultado  # Devuelve diccionario, tamaño y id
    