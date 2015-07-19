from PIL import Image
from numpy import *
import colorsys
#import pygal
#from pygal.style import LightStyle
import save_data
import dist
import datetime
from PIL import ImageFile



def feature_vector_of_image(image_path):

    # if img and img.meta_type == 'Image':
    #     pilImg = PIL.Image.open(StringIO(str(img.data)) )
    # elif imgData:
    #     pilImg = PIL.Image.open(StringIO(imgData) 

    try:
        img = Image.open(image_path)
    except Exception, exception:
        print exception
        return []
    except IOError, error:
        print error
        return []
    # img = Image.open('D:\\98_1.jpg')
    # !!! maybe, index out range
    # hl, sl, vl = [0]*18, [0]*3, [0]*3
    hl, sl, vl = [0]*19, [0]*4, [0]*4
    try:
        # img.load()
        # maybe RGBA, but we only need RGB, avoid too many value unpack exception
        img_split_list = img.split()
        r_object, g_object, b_object = img_split_list[0], img_split_list[1], img_split_list[2]
    # except Exception, e:
    #     print e
    #     return []
    except IOError:
        # print error
        return []
        
    for r, g, b in zip(r_object.getdata(), g_object.getdata(), b_object.getdata()):
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        h = h*360
        hi, si, vi = int(h/20), int(s*3), int(v*3)
        hl[hi], sl[si], vl[vi] = hl[hi] + 1, sl[si] + 1, vl[vi] + 1
    
    # normalize
    width, height = img.size[0], img.size[1]
    pixel_num = float(width * height)
    for i in xrange(0,19):
        hl[i] = hl[i]/pixel_num
    for i in xrange(0,4):
        sl[i], vl[i] = sl[i]/pixel_num, vl[i]/pixel_num
    
    hsvl = hl + sl + vl
    return hsvl
    # print hsvl
    # bar_chart = pygal.Bar(style=LightStyle)
    # bar_chart.title = ' '
    # bar_chart.x_labels = map(str, range(0, 26))
    # bar_chart.add(' ', hsvl)
    # bar_chart.render_in_browser()
    # im = array(Image.open('D:\\test.jpg'))
    # width, height = im.shape[0], im.shape[1]
    # print width, height
    # for i in xrange(0,width):
    #   for j in xrange(0,height):
    #       hsv_tuple = colorsys.rgb
    


def calculate_and_save_feature_vectors(filename, image_set_folder):
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    image_paths = dist.get_imlist(image_set_folder)
    image_feature_vectors = []
    start_time = datetime.datetime.now()
    # count = 0
    for image_path in image_paths:
        image_feature_vector = feature_vector_of_image(image_path)
        image_feature_vectors.append(image_feature_vector)
        # count = count + 1
        print image_path
    end_time = datetime.datetime.now()
    use_time = end_time - start_time
    print str(use_time.seconds+use_time.microseconds/1000000.0)
    save_data.save_data(filename, image_paths, image_feature_vectors)
    return image_feature_vectors