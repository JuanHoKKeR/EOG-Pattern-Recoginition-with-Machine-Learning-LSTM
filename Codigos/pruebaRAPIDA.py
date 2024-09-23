import numpy as np
import matplotlib.pyplot as plt

# Definir la función periódica
def f(x):
    return 4 * np.sin(x)

# Definir el período y la frecuencia angular
T = 2 * np.pi
omega_0 = 1

# Calcular los coeficientes c_n
def calculate_c_n(n):
    integrand = lambda x: f(x) * np.exp(-1j * n * omega_0 * x)
    return (1 / T) * np.trapz(integrand(np.linspace(0, T, 1000)), dx=T/1000)

# Calcular los primeros N términos de la serie de Fourier
N = 10
coefficients = np.array([calculate_c_n(n) for n in range(-N, N + 1)])

# Graficar la función original y la aproximación con la serie de Fourier
x_values = np.linspace(0, T, 1000)
approximation = np.sum([coefficients[n + N] * np.exp(1j * (n + N) * omega_0 * x_values) for n in range(-N, N + 1)], axis=0).real

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, f(x_values), label='Original Function')
plt.plot(x_values, approximation, label='Fourier Series Approximation')
plt.title('Function and Fourier Series Approximation')
plt.legend()

# Graficar el espectro de frecuencia
frequency_spectrum = np.abs(coefficients)
frequency_values = np.arange(-N, N + 1) / T

plt.subplot(2, 1, 2)
plt.stem(frequency_values, frequency_spectrum, basefmt="b-")
plt.title('Frequency Spectrum')

plt.tight_layout()
plt.show()
