from django.contrib import admin
from django.urls import path
from app1 import views
from django.views.generic import RedirectView


urlpatterns = [
    # 在urls.py文件中定义一个重定向的URL模式，
    # 将默认的URL模式重定向到login页面。
    path('', RedirectView.as_view(url='/login/')),
    # 默认情况下，Django提供了一个基本的后台管理页面，
    # 允许管理数据库中的数据、添加、修改和删除对象等操作。
    path('admin/', admin.site.urls),
    # 登录
    path('login/', views.login),
    # 注册
    path('register/',views.register),
    # 管理员登陆成功后进入主页
    path('admin_show/', views.admin_show),
    # 用户登陆成功后进入主页
    path('user_show/', views.user_show),
    # 管理员逐条添加数据
    path('admin_add/', views.admin_add),
    # 管理员批量上传数据
    path('admin_upload/', views.admin_upload),
    # 后台将批量上传的数据进行处理
    path('admin_multi/', views.admin_multi),
    # 上传失败报错并重新上传或上传成功继续上传
    path('admin_multi/admin_upload', views.admin_upload),
    # 上传成功返回主页
    path('admin_multi/admin_show', views.admin_show),
    # 管理员对某条数据进行编辑
    path('admin_edit/<int:id>/', views.admin_edit),
    # 管理员对某条数据进行删除
    path('admin_delete/<int:id>/', views.admin_delete),
    # 查看信息可视化大屏
    path('user_display/', views.user_display),
    # 查看信息分析图表
    path('user_charts/', views.user_charts),
    # 管理员对用户以及其他管理员信息进行管理
    path('admin_list/', views.admin_list),
    # 管理员添加其他用户或管理员
    path('admin_add_user/', views.admin_add_user),
    # 管理员编辑用户或管理员信息
    path('admin_edit_user/<int:id>/', views.admin_edit_user),
    # 管理员删除用户或管理员信息
    path('admin_delete_user/<int:id>/', views.admin_delete_user),
    # 将参数city传给数据处理函数进行图表数据生成
    path('api_data/', views.api_data),
    # 信息可视化大屏跳转到“分析结果”
    path('display_1/', views.display_1),
    # 信息可视化大屏跳转到“文本分类”
    path('display_2/', views.display_2),
    # 信息可视化大屏跳转到“回归预测”
    path('display_3/', views.display_3),
]
