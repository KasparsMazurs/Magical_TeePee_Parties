from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# This status will be used for publishing posts
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Create a model for posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)


class Meta:
    """
    All posts will be displayed the newest first
    """
    ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Create a model for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    likes = models.ManyToManyField(
        User, related_name='post_like', blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Meta:
    """
    All posts will be displayed the oldest first
    """
    ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Image(models.Model):
    """
    Create a model for images which will be used for PostGallery
    and PostProducts
    """
    image = CloudinaryField('image')


class PostGallery(models.Model):
    """
    Create a model for galleries
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    title_image = CloudinaryField('Title_image', default='placeholder')
    images = models.ManyToManyField(Image, related_name='gallery_images')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        All gallerys will be displayed the newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostProducts(models.Model):
    """
    Create a model for products
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    title_image = CloudinaryField('Title_image', default='placeholder')
    images = models.ManyToManyField(Image, related_name='Product_images')
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        All products will be displayed the newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BookAParty(models.Model):
    """
    Create a model for booking parties
    """
    party_themes = [
        ('JU', 'Jungle'),
        ('UN', 'Unicorn'),
        ('ME', 'Mermaid'),
        ('LI', 'Little ladies'),
        ('GA', 'Gamers'),
        ('TI', 'Tik Tok'),
        ('SO', 'Soccer'),
    ]
    party_theme = models.CharField(max_length=2, choices=party_themes)
    balloons = models.BooleanField(default=False)
    bouncy_castle = models.BooleanField(default=False)
    ages = [
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
    ]
    kids_age = models.CharField(max_length=2, choices=ages)
    teepees = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    number_of_teepees = models.CharField(max_length=2, choices=teepees)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    eircode = models.CharField(max_length=10)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    approved = models.BooleanField(default=False)
    email = models.EmailField(default='', blank=False)
    phone_number = models.CharField(max_length=50, default='+353 ')
    additional_info = models.TextField(default='Ask us a question here.')
    order_nr = models.SlugField(max_length=200, unique=True, editable=False,
                                default='new_order')
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
        default=User.objects.first().id
    )

    def save(self, *args, **kwargs):
        if not self.order_nr or self.order_nr == 'new_order':
            max_id = BookAParty.objects.aggregate(models.Max('id'))['id__max']
            if max_id is None:
                max_id = 0
            self.order_nr = slugify(f'order-{max_id+1}')
            while BookAParty.objects.filter(order_nr=self.order_nr).exists():
                self.order_nr = slugify(f'order-{max_id+1}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_nr
