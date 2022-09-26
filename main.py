from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
#import wavio as wv

root= Tk()
root.geometry("500x800+400+80")
root.resizable(False,False)
root.title("Voice Record")
root.configure(background="#AAF0D1")


def Record():
    global recording, start_time
    start_time= time.time()

    freq = 44100
    dur= int(duration.get())
    recording = sound.rec(dur*freq, samplerate= freq, channels=2)

    try:
        temp= int(duration.get())
    except:
        print("Please enter the right value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if (temp==0):
            messagebox.showinfo("Time Countdown", "Time's up")
        Label(text=f"{str(temp)}", font="arial 15", width=4, background="#4a4a4a").place(x=230, y=560)

    sound.wait()
    write("recording.wav",freq, recording)


# def stop_recording():
#     global recording
#     actual_time = time.time()-start_time
#     sound.stop()
#     samples = min(int(actual_time*sound.default.samplerate), len(recording))
#     recording = recording[0:samples, 0]
#     sound.play(recording)
#     sound.wait()
#     # get_axes().clear()
#     # spectrum, freqs, t, im = get_axes().specgram(recording,
#     #                                              Fs=sound.default.samplerate)
#     # redraw()
#     # return np.transpose(spectrum)




icon= PhotoImage(file="icon.png")
root.iconphoto(False,icon)


image = Image.open("icon.png")
resize_image = image.resize((250, 250), Image.ANTIALIAS )
bc_image = ImageTk.PhotoImage(resize_image)

background_photo=Label(image=bc_image,background="#AAF0D1").pack(padx=5, pady=5)


Label(text="Voice Record", font="arial 30 bold", background='#AAF0D1',fg='#2554C7' ).pack()


duration= StringVar()
entry= Entry(root, textvariable=duration, font="arial 30 bold",width=15).pack(pady=10)
Label(text="Enter Time in Seconds", font="arial 30 bold", background='#AAF0D1',fg='#2554C7' ).pack()



record_button= Button(root, font= "arial 20", text="RECORD", bg="#111111", fg="white", border=0, command=Record).pack(pady=30)

# stop_bt= Button(root, font= "arial 20", text="Stop", bg="#111111", fg="white", border=0, command=stop_recording).pack(pady=30)


root.mainloop()