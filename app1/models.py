from django.db import models


class information(models.Model):
    # 反馈人	   城市	 标题	类型	 提交时间	  内容	 回复时间	  回复部门  回复内容  来源  阅读量
    # QueSub  City	Title  Class  Time	Content	 RepTime  RepDep   RepCon  URL  reading
    QueSub = models.CharField('反馈人', max_length=50, default='匿名用户')
    City = models.CharField('城市', max_length=50)
    Title = models.TextField('标题')
    Class = models.CharField('类型', max_length=50)
    Time = models.DateTimeField('提交时间')
    Content = models.TextField('内容')
    RepTime = models.DateTimeField('回复时间')
    RepDep = models.CharField('回复部门', max_length=50)
    RepCon = models.TextField('回复内容')
    URL = models.CharField('来源', max_length=100)
    reading = models.IntegerField('阅读量', default=0)


class user(models.Model):
    name = models.CharField(verbose_name="账号名", max_length=30)
    password = models.CharField(verbose_name="密码", max_length=30)
    root_choice = (
        (1,"管理员"),
        (2,"普通用户")
    )
    root = models.SmallIntegerField(verbose_name="身份",choices=root_choice)

