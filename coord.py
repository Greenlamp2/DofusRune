class Coord:
    loc_recherche_box = (570, 800)
    loc_resultat = (570, 215)
    loc_prix = (700, 400, 1090, 440)
    new_loc_prix = (950, 400, 1090, 440)
    #loc_prix = (655, 281, 1090, 440)
    loc_cancel = (606, 801)

    def __init__(self):
        pass

    def get_loc_prix(value=None):
        prix = Coord.new_loc_prix
        #prix = Coord.loc_prix
        a = prix[0]
        b = prix[1]
        c = prix[2]
        d = prix[3]

        aa = (a, b)
        bb = (c, d)

        pa = Coord.process_res(aa)
        pb = Coord.process_res(bb)

        res = (pa[0], pa[1], pb[0], pb[1])
        return res

    def process_res(value):
        pc  = (1680, 1050)
        portable = (1440, 900)
        resolution = portable

        good_value = (int(value[0]/pc[0] * portable[0]), int(value[1]/pc[1] * portable[1]))

        return good_value