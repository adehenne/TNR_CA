import csv

with open('D:\_Formation Testeur Logiciel ISTQB\Supports de cours\\12-Automatiser avec Selenium et Webdriver\TP\TP1\TP01_Selenium_Webdriver\TP1_Exo4\Pairwise_CURAHealthcare_RDV.csv', newline='') as csvfile:
    appointments = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(appointments)
    for row in appointments:
        print(row[1].split()[0])
