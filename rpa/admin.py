from django.contrib import admin

from rpa.models import Aprovacao

@admin.register(Aprovacao)
class AprovacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'status')
    search_fields = ('cpf',)
    list_filter = ('status',)
