from django import forms
from django.forms import widgets
from django.forms import fields
from django.core.validators import MaxValueValidator, MinValueValidator


class LargeForm(forms.Form):
    input_choices = ((1, 'Use specific SNPs'),(2, 'Search existing GWAS'))
    inputWay = fields.ChoiceField(
        label = '',
        choices = input_choices,
        widget =widgets.RadioSelect,
        required = True
    )

    r2 = forms.FloatField(
        label = 'R² ( [0,1] ) ≥',
        validators = [
            MaxValueValidator(1),
            MinValueValidator(0)
        ],
        required=True
    )

    ppl_choices = ((1, 'AFR'),(2, 'AMR'),(3, 'EAS'),(4, 'EUR'))
    ppl = forms.ChoiceField(
        label = 'Population : ', 
        widget = forms.Select(), 
        choices = ppl_choices,
        initial = ppl_choices[0],
        required = True
        ) 

class ChrSNPForm(forms.Form):

    chr_choices = (
        (0, 'chr1'), (1, 'chr2'), (2, 'chr3'), (3, 'chr4'), (4, 'chr5'),
        (5, 'chr6'), (6, 'chr7'), (7, 'chr8'), (8, 'chr9'),(9, 'chr10'),
        (10, 'chr11'), (11, 'chr12'), (12, 'chr13'), (13, 'chr14'), (14, 'chr15'),
        (15, 'chr16'), (16, 'chr17'), (17, 'chr18'), (18, 'chr19'),(19, 'chr20'),
        (20, 'chr21'),(21, 'chr22')
    )
    chrs = forms.ChoiceField(
        label = 'Chromosome (e.g. chr1) :', 
        widget = forms.Select(), 
        choices = chr_choices,
        initial = chr_choices[0],
        required = True
        )
    snp = forms.IntegerField(
        label = 'SNP Stop Position (e.g. 10000044) :',
        validators = [
            MaxValueValidator(1000000000),
            MinValueValidator(0)
        ],
        initial = 10000044,
        required=True
    )




class UploadSNPs(forms.Form):
    file = forms.FileField()