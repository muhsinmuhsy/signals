from django.http import HttpResponse

def index(request):
    head = 'helloworld'
    dic = {
        'name': 'muhsy',
    }
    
    # Convert the dictionary to a string representation
    dic_str = ', '.join([f"{key}: {value}" for key, value in dic.items()])
    
    # Concatenate the head and dictionary string
    response = f"{head}, {dic_str}"
    
    return HttpResponse(response)
