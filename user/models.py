from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField


class UserManager(BaseUserManager):
    """
    自定义Manager管理器
    """

    def _create_user(self, name, password, phone, **kwargs):
        if not phone:
            raise ValueError("请传入电话号码！")
        if not name:
            raise ValueError("请传入用户名！")
        if not password:
            raise ValueError("请传入密码！")
        user = self.model(name=name, phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name, password, phone, **kwargs):
        """
        创建普通用户
        """
        kwargs['is_superuser'] = False
        return self._create_user(name, password, phone, **kwargs)

    def create_superuser(self, name, password, phone, **kwargs):
        """
        创建超级用户
        """
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(name, password, phone, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    自定义User
    """
    GENDER_TYPE = (
        (1, "男"),
        (2, "女")
    )

    phone    = models.CharField("手机号码", max_length=11, primary_key=True)
    name     = models.CharField("姓名", max_length=15)
    gender   = models.IntegerField("性别", max_length=1, choices=GENDER_TYPE)
    avatar   = models.ImageField("用户头像", upload_to="media/avatar", null=True, blank=True)
    address  = models.CharField("地址", max_length=100, null=True, blank=True)
    card_id  = models.CharField("身份证", max_length=18, null=True, blank=True)
    birthday = models.DateField("生日", null=True, blank=True)

    is_active   = models.BooleanField("激活状态", default=True)
    is_staff    = models.BooleanField("是否是员工", default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateField(auto_now=True)

    USERNAME_FIELD = 'phone'  # 使用authenticate验证时使用的验证字段，可以换成其他字段，但验证字段必须是唯一的，即设置了unique=True
    REQUIRED_FIELDS = ['name', 'phone', 'gender']  # 创建用户时必须填写的字段，除了该列表里的字段还包括password字段以及USERNAME_FIELD中的字段

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return '<{} {}>'.format(self.name, self.phone)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name





