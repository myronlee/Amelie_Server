import os
import image
import feature_vector
import json
import datetime
import save_data

def get_imlist(path):
    """ Returns a list of filenames for all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def dist_between_feature_vector(feature_vector_a, feature_vector_b):
	dist = 0
	for feature_x, feature_y in zip(feature_vector_a, feature_vector_b):
		dist = dist + (feature_x-feature_y)**2
	return dist

def dists(example_image_feature_vector, compare_feature_vectors_file_path):

    target = open(compare_feature_vectors_file_path, 'r')
    feature_vectors_str = target.read()
    target.close()

    feature_vectors_dic = json.loads(feature_vectors_str)

    dists = []

    for image_feature_vector in feature_vectors_dic.values():
        dist = dist_between_feature_vector(example_image_feature_vector, image_feature_vector)
        dists.append(dist)

    return zip(feature_vectors_dic.keys(), dists)

def calculate_and_save_dists(example_image_path):
    start_time = datetime.datetime.now()

    target = open('D:\\feature_vectors.txt', 'r')
    feature_vectors_str = target.read()
    target.close()

    end_time = datetime.datetime.now()
    use_time = end_time - start_time
    print str(use_time.seconds+use_time.microseconds/1000000.0)

    feature_vectors_dic = json.loads(feature_vectors_str)
    example_image_feature_vector = feature_vectors_dic[example_image_path]

    dists = []

    start_time = datetime.datetime.now()

    for image_feature_vector in feature_vectors_dic.values():
        dist = dist_between_feature_vector(example_image_feature_vector, image_feature_vector)
        dists.append(dist)

    end_time = datetime.datetime.now()
    use_time = end_time - start_time
    print str(use_time.seconds+use_time.microseconds/1000000.0)

    start_time = datetime.datetime.now()

    examplae_image_name = example_image_path[14:-4]
    save_data.save_data('D:\\dists\\dists_of_'+examplae_image_name+'.txt', feature_vectors_dic.keys(), dists)
    # examplae_image_name [18:-4]

    end_time = datetime.datetime.now()
    use_time = end_time - start_time
    print str(use_time.seconds+use_time.microseconds/1000000.0)

	# images = []
	# for name, dist in zip(image_paths, dists):
	# 	print name, dist
	# 	images.append(image.Image(name, dist))

	# return images

# def get_dists(example_image_path, image_set_folder):
# 	image_paths = get_imlist(image_set_folder)
# 	image_feature_vectors = []
# 	dists = []

# 	example_image_feature_vector = feature_vector.feature_vector_of_image(example_image_path)

# 	# for i, image_path in enumerate(image_paths):
# 	for image_path in image_paths:

# 		image_feature_vector = feature_vector.feature_vector_of_image(image_path)
# 		image_feature_vectors.append(image_feature_vector)

# 		dist = dist_between_feature_vector(example_image_feature_vector, image_feature_vector)
# 		dists.append(dist)	
# 	images = []
# 	for name, dist in zip(image_paths, dists):
# 		print name, dist
# 		images.append(image.Image(name, dist))

# 	return images

