from django.db import models
# Create your models here.
from django.utils import timezone
# Create your models here. 注意縮排
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
class Meta:
    ordering = ('-pub_date',)
    def __str__(self):#回傳必須是字串
        return self.title
# 類別(Class)需繼承models模組中的Model類別，其中封裝了存取資料庫的所有操作，例如新增、刪除、修改、查詢資料等。
# 而models模組中，提供許多抽象化資料表欄位的類別，例如：
# CharField：字串欄位
# IntegerField：整數欄位
# FloatField：浮點數欄位
# DateField：日期欄位
# ImageField：圖片欄位
# 在類別(Class)中即可利用這些欄位類別，來建立資料庫欄位的屬性(Attribute)。其中，CharField可以透過Python關鍵字參數
# (Keyword Argument)來限制長度。另外，範例中的DateField(日期欄位)，可以引用timezone類別，在新增景點貼文時，預設存入目前時區的時間。
# 最後，由於要建立「景點位置」及「景點貼文」一對多的關係，所以透過ForeignKey類別來進行設定，而on_delete=models.CASCADE的意思是，
# 當「景點位置」資料表中的資料被刪除時，相對應的「景點貼文」資料也跟著刪除。