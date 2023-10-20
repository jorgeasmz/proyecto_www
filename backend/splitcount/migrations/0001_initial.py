# Generated by Django 4.2.6 on 2023-10-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
            ],
        ),
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
                ("contacts", models.ManyToManyField(blank=True, to="splitcount.user")),
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
                        to="splitcount.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="participationactivity",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="participaton_activities",
                to="splitcount.user",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_events",
                to="splitcount.user",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                related_name="events",
                through="splitcount.ParticipationEvent",
                to="splitcount.user",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_activities",
                to="splitcount.user",
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
                to="splitcount.user",
            ),
        ),
    ]
