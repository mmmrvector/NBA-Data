'''
    season      赛季
    tm          队伍
    g           出场次数
    gs          首发
    mp          时间
    fgper       投篮
    fg          命中
    fga         出手
    threepper   三分
    threep      命中
    threepa     出手
    ftper       罚球
    ft          命中
    fta         出回收
    trb         篮板
    orb         前场
    drb         后场
    ast         助攻
    stl         抢断
    blk         盖帽
    tov         失误
    pf          犯规
    pts         得分
    w           胜
    l           负
'''
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
    season      赛季
    tm          球队
    trbper      篮板率
    orbper      进攻板
    drbper      防守板
    astper      助攻率
    stlper      抢断率
    blkper      盖帽率
    tovper      失误率
    usgper      使用率
    ortg        进攻效率
    drtg        防守效率
    ws          WS      win share 胜利贡献值
    ows         进攻WS
    dws         防守WS
    per         PER     效率值
    md          扣篮
'''
class advanced_basic_row:
    def __init__(self, data):
        self.season = data[0]
        self.tm = data[1]
        self.trbper = data[2]
        self.orbper = data[3]
        self.drbper = data[4]
        self.astper = data[5]
        self.stlper = data[6]
        self.blkper = data[7]
        self.tovper = data[8]
        self.usgper = data[9]
        self.ortg = data[10]
        self.drtg = data[11]
        self.ws = data[12]
        self.ows = data[13]
        self.dws = data[14]
        self.per = data[15]
        self.md = data[16]


'''
球员场均数据
'''
class avg_stat:
    def __init__(self):
        #常规赛数据
        self.season_data = []

    def append_row(self, stat_row):
        self.season_data.append(stat_row)

    def append_rows(self, stat_rows):
        for stat_row in stat_rows:
            self.season_data.append(stat_row)


'''
球员进阶数据
'''
class advanced_basic:
    def __init__(self):
        #常规赛数据
        self.season_data = []

    def append_row(self, stat_row):
        self.season_data.append(stat_row)

    def append_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.season_data.append(stat_row)


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
        self.advanced_basic_stats = advanced_basic()