# Generated by Django 2.2.16 on 2021-03-25 04:42

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='in_depth',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='key_info',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='in_depth',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='key_info',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html'))], blank=True),
        ),
    ]
