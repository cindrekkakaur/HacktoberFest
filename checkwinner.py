def checker(digit):
    global count, mark, digits
    if digit==1 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mar
        button1.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==2 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button2.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==3 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button3.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==4 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button4.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==5 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button5.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==6 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button6.config(text = mark)
        count = count+1
        sign 
if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==7 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button7.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==8 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button8.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==9 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button9.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()
  
    if(count>8 and win(panels,'X')==False and win(panels,'O')==False):
        msg.showinfo("Result","Match Tied")
        root.destroy()