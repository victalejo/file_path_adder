import os
import shutil
import tempfile
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


class FilePathAdderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregador de Rutas a Archivos")
        self.root.geometry("800x600")

        # Variables
        self.directory = tk.StringVar(value=os.getcwd())
        self.exclude_dirs = set(['lib', 'vendor', 'tmp', '.git'])
        self.file_extensions = {'.php', '.html', '.sql', '.js', '.css', '.txt', '.md', '.py'}

        self._create_gui()

    def _create_gui(self):
        # Marco principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Selección de directorio
        dir_frame = ttk.LabelFrame(main_frame, text="Directorio", padding="5")
        dir_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        ttk.Entry(dir_frame, textvariable=self.directory, width=60).grid(row=0, column=0, padx=5)
        ttk.Button(dir_frame, text="Examinar", command=self._browse_directory).grid(row=0, column=1, padx=5)

        # Directorios excluidos
        exclude_frame = ttk.LabelFrame(main_frame, text="Directorios Excluidos", padding="5")
        exclude_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5), pady=5)

        # Lista de directorios excluidos
        self.exclude_listbox = tk.Listbox(exclude_frame, height=6)
        self.exclude_listbox.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        for dir_name in sorted(self.exclude_dirs):
            self.exclude_listbox.insert(tk.END, dir_name)

        # Botones para directorios excluidos
        ttk.Button(exclude_frame, text="Agregar", command=self._add_exclude_dir).grid(row=1, column=0, padx=5)
        ttk.Button(exclude_frame, text="Eliminar", command=self._remove_exclude_dir).grid(row=1, column=1, padx=5)

        # Extensiones de archivo
        ext_frame = ttk.LabelFrame(main_frame, text="Extensiones de Archivo", padding="5")
        ext_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0), pady=5)

        # Lista de extensiones
        self.ext_listbox = tk.Listbox(ext_frame, height=6)
        self.ext_listbox.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        for ext in sorted(self.file_extensions):
            self.ext_listbox.insert(tk.END, ext)

        # Botones para extensiones
        ttk.Button(ext_frame, text="Agregar", command=self._add_extension).grid(row=1, column=0, padx=5)
        ttk.Button(ext_frame, text="Eliminar", command=self._remove_extension).grid(row=1, column=1, padx=5)

        # Log de operaciones
        log_frame = ttk.LabelFrame(main_frame, text="Log de Operaciones", padding="5")
        log_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        self.log_text = ScrolledText(log_frame, height=12, width=70)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botón de proceso
        ttk.Button(main_frame, text="Procesar Archivos", command=self._process_files).grid(row=3, column=0,
                                                                                           columnspan=2, pady=10)

        # Configurar expansión
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

    def _browse_directory(self):
        directory = filedialog.askdirectory(initialdir=self.directory.get())
        if directory:
            self.directory.set(directory)

    def _add_exclude_dir(self):
        dir_name = tk.simpledialog.askstring("Agregar Directorio", "Nombre del directorio a excluir:")
        if dir_name:
            self.exclude_dirs.add(dir_name)
            self.exclude_listbox.delete(0, tk.END)
            for dir_name in sorted(self.exclude_dirs):
                self.exclude_listbox.insert(tk.END, dir_name)

    def _remove_exclude_dir(self):
        selection = self.exclude_listbox.curselection()
        if selection:
            dir_name = self.exclude_listbox.get(selection[0])
            self.exclude_dirs.remove(dir_name)
            self.exclude_listbox.delete(selection[0])

    def _add_extension(self):
        ext = tk.simpledialog.askstring("Agregar Extensión", "Extensión de archivo (con punto, ej: .txt):")
        if ext:
            if not ext.startswith('.'):
                ext = '.' + ext
            self.file_extensions.add(ext.lower())
            self.ext_listbox.delete(0, tk.END)
            for ext in sorted(self.file_extensions):
                self.ext_listbox.insert(tk.END, ext)

    def _remove_extension(self):
        selection = self.ext_listbox.curselection()
        if selection:
            ext = self.ext_listbox.get(selection[0])
            self.file_extensions.remove(ext)
            self.ext_listbox.delete(selection[0])

    def _log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()

    def _process_files(self):
        if not os.path.exists(self.directory.get()):
            messagebox.showerror("Error", "El directorio seleccionado no existe")
            return

        try:
            self.log_text.delete(1.0, tk.END)
            self._log("Iniciando proceso...")

            for dirpath, dirnames, filenames in os.walk(self.directory.get()):
                # Excluir directorios no deseados
                dirnames[:] = [d for d in dirnames if d not in self.exclude_dirs]

                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)

                    # Verificar extensión
                    if not any(filename.lower().endswith(ext) for ext in self.file_extensions):
                        continue

                    # Calcular ruta relativa
                    rel_path = os.path.relpath(filepath, self.directory.get())
                    rel_path = rel_path.replace('\\', '/')

                    # Crear archivo temporal
                    temp_fd, temp_path = tempfile.mkstemp()
                    try:
                        with os.fdopen(temp_fd, 'w', encoding='utf-8') as temp_file:
                            # Escribir la ruta como comentario
                            if filepath.endswith('.php'):
                                temp_file.write(f"///{rel_path}\n\n")
                            elif filepath.endswith('.html'):
                                temp_file.write(f"<!-- {rel_path} -->\n\n")
                            elif filepath.endswith(('.js', '.css')):
                                temp_file.write(f"/* {rel_path} */\n\n")
                            else:
                                temp_file.write(f"# {rel_path}\n\n")

                            # Copiar contenido original
                            try:
                                with open(filepath, 'r', encoding='utf-8') as original_file:
                                    temp_file.write(original_file.read())
                            except UnicodeDecodeError:
                                with open(filepath, 'r', encoding='latin-1') as original_file:
                                    temp_file.write(original_file.read())

                        # Reemplazar archivo original
                        shutil.move(temp_path, filepath)
                        self._log(f"Procesado: {rel_path}")

                    except Exception as e:
                        self._log(f"Error procesando {rel_path}: {str(e)}")
                        os.unlink(temp_path)

            self._log("\n¡Proceso completado!")
            messagebox.showinfo("Éxito", "Proceso completado exitosamente")

        except Exception as e:
            self._log(f"Error general: {str(e)}")
            messagebox.showerror("Error", f"Ocurrió un error durante el proceso: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FilePathAdderGUI(root)
    root.mainloop()