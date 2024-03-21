README

Jhair Andres Santamaria
Emanuel Bedoya


Este proyecto consiste en un sistema para calcular el impuesto de renta en base a los ingresos y gastos de un contribuyente. El cálculo se realiza de acuerdo con las normativas fiscales vigentes.

Estructura del proyecto
El proyecto consta de tres archivos principales:

declaracion_console.py: Este archivo contiene el código para interactuar con el usuario a través de la consola. El usuario proporciona los datos necesarios, como los ingresos laborales, otros ingresos, retenciones en la fuente, entre otros. Luego, el sistema procesa esta información y calcula el impuesto de renta a pagar por el contribuyente.

logica.py: Este archivo contiene la lógica para calcular el impuesto de renta. Define una función calcular_impuesto_renta que toma los ingresos y gastos del contribuyente como argumentos y devuelve el impuesto de renta calculado. Además, define una excepción personalizada Invalid para manejar casos donde los datos proporcionados no son válidos.

Pruebas.py: Este archivo contiene un conjunto de pruebas unitarias para verificar el correcto funcionamiento de la función calcular_impuesto_renta. Utiliza el módulo unittest para definir casos de prueba que verifican diferentes escenarios de ingresos y gastos.

Ejemplo de uso
Para utilizar este sistema, sigue los siguientes pasos:

Ejecuta el archivo declaracion_console.py en tu entorno de desarrollo o terminal.

Sigue las instrucciones proporcionadas por el programa para ingresar los datos requeridos, como ingresos laborales, otros ingresos, retenciones en la fuente, etc.

Una vez que hayas ingresado todos los datos, el programa calculará automáticamente el impuesto de renta correspondiente y te mostrará el resultado.

Si los datos ingresados son inválidos, el programa mostrará un mensaje de error indicando la naturaleza del problema.

Notas adicionales
Asegúrate de proporcionar datos válidos y precisos para obtener resultados correctos.
Las pruebas unitarias en Pruebas.py son útiles para verificar que la lógica de cálculo del impuesto de renta funcione correctamente en diferentes casos de prueba.
Si encuentras algún problema o tienes alguna pregunta sobre el funcionamiento del sistema, no dudes en contactar al desarrollador.