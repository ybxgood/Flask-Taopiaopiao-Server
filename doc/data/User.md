# User


### 常用功能
- 注册
- 登录
- 管理员


### 登录注册
- 建表（用户表）
    - 用户名
    - 密码
    - 头像
    - 邮箱
    - 是否删除
    - 是否激活
    - 是否异常
- 添加创建接口
    - 各种验证
    - 存储
    
#### 登录注册 
- 导入了flask-login
- 安装 pip install flask-login
- 初始化
    - 创建一个LoginManager对象
    - 需要使用App对象进行初始化
    - 还需要在Config中配置SECRET_KEY
    - 注册一个装饰器@loginManager.user_loader
    - 注册一个函数上，函数根据id返回对应用户 
- 调用
    - login_user(user)   用户登录
    - logout_user()      用户退出
    - current_user       当前登录的用户
 
    
### 数据安全
- 做了两套
    - 前端做
    - 服务器做
- 服务器实现
    - 使用哈希
   
### 模型进化
- 封装通用功能
- 数据安全


### 用户权限
- 很多网站上，网站存在很多用户
- 权限
    - 游客（READ）
    - USER(READ,WRITE)
    - 辅助管理者 (READ,WTIRE(自己的),DELETE)
    - 超级管理员 (READ,WRITE(谁的都能写),DELETE,DROP USER)
- 对应关系
   - 一个用户对应一条权限信息
   - 一条权限信息要包含多种权限
   - Linux权限 R W X
            - 4 2 1
   - 权限控制
   - 使用函数来进行权限判断        check_permission
   - 也可以使用函数进行状态判断     check_login



### 权限控制
- 使用 & | 实现权限值的控制
- 拥有的权限 都是 2的n次方   
    - 1
    - 2
    - 4 
    - 8 
- 通过或 | 可以实现不同权限的值相加组合
- 通过 & 可以筛选
- 使用装饰器来实现权限控制
    - 用户是否登录
    - 权限检查
        - 更深一层的装饰器
        
### abort
- 抛出状态码，配置信息
- message 关键字参数
- 全局bug


### 项目
- 电影院
- 订单





