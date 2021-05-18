#a form to submit new images
from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput} #	HiddenInput	widget is rendered as HTML input element with a	type="hidden" attribute

    def clean_url(self):   #clean_url() method to clean the url field
        url = self.cleaned_data['url']  
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        # image name by combining the image title slug with the original file extension
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())

        #download image from yhe given url
        response = request.urlopen(image_url)
        # python urllib module to download image & thn call save method
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image