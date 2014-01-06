from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from questionnaire.models import Constituency, Party, AnswerSet

def questionnaire_form(request, error=''):
    payload = {
        'constituencies': Constituency.objects.all(),
        'parties': Party.objects.all(),
        'error': error,
        'data': {
            'constituency': '',
            'party': '',
            'voting': ''
        }
    }

    if ('constituency' in request.POST and request.POST['constituency'].isdigit()):
        payload['data']['constituency'] = int(request.POST['constituency'])

    if ('party' in request.POST):
        payload['data']['party'] = request.POST['party']

    if ('going-to-vote' in request.POST):
        payload['data']['voting'] = request.POST['going-to-vote']

    return render(
        request,
        'questionnaire/form.html',
        payload
    )

def submit_form(request):
    if ('going-to-vote' not in request.POST):
        return questionnaire_form(request, "Please say whether you're planning to vote")

    going_to_vote = request.POST['going-to-vote']
    constituency_id = request.POST['constituency']

    if (not constituency_id.isdigit()):
        return questionnaire_form(request, "Please select a constituency")

    constituency = Constituency.objects.get(id=constituency_id)
    parties = Party.objects.filter(abbreviation=request.POST['party'])
    party = None

    if (parties.count() > 0):
        party = parties[0]

    answer_set = AnswerSet(
        constituency=constituency,
        voting_for=party,
        going_to_vote=request.POST['going-to-vote']
    )
    answer_set.save()

    return HttpResponseRedirect(reverse('form'))
