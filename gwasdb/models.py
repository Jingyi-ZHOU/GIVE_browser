from django.db import models


class Chr10Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr10aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr10Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr10aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr10Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr10aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr10Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr10aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr11Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr11aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr11Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr11aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr11Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr11aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr11Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr11aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr12Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr12aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr12Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr12aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr12Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr12aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr12Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr12aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr13Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr13aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr13Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr13aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr13Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr13aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr13Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr13aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr14Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr14aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr14Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr14aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr14Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr14aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr14Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr14aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr15Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr15aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr15Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr15aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr15Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr15aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr15Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr15aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr16Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr16aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr16Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr16aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr16Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr16aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr16Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr16aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr17Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr17aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr17Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr17aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr17Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr17aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr17Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr17aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr18Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr18aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr18Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr18aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr18Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr18aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr18Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr18aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr19Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr19aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr19Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr19aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr19Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr19aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr19Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr19aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr1Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr1aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr1Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr1aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr1Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr1aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr1Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr1aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr20Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr20aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr20Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr20aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr20Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr20aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr20Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr20aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr21Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr21aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr21Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr21aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr21Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr21aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr21Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr21aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr22Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr22aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr22Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr22aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr22Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr22aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr22Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr22aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr2Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr2aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr2Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr2aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr2Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr2aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr2Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr2aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr3Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr3aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr3Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr3aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr3Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr3aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr3Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr3aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr4Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr4aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr4Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr4aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr4Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr4aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr4Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr4aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr5Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr5aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr5Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr5aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr5Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr5aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr5Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr5aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr6Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr6aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr6Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr6aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr6Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr6aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr6Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr6aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr7Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr7aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr7Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr7aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr7Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr7aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr7Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr7aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr8Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr8aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr8Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr8aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr8Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr8aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr8Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr8aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chr9Aafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr9aAFR'
        unique_together = (('stop1', 'stop2'),)


class Chr9Aamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr9aAMR'
        unique_together = (('stop1', 'stop2'),)


class Chr9Aeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr9aEAS'
        unique_together = (('stop1', 'stop2'),)


class Chr9Aeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chr9aEUR'
        unique_together = (('stop1', 'stop2'),)


class Chrxaafr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chrXaAFR'
        unique_together = (('stop1', 'stop2'),)


class Chrxaamr(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chrXaAMR'
        unique_together = (('stop1', 'stop2'),)


class Chrxaeas(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chrXaEAS'
        unique_together = (('stop1', 'stop2'),)


class Chrxaeur(models.Model):
    stop1 = models.IntegerField(primary_key=True)
    stop2 = models.IntegerField()
    r2 = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'chrXaEUR'
        unique_together = (('stop1', 'stop2'),)


class Gwascatalog(models.Model):
    first_author = models.CharField(max_length=100, blank=True, null=True)
    published_data = models.CharField(max_length=11, blank=True, null=True)
    study_accession = models.CharField(primary_key=True, max_length=11)
    chromosome = models.CharField(max_length=4)
    position = models.CharField(max_length=20)
    disease_trait = models.CharField(max_length=225, blank=True, null=True)
    super_population = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'gwasdb'
        db_table = 'gwascatalog'
        unique_together = (('study_accession', 'chromosome', 'position'),)