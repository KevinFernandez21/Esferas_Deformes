def crear_esfera(arrugada=False, deformada=False):
    theta, phi = crear_terminos()

    if arrugada:
        r = 1 + (1/2) * np.sin(8 * theta) * np.sin(phi)
    elif deformada:
        r = 1 + (1/2) * np.sin(8 * theta) * np.sin(4 * phi)
    else:
        r = 1

    x, y, z = crear_coordenadas_cartesianas(r, theta, phi)

    fig = Figure(figsize=(5, 5))  # Corrección: Agregar el tamaño de la figura (ancho, alto)

    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    return fig

current_canvas = None
current_fig = None

def update_figure(fig, frame):
    global current_canvas, current_fig

    if current_canvas is not None:
        current_canvas.get_tk_widget().destroy()

    # Crear un nuevo lienzo para la figura actual
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, padx=10, pady=10)

    # Actualizar las referencias al lienzo y figura actuales
    current_canvas = canvas
    current_fig = fig

def mostrar_esferas():
    global current_canvas, current_fig

    root = tk.Tk()
    root.title("Visualización de Esferas")

    frame = tk.Frame(root)  # Crear el frame antes de usarlo
    frame.pack(side=tk.TOP, padx=10, pady=10)

    # Crear esferas
    fig1 = crear_esfera()
    fig2 = crear_esfera(arrugada=True)
    fig3 = crear_esfera(deformada=True)

    # Botones para mostrar las figuras
    button1 = tk.Button(frame, text="Esfera Original", command=lambda: update_figure(fig1, frame))
    button1.pack(side=tk.LEFT, padx=10, pady=10)

    button2 = tk.Button(frame, text="Esfera Arrugada", command=lambda: update_figure(fig2, frame))
    button2.pack(side=tk.LEFT, padx=10, pady=10)

    button3 = tk.Button(frame, text="Esfera Deformada", command=lambda: update_figure(fig3, frame))
    button3.pack(side=tk.LEFT, padx=10, pady=10)

    # Mostrar la figura inicial en la ventana
    update_figure(fig1, frame)

    root.mainloop()