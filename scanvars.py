import vcs, cdms2, os

for fname in os.listdir(vcs.sample_data):
    try:
        f = cdms2.open(vcs.sample_data + "/" + fname)
    except:
        continue
    print fname
    for v in f.getVariables():
        if cdms2.isVariable(v):
            try:
                title = v.long_name
            except AttributeError:
                try:
                    title = v.title
                except AttributeError:
                    title = v.id
            print "  ", title
        #if raw_input("More info?"):
        #    import ipdb; ipdb.set_trace()
