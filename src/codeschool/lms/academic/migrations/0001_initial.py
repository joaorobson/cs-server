# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(
                    help_text='Unique short name used on urls.', verbose_name='Short name')),
                ('description', wagtail.wagtailcore.fields.RichTextField(
                    blank=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(
                    help_text='Unique short name used on urls.', verbose_name='Short name')),
                ('description', wagtail.wagtailcore.fields.RichTextField(
                    blank=True, verbose_name='Description')),
                ('code', models.CharField(blank=True, max_length=50)),
                ('since', models.DateField(blank=True, null=True)),
                ('syllabus', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('program', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('bibliography', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(
                    help_text='Unique short name used on urls.', verbose_name='Short name')),
                ('description', wagtail.wagtailcore.fields.RichTextField(
                    blank=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='discipline',
            name='faculty',
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to='academic.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='academic.Faculty'),
        ),
    ]