from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, DetailView, ListView
from .models import Order, Company, UserProfile, ActiveOrder
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import ConfirmForm

class OrderView(LoginRequiredMixin, View):

        def get(self, *arg, **kwargs):
            try:
                order = Order.objects.filter(user__user=self.request.user)
                user = self.request.user.username

                context = {
                    'objects': order,
                    'username': user,
                }
                return render(self.request, "order_summary.html", context)

            except ObjectDoesNotExist:
                messages.warning(self.request, 'شما هیچ سفارش فعالی ندارید')
                redirect("merchant:home")




class HomeView(View):

    def get(self, *arg, **kwargs):
        return render(self.request, "home.html", {})

def confirm_order(request, slug):
    order = get_object_or_404(Order, slug=slug)
    if (order.is_active) == True:
        messages.warning(request, "این آیتم قبلا تایید شده است")
    else:
        order.is_active = True
        order.save()
    return redirect('/order/')

def remove_order(request, slug):
    order_qs = get_object_or_404(Order, slug=slug)
    order_qs.delete()
    messages.warning(request, "این آیتم از لیست سفارشات شما حذف شد")
    return redirect("/order/")

class OrderDetailView(DetailView):
    model = Order
    template_name = 'item_detail.html'

