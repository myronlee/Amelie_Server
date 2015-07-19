import heapq
# from heapq_showtree import show_tree
from image import Image

# top-k
def top_k_dists(dists, k):
    images = []
    for path, dist in dists:
        images.append(Image(path, dist))
    
    # heap = images[:k]
    # heapq.heapify(heap)

    # for i in xrange(k, len(images)):

    #     # if the dist is small than the current biggest dist, replace the biggest dist with this one
    #     if images[i].dist < heap[0].dist:
    #         biggest = heapq.heapreplace(heap, images[i])

    # top_k_images = sorted(heap, key=lambda x:x.dist)
    top_k_images = heapq.nsmallest(k, images, key=lambda x:x.dist)

    top_k_distances = []
    for image in top_k_images:
        top_k_distances.append((image.name, image.dist))

    return top_k_distances

# top-k
def top_k(data, k):
    heap = data[:k]
    # print 'random :'
    # show_tree(heap)
    heapq.heapify(heap)
    # print 'heapified :'
    # show_tree(heap)

    for i in xrange(k, len(data)):

        # if the dist is small than the current biggest dist, replace the biggest dist with this one
        if data[i].dist < heap[0].dist:
            biggest = heapq.heapreplace(heap, data[i])
            # print 'replace %s with %s' % (biggest, data[i])
        # else :
            # print 'abondom :', data[i]
        # show_tree(heap)
    # for i, n in enumerate(heap):
    #   print n
    # print 'k smallest: '
    result = sorted(heap, key=lambda x:x.dist)
    # for i, n in enumerate(result):
    #     print n
    return result
        


# data = [Image('a', 5), Image('b', 4), Image('c', 0), Image('d', 2), Image('e', 9), Image('e', 3), Image('e', 1), Image('e', 19), Image('e', 109), Image('e', 58)]
# heap = 
# print 'random :', data

# for n in data:
#     # print 'add %3d:' % n
#     print n
#     heapq.heappush(heap, n)
    # show_tree(heap)


        

# swap value of different places in list
# def swap(l, i, j):
#   tmp  = l[i]
#   l[i] = l[j]
#   l[j] = tmp

# initialize heap, max heap in this case
# def init_heap(heap):

#   # important !!!
#   start = len(heap)/2 - 1

#   # adjust the heap, from the half to the root
#   for i in xrange(start, -1, -1):
#       big_child_index = 2*i+1
#       if 2*i+2 < len(heap) and heap[2*i+2] > heap[2*i+1]:
#           big_child_index = 2*i+2
#       if heap[big_child_index] > heap[i]:
#           swap(heap, big_child_index, i)




