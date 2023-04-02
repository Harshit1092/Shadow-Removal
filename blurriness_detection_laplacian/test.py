import cv2
import numpy
import json


def fix_image_size(image: numpy.array, expected_pixels: float = 2E6):
    ratio = numpy.sqrt(expected_pixels / (image.shape[0] * image.shape[1]))
    return cv2.resize(image, (0, 0), fx=ratio, fy=ratio)


def estimate_blur(image: numpy.array, threshold: int = 100):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_map = cv2.Laplacian(image, cv2.CV_64F)
    score = numpy.var(blur_map)
    return blur_map, score, bool(score < threshold)


def pretty_blur_map(blur_map: numpy.array, sigma: int = 5, min_abs: float = 0.5):
    abs_image = numpy.abs(blur_map).astype(numpy.float32)
    abs_image[abs_image < min_abs] = min_abs

    abs_image = numpy.log(abs_image)
    cv2.blur(abs_image, (sigma, sigma))
    return cv2.medianBlur(abs_image, sigma)
results = []
images=['test1.png','test2.png','test4.png','test5.png','test6.png','test6.png','test7.png','test8.png']
my_threshold=17
save_path='./results.json'
for image_path in images:
    image = cv2.imread(str(image_path))
    image=fix_image_size(image)
    if image is None:
        print(f'warning! failed to read image from {image_path}; skipping!')
        continue

    print(f'processing {image_path}')

    blur_map, score, blurry = estimate_blur(image, threshold=my_threshold)

    print(f'image_path: {image_path} score: {score} blurry: {blurry}')
    results.append({'input_path': str(image_path), 'score': score, 'blurry': blurry})


    cv2.imshow('input', image)
    cv2.imshow('result', pretty_blur_map(blur_map))

    cv2.waitKey(0)
if save_path is not None:
    print(f'saving json to {save_path}')

    with open(save_path, 'w') as result_file:
        data = {'images':images, 'threshold':my_threshold, 'results': results}
        json.dump(data, result_file, indent=4)
