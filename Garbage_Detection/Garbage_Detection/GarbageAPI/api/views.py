from django.shortcuts import render,HttpResponse
from .models import SImg,DImg
from PIL import Image
from garbage_detection import detect,detection_graph
import random
# Create your views here.

def index(request):
    if request.method == "POST":
        img = request.FILES['image']

        save_img = SImg(img=img)

        save_img.save()

        print(save_img.img.path)



        processed_img = detect(detection_graph,save_img.img.path)
        image = Image.fromarray(processed_img,"RGB")
        img_loc = "C:\\Users\\rohan\\PycharmProjects\\Garbage_Detection\\GarbageAPI\\media\\detect\\"+str(random.randint(1,1000000))+str(img)
        image.save(img_loc)

        print("image_process_done")

        processed = DImg(detect=img_loc)
        processed.save()
        print(img_loc)


        # save_img.save()

        return HttpResponse(img_loc)
    return render(request,'api/index.html')



