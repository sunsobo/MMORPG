from django.contrib import admin


from .models import Profile


# BEGIN Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'email_token',
        'email_token_date',
        'email_confirm',
        'id',
    ]
    
    list_filter = [
        'email_confirm',
    ]

admin.site.register(Profile, ProfileAdmin)
# END Profile