import numpy as nd

C = nd.arange(20,31,1)

K = C + 273.15


print("Celcius/t/tKelvin")

for i in range(len(C)):
    print(f"{C[i]:.2f}/t {K[i]:.2f}")