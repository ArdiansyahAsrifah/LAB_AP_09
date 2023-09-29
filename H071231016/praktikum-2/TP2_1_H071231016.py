#Menghitung BMI yang dibedakan berdasarkan gendernya
beratBadan =float(input('masukkan nilai berat badan(kg) :'))
tinggiBadan=float(input('masukkan nilai tinggi badan(cm):'))
jenis_kelamin = input("pilih jenis kelamin anda [pria/wanita]:").lower()

tinggiBadan = tinggiBadan/100

bmi = beratBadan/(tinggiBadan)**2 #rumus BMI

if jenis_kelamin == "pria":
    if bmi < 18 :
        print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")
    elif 18 <= bmi <= 23.9 :
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi <= 26.9 :
        print (f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    else :
        print (f"Anda tergolong Obese dengan BMI {bmi:.2f}")

if jenis_kelamin == "wanita":
    if bmi < 17 :
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif 17 <= bmi <= 23.9:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi <= 27.9 :
        print(f" Anda tergolong Overweight dengan BMI {bmi:.2f}")
    else :
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")

else:
    print('Inputan tidak valid')





