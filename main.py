import time

def typing_speed(master_text):

    print(f"Refer below typing material:\n"
          f"{master_text}")

    word_count = len(master_text.split())

    t0 = time.time()

    written_text = input("START TYPING ABOVE PARAGRAPH:\n ")

    t1 = time.time()

    accuracy = len(set(written_text.split()) & set(master_text.split()))

    accuracy = (accuracy/word_count)*100

    time_taken = float (t1-t0)


    wpm = float(word_count/time_taken)

    return print(f"WPM        :{wpm} \n"
                 f"ACCURAY (%)   : {accuracy}\n"
                 f"TIME TAKEN : {time_taken}")










print("TYPING SPEED TEST\n")

Para = ("  A teacher's professional duties may extend beyond formal teaching. Outside of "
        "the classroom teachers may accompany students on field trips, supervise study halls, "
        "help with the organization of school functions, and serve as supervisors for extracurricular activities. "
        "In some education systems, teachers may have responsibility for student discipline.\n\n")






typing_speed(Para)



