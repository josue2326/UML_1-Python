import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import datetime
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Autor: {self.nombre} {self.apellido}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return (f"Libro: {self.titulo}, ISBN: {self.isbn}, "
                f"{self.autor.mostrar_info()}, {self.categoria.mostrar_info()}")

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido}, ID: {self.id_usuario}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo - Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre} {self.usuario.apellido}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)

    def devolver_libro(self, libro, usuario, fecha_devolucion):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = fecha_devolucion
                return

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join(libro.mostrar_info() for libro in self.libros)

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(usuario.mostrar_info() for usuario in self.usuarios)

    def mostrar_prestamos(self):
        if not self.prestamos:
            return "No hay préstamos realizados."
        return "\n".join(prestamo.mostrar_info() for prestamo in self.prestamos)

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.init_data()
        self.logo = util_img.leer_imagen("C:/Users/josue/Downloads/INTERFACES/UML_1/imagenes/logo.png", (360, 460))
        self.perfil = util_img.leer_imagen("C:/Users/josue/Downloads/INTERFACES/UML_1/imagenes/Perfil.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def init_data(self):
        autores = [
            Autor("Jane", "Austen"),
            Autor("Mark", "Twain"),
            Autor("George", "Orwell"),
            Autor("Virginia", "Woolf"),
            Autor("F. Scott", "Fitzgerald"),
            Autor("J.K.", "Rowling"),
            Autor("J.R.R.", "Tolkien"),
            Autor("Agatha", "Christie"),
            Autor("Stephen", "King"),
            Autor("Haruki", "Murakami")
        ]

        categorias = [
            Categoria("Ficción"),
            Categoria("Misterio"),
            Categoria("Ciencia Ficción"),
            Categoria("Fantasía"),
            Categoria("Biografía")
        ]

        libros = [
            Libro("Orgullo y prejuicio", "978-0-19-953556-9", autores[0], categorias[0]),
            Libro("Las aventuras de Tom Sawyer", "978-0-14-303956-3", autores[1], categorias[0]),
            Libro("1984", "978-0-452-28423-4", autores[2], categorias[2]),
            Libro("La señora Dalloway", "978-0-15-662870-9", autores[3], categorias[0]),
            Libro("El gran Gatsby", "978-0-743-27313-7", autores[4], categorias[0]),
            Libro("Harry Potter y la piedra filosofal", "978-0-7475-3269-9", autores[5], categorias[3]),
            Libro("El señor de los anillos", "978-0-618-64015-7", autores[6], categorias[3]),
            Libro("Asesinato en el Orient Express", "978-0-06-269366-0", autores[7], categorias[1]),
            Libro("El resplandor", "978-0-307-74463-7", autores[8], categorias[1]),
            Libro("Tokio Blues", "978-0-14-103712-6", autores[9], categorias[0])
        ]

        for libro in libros:
            self.biblioteca.registrar_libro(libro)

        usuarios = [
            Usuario("Carlos", "Rivas", 1),
            Usuario("Elena", "Moreno", 2),
            Usuario("Pablo", "Sánchez", 3),
            Usuario("Laura", "Gómez", 4),
            Usuario("Andrés", "Torres", 5),
            Usuario("Claudia", "Vega", 6),
            Usuario("Diego", "Cruz", 7),
            Usuario("Lucía", "Mendoza", 8),
            Usuario("Javier", "Ortiz", 9),
            Usuario("Natalia", "Ruiz", 10)
        ]
        for usuario in usuarios:
            self.biblioteca.registrar_usuario(usuario)
    def on_enter(self, e):
        e.widget['background'] = COLOR_MENU_CURSOR_ENCIMA

    def on_leave(self, e):
        e.widget['background'] = COLOR_MENU_LATERAL
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("C:/Users/josue/Downloads/INTERFACES/UML_1/imagenes/logo.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="¡MENÚ BIBLIOTECA!")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="POOUP@unipamplona.co")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def toggle_panel(self):
        # Alternar la visibilidad del menú lateral
        if self.menu_lateral.winfo_viewable():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        self.menuLateralBtns = []

        botones_info = [
            ("Inicio", self.mostrar_inicio),
            ("Libros", self.mostrar_libros),
            ("Usuarios", self.mostrar_usuarios),
            ("Préstamos", self.mostrar_prestamos),
            ("Registrar un libro", self.registrar_libro),
            ("Registrar un usuario", self.registrar_usuario),
            ("Realizar un préstamo", self.realizar_prestamo),
            ("Devolver un libro", self.devolver_libro),
            ("Salir", self.destroy)
        ]

        for (text, command) in botones_info:
            btn = tk.Button(self.menu_lateral, text=text, bg=COLOR_MENU_LATERAL, fg="white", 
                            font=("Roboto", 13, "bold"), bd=0, padx=10, pady=10, width=ancho_menu, height=alto_menu,
                            command=command)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.pack()
            self.menuLateralBtns.append(btn)

    def controles_cuerpo(self):
        # Controles del cuerpo principal
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def mostrar_inicio(self):
        self.limpiar_cuerpo()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_libros(self):
        self.limpiar_cuerpo()
        info_libros = self.biblioteca.mostrar_libros()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_libros, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_usuarios(self):
        self.limpiar_cuerpo()
        info_usuarios = self.biblioteca.mostrar_usuarios()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_usuarios, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_prestamos(self):
        self.limpiar_cuerpo()
        info_prestamos = self.biblioteca.mostrar_prestamos()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_prestamos, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)


    def registrar_libro(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Título del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        titulo_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        titulo_entry.pack()

        tk.Label(self.cuerpo_principal, text="ISBN del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        tk.Label(self.cuerpo_principal, text="Autor del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        autor_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        autor_entry.pack()

        tk.Label(self.cuerpo_principal, text="Categoría del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        categoria_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        categoria_entry.pack()

        def submit():
            titulo = titulo_entry.get()
            isbn = isbn_entry.get()
            autor_nombre, autor_apellido = autor_entry.get().split()
            categoria_nombre = categoria_entry.get()

            autor = Autor(autor_nombre, autor_apellido)
            categoria = Categoria(categoria_nombre)
            nuevo_libro = Libro(titulo, isbn, autor, categoria)

            self.biblioteca.registrar_libro(nuevo_libro)
            messagebox.showinfo("Éxito", "Libro registrado con éxito")
            self.mostrar_libros()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)


    def registrar_usuario(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del usuario:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="Apellido del usuario:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        apellido_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        apellido_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del usuario:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id_usuario = int(id_entry.get())

            nuevo_usuario = Usuario(nombre, apellido, id_usuario)
            self.biblioteca.registrar_usuario(nuevo_usuario)
            messagebox.showinfo("Éxito", "Usuario registrado con éxito")
            self.mostrar_usuarios()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)


    def realizar_prestamo(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="ISBN del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del usuario:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            isbn = isbn_entry.get()
            id_usuario = int(id_entry.get())

            libro = next((l for l in self.biblioteca.libros if l.isbn == isbn), None)
            usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == id_usuario), None)

            if libro and usuario:
                fecha_prestamo = datetime.date.today().strftime("%Y-%m-%d")
                self.biblioteca.realizar_prestamo(libro, usuario, fecha_prestamo)
                messagebox.showinfo("Éxito", "Préstamo realizado con éxito")
                self.mostrar_prestamos()
            else:
                messagebox.showerror("Error", "Libro o usuario no encontrado")

        tk.Button(self.cuerpo_principal, text="Realizar Préstamo", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)


    def devolver_libro(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="ISBN del libro:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del usuario:", bg=COLOR_CUERPO_PRINCIPAL,
        font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            isbn = isbn_entry.get()
            id_usuario = int(id_entry.get())

            libro = next((l for l in self.biblioteca.libros if l.isbn == isbn), None)
            usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == id_usuario), None)

            if libro and usuario:
                fecha_devolucion = datetime.date.today().strftime("%Y-%m-%d")
                self.biblioteca.devolver_libro(libro, usuario, fecha_devolucion)
                messagebox.showinfo("Éxito", "Libro devuelto con éxito")
                self.mostrar_prestamos()
            else:
                messagebox.showerror("Error", "Libro o usuario no encontrado")

        tk.Button(self.cuerpo_principal, text="Devolver Libro", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)



