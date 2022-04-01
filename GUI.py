from tkinter import *
import PerceptronAlgorithm


path = 'IrisData.txt'
dataset = PerceptronAlgorithm.read_data("./" + path)

tkint = Tk()
tkint.geometry("500x500")

def StartModel(feature1, feature2, class1, class2, learning_rate, num_of_epochs, biasyn):
    PerceptronAlgorithm.perceptron_Algorithm(dataset, feature1, feature2, class1, class2, learning_rate, num_of_epochs, biasyn)


#Features
feature1 = StringVar(tkint,"X1")
feature2 = StringVar(tkint,"X2")
list_of_features = ["X1", "X2", "X3", "X4"]
drop_menu_feature1 = OptionMenu(tkint, feature1, *list_of_features)
drop_menu_feature2 = OptionMenu(tkint, feature2, *list_of_features)
drop_menu_feature1.place(x=150, y=30)
drop_menu_feature2.place(x=250, y=30)

feature1_label = Label(text="Feature 1")
feature2_label= Label(text="Feature 2")
feature1_label.place(x=150,y=15)
feature2_label.place(x=250,y=15)

#Classes
class1 = StringVar(tkint,"Class1")
class2 = StringVar(tkint,"Class2")
drop_menu_all_class = ["Class1", "Class2", "Class3"]
drop_menu_class1= OptionMenu(tkint, class1, *drop_menu_all_class)
drop_menu_class2 = OptionMenu(tkint, class2, *drop_menu_all_class)
drop_menu_class1.place(x=150, y=100)
drop_menu_class2.place(x=250, y=100)
class1_label= Label(text="Class 1")
class2_label= Label(text="Class 2")
class1_label.place(x=150,y=80)
class2_label.place(x=250,y=80)


#Learning Rate
learning_rate_label = Label(text= "Learning Rate")
learning_rate_text = Text(tkint, height=1, width=18, bg="white")
learning_rate_label.place(x=190, y=160)
learning_rate_text.place(x=160, y=180)

#Number of epochs
num_of_epochs_label = Label(text= "Number of Epochs")
num_of_epochs_text = Text(tkint, height=1, width=18, bg="white")
num_of_epochs_label.place(x=180, y=200)
num_of_epochs_text.place(x=160, y=220)


#Bias
bias = StringVar(tkint,"Yes")
bias_label= Label(text= "Add Bias?")
drop_menu_bias= ["Yes", "No"]
drop_menu_bias_result= OptionMenu(tkint, bias, *drop_menu_bias)
bias_label.place(x=195,y=240)
drop_menu_bias_result.place(x=195,y=260)


#Button
start_button = Button(tkint, height = 2,width = 18, text ="Start The Algorithm",command = lambda:StartModel(feature1.get(), feature2.get(), class1.get(),
class2.get(),learning_rate_text.get("1.0"),num_of_epochs_text.get("1.0"),bias.get()))
start_button.place(x=160,y=300)

tkint.mainloop()