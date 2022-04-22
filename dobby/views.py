from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from dobby.fu_filter import combine_audio2, filter_srt, total_filter
from dobby.subtitle import combine_audio, subtitle_fps, subtitle_generator

# Create your views here.
def edit(request):
    
    return render(request,"dobby/edit.html")

def loading(request):
    
    return render(request,"dobby/loading.html")


def result(request):

    return render(request,"dobby/result.html")

def fun(request):
    global fontnum
    global font_col_num
    global font_bg_num
    # return render(request,"dobby/fun.html")
    if request.method == "GET":
        return render(request, "dobby/fun.html")
    
    elif 'create' in request.POST:
        txt_pth = "C:/Users/User/Desktop/Big-pj/dobbyedit/dobby/static/subtitle.txt"
        video_pth = "C:/Users/User/Desktop/Big-pj/dobbyedit/dobby/static/media.mp4"
      


        font =  request.POST['font']
        if font == "font1":
            fontnum = 1

        elif font == "font2":
            fontnum = 2

        elif font == "font3":
            fontnum = 3

        fontcolor =  request.POST['fontcolor']
        if fontcolor == "font-color1":
            font_col_num = 1

        elif fontcolor == "font-color2":
            font_col_num = 2

        elif fontcolor == "font-color3":
            font_col_num = 3
            print(3)


        font_bg_num = 0
        bgcolor =  request.POST['bgcolor']
        if bgcolor == "bg-color1":
            font_bg_num = 1

        elif bgcolor == "bg-color2":
            font_bg_num = 2

        elif bgcolor == "bg-color3":
            font_bg_num = 3
        
        subtitle_fps(txt_pth,video_pth)
        subtitle_generator(txt_pth,video_pth,fontnum,font_col_num,font_bg_num)
        combine_audio(video_pth)
    
    elif 'filter' in request.POST:
        txt_pth = "C:/Users/User/Desktop/Big-pj/dobbyedit/dobby/static/result.txt"
        video_pth = "C:/Users/User/Desktop/Big-pj/dobbyedit/dobby/static/media_ssiba.mp4"
        filter_srt(txt_pth,video_pth)
        total_filter(txt_pth,video_pth)
        audio_pth = "C:/Users/User/Desktop/Big-pj/dobbyedit/dobby/static/one_final.mp3"
        combine_audio2(audio_pth,video_pth)

    return render(request, 'dobby/result.html')

def test(request):
    if 'font' in request.POST:
        print(1234)




# def create_sub(reqeust):
#     if 'create' in reqeust.POST:
#         print(12312312312312)
#         txt_pth = "/static/subtitle.txt"
#         video_pth = "/static/media.mp4"
#         subtitle_fps(txt_pth,video_pth)
#         subtitle_generator(txt_pth,video_pth)
        
#     return redirect("/dobby/result/")
   