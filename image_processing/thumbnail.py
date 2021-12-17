from io import BytesIO
from PIL import Image

def generate_thumbnail(input_image):
    img = Image.open(input_image)             # PILLOW에서 제공하는 Image 클래스 이용 이미지를 얻어줌
    output = BytesIO()                        # 이미지 프로세싱 결과물을 임시저장해놓을 메모리를 할당
    width, height = img.size                  # 이미지 사이즈를 확인하고 비율을 계산
    ratio = height / width
    pixel = min(250, width)
    img = img.convert('RGB')                  # img.convert & resize -> 원하는 이미지 사이지로 이미지롤 변형
    img.thumbnail((pixel, round(pixel * ratio)))
    img.save(output, format='JPEG', quality=95)  # 이미지를 이전에 만든 메모리 공간에 저장
    # output.seek(0) -> 이미지를 저장하면서 이동한 메모리 포인터를 다시 첫번째 위치로 이동(InMemoryUploadedFile에서 이미지를 읽게 하도록 위함)18
    output.seek(0)
    return output