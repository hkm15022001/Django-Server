import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


from django.db import models
from django.db.models import F
from django.db import models
from django.db.models import Min, OuterRef, Subquery, Sum


def do_something():
    pass


class Base1(models.Model):  # create base class for other class to develop on it
    name_1 = models.CharField(max_length=100)
    age_1 = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["-name_1"]  # sắp xếp theo biến name_1 thứ tự giảm dần


class Base2(models.Model):
    name_2 = models.CharField(max_length=100)
    age_2 = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Der1(Base1, Base2):
    class Meta:
        ordering = []  # Remove parent's ordering effect


class Person(Base1):
    # The first element is the stored value The second element is displayed value. The display value can be accessed using the get_FOO_display() method (ex: get_shirt_size_display)
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    blog = models.ForeignKey(
        Base2, on_delete=models.CASCADE
    )  # tạo Foreign key giữa Person và Base2
    ShirtSize = models.TextChoices(
        "ShirtSize", "Small Medium Large"
    )  # other way to define choice
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    m2m = models.ManyToManyField(
        Base1
    )  # 1 query set chứa nhiều đối tượng Base1, các object Base1 cũng có thể truy cập được đến các đối tượng chứa nó (A QuerySet represents a collection of objects from your database, tương đương vs lệnh SELECT trong SQL)

    def save(self, *args, **kwargs):  # overload pre-build method
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something()


# CLASS.object là manager tool của class đó

# UPDATE FOREIGNKEY
p = Person.objects.create(name="T-shirt", choice="S")  # khởi tạo model
b1 = Base2.objects.get(name="B1")
b2 = Base2.objects.get(name="B2")
p.blog = b2
p.save()

# UPDATE MANYTOMANY
p.m2m.add(b1)


# MAKING QUERIES
all_p = Person.objects.all()
p.name = "New T-shirt"  # ko thay đổi được giá trị của p mà sẽ tạo ra 1 p mới
p.save()
Person.objects.values_list("name", flat=True)  # liệt kê các object theo tên
p = Person.objects.get(name="Cheddar Talk")  # lấy đối tượng

# FILTER

# filter keyword có dạng như sau: field__lookuptype=value
# lookuptype bao gồm: exact, exact, contains, startswith, endswith (hoặc thêm tiền tố i vào)

# span relationship
# model1__model2__...__field__lookuptype
f = Person.objects.filter(pub_date__year=2006)
f = Person.objects.exclude(
    pub_date__lte="2006-01-01"
)  # pub_date<=2006-01-01 #gt,lt,gte,...
f = Person.objects.order_by("headline")

# FILTER ĐÔI
Person.objects.filter(
    blog__headline__contains="Lennon", blog__pub_date__year=2008
)  # blog thỏa mãn cả 2 đk
Person.objects.filter(blog__headline__contains="Lennon").filter(
    blog__pub_date__year=2008
)  # blog thỏa mãn 1 điều kiện

# FILTER ĐỘNG
Person.objects.filter(field_1__gt=F("field_2") * 2)

# NGUYÊN LÝ CACHE QUERYSET
queryset = Person.objects.all()
print(queryset[3])  # not cached
print(
    [p.headline for p in queryset]
)  # Evaluate the query set. (cached) (phải duyệt qua toàn bộ)
