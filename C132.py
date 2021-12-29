import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_stars.csv")

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()
dist = df["Distance"].to_list()

name.sort()
dist.sort()
mass.sort()
radius.sort()
gravity.sort()

plt.plot(name,mass)
plt.title("Name & Mass of the Star")
plt.xlabel("Star Name")
plt.ylabel("Mass")
plt.show()

plt.plot(name,radius)
plt.title("Name & Radius of the Star")
plt.xlabel("Star Name")
plt.ylabel("Radius")
plt.show()

plt.plot(name,dist)
plt.title("Name & Distance of the Star")
plt.xlabel("Star Name")
plt.ylabel("Distance")
plt.show()

plt.plot(name,gravity)
plt.title("Name & Gravity of the Star")
plt.xlabel("Star Name")
plt.ylabel("Gravity")
plt.show()


