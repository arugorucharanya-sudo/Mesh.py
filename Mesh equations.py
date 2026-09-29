 Mesh Analysis of a Two-Mesh Circuit

 Input circuit values
R1 = float(input("Enter R1 (ohm): "))
R2 = float(input("Enter R2 (ohm): "))
R3 = float(input("Enter common resistance R3 (ohm): "))

V1 = float(input("Enter voltage source V1 (V): "))
V2 = float(input("Enter voltage source V2 (V): "))

 Coefficients of mesh equations
a11 = R1 + R3
a12 = -R3

a21 = -R3
a22 = R2 + R3

 Determinant
D = a11 * a22 - a12 * a21

 Calculate mesh currents using Cramer's rule
I1 = (V1 * a22 - a12 * V2) / D
I2 = (a11 * V2 - V1 * a21) / D

 Display results
print("\n--- Mesh Analysis ---")
print("Mesh Current I1 =", round(I1, 4), "A")
print("Mesh Current I2 =", round(I2, 4), "A")

 Current through common resistor
I3 = I1 - I2

print("Current through common resistor R3 =",
      round(I3, 4), "A")
