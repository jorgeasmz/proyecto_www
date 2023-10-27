# Generated by Django 4.2.6 on 2023-10-26 02:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("nickname", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="avatars/users/"
                    ),
                ),
                (
                    "avatar_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "contacts",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="avatars/activities/"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_activities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("TR", "Viaje"),
                            ("HM", "Hogar"),
                            ("PR", "Pareja"),
                            ("FD", "Comida"),
                            ("OT", "Otro"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="avatars/events/"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date", models.DateTimeField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_events",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParticipationActivity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("PR", "Porcentaje"), ("VF", "Valor fijo")],
                        max_length=2,
                    ),
                ),
                ("value_type", models.DecimalField(decimal_places=2, max_digits=5)),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participations",
                        to="splitcount.activity",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participaton_activities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "participation_activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="splitcount.participationactivity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParticipationEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participations",
                        to="splitcount.event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participation_events",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                related_name="events",
                through="splitcount.ParticipationEvent",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="activities",
                to="splitcount.event",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="participants",
            field=models.ManyToManyField(
                related_name="activities",
                through="splitcount.ParticipationActivity",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
