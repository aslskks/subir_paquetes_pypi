el archivo de python se debe llamar __init__.py  
tambien necesitas un setup.py ejemplo setup.py  
despues crea una cuenta en https://pypi.org/  
sigue todos los pasos  
despues crea un api key de tu usuario cualquier nombre solo que pueda manegar todos los paqutes  
para poder usar lo siguente  
ejecuta en windows :  
~~~bash  
pip install wheel  
python setup.py sdist bdist_wheel  
~~~  
en linux y mac:  
~~~bash  
python3 setup.py sdist bdist_wheel  
~~~  
instala twine  
~~~bash
pip install twine  
~~~  
y sube
~~~bash
twine upload dist/*  
username: __token__  
pasword: tu token
~~~
espera a que se suba y listo  
