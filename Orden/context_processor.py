def total_orden(request):

    total=0
    if request.user.is_authenticated:
        if 'orden' in request.session:
            for key,value in request.session['orden'].items():
                total +=value['precio']
    return {'total_orden':total}