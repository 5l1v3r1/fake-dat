import tkinter as tk
from faker import Faker
from bidi.algorithm import get_display
import arabic_reshaper as ar




root = tk.Tk()
root.title("gui generate fake data")
root.geometry("550x650")
root.resizable(0,0)
root.config(bg="#313654")


tk.Label(root, text="Fake Data", fg="black", bg="#313654",font=("Arial", 25)).place(x=190, y=10)

tk.Label(root, text="github :  https://github.com/XDGER", bg="#313654", fg="white", font=("Arial", 8)).place(x=370, y=630)


tk.Label(root, text="Enter Country for Fake Data  : ", fg="#31f3a8", bg="#313654").place(x=10, y=140)

answ = tk.StringVar()
ent = tk.Entry(root , textvariable=answ, width=20, bg='#3123c3', fg='black')
ent.place(x=220, y=140)




st = tk.Label(root, fg="#f4f383", bg="#313654")


def chek():
    if ent.get() in ['ar_AE', 'ar_BH', 'ar_EG', 'ar_JO', 'ar_AA', 'ar_SA', 'ar_PS']:
        fake = Faker(['ar_AE', 'ar_BH', 'ar_EG', 'ar_JO', 'ar_AA', 'ar_SA', 'ar_PS'])
        tex1 = f' First name :  {fake.first_name()} \n \n Last name :  {fake.last_name()} \n \n Date of Birth :  {fake.date_of_birth()} \n \n Address :  {fake.address()} \n \n Country :  {fake.country()} \n \n Zipcode :  {fake.zipcode()} \n \n Email :  {fake.email()}'
        text1 = get_display(ar.reshape(tex1))
        st.config(text=text1)
        st.place(x=15, y=200)
    
    elif ent.get() in ['bs_BA', 'bg_BG', 'bn_BD','bs_BA']:
        fake1 = Faker(['bs_BA', 'bg_BG', 'bn_BD','bs_BA'])
        st.config(text=f' First name :  {fake1.first_name()} \n \n Last name :  {fake1.last_name()} \n \n Date of Birth :  {fake1.date_of_birth()} \n \n Address :  {fake1.address()} \n \n Country :  {fake1.country()} \n \n Zipcode :  {fake1.zipcode()} \n \n Email :  {fake1.email()}')
        st.place(x=15, y=200)

    elif ent.get() == 'cs_CZ':
        fake2 = Faker('cs_CZ')
        st.config(text=f' First name :  {fake2.first_name()} \n \n Last name :  {fake2.last_name()} \n \n Date of Birth :  {fake2.date_of_birth()} \n \n Address :  {fake2.address()} \n \n Country :  {fake2.country()} \n \n Email :  {fake2.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['da_DK', 'de', 'de_AT', 'de_CH', 'de_DE', 'dk_DK']:
        fake3 = Faker(['da_DK', 'de', 'de_AT', 'de_CH', 'de_DE', 'dk_DK'])
        st.config(text=f' First name :  {fake3.first_name()} \n \n Last name :  {fake3.last_name()} \n \n Date of Birth :  {fake3.date_of_birth()} \n \n Address :  {fake3.address()} \n \n Country :  {fake3.country()} \n \n Zipcode :  {fake3.zipcode()} \n \n Email :  {fake3.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['el_CY', 'el_GR']:
        fake4 = Faker(['el_CY', 'el_GR'])
        st.config(text=f' First name :  {fake4.first_name()} \n \n Last name :  {fake4.last_name()} \n \n Date of Birth :  {fake4.date_of_birth()} \n \n Address :  {fake4.address()} \n \n Country :  {fake4.country()} \n \n Zipcode :  {fake4.zipcode()} \n \n Email :  {fake4.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['en', 'en_AU', 'en_CA', 'en_GB', 'en_IE', 'en_IN', 'en_NZ', 'en_PH', 'en_TH', 'en_US']:
        fake5 = Faker(['en', 'en_AU', 'en_CA', 'en_GB', 'en_IE', 'en_IN', 'en_NZ', 'en_PH', 'en_TH', 'en_US'])
        st.config(text=f' First name :  {fake5.first_name()} \n \n Last name :  {fake5.last_name()} \n \n Date of Birth :  {fake5.date_of_birth()} \n \n Address :  {fake5.address()} \n \n Country :  {fake5.country()} \n \n Zipcode :  {fake5.zipcode()} \n \n Email :  {fake5.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['es', 'es_CA', 'es_CL', 'es_CO', 'es_ES', 'es_MX', 'et_EE']:
        fake6 = Faker(['es', 'es_CA', 'es_CL', 'es_CO', 'es_ES', 'es_MX', 'et_EE'])
        st.config(text=f' First name :  {fake6.first_name()} \n \n Last name :  {fake6.last_name()} \n \n Date of Birth :  {fake6.date_of_birth()} \n \n Address :  {fake6.address()} \n \n Country :  {fake6.country()} \n \n Zipcode :  {fake6.zipcode()} \n \n Email :  {fake6.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['fi_FI', 'fil_PH']:
        fake7 = Faker(['fi_FI', 'fil_PH'])
        st.config(text=f' First name :  {fake7.first_name()} \n \n Last name :  {fake7.last_name()} \n \n Date of Birth :  {fake7.date_of_birth()} \n \n Address :  {fake7.address()} \n \n Country :  {fake7.country()} \n \n Email :  {fake7.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'fa_IR':
        fake8 = Faker('fa_IR')
        tex2 = f' First name :  {fake8.first_name()} \n \n Last name :  {fake8.last_name()} \n \n Date of Birth :  {fake8.date_of_birth()} \n \n Address :  {fake8.address()} \n \n Country :  {fake8.country()} \n \n Email :  {fake8.email()}'
        text2 = get_display(ar.reshape(tex2))
        st.config(text=text2)
        st.place(x=15, y=200)
    
    elif ent.get() in ['fr_CA', 'fr_CH', 'fr_FR', 'fr_QC']:
        fake9 = Faker(['fr_CA', 'fr_CH', 'fr_FR', 'fr_QC'])
        st.config(text=f' First name :  {fake9.first_name()} \n \n Last name :  {fake9.last_name()} \n \n Date of Birth :  {fake9.date_of_birth()} \n \n Address :  {fake9.address()} \n \n Country :  {fake9.country()} \n \n Zipcode :  {fake9.zipcode()} \n \n Email :  {fake9.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'ga_IE':
        fake10 = Faker('ga_IE')
        st.config(text=f' First name :  {fake10.first_name()} \n \n Last name :  {fake10.last_name()} \n \n Date of Birth :  {fake10.date_of_birth()} \n \n Address :  {fake10.address()} \n \n Country :  {fake10.country()} \n \n Zipcode :  {fake10.zipcode()} \n \n Email :  {fake10.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['he_IL', 'hr_HR', 'hu_HU', 'hy_AM']:
        fake11 = Faker(['he_IL', 'hr_HR', 'hu_HU', 'hy_AM'])
        st.config(text=f' First name :  {fake11.first_name()} \n \n Last name :  {fake11.last_name()} \n \n Date of Birth :  {fake11.date_of_birth()} \n \n Address :  {fake11.address()} \n \n Country :  {fake11.country()} \n \n Email :  {fake11.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'hi_IN':
        fake12 = Faker('hi_IN')
        st.config(text=f' First name :  {fake12.first_name()} \n \n Last name :  {fake12.last_name()} \n \n Date of Birth :  {fake12.date_of_birth()} \n \n Address :  {fake12.address()} \n \n Country :  {fake12.country()} \n \n Email :  {fake12.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'id_ID':
        fake13 = Faker('id_ID')
        st.config(text=f' First name :  {fake13.first_name()} \n \n Last name :  {fake13.last_name()} \n \n Date of Birth :  {fake13.date_of_birth()} \n \n Address :  {fake13.address()} \n \n Country :  {fake13.country()} \n \n Email :  {fake13.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['ja_JP', 'ka_GE', 'ko_KR']:
        fake14 = Faker(['ja_JP', 'ka_GE', 'ko_KR'])
        st.config(text=f' First name :  {fake14.first_name()} \n \n Last name :  {fake14.last_name()} \n \n Date of Birth :  {fake14.date_of_birth()} \n \n Address :  {fake14.address()} \n \n Country :  {fake14.country()} \n \n Zipcode :  {fake14.zipcode()} \n \n Email :  {fake14.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['la', 'lb_LU', 'lt_LT', 'lv_LV', 'mt_MT']:
        fake15 = Faker(['la', 'lb_LU', 'lt_LT', 'lv_LV', 'mt_MT'])
        st.config(text=f' First name :  {fake15.first_name()} \n \n Last name :  {fake15.last_name()} \n \n Date of Birth :  {fake15.date_of_birth()} \n \n Address :  {fake15.address()} \n \n Country :  {fake15.country()} \n \n Zipcode :  {fake15.zipcode()} \n \n Email :  {fake15.email()}')
        st.place(x=15, y=200)

    elif ent.get() in ['ne_NP', 'nl_BE', 'nl_NL', 'no_NO', 'or_IN']:
        fake16 = Faker(['ne_NP', 'nl_BE', 'nl_NL', 'no_NO', 'or_IN'])
        st.config(text=f' First name :  {fake16.first_name()} \n \n Last name :  {fake16.last_name()} \n \n Date of Birth :  {fake16.date_of_birth()} \n \n Address :  {fake16.address()} \n \n Country :  {fake16.country()} \n \n Zipcode :  {fake16.zipcode()} \n \n Email :  {fake16.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['pl_PL', 'pt_BR', 'pt_PT']:
        fake17 = Faker(['pl_PL', 'pt_BR', 'pt_PT'])
        st.config(text=f' First name :  {fake17.first_name()} \n \n Last name :  {fake17.last_name()} \n \n Date of Birth :  {fake17.date_of_birth()} \n \n Address :  {fake17.address()} \n \n Country :  {fake17.country()} \n \n Email :  {fake17.email()}')
        st.place(x=15, y=200)

    elif ent.get() == 'ro_RO':
        fake18 = Faker('ro_RO')
        st.config(text=f' First name :  {fake18.first_name()} \n \n Last name :  {fake18.last_name()} \n \n Date of Birth :  {fake18.date_of_birth()} \n \n Address :  {fake18.address()} \n \n Country :  {fake18.country()} \n \n Email :  {fake18.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'ru_RU':
        fake19 = Faker('ru_RU')
        st.config(text=f' First name :  {fake19.first_name()} \n \n Last name :  {fake19.last_name()} \n \n Date of Birth :  {fake19.date_of_birth()} \n \n Address :  {fake19.address()} \n \n Country :  {fake19.country()} \n \n Email :  {fake19.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'sk_SK':
        fake20 = Faker('sk_SK')
        st.config(text=f' First name :  {fake20.first_name()} \n \n Last name :  {fake20.last_name()} \n \n Date of Birth :  {fake20.date_of_birth()} \n \n Address :  {fake20.address()} \n \n Country :  {fake20.country()} \n \n Email :  {fake20.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['sl_SI', 'sq_AL', 'sv_SE']:
        fake21 = Faker(['sl_SI', 'sq_AL', 'sv_SE'])
        st.config(text=f' First name :  {fake21.first_name()} \n \n Last name :  {fake21.last_name()} \n \n Date of Birth :  {fake21.date_of_birth()} \n \n Address :  {fake21.address()} \n \n Country :  {fake21.country()} \n \n Zipcode :  {fake21.zipcode()} \n \n Email :  {fake21.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['th', 'th_TH']:
        fake22 = Faker(['th', 'th_TH'])
        st.config(text=f' First name :  {fake22.first_name()} \n \n Last name :  {fake22.last_name()} \n \n Date of Birth :  {fake22.date_of_birth()} \n \n Address :  {fake22.address()} \n \n Country :  {fake22.country()} \n \n Email :  {fake22.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['tr_TR', 'az_AZ']:
        fake23 = Faker(['tr_TR', 'az_AZ'])
        st.config(text=f' First name :  {fake23.first_name()} \n \n Last name :  {fake23.last_name()} \n \n Date of Birth :  {fake23.date_of_birth()} \n \n Address :  {fake23.address()} \n \n Country :  {fake23.country()} \n \n Zipcode :  {fake23.zipcode()} \n \n Email :  {fake23.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'tw_GH':
        fake24 = Faker('tw_GH')
        st.config(text=f' First name :  {fake24.first_name()} \n \n Last name :  {fake24.last_name()} \n \n Date of Birth :  {fake24.date_of_birth()} \n \n Address :  {fake24.address()} \n \n Country :  {fake24.country()} \n \n Zipcode :  {fake24.zipcode()} \n \n Email :  {fake24.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'uk_UA':
        fake25 = Faker('uk_UA')
        st.config(text=f' First name :  {fake25.first_name()} \n \n Last name :  {fake25.last_name()} \n \n Date of Birth :  {fake25.date_of_birth()} \n \n Address :  {fake25.address()} \n \n Country :  {fake25.country()} \n \n Email :  {fake25.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() == 'vi_VN':
        fake26 = Faker('vi_VN')
        st.config(text=f' First name :  {fake26.first_name()} \n \n Last name :  {fake26.last_name()} \n \n Date of Birth :  {fake26.date_of_birth()} \n \n Address :  {fake26.address()} \n \n Country :  {fake26.country()} \n \n Zipcode :  {fake26.zipcode()} \n \n Email :  {fake26.email()}')
        st.place(x=15, y=200)
    
    elif ent.get() in ['zh_CN', 'zh_TW']:
        fake27 = Faker(['zh_CN', 'zh_TW'])
        st.config(text=f' First name :  {fake27.first_name()} \n \n Last name :  {fake27.last_name()} \n \n Date of Birth :  {fake27.date_of_birth()} \n \n Address :  {fake27.address()} \n \n Country :  {fake27.country()} \n \n Email :  {fake27.email()}')
        st.place(x=15, y=200)


    else:
        st.config(text="chose this :  \n \n ar_AA - ar_AE - ar_BH - ar_EG - ar_JO - ar_PS - ar_SA \n \n az_AZ - bg_BG - bn_BD - bs_BA - cs_CZ - da_DK - de \n \n de_AT - de_CH - de_DE - dk_DK - el_CY - el_GR - en \n \n en_AU - en_CA - en_GB - en_IE - en_IN - en_NZ - en_PH \n \n en_TH - en_US - es - es_CA - es_CL - es_CO - es_ES \n \n es_MX - et_EE - fa_IR - fi_FI - fil_PH - fr_CA - fr_CH \n \n fr_FR - fr_QC - ga_IE - he_IL - hi_IN - hr_HR - hu_HU \n \n hy_AM - id_ID - ja_JP - ka_GE - ko_KR \n \n la - lb_LU - lt_LT - lv_LV - mt_MT - ne_NP - nl_BE \n \n nl_NL - no_NO - or_IN - pl_PL - pt_BR - pt_PT - ro_RO \n \n ru_RU - sk_SK - sl_SI - sq_AL - sv_SE - th \n \n th_TH - tr_TR - tw_GH - uk_UA - vi_VN - zh_CN - zh_TW", bg="#313654")
        st.place(x=10, y=180)


btn = tk.Button(root, text="Click", fg="black", bg="green", command=chek)
btn.place(x=385, y=136)




root.mainloop()
