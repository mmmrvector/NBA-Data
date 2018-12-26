
class avg_stat_row:
    def __init__(self, data):
        self.season = data[0]
        self.tm = data[1]
        self.g = data[2]
        self.gs = data[3]
        self.mp = data[4]
        self.fgper = data[5]
        self.fg = data[6]
        self.fga = data[7]
        self.threepper = data[8]
        self.threep = data[9]
        self.threepa = data[10]
        self.ftper = data[11]
        self.ft = data[12]
        self.fta = data[13]
        self.trb = data[14]
        self.orb = data[15]
        self.drb = data[16]
        self.ast = data[17]
        self.stl = data[18]
        self.blk = data[19]
        self.tov = data[20]
        self.pf = data[21]
        self.pts = data[22]
        self.w = data[23]
        self.l = data[24]


'''
球员平均数据
'''
class avg_stat:
    def __init__(self):
        self.data = []

    def append_row(self, stat_row):
        self.data.append(stat_row)

    def append_rows(self, stat_rows):
        for stat_row in stat_rows:
            self.data.append(stat_row)


'''
球员信息
'''
class Player:
    def __init__(self):
        self.name = 'name'
        self.position = 'position'
        self.height = 'height'
        self.weight = 'weight'
        self.date_of_birth = '0000-00-00'
        self.city = 'city'
        self.current_payment = 'no data'
        self.avg_stats = avg_stat()