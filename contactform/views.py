from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


def index(request):
    form = ContactForm()
    return render(request, "contactform/index.html", {"form": form})


class SuccessView(TemplateView):
    template_name = "success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        full_message = (
            f"Received message below from {email}, {subject}\n"
            f"________________________\n\n"
            f"{message}"
        )
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        # 3. Redirect to the success URL (PRG pattern)
        return super().form_valid(form)
