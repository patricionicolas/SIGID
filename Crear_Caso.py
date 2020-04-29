### 
import Crea_datos
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time

### Driver a utilizar y pagina web a interactuar
driver = webdriver.Chrome()
driver.get('https://devsigid.iie.cl/mmida/web/')

time.sleep(1)

### Busqueda de elementos en la pagina login
user_box      = driver.find_element_by_id('InputRun')
pass_box      = driver.find_element_by_id('InputPassword')
submit_button = driver.find_element_by_id('login')
time.sleep(1)

### Estando en Login, ingresamos las claves y clickeamos el boton
user_box.send_keys('')
pass_box.send_keys('')
submit_button.click()


### Busqueda de elementos en la pagina home
time.sleep(1)
agregar_caso_button = driver.find_element_by_css_selector('body._body-100:nth-child(2) div.container-fluid:nth-child(1) div._casos-container.h-100 div.row.h-100.pr-2.mr-0.pl-2:nth-child(1) div.col-md-11 div.tab-content div.tab-pane.fade.show.active:nth-child(1) div.row:nth-child(1) div.text-right.pt-3.pb-3.pl-3:nth-child(1) > button.btn._btn-primary')
agregar_caso_button.click()

## Busqueda de elementos en "Agregar nuevo caso"
time.sleep(1)
cedula_box         = driver.find_element_by_id('inputCedula')
buscacedula_button = driver.find_element_by_css_selector('div.container-fluid div._main-container._container-form._max-width:nth-child(2) div.card._card-rounded.pt-5.pb-5.pl-5.pr-5 div._padding-content:nth-child(2) div.row._instrumento-cacsa:nth-child(1) div.col-sm-6:nth-child(1) div.form-group div.input-group div.input-group-append > button.btn.btn-info._button-primary')
nombre_box         = driver.find_element_by_id('inputNombre')
etnia_list         = Select(driver.find_element_by_id('inputEtnia'))
nacionalidad_box   = driver.find_element_by_id('inputNacionalidad')
nacionalidad_list  = driver.find_element_by_id('nacionalidad')
zona_list          = Select(driver.find_element_by_id('inputZona'))
region_list        = Select(driver.find_element_by_id('inputRegion'))
poblacion_box      = driver.find_element_by_id('inputPoblacion')
calle_box          = driver.find_element_by_id('inputDomicilio')
telefono_box       = driver.find_element_by_id('inputContacto') 
nacimiento_box     = driver.find_element_by_id('inputNacimiento')
sexo_f_button      = driver.find_element_by_id('radioSexo1')
sexo_m_button      = driver.find_element_by_id('radioSexo2')

## Interaccion con elementos en "Agregar nuevo caso"
cedula_box.send_keys(Crea_datos.crea_rut())
buscacedula_button.click()

time.sleep(10) #Esperamos que busque el rut

nombre_box.send_keys(Crea_datos.crea_nombre("masculino"))
etnia_list.select_by_index(Crea_datos.crea_etnia())                             #Seleccionamos una etnia al azar
#print "---->",nacionalidad_list.select_by_index(Crea_datos.crea_nacionalidad())               #Seleccionamos una nacionalidad al azar

if Crea_datos.crea_sexo == "masculino":
    sexo_m_button.click()
else:
    sexo_f_button.click()    

zona_list.select_by_index(Crea_datos.crea_zona())

poblacion_box.send_keys(Crea_datos.crea_poblacion())      
calle_box.send_keys(Crea_datos.crea_calle())          
telefono_box.send_keys(Crea_datos.crea_telefono())       
nacimiento_box.send_keys(Crea_datos.crea_nacimiento())
time.sleep(5)

value_region = Crea_datos.crea_region()
print value_region
region_list.select_by_value(value_region)
time.sleep(2)
input()
driver.quit()