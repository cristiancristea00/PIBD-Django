from dateutil.parser import parse
from django.views.generic import TemplateView

from IJR.models import Programare


class ProgramariPageView(TemplateView):
    template_name = 'programari.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        programari = Programare.objects.all()
        context['programari'] = programari
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateProgramare', None) is not None:

            programare = Programare.objects.get(id_programare=int(self.request.POST.get('Select_programare_Update', None)))
            judecator = programare.judecator
            proces = programare.proces
            oras = self.request.POST.get('Oras_update', None)
            oras = oras if oras != '' else programare.oras
            locatie = self.request.POST.get('Locatie_update', None)
            locatie = locatie if locatie != '' else programare.locatie
            data = self.request.POST.get('Data_update', None)
            data = parse(data) if data != '' else programare.data
            ora = self.request.POST.get('Ora_update', None)
            ora = parse(ora) if ora != '' else programare.ora

            programare = Programare(id_programare=programare.id_programare, judecator=judecator, proces=proces, oras=oras, locatie=locatie, data=data,
                                    ora=ora)

            programare.save(force_update=True)

        elif self.request.POST.get('deleteProgramare', None) is not None:

            programare = Programare.objects.get(id_programare=int(self.request.POST.get('Select_programare_Delete', None)))
            programare.delete()

        return self.render_to_response(self.get_context_data())
