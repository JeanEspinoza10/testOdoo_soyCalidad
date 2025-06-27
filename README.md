# Introducción
Ests repositorio se encuentra la resolución de las diferentes preguntas de la prueba técnica de Odoo en la empresa Soy Calidad.

# Resolución e instalación
Para esta prueba hemos creado 2 módulos para las diferentes preguntas y son:

    1. account_modificated
    2. point_of_sale_modificated

La instalación de los módulos solamente debemos realizar lo siguiente:

    1. Clonar el repositorio en su carpeta donde están sus modulos personalizados.
    2. Posteriormente instalarlo.


## Pregunta :one:
**Agregar al listado de clientes una columna con el campo “Idioma” de contacto (módulo
point_of_sale)**

    La solución se realizo en la carpeta "point_of_sale_modificated/" los siguientes archivos:
    1. point_of_sale_modificated\models\answer_one.py
    2. point_of_sale_modificated\views\answer_one.xml

## Pregunta :two:
**Agregar una validación (alerta) al POS cuando se seleccione un producto con precio S/ 0.0 (módulo point_of_sale)**
    
    Carpetas para la resolución de este ejericios:
    1. point_of_sale_modificated\static\src\js\answer_two.js

## Pregunta :three:
**Crear un módulo que agregue un botón “Boleta” en el PaymentScreen (módulo point_of_sale)**

    Carpetas para la resolución:
    1. point_of_sale_modificated\static\src\js\answer_three.js
    2. point_of_sale_modificated\static\src\xml\answer_three.xml

## Pregunta :four:
**Crear un módulo que agregue un código QR al impreso de la factura por defecto (módulo
account). La imagen correspondiente debe ser un campo en el modelo account.move
El código QR debe estar formado los siguiente campos separados del caracter “|”.
Número factura + “|” + Nombre Cliente + “|” + Fecha Factura + “|” + [TOTAL CANTIDADES
DE LÍNEA] + “|” + Total a pagar**

    Carpetas para la resolución:
    1. account_modificated\views\answer_four.xml
    2. account_modificated\models\answer_four.py

## Pregunta :five:
**Agregar dos campos a la factura (módulo account):
Número de serie y número correlativo. El número de serie se debe formar a partir del campo
“Number” (Ejemplo FV/2019/001)
Número de serie: FV2019
Número correlativo: 00000001**

    Carpetas para la resolución:
    1. account_modificated\models\answer_five.py

## Pregunta :six:
**Agregar un campo Canal de ventas, colocarlo debajo del campo Vendedor. (módulo
account) este campo debe pertenecer a un nuevo modelo cuya data debe ser cargada
cuando se instala el módulo.**

    Carpetas para la resolución:
    1. account_modificated\models\answer_six.py
    2. account_modificated\views\answer_six.xml
    3. account_modificated\security\ir.model.access.csv
    4. account_modificated\data\data_sales_channel.xml

## Pregunta :seven:
**Ocultar el campo Fecha de la factura y reemplazarlo por Fecha de emisión, este nuevo
campo no solo debe tener la fecha sino también la hora. (módulo account)**

    Carpetas para la resolución:
    1. account_modificated\models\answer_seven.py
    2. account_modificated\views\answer_seven.xml

## Pregunta :eight:
**Los cambios solicitados en los puntos 5, 6 y 7 deben también incluirse en el reporte impreso
de la factura. (módulo account)**

    Carpetas para la resolución:
    1. account_modificated\views\answer_eigth.xml

## Pregunta :nine:
**Agregar un campo Many2many en la factura con todos las transferencias (stock.picking)
relacionadas al pedido de venta que originó la factura.**

    Carpetas para la resolución:
    1. account_modificated\models\answer_nine.py

# Deuda Técnica:

    1. Modificar(archivo point_of_sale_modificated\static\src\js\answer_two.js ) la alerta que respondemos cuando seleccionamos un producto con precio "0".

    2. Añadir algunos campos al "@api.depends()" para el cálculo de los nuevos campos del archivo account_modificated\models\answer_five.py
