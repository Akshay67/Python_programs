import requests

Staging_imaakola = [
    'https://devimaakola.healthpole.com/', 'https://devimaakola.healthpole.com/updates',
    'https://devimaakola.healthpole.com/', 'https://devimaakola.healthpole.com/events',
    'https://devimaakola.healthpole.com/committees', 'https://devimaakola.healthpole.com/documents',
    'https://devimaakola.healthpole.com/', 'https://devimaakola.healthpole.com/offers',
    'https://devimaakola.healthpole.com/galleries', 'https://devimaakola.healthpole.com/abouts',
    'https://devimaakola.healthpole.com/contacts', 'https://devimaakola.healthpole.com/dashboards/forgot_password',
    'https://devimaakola.healthpole.com/digitalisations/sign_up'
    ]

staging_bmc = [
    'https://staging.bookmycme.com/', 'https://staging.bookmycme.com/events', 'https://staging.bookmycme.com/speakers',
    'https://staging.bookmycme.com/organizers', 'https://staging.bookmycme.com/#',
    'https://devorganizers.healthpole.com/accounts', 'https://devdoctors.healthpole.com/accounts',
    'https://www.bookmycme.com/cmes/127', 'https://www.bookmycme.com/cmes/137', 'https://www.bookmycme.com/events/109',
    'https://www.bookmycme.com/cmes/125', 'https://www.bookmycme.com/cmes/128', 'https://staging.bookmycme.com/cmes/310',
    'https://staging.bookmycme.com/cmes/316', 'https://staging.bookmycme.com/cmes/324', 'https://staging.bookmycme.com/cmes/319',
    'https://staging.bookmycme.com/cmes/328', 'https://staging.bookmycme.com/cmes/317', 'https://staging.bookmycme.com/cmes/318',
    'https://staging.bookmycme.com/cmes/323', 'https://staging.bookmycme.com/cmes/325', 'https://staging.bookmycme.com/cmes/326',
    'https://staging.bookmycme.com/contacts', 'https://staging.bookmycme.com/terms_of_use',
    'https://staging.bookmycme.com/privacy', 'https://www.facebook.com/bookmyCME', 'https://twitter.com/bookmycme',
    'https://www.instagram.com/bookmycme', 'https://staging.bookmycme.com/profiles/booking-history'
    ]

staging_bcd = [
    'https://devorganizers.healthpole.com/accounts', 'https://devdoctors.healthpole.com/accounts',
    'https://staging.bookmycde.com/#', 'https://staging.bookmycde.com/', 'https://staging.bookmycde.com/events',
    'https://staging.bookmycde.com/profiles/booking-history', 'https://staging.bookmycde.com/profiles/personal-information',
    'https://staging.bookmycde.com/profiles/change-password', 'https://staging.bookmycde.com/contact-us',
    'https://staging.bookmycde.com/accounts/logout', 'https://www.bookmycde.com/cdes/276',
    'https://www.bookmycde.com/cdes/293', 'https://www.bookmycde.com/cdes/278', 'https://www.bookmycde.com/cdes/268',
    'https://www.bookmycde.com/cdes/277', 'https://www.bookmycde.com/cdes/291',
    'https://staging.bookmycde.com/cdes/380', 'https://staging.bookmycde.com/cdes/379', 'https://staging.bookmycde.com/cdes/382',
    'https://staging.bookmycde.com/cdes/313', 'https://staging.bookmycde.com/cdes/298', 'https://staging.bookmycde.com/cdes/283',
    'https://staging.bookmycde.com/cdes/284', 'https://staging.bookmycde.com/cdes/276', 'https://staging.bookmycde.com/terms-of-use',
    'https://staging.bookmycde.com/privacy', 'https://www.facebook.com/bookmyCDE', 'https://twitter.com/bookmyCDE',
    'https://www.instagram.com/bookmyCDE', 'https://www.linkedin.com/showcase/bookmycde',
    ]

production_bmc = [
    'https://organizers.healthpole.com/accounts', 'https://doctors.healthpole.com/accounts', 'https://www.bookmycme.com/#',
    'https://www.bookmycme.com/', 'https://www.bookmycme.com/events', 'https://www.bookmycme.com/speakers',
    'https://www.bookmycme.com/organizers', 'https://www.bookmycme.com/profiles/booking-history','https://www.bookmycme.com/profiles/change-password',
    'https://www.bookmycme.com/contact-us', 'https://www.bookmycme.com/accounts/logout',
    'https://www.bookmycme.com/events/118', 'https://www.bookmycme.com/events/116', 'https://www.bookmycme.com/cmes/178',
    'https://www.bookmycme.com/cmes/290', 'https://www.bookmycme.com/cmes/289', 'https://www.bookmycme.com/cmes/294',
    'https://www.bookmycme.com/cmes/299', 'https://www.bookmycme.com/cmes/305', 'https://www.bookmycme.com/cmes/306',
    'https://www.bookmycme.com/cmes/301', 'https://www.bookmycme.com/cmes/304', 'https://www.bookmycme.com/cmes/302',
    'https://www.bookmycme.com/cmes/295', 'https://www.bookmycme.com/cmes/297', 'https://www.bookmycme.com/cmes/282',
    'https://www.bookmycme.com/cmes/286', 'https://www.bookmycme.com/cmes/285', 'https://www.bookmycme.com/cmes/288',
    'https://www.bookmycme.com/cmes/281', 'https://www.bookmycme.com/cmes/283', 'https://www.bookmycme.com/cmes/280',
    'https://www.bookmycme.com/cmes/200', 'https://www.bookmycme.com/cmes/272', 'https://www.bookmycme.com/cmes/275',
    'https://www.bookmycme.com/cmes/210', 'https://www.bookmycme.com/cmes/202', 'https://www.bookmycme.com/cmes/183',
    'https://www.bookmycme.com/cmes/203', 'https://www.bookmycme.com/cmes/214', 'https://www.bookmycme.com/cmes/208',
    'https://www.bookmycme.com/cmes/209', 'https://www.bookmycme.com/cmes/204', 'https://www.bookmycme.com/cmes/181',
    'https://www.bookmycme.com/cmes/189', 'https://www.bookmycme.com/cmes/188', 'https://www.bookmycme.com/cmes/141',
    'https://www.bookmycme.com/cmes/176', 'https://www.bookmycme.com/cmes/179', 'https://www.bookmycme.com/cmes/194',
    'https://www.bookmycme.com/cmes/171', 'https://www.bookmycme.com/cmes/180', 'https://www.bookmycme.com/cmes/175',
    'https://www.bookmycme.com/terms-of-use', 'https://www.bookmycme.com/privacy',
    'https://www.facebook.com/bookmyCME',   'https://twitter.com/bookmyCME',
    'https://www.instagram.com/bookmyCME', 'https://www.linkedin.com/showcase/bookmycme',
    ]

production_imaakola_url = [
    'https://www.imaakola.com/', 'https://www.imaakola.com/updates', 'https://www.imaakola.com/#',
    'https://www.imaakola.com/events', 'https://www.imaakola.com/office-bearers', 'https://www.imaakola.com/documents',
    'https://www.imaakola.com/jobs', 'https://www.imaakola.com/offers', 'https://www.imaakola.com/gallery',
    'https://www.imaakola.com/about-us', 'https://www.imaakola.com/contact-us', 'https://www.imaakola.com/events?past=true',
    'https://www.imaakola.com/dashboards/forgot-password', 'https://www.imaakola.com/digitalisations/sign-up',
    'https://www.imaakola.com/events/306/show?feed_type=Cme', 'https://www.imaakola.com/events/272/show?feed_type=Cme',
    'https://www.imaakola.com/events/163/show?feed_type=Cme', 'https://www.imaakola.com/events/176/show?feed_type=Cme',
    'https://www.imaakola.com/events/137/show?feed_type=Cme', 'https://www.imaakola.com/events/147/show?feed_type=Cme',
    'https://www.imaakola.com/gallery/2/gallery', 'https://www.imaakola.com/gallery/3/gallery',
    'https://www.imaakola.com/gallery/4/gallery', 'https://www.imaakola.com/gallery/38/gallery',
    'https://www.imaakola.com/gallery/44/gallery', 'http://tiny.cc/xxyt9y',
    ]

production_amravati = [
    'https://imaamravati.healthpole.com/','https://imaamravati.healthpole.com/updates',
    'https://imaamravati.healthpole.com/#','https://imaamravati.healthpole.com/events',
    'https://imaamravati.healthpole.com/office-bearers','https://imaamravati.healthpole.com/documents',
    'https://imaamravati.healthpole.com/jobs','https://imaamravati.healthpole.com/offers',
    'https://imaamravati.healthpole.com/gallery','https://imaamravati.healthpole.com/about-us',
    'https://imaamravati.healthpole.com/contact-us','https://imaamravati.healthpole.com/events?past=true',
    'https://imaamravati.healthpole.com/dashboards/forgot-password','https://imaamravati.healthpole.com/digitalisations/sign-up',
    ]

production_bcd = [
    'https://organizers.healthpole.com/accounts', 'https://doctors.healthpole.com/accounts',
    'https://www.bookmycde.com/#', 'https://www.bookmycde.com/',
    'https://www.bookmycde.com/events', 'https://www.bookmycde.com/profiles/booking-history', 'https://www.bookmycde.com/profiles/change-password',
    'https://www.bookmycde.com/contact-us', 'https://www.bookmycde.com/accounts/logout',
    'https://www.bookmycde.com/cdes/276', 'https://www.bookmycde.com/cdes/293', 'https://www.bookmycde.com/cdes/278',
    'https://www.bookmycde.com/cdes/268', 'https://www.bookmycde.com/cdes/277', 'https://www.bookmycde.com/cdes/291',
    'https://www.bookmycde.com/cdes/303', 'https://www.bookmycde.com/cdes/296', 'https://www.bookmycde.com/cdes/298',
    'https://www.bookmycde.com/cdes/300', 'https://www.bookmycde.com/cdes/151', 'https://www.bookmycde.com/cdes/216',
    'https://www.bookmycde.com/cdes/164', 'https://www.bookmycde.com/cdes/217', 'https://www.bookmycde.com/cdes/211',
    'https://www.bookmycde.com/cdes/213', 'https://www.bookmycde.com/cdes/205', 'https://www.bookmycde.com/cdes/160',
    'https://www.bookmycde.com/cdes/148', 'https://www.bookmycde.com/terms-of-use', 'https://www.bookmycde.com/privacy',
    'https://www.facebook.com/bookmyCDE', 'https://twitter.com/bookmyCDE', 'https://www.instagram.com/bookmyCDE',
    'https://www.linkedin.com/showcase/bookmycde'
    ]

def staging_akola():
    print(" ---- Finding broken link in staging imaakola ---- \n")
    for url in Staging_imaakola:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def staging_bookmycme():
    print(" ---- Finding broken link in staging bookmycme ---- \n")
    for url in staging_bmc:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def staging_bookmyde():
    print(" ---- Finding broken link in staging bookmycde ---- \n")
    for url in staging_bcd:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def production_bookmycme():
    print(" ---- Finding broken link in production bookmycme ---- \n")
    for url in production_bmc:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def production_imaakola():
    print(" ---- Finding broken link in production imaakola ---- \n")
    for url in production_imaakola_url:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def production_imaamravati():
    print(" ---- Finding broken link in production ima Amravati ---- \n")
    for url in production_amravati:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')

def production_bookmycde():
    print(" ---- Finding broken link in production bookmycde ---- \n")
    for url in production_bcd:
        response = requests.get(url)
        if response.status_code == 200:
            print(url,' - 200 OK!')
        elif response.status_code == 404:
            print(url,' - 404 Not Found! ')
        elif response.status_code == 500:
            print(url,' - Yooo Man We Got 500 -->  Need Backup..!')
    print('\n')


staging_akola()
staging_bookmycme()
staging_bookmyde()

production_bookmycme()
production_imaakola()
production_imaamravati()
production_bookmycde()