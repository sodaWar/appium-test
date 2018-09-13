# -* encoding:utf-8 *-
import traceback
import pymysql
import time
import datetime

#自定义的异常，抛出后用来捕获
def myexcept(len):
    if len < 1:
        raise Exception("IDNullError",len)   #

def connDB():
    print ("正在连接服务器....")
    conn = pymysql.connect(     #连接数据库，其实就是建立一个pymysql.connect()的实例对象conn，该对象有commit()、rollback()、cursor（）等属性
        host="34.235.86.20",
        user="sokamgrdev",
        password="sokamgr@Pwd",
        port=3306,
        charset="utf8mb4",
        db="sokadb"
    )
    print ("连接服务器成功")
    cur = conn.cursor()  #通过游标（指针）cursor的方式操作数据库，该代码作用是得到当前指向数据库的指针
    return (conn, cur)

def selectDB(cur, id):
    sql = "select * from article WHERE id = '%d'" % (id)
    joke = cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        print ("查询结束，数据库无数据，请重新输入id")
    else:
        for row in result:
            id = row[0]
            title = row[1]
            content = row[2]
            small_cover = row[3]
            create_time = row[9]
            print ("id:%d,title:%s,content:%s,small_cover:%s,create_time:%s") \
                  % (id, title, content, small_cover, create_time)
            return (joke)

def selectDBAuto(cur,field,table):   #查询数据库，查询条件中需要使用传入的参数
    sql = "select %s from %s" % (field,table)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        print ("查询结束，数据库无数据，请重新输入id")
    else:
        return result

def feedbackAuto(cur):      #用户发送一个feedback后查询出他的uid
    sql1 = "select from_id from message WHERE create_time = " \
          "(select create_time from message order by create_time desc limit 1) and message = 'this is autotest'"
    cur.execute(sql1)
    result1 = cur.fetchall()
    if len(result1) == 0:
        print ("查询结束，数据库无数据,现在进入feedback表开始查询")
        sql2 = "select uid from feedback WHERE create_time = " \
          "(select create_time from feedback order by create_time desc limit 1) and content = 'this is autotest'"
        cur.execute(sql2)
        result2 = cur.fetchall()
        if len(result2) == 0:
            print ('查询结束，该用户无反馈信息提交,请在数据库核对')
        else:
            return result2
    else:
        return result1

def permission(cur,uid):      #用户兑换积分的权限（查询）
    sql = "select * from user_permission WHERE user_id = '%d' and pid = 1" % (uid)
    cur.execute(sql)
    result = cur.fetchall()
    if(len(result)) == 0:
        print ("该用户无积分兑换权限，现增加他的权限，等待3s....")
        return 0
    else:
        return 1

def insert_permission(conn,cur,uid):     #增加用户兑换积分的权限
    sql1 = "select id from user_permission WHERE create_time = " \
           "(select create_time from user_permission order by create_time desc limit 1)"
    cur.execute(sql1)
    result1 = cur.fetchall()[0][0]
    id = result1 + 1

    sql2 = "insert into user_permission VALUE(%d,1,'exchange',%d,0,now(),now()) " % (id,uid)
    result2 = cur.execute(sql2)
    conn.commit()
    return (result2)

def delete_permission(conn, cur, uid):   #删除用户兑换积分权限
    sql = "delete  from user_permission WHERE user_id = '%d'" % (uid)
    result = cur.execute(sql)
    conn.commit()
    return (result)

#这个方法暂时用不到，因为在直接在数据库中更改一条banner的status值时，在android端是看不到更新的banner能够发生改变，原因是前端是调了缓存数据库的接口
# 取了缓存数据库中banner的status值，而不是直接从数据库中取值，所以会出现直接改数据库的值，android端看不到效果，而通过后台操作可以成功，后台操作
#是调了缓存接口的，所以换成直接调接口，而不直接改数据库
def update_banner1(conn,cur,id,order):   #对banner上下线，需要用户输入上下线所对应操作的参数值0或1
    sql1 = "select status from banner WHERE id = '%d'" % (id)
    cur.execute(sql1)
    result = cur.fetchall()    #order为0是将下线banner变为上线，为1是将上线banner变为下线
    result1 = result[0][0]              #该方法需要实现时弹出框，用户来输入order的值实现
    try:
        myexcept(len(result))
    except "IDNullError":
        print ("更新数据ID有误，需重新输入")
    else:
        if result1 == 1 and order == 0:
            sql2 = "update banner set status = 0 WHERE id = '%d'" % (id)
            cur.execute(sql2)
            conn.commit()
            print ("该banner已成功下线")
        elif result1 == 1 and order == 1:
            print ("该banner已下线，如需上线请输入order为0")
        elif result1 == 0 and order == 0:
            print ("该banner已上线，如需下线请输入order为1")
        elif result1 == 0 and order == 1:
            sql3 = "update banner set status = 1 WHERE id = '%d'" % (id)
            cur.execute(sql3)
            conn.commit()
            print ("该banner已成功上线")
        elif result1 == 2:
            print ("该banner已被删除，请选择其他banner")
        else:
            print ("获取的status值已做更改，请在数据库中查看之")
#该方法也暂时用不到
def update_banner(conn,cur,id):    #对banner进行上下线操作，不需要用户传入上下线对应的操作参数
    sql1 = "select status from banner WHERE id = '%d'" % (id)
    cur.execute(sql1)
    result = cur.fetchall()    #order为0是将下线banner变为上线，为1是将上线banner变为下线
    result1 = result[0][0]
    try:
        myexcept(len(result))
    except "IDNullError":
        print ("更新数据ID有误，需重新输入")
    else:
        if result1 == 1:
            sql2 = "update banner set status = 0 WHERE id = '%d'" % (id)
            cur.execute(sql2)
            conn.commit()
            print ("该banner已成功上线")
        elif result1 == 0:
            sql3 = "update banner set status = 1 WHERE id = '%d'" % (id)
            cur.execute(sql3)
            conn.commit()
            print ("该banner已成功下线")
        elif result1 == 2:
            print ("该banner已被删除，请选择其他banner")
        else:
            print ("数据库中该表的status字段值范围已做更改，请在数据库中查看确定")

def show_matchIndex(cur):    #查询主页显示的比赛信息，并返回更新函数所需要的参数
    sql1 = "select * from dictionary WHERE code = 2"
    cur.execute(sql1)
    x = cur.fetchall()
    result1 = int(x[0][2])
    result2 = x[0][3]
    print '主页显示的比赛ID：',
    print result1

    sql2 = "select * from `match` WHERE match_id = '%d'" % (result1)
    cur.execute(sql2)
    y = cur.fetchall()
    a = y[0][3]
    b = y[0][6]
    c = y[0][9]
    d = y[0][20]
    result3 = [a, b, c, d]
    if result2 == 1:
        print '该主页显示的比赛信息如下，请核对之:'
        return result3,1
    elif result2 == 0:
        print '该比赛在主页显示的状态为停用，请核对之:'
        return result3, 0
    else:
        print ("数据库中该表的status字段值范围已做更改，请在数据库中查看确定")

def update_matchIndex(conn,cur,status):     #更新主页显示的比赛状态值，启动比赛的主页显示或停用
    if status == 1:
        sql1 = "update dictionary set status = 0 WHERE code = 2"
        cur.execute(sql1)
        conn.commit()
        print ("该比赛在主页显示已更改为停用状态")
    elif status == 0:
        sql1 = "update dictionary set status = 1 WHERE code = 2"
        cur.execute(sql1)
        conn.commit()
        print ("该比赛在主页显示已更改为启用状态")
    else:
        print ("数据库中该表的status字段值范围已做更改，请在数据库中查看确定")

def update_userSign(conn,cur,uid):                            #更改用户今日签到的时间
    now = datetime.datetime.now()
    a = now.day                                         #今日时间的日数，如11月6日的天数6
    sql1 = "select sign_count,create_time from user_sign WHERE uid = '%d' order by create_time desc" %(uid)
    cur.execute(sql1)
    result = cur.fetchall()
    c = len(result)                 #根据uid查询出用户签到的记录数
    for i in range(c):
        result1 = result[i][0]       #第一条记录的sign_count值
        result2 = result[i][1]       #第一条记录的create_time值，通过循环i值变化，可以得到第二条记录的sign_count和create_time值
        result3 = result[0][1]     #最后一条记录的create_time值
        b = result3.day              #最后一条记录的天数，可用来与今日的天数相比较
        if a == b:                   #相等则说明今日已签到
            date = result2 - datetime.timedelta(days = 1)        #在datetime模块中有一个timedelta这个方法，它代表两个datetime之间的时间差。我们可以使用它来实现
            sql2 = "update user_sign set create_time = '%s' WHERE uid = '%d' and sign_count = '%d'" % (date, uid,c-i)        #可以利用timedelta方法实现日期加上天数的需求
            cur.execute(sql2)         #该sql语句中sign_count的判断条件很重要，这样就能根据每个连续签到的天数判断出不同的签到记录，从而进行不同的更新
            conn.commit()
        else:
            print '今日没有签到'

def delete_userSign(conn,cur,uid):                #删除用户签到记录
    sql = "delete from user_sign WHERE uid = '%d'" %(uid)
    cur.execute(sql)
    conn.commit()

def delete_userFetch(conn,cur,uid):            #删除用户观看视频和文章的记录
    sql = "delete from user_fetch WHERE uid = '%d'" %(uid)
    cur.execute(sql)
    conn.commit()

def select_match(cur):
    now = datetime.datetime.now()                               #获取当前日期
    a = now.strftime('%Y-%m-%d %H:%M:%S')                       #将datetime类型的日期转换成string类型，主要是为了去掉秒数后的小数点位数
    b = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')       #再讲string类型的日期转换成datetime类型，主要是为了能够将日期进行加减操作
    c = b - datetime.timedelta(hours=8)
    print c
    sql1 = "select team_A_name,team_B_name,match_id,status from `match` WHERE start_play > '%s' " \
           "and leg_name = 'EPL' LIMIT 1" %(c)
    cur.execute(sql1)
    result1 = cur.fetchall()                                     #查询出离现在最近的一场且没有开始的比赛
    team_a_name = result1[0][0]
    team_b_name = result1[0][1]
    match_id = result1[0][2]
    status = result1[0][3]
    return team_a_name,team_b_name,match_id,status

def update_match(conn,cur,match_id,status):                     #更改比赛的状态为直播中或未开始
    if status == 2:
        sql2 = "update `match` set status = 1 WHERE match_id = '%d'" %(match_id)
        cur.execute(sql2)
        conn.commit()
    elif status == 1:
        sql2 = "update `match` set status = 2 WHERE match_id = '%d'" %(match_id)
        cur.execute(sql2)
        conn.commit()
    else:
        print '数据库中该表字段值发生变化，请核对之'

def delete_point_record(conn,cur,uid):          #删除用户完成观看比赛任务的记录
    sql = "delete from user_point_record WHERE uid = '%d'" %(uid)
    cur.execute(sql)
    conn.commit()

def deleteDB(conn, cur, id):
    sql = "delete  from article WHERE id = '%d'" % (id)
    joke = cur.execute(sql)
    conn.commit()
    return (joke)

def select_recharge(cur,uid):
    sql = "select status from user_permission WHERE user_id = '%d' and pid = 2"% (uid)
    cur.execute(sql)
    result = cur.fetchall()
    try:
        if len(result) == 0:
            print '该用户没有充值权限'               #用户没有记录的时候会报错
            return 2
        else:
            result1 = result[0][0]
            if result1 == 1:
                print '该用户的充值权限已删除，请更改status值'
                return result1
            elif result1 == 0:
                print  '该用户已拥有充值权限，且正常状态'
                return result1
            else:
                print '数据库中该表的字段值范围发生变化，请去核对之'
    except pymysql.err.OperationalError():
        print '狗日的又服务器炸了，我丢雷老母'

def update_recharge(conn,cur,uid,status):
    if status == 2:
        sql = "INSERT into user_permission(pid,perm_name,user_id,status,create_time,update_time) " \
              "VALUES (2,'recharge','%d',0,now(),now())" % (uid)            #如果用户没有充值权限记录，增加用户权限
        cur.execute(sql)
        conn.commit()
        print '新增用户充值权限成功'
    elif status == 1:
        sql = "update user_permission set status = 0 WHERE user_id = '%d' and pid = 2"% (uid)       #
        cur.execute(sql)                                            #如果用户有充值权限记录，但是权限状态为已删除，更改其状态为正常
        conn.commit()
        print '用户充值权限已更改为正常'
        print ''
    elif status == 0:
        sql = "update user_permission set status = 1 WHERE user_id = '%d' and pid = 2" % (uid)
        cur.execute(sql)                                            #如果用户有充值权限记录且状态正常，更改其状态为已删除
        conn.commit()
        print '用户充值权限更改为已删除'
    else:
        print '传入的status值有问题，请在数据库表中查看是否发生变化'

def delete_subscription(conn,cur,uid):
    sql1 = "select * from user_team_subscription WHERE uid = '%d'"% (uid)
    cur.execute(sql1)
    result = cur.fetchall()
    if len(result) == 0:
        print '用户未关注任何球队'
    else:
        sql2 = "delete from user_team_subscription WHERE uid = '%d'"% (uid)
        cur.execute(sql2)
        conn.commit()

def select_subscribption(cur,uid):                  #查询用户订阅的球队
    sql = "select team_id from user_team_subscription WHERE uid = '%d'"% (uid)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        print '用户未关注任何球队'
        return 0
    else:
        return result

def select_match_subcribption1(cur,teamId):              #这个先留着，现在没有用
    now = datetime.datetime.now()
    a = now.strftime('%Y-%m-%d %H-%M-%S')
    b = datetime.datetime.strptime(a,'%Y-%m-%d %H-%M-%S')
    sql = "select * from `match` WHERE team_A_id = '%d' and start_play > '%s' or team_B_id = '%d' and start_play > '%s'"% (teamId,b,teamId,b)
    try:
        c = cur.execute(sql)
        return c
    except pymysql.err.ProgrammingError:
        print 'sql语句错误，请核对查询的表或者其他字段是否错误'
        traceback.print_exc()

def select_match_subcribption(cur,teamId):              #查询用户订阅球队的比赛
    now = datetime.datetime.now()
    a = now.strftime('%Y-%m-%d %H-%M-%S')
    b = datetime.datetime.strptime(a,'%Y-%m-%d %H-%M-%S')
    sql = "select * from `match` WHERE team_A_id = '%d' and start_play > '%s' or team_B_id = '%d' and start_play > '%s'"% (teamId,b,teamId,b)
    try:
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except pymysql.err.ProgrammingError:
        print 'sql语句错误，请核对查询的表或者其他字段是否错误'
        traceback.print_exc()


def updateDB(conn, cur, name, id):
    sql1 = "select * from tag WHERE id = '%d'" % (id)
    cur.execute(sql1)
    result1 = cur.fetchall()
    try:
        myexcept(len(result1))
    except "IDNullError":
        print ("更新数据ID有误，请重新输入")
    else:
        sql2 = "update tag set name = '%s' WHERE id = '%d'" % (name, id)
        joke = cur.execute(sql2)
        conn.commit()
        return (joke)


def insertDB(conn, cur, sql):
    joke = cur.execute(sql)
    conn.commit()
    return (joke)


def closeDB(conn, cur):
    conn.close()
    cur.close()


def main_1():
    result = True
    conn, cur = connDB()
    print ("请选择以上四个操作：1、查询记录 2、删除记录 3、更新记录 4、增加记录.(按Q退出程序)")
    number = raw_input()
    while (result):
        if (number == 'q' or number == 'Q'):
            print("退出程序中...")
            time.sleep(3)
            break

        elif (int(number) == 1):
            id = input("请输入查询的文章ID：")
            try:
                selectDB(cur, id)
                print ("查询成功")
            except Exception, e:
                traceback.print_exc()
            finally:
                closeDB(conn,cur)

        elif (int(number) == 2):
            id = input("请输入删除的文章ID：")
            try:
                deleteDB(conn, cur, id)
                print("删除成功")
            except pymysql1.err.ProgrammingError as e:
                print ("删除的记录id在数据库中不存在")
            finally:
                closeDB(conn,cur)

        elif (int(number) == 3):
            name = raw_input("请输入更新的tag表名字：")
            id = input("请输入更新的tag表ID:")
            try:
                updateDB(conn, cur, name, id)
                print ("更新成功")
            except Exception as e:
                traceback.print_exc()
            closeDB(conn,cur)

        elif (int(number) == 4):
            sql = raw_input("请输入插入数据的sql语句:")
            try:
                insertDB(conn, cur, sql)
                print ("插入数据成功")
            except Exception as e:
                raise
            finally:
                closeDB(conn,cur)

        else:
            print ("非法输入，将结束进程")
            closeDB(conn, cur)
            print conn.open    #判断数据库连接状态
            break
        print ("请选择以上四个操作：1、查询记录 2、删除记录 3、更新记录 4、增加记录.(按Q退出程序)")
        number = raw_input("请选择操作")


if __name__ == "__main__":
    main_1()
