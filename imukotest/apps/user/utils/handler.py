from rest_framework.views import exception_handler

# Este método sobreescribe el exception_handler que viene por defecto en rest_framework
# captura la información de los errores y los muestra en el response en caso de haber uno.

# este método puede escribirse de manera individual en cada view, pero este funciona de 
# manera global, actuando como un middleware ya que esta definido en el settings.

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)
 
    if response is not None:
        data = response.data
        response.data = {}
        errors = []
        for field, value in data.items():
            errors.append("{} : {}".format(field, "".join(value)))

        response.data['errors'] = errors
        response.data['status'] = response.status_code
 
        response.data['exception'] = str(exc)
        response.data['hint'] = "take a break, drink a beer and come back"
 
    return response