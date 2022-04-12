import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class PhoneNumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', password):
            raise ValidationError(
                _("یک شماره تلفن معتبر وارد کنید"),
                code='password_no_number',
            )

    # def get_help_text(self):
    #     return _(
    #         "Your password must contain at least 1 digit, 0-9."
    #     )
