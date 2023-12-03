# Programa-1-Simular-procesamiento-por-lotes.
1. Introducir desde teclado N procesos, estos serán los que conformen los lotes, la capacidad 
máxima de un lote es de 5, si el número de procesos que se introduce excede esta cantidad, 
se conformará otro lote. Al terminar un lote automáticamente se ejecuta el siguiente lote en 
espera. 
Información a Capturar por proceso: 
o Nombre de Programador 
o Operación a realizar (+, -, *, /, residuo, porcentaje) con sus respectivos datos 
(validar operaciones) 
o Tiempo Máximo Estimado (validar, debe ser mayor a 0) 
o Número de Programa (validar que sea Único, ID) 
2. Los procesos se atenderán en el orden en que se capturaron. 
3. En pantalla deberá mostrarse lo siguiente: 
• Número de lotes pendientes: Con el total de procesos que se capturaron se conformarán 
uno o más lotes, dependiendo del número de procesos. En un principio el primer Lote es 
al que denominaremos Lote en Ejecución, si hay más de un Lote se anotará el número de 
lotes pendientes por ejecutar en este espacio (solo número). 
• Lote en Ejecución: Por cada proceso que conforma el lote en ejecución se listarán los 
siguientes datos antes capturados: 
o Numero de programa (ID).
o Tiempo Máximo Estimado. 
• Proceso en Ejecución: 
o Se deberán mostrar todos los datos del proceso (Nombre, Operación, Tiempo 
Máximo Estimado, Número de Programa) 
o Tiempo transcurrido en ejecución. 
o Tiempo restante por ejecutar. 
• Procesos Terminados: 
o Número de Programa. 
o Operación y datos. 
o Resultado de la operación. 
• Contador Global: Desde que inicia la simulación, se desplegará un reloj global, es decir, 
un contador que lleve el tiempo desde el inicio del programa hasta que termine. 
4. Se depreciarán interrupciones y errores. 
5. Al terminar un Lote automáticamente se continuará con el siguiente lote pendiente, 
actualizándose los datos en pantalla, el número de lotes pendientes disminuye, en el Lote en 
Ejecución ahora se listarán los procesos del lote que se trabaja, y en procesos terminados se 
marcará el fin de un lote y el comienzo del nuevo lote. 
6. El programa terminará cuando todos los procesos de todos los lotes se hayan ejecutado, en 
este punto se pausará el programa para observar. (Pausarlo) 
Para la entrega del programa deberá realizar un video con las especificaciones que se soliciten al 
momento de la explicación, además deberá tener un reporte de este el cual consta de: 
Centro Universitario de Ciencias Exactas e Ingenierías
M. en C. Violeta del Rocío Becerra Velázquez
• Datos personales 
• Datos de la materia
• Número de actividad
• Objetivo de la actividad
• Notas acerca del lenguaje (anote el lenguaje que utilizo y la razón por la que lo eligió) así 
como TDA o estructuras que manejo en el programa, como soluciono y conclusiones. 
