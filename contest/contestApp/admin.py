from django.contrib import admin
from .models import Province, Participant, Picture, Vote

admin.site.register(Province)



# Register in the admin dashboard
@admin.register(Picture)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = [ 'description', 'created', 'get_votes', 'image_img']

#admin.site.register(Picture)


# Register in the admin dashboard
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'dni', 'email', 'phone', 'profession', 'province', 'created']

#admin.site.register(Participant)


# Register in the admin dashboard
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['foto', 'created', 'email']

#admin.site.register(Vote)
