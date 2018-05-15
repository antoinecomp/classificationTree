import xlrd
import pandas as pd
import numpy as np

# Leer la hoja
df = pd.read_excel("Trees.xlsx")[1:]
df.columns=["A", "B", "C", "D"]

# Separar los números en la columna A a otra columna (E)
df['E'] = df.A.apply(lambda x: x if type(x)==int else "---")
df.A = df.A.apply(lambda x: np.nan if type(x) == int else x)

# Rellenar encabezados de nivel 2, 3, etc. cuando se "resetean"
df.B = np.where(pd.notnull(df.A), "---", df.B)
df.C = np.where(pd.notnull(df.B), "---", df.C)
df.D = np.where(pd.notnull(df.C), "---", df.D)

# Eliminar los NaN de los encabezados
df = df.fillna(method="pad")

# Multi-index
df = df.set_index(['A','B','C','D'])

#df = pd.DataFrame(df,index=['A'])

#print(df.iloc[:5])

#df.columns = df['A']


def obtener_subniveles(df, tupla=None):
	if tupla:
		indice = df.loc[tupla].index
	else:
		indice = df.index
	return indice.get_level_values(0).unique().tolist()

def obtener_dato(df, tupla):
	dato = df.loc[tupla].values
	return dato[0][0]



elegido = tuple() # Inicialmente nada elegido

for opc in range(4):
	opciones = obtener_subniveles(df, elegido)
	print("-"*50)
	print(elegido)  # Mostrar lo que ha elegido de momento en niveles anteriores

	print("Choose one of the following:")

	for i,txt in enumerate(opciones):
		print("{}. {}".format(i, txt))

  	# Añadir elección de este nivel
	eleccion = int(input("Choice: (type -1 to take into account all the options included) "))
	if eleccion == -1:
		searched = df.loc(elegido)
		break
	elegido = elegido + (opciones[eleccion],)


# Mostrando resultado final
print("="*80)
print(elegido)
print(obtener_dato(df, elegido))
#print(df.loc['Division A: Agriculture, Forestry, And Fishing','Agricultural production-crop'])

if elegido[1] == "---":
	# on doit avoir i-1 fois elegido[i] dans le print(df.loc[])
	df_query = df.loc[elegido[0]]
	print("You selected :\n",df.loc[elegido[0]])
elif elegido[2] == "---":
	df_query = df.loc[elegido[0],elegido[1]]
	print("You selected :\n",df.loc[elegido[0],elegido[1]])
elif elegido[3] == "---":
	df_query = df.loc[elegido[0],elegido[1],elegido[2]]
	print("You selected :\n",df.loc[elegido[0],elegido[1],elegido[2]])
else:
	df_query = df.loc[elegido[0],elegido[1],elegido[2],elegido[3]]
	print("You selected :\n", df.loc[elegido[0],elegido[1],elegido[2],elegido[3]])


	
print("∰"*80)
