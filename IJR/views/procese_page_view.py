from django.db import transaction
from django.views.generic import TemplateView

from IJR.models import Proces


class ProcesePageView(TemplateView):
    template_name = 'procese.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            procese = Proces.objects.all()
        context['procese'] = procese
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateProces') is not None:

            proces = Proces.objects.get(id_proces=int(self.request.POST.get('Select_proces_Update')))
            numar = self.request.POST.get('Numar_update')
            numar = numar if numar != '' else proces.numar
            obiect = self.request.POST.get('Obiect_update')
            obiect = obiect if obiect != '' else proces.obiect
            materie_juridica = self.request.POST.get('Materie_juridica_update')
            materie_juridica = materie_juridica if materie_juridica != '' else proces.materie_juridica
            stadiu_procesual = self.request.POST.get('Stadiu_procesual_update')
            stadiu_procesual = stadiu_procesual if stadiu_procesual != '' else proces.stadiu_procesual
            reclamant = self.request.POST.get('Reclamant_update')
            reclamant = reclamant if reclamant != '' else proces.reclamant
            parat = self.request.POST.get('Parat_update')
            parat = parat if parat != '' else proces.parat

            proces = Proces(id_proces=proces.id_proces, numar=numar, obiect=obiect, materie_juridica=materie_juridica,
                            stadiu_procesual=stadiu_procesual, reclamant=reclamant, parat=parat)

            proces.update()

        elif self.request.POST.get('deleteProces') is not None:

            with transaction.atomic():
                proces = Proces.objects.get(id_proces=int(self.request.POST.get('Select_proces_Delete')))

            proces.remove()

        return self.render_to_response(self.get_context_data())
