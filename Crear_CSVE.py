### Recursos necesarios
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time, random


###
### Rellenara el formulario de forma aleatorea
###
def relleno_aleatoreo():
    ## q[x]_0 -- q[x]_1 -- q[x]_3 -- q[x]_5 -- q[x]_6 -- q[x]_s1 -- q[x]_s2
    te_ha_pasado_esto = ['ps','pn']
    importancia       = ['ini','iba','ime','ial','ima']
    valor             = ['pos', 'neu', 'neg']
    ultimos_12_meses  = ['us', 'un'] 

    for id in range (1,84):
        print '-----------------------------------------------------> Respondiendo Pregunta ',id
        id_preg = "q" + str(id) + "_"

        ## Crearemos aleatoreo el click de la seccion "Te ha pasado esto"
        te_ha_pasado_esto_select   = te_ha_pasado_esto[random.randint(0,1)] 
        id_te_ha_pasado            = id_preg + te_ha_pasado_esto_select
        radio_button_te_ha_pasado  = driver.find_element_by_id(id_te_ha_pasado)
        radio_button_te_ha_pasado.click()                                           ##Clickeamos el button
        time.sleep(1)

        if te_ha_pasado_esto_select == 'ps':                                               ## Si selecciona la opcion "Si" de deben seleccionar los otros campos
            ## Seleccion de importancia
            importancia_select = importancia[random.randint(0,len(importancia)-1)]
            id_importancia    = id_preg + importancia_select
            importancia_button = driver.find_element_by_id(id_importancia)
            importancia_button.click()

            ## Seleccion de valor 
            valor_select  = valor[random.randint(0,len(valor)-1)]
            id_valor      = id_preg + valor_select
            valor_button  = driver.find_element_by_id(id_valor)
            valor_button.click()

            ## Seleccion de opcion ultimos 12 meses
            valor_ultimos_12_meses  = ultimos_12_meses[random.randint(0,len(ultimos_12_meses)-1)]
            id_ultimos_12_meses     = id_preg + valor_ultimos_12_meses
            ultimos_12_meses_button = driver.find_element_by_id(id_ultimos_12_meses)
            ultimos_12_meses_button.click()


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
time.sleep(3)
guardar_button = driver.find_element_by_xpath('//body//button[2]')   ## Buscamos el boton de guardado
guardar_button.click()                                               ## Clickemos el boton guardar   
driver.quit()                                                        ## Cerramos la libreria driver  
print ("Finalizado")