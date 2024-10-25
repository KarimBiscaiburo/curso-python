# Entorno virtual

Estos sirven para aislar las dependencias que agreguemos a un proyecto y no generar posibles conflictos si los instalamos globalmente en nuestro sistema

* Para hacerlo debemos hacer lo siguiente:

1. Ejecutar este comando en la raiz del proyecto: "python -m venv [nombre carpeta]" (Por lo general terminan en _env para diferenciarlos)
2. Activar el entorno virtual: [nombre carpeta]\Scripts\activate
3. Instalar las dependencias

>![WARNING]
> Puede ser que dependiendo de como tengas configurada la seguridad en tu sistema tengas un error como el siguiente:
> ![error](error.png)
> para solucionarlo basta con ejecutar Powershell como administrador y correr el siguiente comando "Set-ExecutionPolicy RemoteSigned", luego por seguridad podrias volver a la configuración de restricción "Set-ExecutionPolicy Restricted"