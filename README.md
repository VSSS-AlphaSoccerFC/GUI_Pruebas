# Instrucciones

Para correr, ejecuta el `main.py`, puedes cambiar las IPs de los robots desde `config.py`, esto es para el envío de instrucciones (hay una línea comentada).

### Main

Tiene un loop donde corre tkinter y otro donde corre `listener`, este último es un socket que escucha en el puerto especificado lo que le envíe la visión/giroscopio empaquetado con `protobuf`.

Después de recibir el paquete, el estado global (`game_state`) se actualiza con la última información recibida.

### Game

Contiene objetos de tipo _Robot_, _Ball_ y _State_


### Config

Contiene las direcciones IP y puerto de cada robot, estas se usan para enviarles/escuchar información.

