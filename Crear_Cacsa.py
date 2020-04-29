### Recursos necesarios
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time, random


###
### Rellenara el formulario de forma aleatorea
###
def relleno_aleatoreo():
    ## q[x]_0 -- q[x]_1 -- q[x]_3 -- q[x]_5 -- q[x]_6 -- q[x]_s1 -- q[x]_s2
    op        = [0,1,3,5,6]                                                #Sera util para llenar los radio button
    
    for id in range (1,75):
        print '-----------------------------------------------------> Respondiendo Pregunta ',id
        op_select = op[random.randint(0,len(op)-1)]                          ## Opcion de radio button a seleccionar

        if id <10: id = str(0)+str(id)                                       ## El id de cada pregunta es de dos numeros

        variable     = "q" +str(id)+ "_" + str(op_select)                    ## Armamos el id de cada boton ej:  q13_3  
        radio_button = driver.find_element_by_id(variable)                   ## Seleccionamos el boton
 
        if op_select != 0:                                                       ## Si la seleccion es distinta de cero se debe seleccionar la segunda opcion 
            variable2          = "q" +str(id)+ "_s" + str(random.randint(1,2))   ## Creamos la id de las dos opciones 
            radio_button_si_no = driver.find_element_by_id(variable2)            ## Seleccionamos el boton 

        radio_button.click()    ## Clickeamos el boton

        if op_select != 0: radio_button_si_no.click()                            ## Si la seleccion es distinta de cero, clickeamos el boton
        time.sleep(1)                                                            ## Esperamos un segundo por pregunta   


### Driver a utilizar y pagina web a interactuar
driver = webdriver.Chrome()
driver.get('https://devsigid.iie.cl/mmida/web/')

RUT = ''
RUC = ''

### Deteccion de elementos pagina inicio
acceso_adolescente_button = driver.find_element_by_xpath("//button[@class='btn _btn-volver text-white btn-sm']")
acceso_adolescente_button.click()

time.sleep(4)
adolescente_run_box         = driver.find_element_by_id('InputRun')
adolescente_ruc_box         = driver.find_element_by_id('InputRuc')
adolescente_ingresar_button = driver.find_element_by_xpath("//button[@type='button']")

adolescente_run_box.send_keys(RUT)
adolescente_ruc_box.send_keys(RUC)
adolescente_ingresar_button.click()

time.sleep(4)

########## En este punto ya estamos en el instrumento
relleno_aleatoreo()


print ("Esperando 8 segundos")
time.sleep(12)
guardar_button = driver.find_element_by_xpath('//body//button[2]')   ## Buscamos el boton de guardado
guardar_button.click()                                               ## Clickemos el boton guardar   
driver.quit()                                                        ## Cerramos la libreria driver  
print ("Finalizado")