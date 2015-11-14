import numpy, math


def levels(ndarr, partition_count=None):
    flat = ndarr.flatten().data
    flat.sort()  # nlog(n)

    # Calculated using Sturges' rule
    if partition_count is None:
        partition_count = math.log(len(flat), 2) + 1

    std_dev = numpy.std(flat)
    minimum, maximum = flat[0], flat[-1]

    mean = numpy.mean(flat)

    subtracted = flat - mean
    deviated = subtracted / std_dev

    min_val = int(numpy.floor(deviated.min()))
    max_val = int(numpy.ceil(deviated.max()))
    
    deviations = range(min_val, max_val + 1)
    bins = [mean + v * std_dev for v in deviations]

    while len(bins) + 1 < partition_count:
        variance, binned = calculate_variance(bins, flat)
        # A list of the keys of variance, sorted by greatest to least variant
        most_variant = None
        variant_set = None
        for k in variance:
            k_var = variance[k]
            k_vals = flat[binned == k]
            if most_variant is None or len(k_vals) * k_var > variance[most_variant] * len(variant_set):
                variant_set = k_vals
                most_variant = k

        # Get the bin
        binvals = flat[binned == most_variant]
        # Split the bin into two parts
        left, right = numpy.array_split(binvals, 2)
        # Replace the most_variant bin with the median of left and right
        low_med, high_med = numpy.median(left), numpy.median(right)
        bins = bins[:most_variant] + [low_med, high_med] + bins[most_variant + 1:]

    return bins

def calculate_variance(bins, values):
    variance = {}

    # Split up the values into buckets by std_dev
    binned_values = numpy.digitize(values, bins)

    # Calculate intraset variance
    for ind in range(len(bins)):
        vals = values[binned_values == ind]
        if len(vals) > 1:
            variance[ind] = numpy.var(vals)
        else:
            variance[ind] = 0

    return variance, binned_values


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

    outline = vcs.createline(source="default")
    outline.viewport = fa.viewport
    outline.x = x
    outline.y = y
    
    canvas.plot(fa)
    canvas.plot(outline)


if __name__ == "__main__":
    #datafile = cdms2.open(vcs.sample_data + "/tas_mo.nc")
    #var = datafile("tas")
    datafile = cdms2.open(vcs.sample_data + "/clt.nc")
    var = datafile('clt')

    left_tmpl = vcs.createtemplate("left")
    left_tmpl.scale(.5, "x")
    left_tmpl.move(-.02, "x")
    
    right_tmpl = vcs.createtemplate("right", left_tmpl)
    right_tmpl.move(.5, "x")

    canvas = vcs.init()
    canvas.bgX = 1500
    canvas.bgY = 750

    levs = levels(var, partition_count=10)

    stat_iso = vcs.createisofill()
    int_levs = []
    for l in levs:
        int_levs.append(int(l))
    stat_iso.levels = int_levs
    stat_iso.ext_2 = True
    stat_iso.ext_1 = True
    stat_iso.missing = 1
    stat_iso.fillareacolors = vcs.getcolors(stat_iso.levels, split=0)
    
    iso = vcs.createisofill()
    v_min, v_max = vcs.minmax(var[0])
    scale = vcs.mkscale(v_min, v_max)
    iso.levels = scale
    iso.ext_2 = True
    iso.ext_1 = True
    iso.missing = 1
    iso.fillareacolors = vcs.getcolors(iso.levels, split=0)

    flat = var.flatten().data
    stats_variance, stats_binned = calculate_variance(levs, flat)
    auto_variance, auto_binned = calculate_variance(scale, flat)
    stats_counts = []
    auto_counts = []
    for index in range(len(levs)):
        stat_var = stats_variance[index]
        auto_var = auto_variance[index]
        stats_vals = flat[stats_binned == index]
        auto_vals = flat[auto_binned == index]
        
        if auto_var == 0:
            print "No values for auto at level %d" % index
            continue
        if stat_var == 0:
            print "No values for stat at level %d" % index
            continue

        if auto_var > stat_var:
            print "Automatic %d has greater variance" % index
        else:
            print "Stats %d has greater variance" % index

        auto_count, stats_count = auto_vals.size, stats_vals.size
        auto_distance_from_goal = abs(auto_count * 1.0 / flat.size - .1)
        stats_distance_from_goal = abs(stats_count * 1.0 / flat.size - .1)
        if auto_distance_from_goal > stats_distance_from_goal:
            print "Auto %d is further from targeted" % index
        if stats_distance_from_goal > auto_distance_from_goal:
            print "Stats %d is further from targeted" % index

    # Plot one png per time slice
    canvas.plot(var, left_tmpl, stat_iso, bg=1)
    canvas.plot(var, right_tmpl, iso, bg=1)
    canvas.animate.create()
    raw_input("wait")

    for i in range(var.shape[0]):
        print "Drawing", i, "of", var.shape[0]
        canvas.animate.draw_frame(i, render_offscreen=False, allow_static=False)
        canvas.png("anim/%d" % i, width=1500, height=750)
