from symtable import Class

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)

# class ProfileForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Name")
#     age = forms.IntegerField(min_value=0, label="Age")
#     is_student = forms.BooleanField(required=False, label="Student?")
#     level = forms.ChoiceField(choices=[
#         ("beginner", "Beginner"),
#         ("intermediate", "Intermediate"),
#         ("advanced", "Advanced"),
#     ], label="Level")

class ProfileForm(forms.Form):
    # --- ТЕКСТОВІ / СТРІЧКОВІ ПОЛЯ ---

    name = forms.CharField(
        max_length=100,
        label="Name",
        help_text="CharField – звичайний текст",
    )

    email = forms.EmailField(
        label="Email",
        help_text="EmailField – перевіряє валідність email",
    )

    url = forms.URLField(
        required=False,
        label="Personal website",
        help_text="URLField – посилання (http/https)",
    )

    slug = forms.SlugField(
        required=False,
        label="Slug",
        help_text="SlugField – тільки букви, цифри, дефіс, підкреслення",
    )

    regex_code = forms.RegexField(
        regex=r"^[A-Z0-9]{4}$",
        required=False,
        label="Promo code",
        help_text="RegexField – перевірка за регулярним виразом (4 символи A-Z/0-9)",
    )

    uuid = forms.UUIDField(
        required=False,
        label="UUID",
        help_text="UUIDField – значення типу UUID",
    )

    ip_address = forms.GenericIPAddressField(
        required=False,
        label="IP address",
        protocol="both",      # 'ipv4', 'ipv6', або 'both'
        unpack_ipv4=True,
        help_text="GenericIPAddressField – IPv4/IPv6",
    )

    json_data = forms.JSONField(
        required=False,
        label="JSON data",
        help_text="JSONField – валідний JSON (словар, список тощо)",
    )

    # --- ЧИСЛОВІ ПОЛЯ ---

    age = forms.IntegerField(
        min_value=0,
        label="Age",
        help_text="IntegerField – ціле число",
    )

    height = forms.FloatField(
        required=False,
        label="Height (m)",
        help_text="FloatField – число з плаваючою комою",
    )

    salary = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        label="Salary",
        help_text="DecimalField – десяткове число з фіксованою точністю",
    )

    # --- БУЛЕВІ ПОЛЯ ---

    is_student = forms.BooleanField(
        required=False,
        label="Student?",
        help_text="BooleanField – checkbox True/False",
    )

    # --- ПОЛЯ ВИБОРУ ---

    level = forms.ChoiceField(
        choices=[
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
        label="Level (ChoiceField)",
        help_text="ChoiceField – один варіант із списку",
    )

    typed_level = forms.TypedChoiceField(
        choices=[("1", "Level 1"), ("2", "Level 2"), ("3", "Level 3")],
        coerce=int,   # значення буде int 1/2/3
        empty_value=None,
        required=False,
        label="Typed level",
        help_text="TypedChoiceField – перетворює значення до потрібного типу",
    )

    interests = forms.MultipleChoiceField(
        required=False,
        choices=[
            ("python", "Python"),
            ("django", "Django"),
            ("js", "JavaScript"),
        ],
        label="Interests",
        help_text="MultipleChoiceField – список із можливістю вибрати кілька значень",
    )

    typed_interests = forms.TypedMultipleChoiceField(
        required=False,
        choices=[
            ("1", "Backend"),
            ("2", "Frontend"),
            ("3", "DevOps"),
        ],
        coerce=int,
        label="Typed interests",
        help_text="TypedMultipleChoiceField – кілька значень з приведенням типу",
    )

    # --- ДАТИ / ЧАС ---

    birth_date = forms.DateField(
        required=False,
        label="Birth date",
        widget=forms.DateInput(attrs={"type": "date"}),
        help_text="DateField – дата (yyyy-mm-dd)",
    )

    wake_up_time = forms.TimeField(
        required=False,
        label="Wake up time",
        widget=forms.TimeInput(attrs={"type": "time"}),
        help_text="TimeField – час (HH:MM[:ss])",
    )

    meeting_datetime = forms.DateTimeField(
        required=False,
        label="Meeting datetime",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        help_text="DateTimeField – дата + час",
    )

    duration = forms.DurationField(
        required=False,
        label="Study duration",
        help_text="DurationField – проміжок часу (тип timedelta)",
    )

    split_datetime = forms.SplitDateTimeField(
        required=False,
        label="Split datetime",
        help_text="SplitDateTimeField – два окремих поля для дати і часу",
    )

    # --- ФАЙЛИ ---

    avatar = forms.ImageField(
        required=False,
        label="Avatar image",
        help_text="ImageField – завантаження зображення (потрібен Pillow)",
    )

    attachment = forms.FileField(
        required=False,
        label="Attachment",
        help_text="FileField – завантаження будь-якого файлу",
    )

class DemoControlsForm(forms.Form):
    username = forms.CharField(label="Логін", max_length=50)
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    age = forms.IntegerField(label="Вік", min_value=0, max_value=120)
    birth_date = forms.DateField(
        label="Дата народження",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    color = forms.ChoiceField(
        label="Улюблений колір",
        choices=[
            ("red", "Червоний"),
            ("green", "Зелений"),
            ("blue", "Синій"),
        ]
    )
    interests = forms.MultipleChoiceField(
        label="Інтереси",
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ("music", "Музика"),
            ("sport", "Спорт"),
            ("coding", "Програмування"),
        ]
    )
    agree = forms.BooleanField(
        label="Погоджуюсь з умовами",
        required=True
    )

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20, min_length=3)
    age = forms.IntegerField(label="Age", min_value=18, max_value=100)
    email = forms.EmailField(label="Email", max_length=30)
    password = forms.CharField(label="Password", min_length=6, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", min_length=6, widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data["username"]
        if "admin" in username.lower():
            raise forms.ValidationError("Логін не може містити 'admin'.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Паролі не співпадають.")

        return cleaned_data