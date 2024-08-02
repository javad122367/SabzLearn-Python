# 1- دریافت رشته از کاربر ! نمایش تعداد جملات ، کلمات ، کاراکترها ، تعداد حروف انگلیسی
print("Task1 : Get string from user & Display number of sentences, words, characters & number of English letters \n")
get_String = input("Please write a Text: ")
sentence_Counter = get_String.count(".") + get_String.count("?") + get_String.count("!") + get_String.count(";") # بررسی تعداد جملات با استفاده از نقطه باتوجه به اینکه پایان جملات را نقطه گذاری می کنند
word_Separator = get_String.split(" ") #  شناسایی جدا کننده کلمات از هم و ریختن کلمات در یک لیست
word_Counter = len(word_Separator) - word_Separator.count("")  # شمارش تعداد ایندکسهای لیست کلمات
character_Counter = len(get_String) # شمارش تمامی کاراکترهای رشته
leters_Counter = character_Counter - (get_String.count(".")+
                                      get_String.count(" ")+
                                      get_String.count(";")+
                                      get_String.count("!")+
                                      get_String.count("?")+
                                      get_String.count(",")+
                                      get_String.count("0")+
                                      get_String.count("1")+
                                      get_String.count("2")+
                                      get_String.count("3")+
                                      get_String.count("4")+
                                      get_String.count("5")+
                                      get_String.count("6")+
                                      get_String.count("7")+
                                      get_String.count("8")+
                                      get_String.count("9"))

char_find = get_String.lower() # تبدیل کل حروف رشته به حروف کوچک جهت شناسایی کاراکترهای خاص حرفی
print(f"Number of Sentences: {sentence_Counter}")
print(f"Number of Words: {word_Counter}")
print(f"Number of All characters: {character_Counter}")
print(f"Number of All EnglishLeters: {leters_Counter}")
print(f"Number of 'a': {char_find.count('a')}")
print(f"Number of 'd': {char_find.count('d')}")
print(f"Number of 'f': {char_find.count('f')}")
print("-------------------------------------------------------")

# 2 - دریافت کاراکتر از کاربر و چاپ یونیکد آن در خروجی
print("Task2: Get a character from user and print Unicode of this \n")
get_Character = input("Enter a character: ")
print(f"The Unicode of {get_Character} is {ord(get_Character)}")
print("-------------------------------------------------------")

# 3- دریافت شماره تلفن از کاربر و چک کردن اینکه آیا کاربر فقط عدد وارد کرده یا خیر
print("Task3 : Get phone number from user and check it's a number or not \n")
get_PhoneNumber = input("Enter a your Phone Number: ")
is_numeric = get_PhoneNumber.isnumeric()
print(is_numeric)