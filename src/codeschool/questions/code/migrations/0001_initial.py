# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 21:25
from __future__ import unicode_literals

import codeschool.lms.activities.models.activity
import codeschool.mixins
import codeschool.questions.base.models
import codeschool.vendor.wagtailmarkdown.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeFeedback',
            fields=[
                ('feedback_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Feedback')),
                ('error_message', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.base.models.QuestionMixin, 'activities.feedback'),
        ),
        migrations.CreateModel(
            name='CodeProgress',
            fields=[
                ('progress_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Progress')),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.base.models.QuestionMixin, 'activities.progress'),
        ),
        migrations.CreateModel(
            name='CodeQuestion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('short_description', models.CharField(help_text='A short textual description to be used in titles, lists, etc.', max_length=140, verbose_name='short description')),
                ('author_name', models.CharField(blank=True, help_text="The author's name, if not the same user as the question owner.", max_length=100, verbose_name="Author's name")),
                ('visible', models.BooleanField(default=codeschool.lms.activities.models.activity.bool_to_true, help_text='Makes activity invisible to users.', verbose_name='Invisible')),
                ('closed', models.BooleanField(default=bool, help_text='A closed activity does not accept new submissions, but users can see that they still exist.', verbose_name='Closed to submissions')),
                ('group_submission', models.BooleanField(default=bool, help_text='If enabled, submissions are registered to groups instead of individual students.', verbose_name='Group submissions')),
                ('max_group_size', models.IntegerField(default=6, help_text='If group submission is enabled, define the maximum size of a group.', verbose_name='Maximum group size')),
                ('disabled', models.BooleanField(default=bool, help_text='Activities can be automatically disabled when Codeshool encounters an error. This usually produces a message saved on the .disabled_message attribute. This field is not controlled directly by users.', verbose_name='Disabled')),
                ('disabled_message', models.TextField(blank=True, help_text='Messsage explaining why the activity was disabled.', verbose_name='Disabled message')),
                ('has_submissions', models.BooleanField(default=bool)),
                ('has_correct_submissions', models.BooleanField(default=bool)),
                ('body', wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('markdown', codeschool.vendor.wagtailmarkdown.blocks.MarkdownBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock())), blank=True, help_text='Describe what the question is asking and how should the students answer it as clearly as possible. Good questions should not be ambiguous.', null=True, verbose_name='Question description')),
                ('comments', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='(Optional) Any private information that you want to associate to the question page.', verbose_name='Comments')),
                ('import_file', models.FileField(blank=True, help_text='Fill missing fields from question file. You can safely leave this blank and manually insert all question fields.', null=True, upload_to='question-imports', verbose_name='import question')),
                ('grader', models.TextField(help_text='The grader is a Python script that defines a "grade(test, reference)" function that takes the test function and a reference implementation and raise AssertionErrors if something fail.', verbose_name='Grader source code')),
                ('reference', models.TextField(help_text='Reference implementation for the correct function.', verbose_name='Reference implementation')),
                ('function_name', models.CharField(default='func', help_text='The name of the test object. (This is normally a function, but we can also test classes, data structures, or anything)', max_length=80, verbose_name='Function name')),
                ('timeout', models.FloatField(default=1.0, help_text='Maximum interval (in seconds) used to grade the question.', verbose_name='Timeout')),
            ],
            options={
                'permissions': (('download_question', 'Can download question files'),),
                'abstract': False,
            },
            bases=(codeschool.mixins.CommitMixin, wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='CodeSubmission',
            fields=[
                ('submission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Submission')),
                ('source', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.base.models.QuestionMixin, 'activities.submission'),
        ),
    ]
