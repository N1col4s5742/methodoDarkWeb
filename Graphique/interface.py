from tkinter import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
from tkinter import ttk
import time

class MainWindow():

    def __init__(self, main):
        main.geometry("1470x700")
        # main.configure(background='grey')
        self.canvas = Canvas(main, width=640, height=480)
        self.canvas.grid(row=1, column = 0)
        self.MAX_SIZE = 60

        self.classificationCateg = []

        # images
        self.my_images = []
        self.my_images.append(PhotoImage(file = "./DW.png"))
        self.my_images.append(PhotoImage(file="./resume.png"))
        self.my_images.append(PhotoImage(file="./analyze.png"))

        self.my_image_number = 0

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images[self.my_image_number])

        # button to change image
        self.button = Button(main, text="Valider", command=self.onButton, width = 20, height = 3, font = "Helvetica 12 bold italic")
        self.button.grid(row=2, column = 1,sticky=W)

        self.var = StringVar(main)
        #self.var.set("metz")  # initial value

        self.listSites = []
        self.fillInListSites()
        # self.option = OptionMenu(main, self.var, *self.listSites)
        # self.option.grid(row=2, column = 0)

        self.labelPresentation = Label(main, text="IR DARK WEB", font = "Helvetica 16 bold italic")
        self.labelPresentation.grid(row=0, sticky=W, columnspan = 2)
        self.labelInfos = Label(main, text="", font="Helvetica 16 bold italic", justify="left")
        self.labelInfos.grid(row=1, column = 1)

        self.comboBoxSites = ttk.Combobox(main,values=self.listSites, width = 78, height = 9)
        self.comboBoxSites.grid(row=2, column=0, sticky=NE)
        self.labelDate = Label(main, text="Entrer une date (ex : 29/04/19) : ")
        self.labelDate.grid(row=3, column=0, sticky=E)
        v = StringVar(root, value=str(time.strftime("%d/%m/%Y")))
        self.entryDate = Entry(main, bd=5, text="text")
        self.entryDate.grid(row=4, column=0, sticky=E)
        self.entryDate.delete(0, END)
        self.entryDate.insert(0, str(time.strftime("%d/%m/%Y")))
        self.buttonDate = Button(main, text="OK", command=self.sitePerDate, width=20, height=1,
                             font="Helvetica 12 bold italic")
        self.buttonDate.grid(row=4, column=1, sticky=W)
        self.buttonRecap = Button(main, text="Résumé", command=self.resumeDatas, width=20, height=1,
                                 font="Helvetica 12 bold italic")
        self.buttonRecap.grid(row=5, column=1, sticky=W)

    # def createDiagram(self,adu, vir, cri, mar, dru, oth):
    def createDiagram(self, dictionaryClassification):
        #data = {'Adult': int(adu), 'Virus': int(vir), 'Crime': int(cri), 'Market': int(mar), 'Drugs': int(dru), 'Other':oth}
        data = dictionaryClassification
        names = list(data.keys())
        values = list(data.values())

        colors = ['pink', 'black', 'grey', 'gold', 'lightskyblue','red', 'green']
        patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, names, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('./analyze.png')
        plt.close()
        # plt.show()

    def createDiagramResume(self, dictionnaryClassification):
        data = dictionnaryClassification
        names = list(data.keys())
        values = list(data.values())

        colors = ['pink', 'black', 'grey', 'gold', 'lightskyblue', 'red', 'green']
        plt.pie(values, colors=colors, labels=values, counterclock=False, shadow=True)
        plt.title('Résumé des sites collectés')
        plt.legend(names, loc='best')
        plt.savefig('./resume.png')
        plt.close()

    def sitePerDate(self):
        self.listSites[:] = []
        if(self.entryDate.get()=="" or self.entryDate.get()=="all"):
            self.fillInListSites()
        else:
            falseDate = True
            with open("../wordClassification/classification.txt") as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    if data[key]["info"]['date'] == self.entryDate.get():
                        falseDate = False
                        self.listSites.append(key)
            if falseDate == True:
                self.fillInListSites()
        self.comboBoxSites.config(values=self.listSites)

    def onButton(self):
        if len(self.comboBoxSites.get()) >= self.MAX_SIZE:
            self.labelPresentation['text']="Site analysé : " +self.comboBoxSites.get()[0:110]+"..."
        else:
            self.labelPresentation['text']="Site analysé : " +self.comboBoxSites.get()
        self.classificationCateg = self.fillInCategory(str(self.comboBoxSites.get()))
        self.labelInfos['text'] = self.fillInInfos(self.comboBoxSites.get())
        self.createDiagram(self.classificationCateg)
        self.my_images[2] = (PhotoImage(file="./analyze.png"))
        self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[2])

    def resumeDatas(self):
        self.labelPresentation['text'] = "Résumé des sites analysés"
        nbSites = 0
        chaine = "Résumé des sites analysés : \n"
        dict_resume = {}
        dict_resume["Virus"] = 0
        dict_resume["Adult"] = 0
        dict_resume["Money"] = 0
        dict_resume["Market"] = 0
        dict_resume["Crime"] = 0
        dict_resume["Drug"] = 0
        dict_resume["Other"] = 0
        with open("../wordClassification/classification.txt") as json_file:
            data = json.load(json_file)
            for key in data.keys():
                nbSites = nbSites +1
                for categ in data[key]["classification"]:
                    dict_resume[categ]+=int(data[key]["classification"][categ])
        self.createDiagramResume(dict_resume)
        self.my_images[1] = (PhotoImage(file="./resume.png"))
        self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[1])
        for cat in dict_resume:
            chaine += cat + " --> " + str(dict_resume[cat]) + " occurences \n"
        chaine += "Nombre de sites analysés : " + str(nbSites) + " \n"
        self.labelInfos['text'] = chaine

    def fillInCategory(self,nameSite):
        with open("../wordClassification/classification.txt") as json_file:
            data = json.load(json_file)
            return data[nameSite]['classification']

    def fillInListSites(self):
        with open("../wordClassification/classification.txt") as json_file:
            data = json.load(json_file)
            for key in data.keys():
                self.listSites.append(key)

    def fillInInfos(self, nameSite):
        chaine = ""
        with open("../wordClassification/classification.txt") as json_file:
            data = json.load(json_file)
            for key in data[nameSite]['info']:
                if key == "name":
                    if len(data[nameSite]['info'][key])>self.MAX_SIZE:
                        chaine += key + " : " + data[nameSite]['info'][key][0:self.MAX_SIZE]+"..." + "\n"
                    else:
                        chaine += key + " : " + data[nameSite]['info'][key] + "\n"
                else:
                    chaine += key + " : " + data[nameSite]['info'][key] + "\n"
            chaine += "-------------------------------\n"
            for key in data[nameSite]['keywords']:
                chaine += key + " : " + str(data[nameSite]['keywords'][key]['occurrences']) + " occurences \n"
        return chaine

root = Tk()
MainWindow(root)
root.mainloop()


