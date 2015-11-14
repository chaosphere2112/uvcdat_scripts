import vcs, cdms2, os

for fname in os.listdir(vcs.sample_data):
    try:
        f = cdms2.open(vcs.sample_data + "/" + fname)
    except:
        continue
    slices = {}
    for v in f.getVariables():
        if cdms2.isVariable(v):
            try:
                title = v.long_name
            except AttributeError:
                try:
                    title = v.title
                except AttributeError:
                    title = v.id
            axes = v.getAxisList()
            time_len = 0
            for axis in axes:
                if axis.isTime():
                    time_len = len(axis)
            if time_len <= 1:
                continue
            print fname, title, time_len
