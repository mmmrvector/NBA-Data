import re

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
    season      赛季
    tm          球队
    dist        出手距离
    s0_3_       篮下命中率
    s0_3_fg     篮下平均命中次数
    s0_3_fga    篮下平均出手次数
    s0_3        篮下投篮占比
    s3_10_      近距两分命中率
    s3_10_fg    近距两分平均命中次数
    s3_10_fga   近距两分平均出手次数
    s3_10       近距两分投篮占比
    s10_16_     中距两分命中率
    S10_16_fg   中距两分平均命中次数
    S10_16_fga  中距两分平均出手次数
    s10_16      中距两分投篮占比
    s16_3_      远距两分命中率
    s16_3_fg    远距两分平均命中次数
    s16_3_fga   远距两分平均出手次数
    s16_3       远距两分投篮占比
    tsper       真实命中率
    efgper      投篮效率
'''
class avg_shot_stat_row:
    def __init__(self, data):
        self.season = data[0]
        self.tm = data[1]
        self.dist = data[2]
        self.s0_3_ = data[3]
        self.s0_3_fg = data[4]
        self.s0_3_fga = data[5]
        self.s0_3 = data[6]
        self.s3_10_ = data[7]
        self.s3_10_fg = data[8]
        self.s3_10_fga = data[9]
        self.s3_10 = data[10]
        self.s10_16_ = data[11]
        self.s10_16_fg = data[12]
        self.s10_16_fga = data[13]
        self.s10_16 = data[14]
        self.s16_3_ = data[15]
        self.s16_3_fg = data[16]
        self.s16_3_fga = data[17]
        self.s16_3 = data[18]
        self.tsper = data[19]
        self.efgper = data[20]

'''
球员场均数据
'''
class avg_stat:
    def __init__(self):
        #常规赛数据
        self.season_data = []
        #季后赛数据
        self.play_off_data = []
    def append_row(self, stat_row):
        self.season_data.append(stat_row)

    def append_rows(self, stat_rows):
        for stat_row in stat_rows:
            self.season_data.append(stat_row)

    def append_playoff_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.play_off_data.append(stat_row)


'''
球员进阶数据
'''
class advanced_basic:
    def __init__(self):
        #常规赛数据
        self.season_data = []
        #季后赛数据
        self.play_off_data = []
    def append_row(self, stat_row):
        self.season_data.append(stat_row)

    def append_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.season_data.append(stat_row)

    def append_playoff_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.play_off_data.append(stat_row)


'''
球员投篮数据
'''
class advanced_shooting_stat:
    def __init__(self):
        #常规赛数据
        self.season_data = []
        # 季后赛数据
        self.play_off_data = []

    def append_row(self, stat_row):
        self.season_data.append(stat_row)

    def append_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.season_data.append(stat_row)

    def append_playoff_rows(self,stat_rows):
        for stat_row in stat_rows:
            self.play_off_data.append(stat_row)

'''
球员关键时刻数据（最后五分钟数据）(生涯场均）
    g           场次
    fgper       投篮命中率
    fg          命中次数
    fga         出手次数
    threepper   三分命中率
    threep      三分命中次数
    threepa     三分出手次数
    ftper       罚球命中率
    ft          罚球命中次数
    fta         罚球出手次数
    trb         篮板数
    orb         前场篮板数
    drb         后场篮板数
    ast         助攻数
    stl         抢断数
    blk         盖帽数
    tov         失误数
    pf          犯规数
    pts         得分数    
'''
class key_time_stat:
    def __init__(self, data):
        self.g = data[2]
        self.fgper = data[3]
        self.fg = data[4]
        self.fga = data[5]
        self.threepper = data[6]
        self.threep = data[7]
        self.threepa = data[8]
        self.ftper = data[9]
        self.ft = data[10]
        self.fta = data[11]
        self.trb = data[12]
        self.orb = data[13]
        self.drb = data[14]
        self.ast = data[15]
        self.stl = data[16]
        self.blk = data[17]
        self.tov = data[18]
        self.pf = data[19]
        self.pts = data[20]
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
        self.advanced_shooting_stats = advanced_shooting_stat()
        self.key_time_stats = None
