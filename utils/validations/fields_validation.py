from django.core.validators import RegexValidator


class FieldsValidation:

    # alpha_spaces_allowed = RegexValidator(r'^[a-zA-Z]+$', 'Only letters and spaces are allowed in the field!')

    def alphabets_spaces_allowed(self, field_name='field'):
        return RegexValidator(r'^[A-Za-z ]+$', f'Only alphabets and spaces are allowed in the {field_name}!')

    def alphabets_numbers_spaces_allowed(self, field_name='field'):
        return RegexValidator(r'^[A-Za-z0-9 ]+$', f'Only alphabets, numbers and spaces are allowed in the {field_name}!')

    def alphabets_numbers_spaces_and_comma_dot_allowed(self, field_name='field'):
        return RegexValidator(r'^[A-Za-z0-9 &,.]+$', f'Only alphabets, numbers, comma & dot are allowed in the {field_name}!')

    def alphabets_numbers_spaces_and_comma_dot_at_allowed(self, field_name='field'):
        return RegexValidator(r'^[A-Za-z0-9 &,.@]+$', f'Only alphabets, numbers, comma & dot are allowed in the {field_name}!')

    def alphabets_numbers_dot_allowed(self, field_name='field'):
        return RegexValidator(r'^[A-Za-z0-9.]+$', f'Only alphabets, numbers and dot are allowed in the {field_name}!')

    def numbers_allowed(self, field_name='field'):
        return RegexValidator(r'^[0-9]+$', f'Only numbers are allowed in the {field_name}!')
