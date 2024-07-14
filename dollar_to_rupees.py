from tkinter import * 
from tkinter.messagebox import * 
from requests import * 

root = Tk()
root.title("Live CC by harshvardhan")
root.geometry("600x400+50+50")
f = ("Arial", 30, "bold")

lab_header = Label(root, text="Live CC by harshvardhan", font=f)

def convert():
	try:
		wa = "https://api.exchangerate-api.com/v4/latest/USD"
		res = get(wa)
		data = res.json()
		DOLLAR = data["rates"]["INR"]
		dollars = float(ent_amt.get())
		rupees = dollars * DOLLAR
		msg = "\u20b9" + str(round(rupees, 2))
		showinfo("Result", msg)
	except ValueError:
		showerror("issue", "u did not enter amt")
	except Exception as e:
		showerror("issue ", e)


lab_amt = Label(root, text="Enter amt in $$", font=f)
ent_amt = Entry(root, font=f)
btn_convert = Button(root, text="Convert", font=f, command=convert)

lab_header.pack(pady=20)
lab_amt.pack(pady=10)
ent_amt.pack(pady=10)
btn_convert.pack(pady=10)

root.mainloop()