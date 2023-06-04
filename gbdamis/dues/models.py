from django.db import models
from django.conf import settings

# Create a model named Dues with the following fields: user, month, amount, paid, date_paid.
# The user field is a foreign key to the User model.
# The month field is a MonthField.
# The amount field is a DecimalField with max_digits=6 and decimal_places=2.
# The paid field is a BooleanField with default=False.
# The date_paid field is a DateField with null=True and blank=True.
# The month field should be a custom field that only allows the user to select a month and year.
# The amount field should only allow positive values.
# The paid field should be set to True when the dues are paid.
# The date_paid field should be set to the date the dues were paid.
# The date_paid field should be blankable and nullable.
# Add a method to get all dues that are not paid and return the sum of all amounts of those dues.


class Dues(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)
    date_paid = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'month')

    def __str__(self):
        return f"{self.user.id} - {self.month.strftime('%B')} | {self.month.year}"
    
    def get_unpaid_dues(self):
        # get all dues that are not paid for user and return the sum of all amounts of those dues.
        return Dues.objects.filter(user=self.user, paid=False).aggregate(models.Sum('amount'))['amount__sum'] or 0
 