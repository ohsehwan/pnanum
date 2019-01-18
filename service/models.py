import uuid

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='제목',
    )
    html = RichTextField()
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
        verbose_name='사진',
    )
    file = models.FileField(
        upload_to='files',
        null=True,
        blank=True,
        verbose_name='파일',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        sault = 'mtschoolm'
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if self.file and sault not in self.file.name:
            self.file.name = f'{sault}_{now}.{self.file.name.split(".")[-1]}'
        if self.image and sault not in self.image.name:
            self.image.name = f'{sault}_{now}.{self.image.name.split(".")[-1]}'
        super().save()




class msch(models.Model): 			
	ms_id = models.CharField(max_length=10, primary_key=True, verbose_name='멘토스쿨ID' )
	ms_name = models.CharField(max_length=7, null=True, verbose_name='멘토스쿨 명' )
	ms_sname = models.CharField(max_length=2, null=True, verbose_name='멘토스쿨 관리 영역' )
	ms_intro = models.CharField(max_length=1000, null=True, verbose_name='멘토스쿨 소개' )
	mng_area = models.CharField(max_length=2, null=True, verbose_name='멘토스쿨 관리 영역' )
	mgr_id = models.CharField(max_length=10, null=True, verbose_name='멘토스쿨 관리자 ID' )
	mgr_nm = models.CharField(max_length=20, null=True, verbose_name='멘토스쿨 관리자 명' )
	mng_org = models.CharField(max_length=10, null=True, verbose_name='관리기관' )
	sup_org = models.CharField(max_length=10, null=True, verbose_name='주관기관' )
	apl_time = models.CharField(max_length=2, null=True, verbose_name='모집시기' )
	apl_fr = models.CharField(max_length=8, null=True, verbose_name='모집기간-시작' )
	apl_to = models.CharField(max_length=8, null=True, verbose_name='모집기간-종료' )
	trn_time = models.CharField(max_length=2, null=True, verbose_name='교육이시기' )
	trn_fr = models.CharField(max_length=8, null=True, verbose_name='교육기간-시작' )
	trn_to = models.CharField(max_length=8, null=True, verbose_name='교육기간-종료' )
	tot_apl = models.PositiveIntegerField(default=0, verbose_name='모집인원(정원)-합격' )
	cnt_apl = models.PositiveIntegerField(default=0, verbose_name='지원인원' )
	cnt_doc_suc = models.PositiveIntegerField(null=True, verbose_name='서류전형 합격인원' )
	cnt_doc_res = models.PositiveIntegerField(null=True, verbose_name='서류전형 예비인원(실제 없음)' )
	cnt_intv_pl = models.PositiveIntegerField(null=True, verbose_name='면접전형 참여 계획 인원' )
	cnt_intv_ac = models.PositiveIntegerField(null=True, verbose_name='면접전형 참여 인원' )
	intv_dt = models.CharField(max_length=8, null=True, verbose_name='면접일' )
	cnt_intv_suc = models.PositiveIntegerField(null=True, verbose_name='면접전형 합격인원' )
	cnt_iintv_res = models.PositiveIntegerField(null=True, verbose_name='면접전형 예비합격인원' )
	cnt_trn = models.PositiveIntegerField(null=True, verbose_name='교육인원' )
	cnt_mtr = models.PositiveIntegerField(null=True, verbose_name='최종합격 멘토인원' )
	doc_dt = models.CharField(max_length=8, null=True, verbose_name='서류전형일' )
	doc_tm = models.CharField(max_length=4, null=True, verbose_name='서류전형시' )
	doc_mgr = models.CharField(max_length=10, null=True, verbose_name='서류전형 수행자' )
	intv_dt = models.CharField(max_length=8, null=True, verbose_name='면접전형-입력-일' )
	intv_tm = models.CharField(max_length=4, null=True, verbose_name='면접전형-입력-시' )
	intv_mgr = models.CharField(max_length=10, null=True, verbose_name='면접전형-입력-자' )
	fin_dt = models.CharField(max_length=8, null=True, verbose_name='최종합격-입력-일' )
	fin_tm = models.CharField(max_length=4, null=True, verbose_name='최종합격-입력-시' )
	fin_mgr = models.CharField(max_length=10, null=True, verbose_name='최종합격-입력-자' )
	ins_id = models.CharField(max_length=10, null=True, verbose_name='입력자ID' )
	ins_ip = models.CharField(max_length=20, null=True, verbose_name='입력자IP' )
	ins_dt = models.DateTimeField(null=True, verbose_name='입력일시' )
	ins_pgm = models.CharField(max_length=20, null=True, verbose_name='입력프로그램ID' )
	upd_id = models.CharField(max_length=10, null=True, verbose_name='수정자ID' )
	upd_ip = models.CharField(max_length=20, null=True, verbose_name='수정자IP' )
	upd_dt = models.DateTimeField(null=True, verbose_name='수정일시' )
	upd_pgm = models.CharField(max_length=20, null=True, verbose_name='수정프로그램ID' )
	class Meta: 
		verbose_name = '개설멘토스쿨'
		verbose_name_plural =  verbose_name


# Create your models here.
