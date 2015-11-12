import numpy, math


def levels(ndarr):
    flat = ndarr.flatten().data
    flat.sort()  # nlog(n)
    # Calculated using Sturges' rule
    partition_count = math.log(len(flat), 2) + 1
    std_dev = numpy.std(flat)  #
    minimum, maximum = flat[0], flat[-1]
    print std_dev, (maximum - minimum) / partition_count
    mean = numpy.mean(flat)

    subtracted = flat - mean
    deviated = subtracted / std_dev
    positive = deviated[deviated > 0]
    negative = deviated[deviated < 0]
    if len(negative) > 0:
        negative = numpy.floor(negative)
        neg_vals, neg_counts = numpy.unique(negative, return_counts=True)
    else:
        neg_vals = []
        neg_counts = []

    if len(positive) > 0:
        positive = numpy.ceil(positive)
        pos_vals, pos_counts = numpy.unique(positive, return_counts=True)
    else:
        pos_vals, pos_counts = [], []

    print neg_vals, neg_counts
    print pos_vals, pos_counts

    stddev_histo = {}
    for key, count in zip(neg_vals, neg_counts):
        stddev_histo[key] = count
    for key, count in zip(pos_vals, pos_counts):
        stddev_histo[key] = count
    return stddev_histo


import vcs, cdms2


def histogram(canvas, values, xaxis=None, yaxis=None):
    fa = canvas.createfillarea()
    t = canvas.gettemplate("default")
    fa.viewport = [t.data.x1, t.data.x2, t.data.y1, t.data.y2]
    num_fills = len(values)
    fa.color = vcs.getcolors(range(num_fills))
    x, y = [], []
    
    for i in range(num_fills):
        point1, point2 = i / float(num_fills), (i + 1) / float(num_fills)
        xl = [point1, point1, point2, point2]
        yl = [0, values[i], values[i], 0]
        x.append(xl)
        y.append(yl)
    fa.x = x
    fa.y = y

    outline = vcs.createline("outline", "default")
    outline.viewport = fa.viewport
    outline.x = x
    outline.y = y
    
    canvas.plot(fa)
    canvas.plot(outline)



if __name__ == "__main__":
    geos = cdms2.open(vcs.sample_data + "/geos5-sample.nc")
    sphu = geos("sphu")

    cltf = cdms2.open(vcs.sample_data + "/clt.nc")
    clt = cltf("clt")
    """
    histo = levels(sphu)

    total_count = 1.0
    for v in sphu.shape:
        total_count *= v

    xaxis = cdms2.createAxis(sorted(histo.keys()))
    values = [histo[k] / total_count for k in xaxis]
    var = cdms2.createVariable(values)
    var.setAxis(0, xaxis)
    """
    canvas = vcs.init()
    yx = canvas.createyxvsx()
    arr = sphu.flatten().data
    arr.sort()
    canvas.plot(arr, yx)
    canvas.png("sphu_curve")

    #canvas.plot(var)
    
    #histogram(canvas, values)