# Pokenea

Pokenea es una aplicación Flask que actúa como una Pokédex personalizada. Cada Pokenea tiene información específica como su ID, nombre, altura, habilidad, imagen y una frase filosófica.

## Rutas

- **/**: Página inicial de la pokédex.

- **/pokenea**: Muestra una página HTML con la imagen y la frase filosófica de un Pokenea seleccionado aleatoriamente, junto con el id del contenedor desde el cual se está corriendo la aplicación.

- **/pokenea/< int:id >**: Muestra una página HTML con la imagen y la frase filosófica de un Pokenea seleccionado en la pantalla, junto con el id del contenedor desde el cual se está corriendo la aplicación.

- **/api**: Devuelve un JSON con el id, nombre, altura, y habilidad de todos los Pokenea, junto con el id del contenedor desde el cual se está corriendo la aplicación.

- **/api/pokenea**: Devuelve un JSON con el id, nombre, altura, y habilidad de un Pokenea seleccionado aleatoriamente, junto con el id del contenedor desde el cual se está corriendo la aplicación.