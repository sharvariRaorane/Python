from tkinter import *
import tkinter
import pyqrcode
import png
from fpdf import FPDF

class PDFCV(FPDF):

    def header(self):
        self.image("Github.png",10,8,33,title ="Github")

    def footer(self):
        pass
    
    def generate_CV(self,name,email,phone,address,link,skills,work,education,abotme):
        self.add_page()
        self.ln(20)

        #Displaying name
        self.set_font("Arial","B",26)
        self.cell(0,10,name,new_x="LMARGIN",new_y="Next",align="C")

        #Contact information
        self.set_font("Arial","B",12)
        self.cell(0,10,"Contact Information",new_x="LMARGIN",new_y="Next",align="L")

        self.set_font("Arial","",10)
        self.cell(0,5,"Email: {}".format(email),new_x="LMARGIN",new_y="Next")
        self.set_font("Arial","",10)
        self.cell(0,5,"Phone: {}".format(phone),new_x="LMARGIN",new_y="Next")
        self.set_font("Arial","",10)
        self.cell(0,5,"Address: {}".format(address),new_x="LMARGIN",new_y="Next")

        #Adding skills
        self.ln(10)
        self.set_font("Arial","B",12)
        self.cell(0,10,"Skills",new_x="LMARGIN",new_y="Next",align="L")
        for skill in skills:
            self.cell(0,5," - {}".format(skill),new_x="LMARGIN",new_y="Next")

        #Adding work experience
        self.ln(10)
        self.set_font("Arial","B",12)
        self.cell(0,10,"Work Experience",new_x="LMARGIN",new_y="Next",align="L")
        for experience in work:
            self.cell(0,5,"{}: {}".format(experience['Designation'],experience['Responsibilities']),new_x="LMARGIN",new_y="Next")

        #Adding education
        self.ln(10)
        self.set_font("Arial","B",12)
        self.cell(0,10,"education",new_x="LMARGIN",new_y="Next",align="L")
        for ed in education:
            self.cell(0,5,"{}: {}".format(ed['Degree'],ed['University']),new_x="LMARGIN",new_y="Next")

        #Adding aboutMe
        self.ln(10)
        self.set_font("Arial","B",12)
        self.cell(0,10,"About ME",new_x="LMARGIN",new_y="Next",align="L")
        self.multi_cell(0,5,abotme)

        self.output("cv.pdf")
        

def generateCVPDF():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    link = entry_link.get()
    skills = entry_skills.get("1.0",END).strip().split('\n')
    work = []
    education = []

    work_experience_lines = entry_experience.get("1.0",END).strip().split('\n')
    for line in work_experience_lines:
        designation,responsibilities =  line.split(":")
        work.append({"Designation":designation.strip(),"Responsibilities":responsibilities.strip()})

    print(work)

    education_lines = entry_education.get("1.0",END).strip().split('\n')
    for line in education_lines:
        degree,university =  line.split(":")
        education.append({"Degree":degree.strip(),"University":university.strip()})
    
    print(education)

    abotme =    entry_about.get("1.0",END)

    #Create QRCode
    qrcode = pyqrcode.create(link)
    qrcode.png("Github.png",scale = 6)

    if not name or not email or not phone or not address or not link or not skills or not education or not work or not abotme:
        tkinter.messagebox.showerror("Error","Please fill in all details")
        return
    
    cv = PDFCV()
    cv.generate_CV(name,email,phone,address,link,skills,work,education,abotme)

# UI
window = Tk()
window.title("CV Generator")

label_name = Label(window,text="Name:")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window,text="Email:")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone = Label(window,text="Phone:")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(window,text="Address:")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_link = Label(window,text="Github Link:")
label_link.pack()
entry_link = Entry(window)
entry_link.pack()

label_skills = Label(window,text="Skills(Enter one Skill per line)")
label_skills.pack()
entry_skills = Text(window,height=5)
entry_skills.pack()

label_education = Label(window,text="Education(Enter one per line format Degree:University)")
label_education.pack()
entry_education = Text(window,height=5)
entry_education.pack()

label_experience = Label(window,text="Work Experience(Enter one per line format Designation:Responsibilities)")
label_experience.pack()
entry_experience = Text(window,height=5)
entry_experience.pack()

label_about = Label(window,text="About Me:")
label_about.pack()
entry_about = Text(window,height=5)
entry_about.pack()

button_generate = Button(window,text="Generate CV",command=generateCVPDF)
button_generate.pack()

window.mainloop()