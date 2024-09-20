import os
import shutil
import tempfile


temp_user = os.getenv('TEMP')  
temp = 'C:\\Windows\\Temp'     
prefetch = 'C:\\Windows\\Prefetch'  


def klasor_ici_temizle(klasor_yolu):
    
    if os.path.exists(klasor_yolu):
        
        for root, dirs, files in os.walk(klasor_yolu):
            for dosya in files:
                dosya_yolu = os.path.join(root, dosya)
                try:
                    os.remove(dosya_yolu)
                except Exception:
                    pass  
            for klasor in dirs:
                klasor_yolu = os.path.join(root, klasor)
                try:
                    shutil.rmtree(klasor_yolu)
                except Exception:
                    pass  


klasor_ici_temizle(temp)
klasor_ici_temizle(temp_user)
klasor_ici_temizle(prefetch)


def vbs_mesaj_kutusu():
    vbs_kodu = '''
    MsgBox "Gecici dosyalar" & vbCrLf & "temizlenmistir.", 262192, "By Yay"
    '''
    
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".vbs") as vbs_dosya:
        vbs_dosya.write(vbs_kodu.encode('utf-8'))
        vbs_dosya_yolu = vbs_dosya.name
    
    
    os.system(f'wscript "{vbs_dosya_yolu}"')


vbs_mesaj_kutusu()
