# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Admin(models.Model):
    adminid = models.CharField(db_column='adminID', primary_key=True, max_length=15)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cart(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField()
    productid = models.CharField(db_column='productId', max_length=15)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=40)  # Field name made lowercase.
    quantity = models.IntegerField()
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Customer(models.Model):
    phoneno = models.CharField(db_column='phoneNo', primary_key=True, max_length=15)  # Field name made lowercase.
    custid = models.CharField(db_column='custID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    streetaddr = models.CharField(db_column='streetAddr', max_length=40, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=25, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Order(models.Model):
    customerid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='customerId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', primary_key=True, max_length=15)  # Field name made lowercase.
    date_ordered = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'


class Orderitem(models.Model):
    product = models.ForeignKey('Part', models.DO_NOTHING, db_column='product')
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='order', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orderitem'


class Part(models.Model):
    image = models.TextField(blank=True, null=True)
    partno = models.CharField(db_column='partNo', primary_key=True, max_length=15)  # Field name made lowercase.
    partname = models.CharField(db_column='partName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    partcategory = models.CharField(db_column='partCategory', max_length=30, blank=True, null=True)  # Field name made lowercase.
    partyear = models.DateField(db_column='partYear', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class Shippingaddress(models.Model):
    customer = models.IntegerField()
    order = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postalcode = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shippingaddress'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
