import os
import threading
import pymysql
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning


def download_img(start, end, fanhaoname):
    for i in range(start, end):
        try:
            fanhao = fanhaoname + '-' + str(i)
            if i < 100:
                fanhao = fanhaoname + '-0' + str(i)
            if i < 10:
                fanhao = fanhaoname + '-00' + str(i)
            res = requests.get('https://www5.javmost.com/' + fanhao + '/', verify=False)
            if '404' in res.text:
                print(fanhao + "->continue")
                continue
            print(fanhao + "存在->下载图片")
            doc = BeautifulSoup(res.text, features='lxml')
            src = doc.select_one('#content div.card.bg-black img').get('src')
            if not src.startswith('http'):
                src = 'https:' + src
            title = doc.select_one('#content div.card.bg-black h5').text
            # 下载图片
            r = requests.get(src, verify=False)
            r.raise_for_status()
            with open(download_dir + fanhao + ".jpg", 'wb') as f:
                f.write(r.content)
            # 插入数据库
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "Yang163110", "tianba")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            print(fanhao + '插入DB')
            sql = 'INSERT INTO javmost(series, `name`, title, img_url, play_url) VALUES ("%s", "%s", "%s", "%s", "%s")' % (
            fanhaoname, fanhao, title, src, 'https://www5.javmost.com/' + fanhao + '/')
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()
            # 关闭数据库连接
            db.close()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    fanhaoname_arr = ['NHDTA', 'IESP', 'IDOL', 'IENE', 'SVND', 'VD', 'HBAD', 'VSPDS', 'VSPDR', 'FSET', 'LADY', 'HUNT', 'GAR', 'SVDVD', 'RCT', 'NGKS', 'RD', 'KUF', 'NSS', 'BDD', 'ARSO', 'SW', 'YMDD', 'TMD', 'DSD', 'RJMD', 'ALD', 'DBE', 'DOJ', 'OFCD', 'SEND', 'ULJM', 'DSS', 'MOED', 'DER', 'OPD', 'GRYD', 'MSBD', 'SS', 'HD', 'DVH', 'REID', 'GEN', 'DBUD', 'IBW', 'MMO', 'MAX', 'XV', 'SRXV', 'UPSM', 'DV', 'SERO', 'MILD', 'RMLD', 'MDS', 'MDB', 'RMDBB', 'RMDS', 'REAL', 'NATR', 'SCOP', 'SAMA', 'MADA', 'ABS', 'ABP', 'JOB', 'EDD', 'MAS', 'PPP', 'YRZ', 'EVO', 'SAD', 'GYD', 'HYK', 'FST', 'TBL', 'LOO', 'TOR', 'TD', 'RBS', 'MAN', 'ZZR', 'WPC', 'BNDV', 'CRS', 'HODV', 'X', 'ADZ', 'AKB', 'HITMA', 'RAY', 'COSQ', 'PPS', 'GRET', 'GATE', 'GEXP', 'GGFH', 'GGTB', 'GMMD', 'GODS', 'GPTM', 'GSAD', 'GXXD', 'GDGA', 'GOMK', 'GTRL', 'GOMD', 'GDSC', 'TBW', 'TBB', 'TDP', 'TDLN', 'TGGP', 'THP', 'THZ', 'TMS', 'GIGA', 'TZZ', 'TRE', 'TSGS', 'TSDL', 'TSWN', 'TSW', 'TTRE', 'TBBH', 'TKHD', 'ATHB', 'AKBD', 'DMG', 'MGJH', 'ANIX', 'CYCD', 'YNO', 'AZGB', 'SKOT', 'SSPD', 'SHP', 'JMSZ', 'JHZD', 'NFDM', 'CGAD', 'CGBD', 'CHSD', 'CUSD', 'CHSH', 'CMV', 'PAED', 'RGI', 'ZARD', 'ZATS', 'ZDAD', 'ZKV', 'SKY', 'RHJ', 'RED', 'CRD', 'SMD', 'SMDV', 'SMBD', 'DBD', 'CWDV', 'CWPBD', 'TRP', 'TRG', 'MKD', 'MX', 'MG', 'MW', 'MUD', 'BD', 'FH', 'KP', 'KS', 'KG', 'YZD', 'GOD', 'YUU', 'EMP', 'PB', 'DRC', 'DRG', 'DSAM', 'EB', 'SMR', 'SP', 'XXX', 'OPC', 'PT', 'AV', 'G', 'SSKJ', 'UTF']
    for fanhaoname in fanhaoname_arr:
        download_dir = 'E://SDDE//javmost//' + fanhaoname + '//'
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        if not os.path.exists(download_dir + "//movie"):
            os.mkdir(download_dir + "//movie")
        if not os.path.exists(download_dir + "//recommand"):
            os.mkdir(download_dir + "//recommand")
        download_img(1, 1000, fanhaoname)

    # ids = ['ONE', 'MXSPS', 'DS', 'MKBD', 'CWP', 'IDBD', 'SUPD', 'IPSD', 'MDED', 'MIRD', 'MIGD', 'MIID',
    #                   'MIAD', 'MIBD', 'MINT', 'MIMK', 'ONED', 'SOE', 'SPS', 'ONSD', 'PGD', 'PBD', 'PJD', 'KAWD', 'KAPD',
    #                   'JUKD', 'JUC', 'JUX', 'ATID', 'RBD', 'MDYD', 'KIRD', 'BLK', 'KISD', 'STAR', 'SACE', 'SDDM',
    #                   'SDDE', 'DVDES', 'NHDTA', 'IESP', 'IDOL', 'IENE', 'IESP', 'IDOL', 'IENE', 'SVND', 'VD', 'HBAD',
    #                   'VSPDS', 'VSPDR', 'FSET', 'LADY', 'HUNT', 'GAR', 'SVDVD', 'RCT', 'NGKS', 'RD', 'KUF', 'NSS',
    #                   'BDD', 'ARSO', 'SW', 'YMDD', 'TMD', 'DSD', 'IDBD', 'RJMD', 'ALD', 'DBE', 'DOJ', 'OFCD', 'SEND',
    #                   'ULJM', 'DSS', 'MOED', 'DER', 'OPD', 'GRYD', 'MSBD', 'SS', 'HBAD', 'HD', 'DVH', 'REID', 'GEN',
    #                   'IENE', 'DOJ', 'DBUD', 'IBW', 'MMO', 'MAX', 'XV', 'SRXV', 'XV', 'UPSM', 'MAX', 'MAX', 'SRXV',
    #                   'XV', 'XV', 'SRXV', 'SRXV', 'XV', 'MAX', 'DV', 'SERO', 'MILD', 'RMLD', 'MDS', 'MDB', 'RMDBB',
    #                   'RMDS', 'REAL', 'NATR', 'SCOP', 'SAMA', 'MADA', 'ABS', 'ABP', 'JOB', 'EDD', 'MAS', 'PPP', 'YRZ',
    #                   'EVO', 'SAD', 'GYD', 'HYK', 'FST', 'TBL', 'LOO', 'TOR', 'TD', 'RBS', 'MAN', 'ZZR', 'WPC', 'BNDV',
    #                   'CRS', 'HODV', 'BNDV', 'X', 'ADZ', 'AKB', 'HITMA', 'RAY', 'RAY', 'COSQ', 'PPS', 'GRET', 'GATE',
    #                   'GEXP', 'GGFH', 'GGTB', 'GMMD', 'GODS', 'GPTM', 'GRET', 'GSAD', 'GXXD', 'GDGA', 'GOMK', 'GTRL',
    #                   'GPTM', 'GXXD', 'GTRL', 'GOMD', 'GEXP', 'GDSC', 'GRET', 'TBW', 'TBB', 'TDP', 'TDLN', 'TGGP',
    #                   'THP', 'THZ', 'TMS', 'TMS', 'TMS', 'TMS', 'TMS', 'TOR', 'GIGA', 'TZZ', 'TRE', 'TSGS', 'TSDL',
    #                   'TSWN', 'TSW', 'TTRE', 'TBBH', 'TKHD', 'TBW', 'ATHB', 'AKBD', 'DMG', 'MGJH', 'ANIX', 'CYCD',
    #                   'YNO', 'AZGB', 'ATID', 'SKOT', 'SSPD', 'SHP', 'JMSZ', 'JHZD', 'NFDM', 'CGAD', 'CGBD', 'CHSD',
    #                   'CYCD', 'CUSD', 'CGBD', 'CHSH', 'CMV', 'MDYD', 'MGJH', 'PAED', 'RGI', 'ZARD', 'ZATS', 'ZDAD',
    #                   'ZKV', 'ZDAD', 'SKY', 'RHJ', 'RED', 'CRD', 'SMD', 'SMDV', 'SMBD', 'DBD', 'CWDV', 'CWPBD', 'DBD',
    #                   'TRP', 'TRG', 'MKD', 'MX', 'MG', 'MW', 'MUD', 'MKD', 'BD', 'BD', 'FH', 'KP', 'KS', 'KG', 'KS',
    #                   'YZD', 'GOD', 'YUU', 'EMP', 'PB', 'DRC', 'DRG', 'DSAM', 'EB', 'SMR', 'SP', 'XXX', 'MKD', 'MKD',
    #                   'OPC', 'PT', 'AV', 'FH', 'G', 'G', 'SSKJ', 'UTF']
    # print(len(ids))
    # news_ids = []
    # for id in ids:
    #     if id not in news_ids:
    #         news_ids.append(id)
    # print(len(news_ids))
    # print(news_ids)

