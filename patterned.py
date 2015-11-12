import vcs


def make_shape(x, y, width=.1, height=.1):
    xarr = [[x, x, x + width / 2, x + width / 2, x + width / 4, x + width / 4, x],
            [x + width / 4, x + width / 4, x + width / 2, x + width / 2, x + width / 4],
            [x + width / 2, x + width / 2, x + width * 3 / 4, x + width * 3 / 4, x + width / 2],
            [x + width / 2, x + width / 2, x + width * .75, x + width * .75, x + width, x + width, x + width / 2]]
    yarr = [[y + height / 2, y + height, y + height, y + .75 * height, y + .75 * height, y + .5 * height, y + .5 * height],
            [y + .25 * height, y + .5 * height, y + .5 * height, y + .25 * height, y + .25 * height],
            [y + .5 * height, y + .75 * height, y + .75 * height, y + .5 * height, y + .5 * height],
            [y, y + .25 * height, y + .25 * height, y + .5 * height, y + .5 * height, y, y]]
    return xarr, yarr

fa = vcs.createfillarea()
fa.x, fa.y = make_shape(0, 0, 1., 1.)
canvas = vcs.init()
canvas.plot(fa)
