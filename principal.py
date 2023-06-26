from tkinter import *
from tkinter.messagebox import *
import mariadb

root = Tk()
root.title("Base de datos sobre estudiantes")
root.resizable(0, 0)
root.geometry("500x500")


try:
    conexion = mariadb.connect(
       user="root",
       password="",
       host="127.0.0.1",
       port=3306,
       database="estudiantes"
    )
    cursor = conexion.cursor()
except mariadb.Error as error:
    print(f"Hubo un error al conectarse a la base de datos: {error}")





#FUNCIÓN DE 4TA TABLA DE DATOS

def ventana_añadir_4():

    

#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_COV




    def guardar_datos4():
        try:
            cov_1 = cov_1dos.get()
            lot_1 = lote_1.get()
            cov_2 = cov_2dos.get()
            lot_2 = lote_2.get()
            cov_3 = cov_3dos.get()
            lot_3 = lote_3.get()
            cursor.execute("INSERT INTO dat_cov (dos_uno, lot_uno, dos_dos, lot_dos, dos_tre, lot_tre) VALUES(?, ?, ?, ?, ?, ?)",(cov_1, lot_1, cov_2, lot_2, cov_3, lot_3))
            conexion.commit()
        except mariadb.Error as error_ventana4:
            print(f"Hubo un error en el sexto guardado: {error_ventana4}")




#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_FEC



    def guardar_datos4_1():
        try:
            dia = dia_1.get()
            mes = mes_1.get()
            mes_letra = mes_letra_1.get()
            anio = anio_1.get()
            cursor.execute("INSERT INTO dat_fec (dia_fec, mes_fec, mel_fec, anio_fec) VALUES(?, ?, ?, ?)", (dia, mes, mes_letra, anio))
            conexion.commit()
        except mariadb.Error as error_ventana4_1:
            print(f"Hubo un error el séptimo guardado: {error_ventana4_1}")
        




#FUNCIÓN PARA GUARDAR LOS DATOS Y FINALIZAR LAS HOJAS



    def ventana4_aviso():
        pregunta4 = askokcancel(title="Añadir", message="Desea añadir estos datos?")
        if pregunta4 == 1:
            guardar_datos4()
            guardar_datos4_1()





    añadir_4 = Toplevel()
    añadir_4.title("Añadir un nuevo estudiante")
    añadir_4.resizable(0, 0)
    añadir_4.geometry("1000x600")

    Label(añadir_4, text="Ingrese los datos restantes", font="Calibri 18").grid(row=0, columnspan=5, padx=155, pady=20)

    Label(añadir_4, text="Covid 1 dos.: ", font="calibri 12").grid(row=1, column=0, padx=5, pady=30)
    cov_1dos = Entry(añadir_4)
    cov_1dos.grid(row=1, column=1,padx=3, pady=30)

    Label(añadir_4, text="Lote 1: ", font="calibri 12").grid(row=1, column=2, padx=5, pady=30)
    lote_1 = Entry(añadir_4)
    lote_1.grid(row=1, column=3,padx=3, pady=30)

    Label(añadir_4, text="Covid 2 dos.: ", font="calibri 12").grid(row=1, column=4, padx=5, pady=30)
    cov_2dos = Entry(añadir_4)
    cov_2dos.grid(row=1, column=5,padx=3, pady=30)

    Label(añadir_4, text="Lote 2: ", font="calibri 12").grid(row=1, column=6, padx=5, pady=30)
    lote_2 = Entry(añadir_4)
    lote_2.grid(row=1, column=7,padx=3, pady=30)

    Label(añadir_4, text="Covid 3 dos.: ", font="calibri 12").grid(row=2, column=0, padx=5, pady=30)
    cov_3dos = Entry(añadir_4)
    cov_3dos.grid(row=2, column=1,padx=3, pady=30)

    Label(añadir_4, text="Lote 3: ", font="calibri 12").grid(row=2, column=2, padx=5, pady=30)
    lote_3 = Entry(añadir_4)
    lote_3.grid(row=2, column=3,padx=3, pady=30)

    Label(añadir_4, text="Día: ", font="calibri 12").grid(row=2, column=4, padx=5, pady=30)
    dia_1 = Entry(añadir_4)
    dia_1.grid(row=2, column=5,padx=3, pady=30)

    Label(añadir_4, text="Mes(Número): ", font="calibri 12").grid(row=2, column=6, padx=5, pady=30)
    mes_1 = Entry(añadir_4)
    mes_1.grid(row=2, column=7,padx=3, pady=30)

    Label(añadir_4, text="Mes(Letra): ", font="calibri 12").grid(row=3, column=0, padx=5, pady=30)
    mes_letra_1 = Entry(añadir_4)
    mes_letra_1.grid(row=3, column=1,padx=3, pady=30)

    Label(añadir_4, text="Año: ", font="calibri 12").grid(row=3, column=2, padx=5, pady=30)
    anio_1 = Entry(añadir_4)
    anio_1.grid(row=3, column=3,padx=3, pady=30)


    botones_2 = Frame(añadir_4)
    botones_2.config(width=200, height=900)
    botones_2.grid(row=5, columnspan=8)
    Button(botones_2, text="Volver", bg="Yellow", width=25, height=5, command=añadir_4.destroy).grid(row=0, column=0, padx=60, pady=30)
    Button(botones_2, text="Limpiar campos", bg="red", width=25, height=5).grid(row=0, column=3, padx=60, pady=30)
    Button(botones_2, text="Guardar datos", bg="green", width=25, height=5, command=ventana4_aviso).grid(row=0, column=5, padx=60, pady=30)





#FUNCIÓN DE 3ERA TABLA DE DATOS

def ventana_añadir_3():


    


#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_REP





    def guardar_datos3():
        try:
            ced_re = ced_repre.get()
            ape_rep = ced_repre.get()
            nom_rep = nom_repre.get()
            telf_rep = telf_repre.get()
            dire_rep = dire_repre.get()
            cursor.execute("INSERT INTO dat_rep (ced_rep, ape_rep, nom_rep, tel_rep, dir_rep) VALUES(?, ?, ?, ?, ?)", (ced_re, ape_rep, nom_rep, telf_rep, dire_rep))
            conexion.commit()
        except mariadb.Error as error_ventana3:
            print(f"Hubo un error en el cuarto guardado: {error_ventana3}")



#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_PRO




    def guardar_datos3_1():
        try:
            ced_mad = ced_madre.get()
            ape_mad = ape_madre.get()
            nom_mad = nom_madre.get()
            ced_pad = ced_padre.get()
            ape_pad = ape_padre.get()
            nom_pad = nom_padre.get()
            cursor.execute("INSERT INTO dat_pro (ced_mad, ape_mad, nom_mad, ced_pad, ape_pad, nom_pad) VALUES(?, ?, ?, ?, ?, ?)",(ced_mad, ape_mad, nom_mad, ced_pad, ape_pad, nom_pad))
            conexion.commit()
        except mariadb.Error as error_ventana3_1:
            print(f"Hubo un error en el quinto guardado: {error_ventana3_1}")








#FUNCIÓN PARA GUARDAR LOS DATOS Y PASAR A LA SIGUIENTE HOJA



    def ventana3_aviso():
        pregunta3 = askokcancel(title="Añadir", message="Desea añadir estos datos?")
        if pregunta3 == 1:
            guardar_datos3()
            guardar_datos3_1()
            ventana_añadir_4()





    añadir_3 = Toplevel()
    añadir_3.title("Añadir un nuevo estudiante")
    añadir_3.resizable(0, 0)
    añadir_3.geometry("1000x600")

    Label(añadir_3, text="Ingrese los datos restantes", font="Calibri 18").grid(row=0, columnspan=5, padx=155, pady=20)

    Label(añadir_3, text="Ced. Repre.: ", font="calibri 12").grid(row=1, column=0, padx=5, pady=30)
    ced_repre = Entry(añadir_3)
    ced_repre.grid(row=1, column=1,padx=3, pady=30)

    Label(añadir_3, text="Ape. Repre.: ", font="calibri 12").grid(row=1, column=2, padx=5, pady=30)
    ape_repre = Entry(añadir_3)
    ape_repre.grid(row=1, column=3,padx=3, pady=30)

    Label(añadir_3, text="Nom. Repre.: ", font="calibri 12").grid(row=1, column=4, padx=5, pady=30)
    nom_repre = Entry(añadir_3)
    nom_repre.grid(row=1, column=5,padx=3, pady=30)

    Label(añadir_3, text="Telf. Repre.: ", font="calibri 12").grid(row=1, column=6, padx=5, pady=30)
    telf_repre = Entry(añadir_3)
    telf_repre.grid(row=1, column=7,padx=3, pady=30)

    Label(añadir_3, text="Direc. Repre.: ", font="calibri 12").grid(row=2, column=0, padx=5, pady=30)
    dire_repre = Entry(añadir_3)
    dire_repre.grid(row=2, column=1,padx=3, pady=30)

    Label(añadir_3, text="C.I. Madre: ", font="calibri 12").grid(row=2, column=2, padx=5, pady=30)
    ced_madre = Entry(añadir_3)
    ced_madre.grid(row=2, column=3,padx=3, pady=30)

    Label(añadir_3, text="Ape. Madre: ", font="calibri 12").grid(row=2, column=4, padx=5, pady=30)
    ape_madre = Entry(añadir_3)
    ape_madre.grid(row=2, column=5,padx=3, pady=30)

    Label(añadir_3, text="Nom. Madre: ", font="calibri 12").grid(row=2, column=6, padx=5, pady=30)
    nom_madre = Entry(añadir_3)
    nom_madre.grid(row=2, column=7,padx=3, pady=30)

    Label(añadir_3, text="C.I. Padre: ", font="calibri 12").grid(row=3, column=0, padx=5, pady=30)
    ced_padre = Entry(añadir_3)
    ced_padre.grid(row=3, column=1,padx=3, pady=30)

    Label(añadir_3, text="Ape. Padre: ", font="calibri 12").grid(row=3, column=2, padx=5, pady=30)
    ape_padre = Entry(añadir_3)
    ape_padre.grid(row=3, column=3,padx=3, pady=30)

    Label(añadir_3, text="Nom. Padre: ", font="calibri 12").grid(row=3, column=4, padx=5, pady=30)
    nom_padre = Entry(añadir_3)
    nom_padre.grid(row=3, column=5,padx=3, pady=30)

    botones_2 = Frame(añadir_3)
    botones_2.config(width=200, height=900)
    botones_2.grid(row=5, columnspan=8)
    Button(botones_2, text="Volver", bg="Yellow", width=25, height=5, command=añadir_3.destroy).grid(row=0, column=0, padx=60, pady=30)
    Button(botones_2, text="Limpiar campos", bg="red", width=25, height=5).grid(row=0, column=3, padx=60, pady=30)
    Button(botones_2, text="Campos siguientes", bg="green", width=25, height=5, command=ventana3_aviso).grid(row=0, column=5, padx=60, pady=30)










#FUNCIÓN DE 2DA TABLA DE DATOS

def ventana_añadir_2():




#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_NAC




    def guardar_datos2():
        try:
            lugar_nac = lug_nac.get()
            entidad = enti_fed.get()
            nacionalidad = pais_nac.get()
            condicion = cond_pais.get()
            cursor.execute("INSERT INTO dat_nac (lug_nac, ent_fed, pai_nac, con_pai) VALUES(?, ?, ?, ?)",(lugar_nac, entidad, nacionalidad, condicion))
            conexion.commit()
        except mariadb.Error as error_ventana2:
            print(f"Hubo un error en el segundo guardado: {error_ventana2}")
    





#FUNCIÓN PARA GUARDAR LOS DATOS DE LA TABLA DAT_ACA

    def guardar_datos2_1():
        try:
            nivel = nivel_1.get()
            seccion = seccion_1.get()
            turno = turno_1.get()
            zapato = zapato_1.get()
            camisa = camisa_1.get()
            pantalon = pantalon_1.get()
            docente = docente_1.get()
            cursor.execute("INSERT INTO dat_aca (niv_aca, sec_aca, tur_aca, zap_aca, cam_aca, pan_aca, doc_aca) VALUES(?, ?, ?, ?, ?, ?, ?)", (nivel, seccion, turno, zapato, camisa, pantalon, docente))
            conexion.commit()
        except mariadb.Error as error_ventana2_1:
            print(f"Hubo un error en el tercer guardado: {error_ventana2_1}")




#FUNCIÓN PARA GUARDAR LOS DATOS Y PASAR A LA SIGUIENTE HOJA

    def ventana2_aviso():
        pregunta2 = askokcancel(title="Añadir", message="Desea añadir estos datos?")
        if pregunta2 == 1:
            guardar_datos2()
            guardar_datos2_1()
            ventana_añadir_3()






    añadir_2 = Toplevel()
    añadir_2.title("Añadir un nuevo estudiante")
    añadir_2.resizable(0, 0)
    añadir_2.geometry("1000x600")


    Label(añadir_2, text="Ingrese los datos restantes", font="Calibri 18").grid(row=0, columnspan=5, padx=155, pady=20)

    Label(añadir_2, text="Lugar Nac.: ", font="calibri 12").grid(row=1, column=0, padx=5, pady=30)
    lug_nac = Entry(añadir_2)
    lug_nac.grid(row=1, column=1,padx=3, pady=30)

    Label(añadir_2, text="Entidad Fed.: ", font="calibri 12").grid(row=1, column=2, padx=5, pady=30)
    enti_fed = Entry(añadir_2)
    enti_fed.grid(row=1, column=3,padx=3, pady=30)

    Label(añadir_2, text="País/Nac.: ", font="calibri 12").grid(row=1, column=4, padx=5, pady=30)
    pais_nac = Entry(añadir_2)
    pais_nac.grid(row=1, column=5,padx=3, pady=30)

    Label(añadir_2, text="Cond. País: ", font="calibri 12").grid(row=1, column=6, padx=5, pady=30)
    cond_pais = Entry(añadir_2)
    cond_pais.grid(row=1, column=7,padx=3, pady=30)

    Label(añadir_2, text="Nivel: ", font="calibri 12").grid(row=2, column=0, padx=5, pady=30)
    nivel_1 = Entry(añadir_2)
    nivel_1.grid(row=2, column=1,padx=3, pady=30)

    Label(añadir_2, text="Sección: ", font="calibri 12").grid(row=2, column=2, padx=5, pady=30)
    seccion_1 = Entry(añadir_2)
    seccion_1.grid(row=2, column=3,padx=3, pady=30)

    Label(añadir_2, text="Turno: ", font="calibri 12").grid(row=2, column=4, padx=5, pady=30)
    turno_1 = Entry(añadir_2)
    turno_1.grid(row=2, column=5,padx=3, pady=30)

    Label(añadir_2, text="Zapato: ", font="calibri 12").grid(row=2, column=6, padx=5, pady=30)
    zapato_1 = Entry(añadir_2)
    zapato_1.grid(row=2, column=7,padx=3, pady=30)

    Label(añadir_2, text="Camisa: ", font="calibri 12").grid(row=3, column=0, padx=5, pady=30)
    camisa_1 = Entry(añadir_2)
    camisa_1.grid(row=3, column=1,padx=3, pady=30)

    Label(añadir_2, text="Pantalón: ", font="calibri 12").grid(row=3, column=2, padx=5, pady=30)
    pantalon_1 = Entry(añadir_2)
    pantalon_1.grid(row=3, column=3,padx=3, pady=30)

    Label(añadir_2, text="Docente: ", font="calibri 12").grid(row=3, column=4, padx=5, pady=30)
    docente_1 = Entry(añadir_2)
    docente_1.grid(row=3, column=5,padx=3, pady=30)

    botones_2 = Frame(añadir_2)
    botones_2.config(width=200, height=900)
    botones_2.grid(row=5, columnspan=8)
    Button(botones_2, text="Volver", bg="Yellow", width=25, height=5, command=añadir_2.destroy).grid(row=0, column=0, padx=60, pady=30)
    Button(botones_2, text="Limpiar campos", bg="red", width=25, height=5).grid(row=0, column=3, padx=60, pady=30)
    Button(botones_2, text="Campos siguientes", bg="green", width=25, height=5, command=ventana2_aviso).grid(row=0, column=5, padx=60, pady=30)




#FUNCIÓN DE 1ERA TABLA DE DATOS
def ventana_añadir():

        
#FUNCIÓN PARA GUARDAR LOS DATOS



    def guardar_datos1():
        try:
            cedula = cedula_est.get()
            apellido = apellido_est.get()
            nombre = nombre_est.get()
            nacimiento = nacimiento_est.get()
            edad = edad_est.get()
            sexo = sexo_est.get()
            talla = talla_est.get()
            peso = peso_est.get()
            cursor.execute("INSERT INTO dat_per (ced_est, ape_est, nom_est, nac_est, edad_est, sex_est, tal_est, pes_est) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (cedula, apellido, nombre, nacimiento, edad, sexo, talla, peso))
            conexion.commit()
        except mariadb.Error as error_ventana1:
            print(f"Hubo un error en el primer guardado: {error_ventana1}")



#FUNCIÓN PARA GUARDAR LOS DATOS Y PASAR A LA SIGUIENTE HOJA

    def ventana1_aviso():
        pregunta1 = askokcancel(title="Añadir", message="Desea añadir estos datos?")
        if pregunta1 == 1:
            guardar_datos1()
            ventana_añadir_2()


    añadir = Toplevel()
    añadir.title("Añadir un nuevo estudiante")
    añadir.resizable(0, 0)
    añadir.geometry("740x600")

    


    Label(añadir, text="Ingrese los datos del estudiante nuevo", font="Calibri 18").grid(row=0, columnspan=5, padx=155, pady=20)

    Label(añadir, text="Cédula: ", font="calibri 12").grid(row=1, column=0, padx=5, pady=30)
    cedula_est = Entry(añadir)
    cedula_est.grid(row=1, column=1,padx=3, pady=30)

    Label(añadir, text="Apellidos: ", font="calibri 12").grid(row=1, column=3, padx=5, pady=30)
    apellido_est = Entry(añadir)
    apellido_est.grid(row=1, column=4,padx=3, pady=30)

    Label(añadir, text="Nombres: ", font="calibri 12").grid(row=2, column=0, padx=5, pady=30)
    nombre_est = Entry(añadir)
    nombre_est.grid(row=2, column=1,padx=3, pady=30)

    Label(añadir, text="Fecha Nac.: ", font="calibri 12").grid(row=2, column=3, padx=5, pady=30)
    nacimiento_est = Entry(añadir)
    nacimiento_est.grid(row=2, column=4,padx=3, pady=30)

    Label(añadir, text="Edad: ", font="calibri 12").grid(row=3, column=0, padx=5, pady=30)
    edad_est = Entry(añadir)
    edad_est.grid(row=3, column=1,padx=3, pady=30)

    Label(añadir, text="Sexo: ", font="calibri 12").grid(row=3, column=3, padx=5, pady=30)
    sexo_est = Entry(añadir)
    sexo_est.grid(row=3, column=4,padx=3, pady=30)

    Label(añadir, text="Talla: ", font="calibri 12").grid(row=4, column=0, padx=5, pady=30)
    talla_est = Entry(añadir)
    talla_est.grid(row=4, column=1,padx=3, pady=30)

    Label(añadir, text="Peso: ", font="calibri 12").grid(row=4, column=3, padx=5, pady=30)
    peso_est = Entry(añadir)
    peso_est.grid(row=4, column=4,padx=3, pady=30)

    botones = Frame(añadir)
    botones.config(width=80, height=740)
    botones.grid(row=5, columnspan=5)
    Button(botones, text="Limpiar campos", bg="red", width=20, height=5).grid(row=0, column=0, padx=80, pady=30)
    Button(botones, text="Campos siguientes", bg="green", width=20, height=5, command=ventana1_aviso).grid(row=0, column=3, padx=80, pady=30)

#PRINCIPAL

Label(root, text="Matrícula de estudiantes", font="CALIBRI 20").grid(row=0, columnspan=3, pady=20, padx=110)

boton_añadir = Button(root, text="Nuevo estudiante", bg="green", fg="white", width=15, height=5, command=ventana_añadir)
boton_añadir.grid(row=2, column=0, padx=20, pady=40)

boton_actualizar = Button(root,text="Actualizar información", bg="blue", fg="white", width=15, height=5)
boton_actualizar.grid(row=2, column=2, padx=20, pady=40)

boton_visualizar = Button(root, text="Borrar estudiantes", bg="red", fg="white", width=15, height=5)
boton_visualizar.grid(row=3, column=1)

boton_borrar = Button(root, text="Ver estudiante", bg="pink", fg="black", width=15, height=5)
boton_borrar.grid(row=4, column=0, padx=20, pady=40)

boton_buscar = Button(root, text="Buscar estudiante", bg="yellow", fg="black", width=15, height=5)
boton_buscar.grid(row=4, column=2, padx=20, pady=40)

root.mainloop()