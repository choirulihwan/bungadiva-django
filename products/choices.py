from categories.models import Category

status_choices = {
    "READY": "Ready",
    "SOLDOUT": "Soldout",
}

price_choices = {
    "50000": "Rp.50000",
    "100000": "Rp.100000",
    "150000": "Rp.150000",
}

categories = Category.objects.all().values()
category_choices = []
for category in categories:
    category_choices.append(category['name'])

