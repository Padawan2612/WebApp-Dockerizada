Para ejecutar el programa se necesta realizar los siguientes pasos

1.-Instalar las librerias de flask que estan en el archivo requirements.txt

pip install -r requirements.txt

2.-Contruimos la imagen

docker build -t imagga-webapp .

3.-Ejecutamos la app dockerizada

docker run -p 5000:5000 imagga-webapp

4.-Ejecutar app.py

python app.py

5.-Ingresamos al host

http://127.0.0.1:5000/