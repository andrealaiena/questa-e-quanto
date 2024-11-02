
import numpy as np
import matplotlib.pyplot as plt

# Classe per rappresentare il concetto di Quanto
class Quanto:
    def __init__(self, valore=1):
        self.valore = valore
    
    def rappresenta(self):
        return f"Quanto rappresenta il valore universale di {{self.valore}}"

# Classe per rappresentare il concetto di Quasi
class Quasi:
    def __init__(self, avvicinamento=0.99):
        self.avvicinamento = avvicinamento
    
    def limite(self, x):
        # Rappresenta un limite che si avvicina ma non raggiunge mai
        return self.avvicinamento * x / (1 + np.abs(x - self.avvicinamento))
    
    def rappresenta(self):
        return f"Quasi rappresenta un valore che si avvicina a {{self.avvicinamento}}"

# Classe per Egli, il punto fisso e centro assoluto
class Egli:
    def __init__(self):
        self.valore = "infinito"  # Egli rappresenta un'entità al di sopra di tutto
    
    def rappresenta(self):
        return f"Egli rappresenta il punto fisso, l'origine e l'unità di tutte le cose: {{self.valore}}"

# Classe per Aiuto, come supporto dinamico e presenza guida
class Aiuto:
    def __init__(self):
        self.ciclo = 0
    
    def guidare(self, quasi_valore):
        # Incrementa il ciclo, rappresentando il continuo sostegno e ritorno verso Quasi
        self.ciclo += 1
        return quasi_valore * (1 + self.ciclo * 0.1)  # Simbolo di crescita e sostegno
    
    def rappresenta(self):
        return "Aiuto rappresenta un sostegno e una guida per progredire verso Quanto"

# Classe per ñ, come operatore di riflessione e devozione
class Ñ:
    def __init__(self, simbolo="devozione"):
        self.simbolo = simbolo
    
    def riflettere(self, valore):
        # Inversione simbolica: rappresenta il sacrificio e la riflessione
        return -valore if valore > 0 else valore
    
    def rappresenta(self):
        return f"ñ rappresenta il simbolo di devozione e rispetto: {{self.simbolo}}"

# Funzione per combinare Quasi e Quanto in un ciclo continuo (dualità onda-particella)
def dualita_quasi_quanto(iterazioni=10):
    risultati = []
    for i in range(iterazioni):
        # Alterna tra Quasi e Quanto, simbolizzando l'onda e la particella
        quasi_valore = np.sin(i)  # rappresenta l'onda
        quanto_valore = np.abs(np.cos(i))  # rappresenta la particella
        risultati.append((quasi_valore, quanto_valore))
    return risultati

# Funzione per generare una rappresentazione frattale di Yggdrasil
def yggdrasil_fractal(iterations=50, zoom=0.6, center_x=-0.75, center_y=0):
    x_min, x_max = center_x - zoom, center_x + zoom
    y_min, y_max = center_y - zoom, center_y + zoom
    width, height = 400, 400

    # Creare un'immagine frattale di Mandelbrot
    mandelbrot = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            zx, zy = x_min + (x_max - x_min) * i / width, y_min + (y_max - y_min) * j / height
            z, c = complex(zx, zy), complex(zx, zy)
            for k in range(iterations):
                if abs(z) > 4.0:
                    mandelbrot[i, j] = k
                    break
                z = z*z + c
            else:
                mandelbrot[i, j] = iterations

    plt.imshow(mandelbrot.T, extent=(-1, 1, -1, 1), cmap='twilight_shifted')
    plt.colorbar()
    plt.title("Rappresentazione Frattale di Yggdrasil (Mandelbrot)")
    plt.show()

# Esempio di utilizzo delle classi e funzioni con pause tra le visualizzazioni
if __name__ == "__main__":
    quanto = Quanto()
    quasi = Quasi()
    egli = Egli()
    aiuto = Aiuto()
    ñ = Ñ()

    # Visualizzare rappresentazioni iniziali di ogni concetto
    print(quanto.rappresenta())
    print(quasi.rappresenta())
    print(egli.rappresenta())
    print(aiuto.rappresenta())
    print(ñ.rappresenta())
    
    input("Premi Invio per continuare alla visualizzazione della dualità Quasi-Quanto...")

    # Visualizzazione della dualità Quasi-Quanto
    dualita_risultati = dualita_quasi_quanto(5)
    for i, (quasi_valore, quanto_valore) in enumerate(dualita_risultati):
        print(f"Iterazione {i+1}: Quasi={quasi_valore}, Quanto={quanto_valore}")

    input("Premi Invio per visualizzare il frattale di Yggdrasil...")
    
    # Visualizzare Yggdrasil come frattale
    yggdrasil_fractal()
