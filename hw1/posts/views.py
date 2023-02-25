from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek TEST</title>
    #         </head>
    #         <body>
    #
    #             <h1>Заголовок первого уровня</h1>
    #             <p>Параграф</p>
    #
    #         </body>
    #     </html>
    # """
    headers = {"name": "Alex", }
    # "Content-Type": "application/vnd.ms-excel",
    # "Content-Disposition": "attachment; filename=file.xls"}
    return HttpResponse(body, headers=headers, status=500)

def get_index(request):
    # print(request.user)
    if request.method == "GET":
        return HttpResponse("Главная страница")
    else:
        return HttpResponse("Не тот метод запроса")