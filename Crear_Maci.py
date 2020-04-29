### Recursos necesarios
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time, random


###
### Rellenara el formulario de forma aleatorea
###
def relleno_aleatoreo():
    op        = ['v','f']                                                #Sera util para llenar los radio button
    
    for id in range (1,161):
        print '-----------------------------------------------------> Respondiendo Pregunta ',id
        op_select           = op[random.randint(0,1)]                          ## Opcion de radio button a seleccionar 
        id_radio_button     = 'q' + str(id) + '_' + op_select
        radio_button_select = driver.find_element_by_id(id_radio_button)
        radio_button_select.click()  
        time.sleep(0.8)

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
time.sleep(20)
guardar_button = driver.find_element_by_xpath('//body//button[2]')   ## Buscamos el boton de guardado
guardar_button.click()                                               ## Clickemos el boton guardar   
driver.quit()                                                        ## Cerramos la libreria driver  
print ("Finalizado")