from dateutil.parser import parse
from django.views.generic import TemplateView

from IJR.models import Judecator


class JudecatoriPageView(TemplateView):
    template_name = 'judecatori.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        judecatori = Judecator.objects.all()
        context['judecatori'] = judecatori
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateJudecator', None) is not None:

            judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('Select_judecator_Update', None)))
            cnp = self.request.POST.get('CNP_update', None)
            cnp = cnp if cnp != '' else judecator.cnp
            nume = self.request.POST.get('Nume_update', None)
            nume = nume.upper() if nume != '' else judecator.nume
            prenume = self.request.POST.get('Prenume_update', None)
            prenume = prenume if prenume != '' else judecator.prenume
            telefon = self.request.POST.get('Telefon_update', None)
            telefon = telefon if telefon != '' else judecator.telefon
            email = self.request.POST.get('Email_update', None)
            email = email if email != '' else judecator.email
            specializare = self.request.POST.get('Specializare_update', None)
            specializare = specializare if specializare != '' else judecator.specializare
            preluare_mandat = self.request.POST.get('Preluare_mandat_update', None)
            preluare_mandat = parse(preluare_mandat) if preluare_mandat != '' else judecator.preluare_mandat
            expirare_mandat = self.request.POST.get('Expirare_mandat_update', None)
            expirare_mandat = parse(expirare_mandat) if expirare_mandat != '' else judecator.expirare_mandat

            judecator = Judecator(id_judecator=judecator.id_judecator, cnp=cnp, nume=nume, prenume=prenume, telefon=telefon, email=email,
                                  specializare=specializare, preluare_mandat=preluare_mandat, expirare_mandat=expirare_mandat)

            judecator.save(force_update=True)

        elif self.request.POST.get('deleteJudecator', None) is not None:

            judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('Select_judecator_Delete', None)))
            judecator.delete()

        return self.render_to_response(self.get_context_data())
