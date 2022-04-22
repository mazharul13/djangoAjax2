from django.urls import path
from . import views
# from contact import

urlpatterns = [
    path('info', views.list_view),
    path('new_contact', views.new_contact),
    path('delete/<int:id>', views.delete_cntact),
    path('delete_ajax', views.delete_ajax_cntact),
    # path(r'^delete_ajax/$', views.delete_ajax_cntact, name='delete by ajax'),


# http://127.0.0.1:8000/contact/delete/delete_ajax_cntact?post_id=5
    # path('show', views.show),
    # path('edit/<int:id>', views.edit),
    # path('update/<int:id>', views.update),
    # path('delete/<int:id>', views.destroy),
    # # path('contact/', contact.ContactForm),
    #
    # path('morning', views.test1)
]