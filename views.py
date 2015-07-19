#coding=gbk
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
import json
import feature_vector
import dist
import top_k
import re
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_faq(request):
    return render_to_response('faq.html', {})
def get_liscense(request):
    return render_to_response('liscense.html', {})

def get_about(request):
    return render_to_response('about.html', {})

def get_protocol(request):
    return render_to_response('protocol.html', {})

def search_similar_images(request):
    response_dict = {}
    if request.method == 'POST':
        # if 'image' in request.FILES:
        upload_image_path = save_file(request.FILES['upload_image'])
    upload_image_feature_vector = feature_vector.feature_vector_of_image(upload_image_path)
    distances = dist.dists(upload_image_feature_vector, 'D:\\Data\\amazon_dress_feature_vectors.txt')
    k = 20
    top_k_distances = top_k.top_k_dists(distances, k)
    # for image_path, distance in top_k_distances:
    #     clothes_index = image_path.split('\\')[-1].split('_')[0]
    #     clothes_info = 
    
    image_size_file = open('D:\\Data\\amazon_dress_image_size.txt', 'r')
    image_size_dict = json.loads(image_size_file.read())
    image_size_file.close()

    clothes_info_file = open('D:\\clothes_info_1000_utf8.txt', 'r')
    clothes_info = clothes_info_file.read()
    clothes_info_file.close()
    if clothes_info[:3] == codecs.BOM_UTF8:
        clothes_info = clothes_info[3:]

    # clothes_info = clothes_info.encode('gbk')
    # print clothes_info

    similar_image_dict_list = []
    # similar_image_urls = []
    similar_image_url_prefix = "http://202.119.84.68:8000/Images/"
    for image_path, distance in top_k_distances:
        image_dict = {}

        image_name = image_path.split('\\')[-1]
        clothes_index = image_name.split('_')[0]

        similar_image_url = '%s%s' % (similar_image_url_prefix, image_name)
        similar_image_size = image_size_dict[image_name]

        image_dict['download_url'] = similar_image_url
        image_dict['width'] = similar_image_size[0]
        image_dict['height'] = similar_image_size[1]
        info = getClotheInfo(clothes_index, clothes_info)
        # image_dict['shopping_url'] = 'http://item.jd.com/1482711935.html'
        image_dict['shopping_url'] = info[-1]
        # image_dict['other_info'] = 'Uniqlo UT RMB199'
        image_dict['other_info'] = ' '.join(info[:-1])
        # image_dict['shopping_url'] = get_shopping_url(clothes_info, clothes_index)
        # image_dict['other_info'] = get_other_info(clothes_info, clothes_index)

        # print image_dict['shopping_url']
        # print image_dict['other_info']
        # print clothes_index
        similar_image_dict_list.append(image_dict)


        # similar_image_urls.append(similar_image_url)
    # for x in xrange(70,85):
    #     similar_images_url = '%s%d_0.jpg' % (similar_images_url_prefix, x)
    #     similar_images_urls.append(similar_images_url)
    response_dict["status"] = 1
    response_dict["data"] = similar_image_dict_list
    return HttpResponse(json.dumps(response_dict))


def getClotheInfo(id, all_clothes_info):
    regex_expression = r'"id":' + id +r'.*?"brand":"(.*?)".*?"productName":"(.*?)".*?"material":"(.*?)".*?"price":"(.*?)".*?"buyUrl":"(.*?)"'
    pattern = re.compile(regex_expression)
    match = pattern.search(all_clothes_info)
    if match:
        return match.groups()
    else:
        return ("Unknown", "Unknown", "Unknown", "Unknown", "http://item.jd.com/1547204870.html")

if __name__ == '__main__':
    f = open('clothes_info_1000_utf8.txt')
    all_clothes_info = f.read()
    f.close()
    if all_clothes_info[:3] == codecs.BOM_UTF8:
        all_clothes_info = all_clothes_info[3:]

    all_clothes_info = all_clothes_info.encode('gbk')
    print getClotheInfo('1', all_clothes_info)
    print getClotheInfo('20', all_clothes_info)
    print getClotheInfo('39', all_clothes_info)

def get_shopping_url(clothes_info, clothes_index):
    # regExp = r'\{.+\"id\":' + clothes_index + r',.+\"buyUrl\":\"(.+)\"\}'
    regExp = r'\{[^\{\}]+\"id\":' + clothes_index + r',[^\{\}]+\"buyUrl\":\"([^\{\}]+)\"\}'
    # print regExp
    searchObj = re.search(regExp, clothes_info, re.I|re.M)
    return searchObj.groups()[0];

def get_other_info(clothes_info, clothes_index):
    regExp = r'\{[^\{\}]+\"id\":' + clothes_index + r',[^\{\}]+\"brand\":\"([^\{\}\"]+)\"[^\{\}]+\"productName\":\"([^\{\}\"]+)\"[^\{\}]+\"material\":\"([^\{\}\"]+)\"[^\{\}]+\"price\":\"([^\{\}\"]+)\"\}'
    searchObj = re.search(regExp, clothes_info, re.I|re.M)
    other_info_dict = {}
    other_info_dict['brand'] = searchObj.groups()[0]
    other_info_dict['productName'] = searchObj.groups()[1]
    other_info_dict['material'] = searchObj.groups()[2]
    other_info_dict['price'] = searchObj.groups()[3]
    return other_info_dict;

def get_clothes_info(path='D:\\clothes_info.txt'):
    target = open(path, 'r')
    clothes_info_str = target.read()
    target.close()
    clothes_info_dic = json.loads(clothes_info_str)
    return clothes_info_dic

def save_file(file, path=''):
    ''' Little helper to save a file
    ''' 
    filename = file._get_name()
    # fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    print filename

    upload_image_path = 'D:\\UploadImages\\%s' % str(filename)

    fd = open(upload_image_path, 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()

    return upload_image_path
    # assert False

#TODO analyse image_name, get the type of wanted image, and treat them distingushly
def get_similar_image(request, image_name):
    response_dict = {}

    # open image
    # image_path = 'D:\\Images\\' + image_name
    image_path = 'D:\\clothes_1000\\' + image_name
    try:
    	image_data = open(image_path, 'rb').read()
    except Exception, e:
    	# raise e
    	print e
    	response_dict["status"] = 0
    	response_dict["data"] = "open image error"
    	return HttpResponse(json.dumps(response_dict))
    
    # check image type
    # image_type = image_name.split('.')[-1]
    # print image_type
    if image_name.endswith('jpeg') or image_name.endswith('jpg'):
     	return HttpResponse(image_data, content_type="image/jpeg")
    else:
    	return HttpResponse(image_data, content_type="image/png")
    