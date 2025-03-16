print("habit tracker")
print("Let's setup your habit tracker!")
print("type 'y' for yes and 'n' for no")
jog_aim = None
book_aim = None
gym_aim = None
study_aim = None

d_jog = input("Do you wanna add a jogging track?: ").lower()
if d_jog == "y":
    jog_aim = int(input("How many kms do you aim to jog a day?: "))

d_book = input("Do you wanna add a book reading track?: ").lower()
if d_book == "y":
    book_aim = int(input("How many pages do you aim to read a day?: "))

d_gym = input("Do you wanna add a gym track?: ").lower()
if d_gym == "y":
    gym_aim = int(input("How many hours do you aim to workout a day?: "))

d_study = input("Do you wanna add a study track?: ").lower()
if d_study == "y":
    study_aim = int(input("How many hours do you aim to study a day?: "))
def habit_tracker():
    jog = int(input("How many kms did you jog today?: ")) if jog_aim is not None else None
    book = int(input("How many pages did you read today?: ")) if book_aim is not None else None
    gym = int(input("How many hours did you workout today?: ")) if gym_aim is not None else None
    study = int(input("How many hours did you study today?: ")) if study_aim is not None else None
    return study, book, gym, jog
study, book, gym, jog = habit_tracker()
print(":::::::::::::::::::::::::PROGRESS SHEET::::::::::::::::::::::::")
if study_aim is not None and study is not None:
    stud_per = round(study / study_aim * 100)
    print(f"STUDYING: You have studied {study} hours today. {stud_per}% TARGET ACHIEVED!")

if gym_aim is not None and gym is not None:
    gym_per = round(gym / gym_aim * 100)
    print(f"WORKOUT: You have worked-out {gym} hours today. {gym_per}% TARGET ACHIEVED!")

if jog_aim is not None and jog is not None:
    jog_per = round(jog / jog_aim * 100)
    print(f"JOGGING: You have jogged {jog} kms today. {jog_per}% TARGET ACHIEVED!")

if book_aim is not None and book is not None:
    read_per = round(book / book_aim * 100)
    print(f"BOOK-READING: You have read {book} pages today. {read_per}% TARGET ACHIEVED!")
