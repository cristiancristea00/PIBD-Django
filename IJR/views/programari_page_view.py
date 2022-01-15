from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from IJR.models import Programare


class ProgramariPageView(TemplateView):
    template_name = 'programari.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            programari = Programare.objects.all()
        context['programari'] = programari
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateProgramare') is not None:

            with transaction.atomic():
                programare = Programare.objects.get(
                    id_programare=int(self.request.POST.get('Select_programare_Update')))

            judecator = programare.judecator
            proces = programare.proces
            oras = self.request.POST.get('Oras_update')
            oras = oras if oras != '' else programare.oras
            locatie = self.request.POST.get('Locatie_update')
            locatie = locatie if locatie != '' else programare.locatie
            data = self.request.POST.get('Data_update')
            data = parse(data) if data != '' else programare.data
            ora = self.request.POST.get('Ora_update')
            ora = parse(ora) if ora != '' else programare.ora

            programare = Programare(id_programare=programare.id_programare, judecator=judecator,
                                    proces=proces,
                                    oras=oras, locatie=locatie, data=data, ora=ora)

            programare.update()

        elif self.request.POST.get('deleteProgramare') is not None:

            with transaction.atomic():
                programare = Programare.objects.get(
                    id_programare=int(self.request.POST.get('Select_programare_Delete')))

            programare.remove()

        return self.render_to_response(self.get_context_data())
