from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title","author", "description", "price", "isbn")

    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)
        price = data.get("price", None)
        isbn = data.get("isbn", None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError({
                    "success": False,
                    "message": "Kitobni sarlavhasi faqat harflardan tashkil topgan bolishi kerak!"
                })
        # check title and author from database existense
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "success": False,
                    "message": "Bunday kitob mavjud!"
                }
            )
        # check price is true
        if 0 > price or price > 999999999:
            raise ValidationError(
                {
                    "success": False,
                    "message": "Narx notogri kiritilgan"
                }
            )
        if price.isalpha():
            raise ValidationError({
                "message": "Narx son bilan yoziladi!"
            })
        # check isbn is number
        if isbn.isalpha():
            raise ValidationError({
                "status": False,
                "message": "Isbn sonlardan iborat bolishi kerak"
            })
        if Book.objects.filter(isbn=isbn).exists():
            raise ValidationError(
                {
                    "success": False,
                    "message": "Book with this isbn is already exists in database"
                }
            )
        return data



