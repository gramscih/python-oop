from report_generator import ReportGeneretor

run = True
rpt = ReportGeneretor()

def generate_report(opt):
    if opt == '1':
        sicks = rpt.get_sicks()
        print("Patients that are sicks are:", sicks)
    if opt == '2':
        pass
    if opt == '3':
        pass
    if opt == '4':
        pass

while run:
    print("***********************************************************")
    print("1. All people sick")
    print("2. Classified by gender")
    print("3. Classified by Ege")
    print("4. Get a complete report")
    print("5. Exit")
    print("***********************************************************")
    opt = input("Select an option: ")
    if opt == '5':
        run = False
    else:
        generate_report(opt)
    