***Temporary Files Cleaner***

This Python script is designed to clean specific temporary directories on a Windows machine, such as the Temp, Windows\Temp, and Prefetch folders. After cleaning these directories, it shows a message box using a VBScript to notify the user that the temporary files have been successfully deleted.

**Features**

Cleans the following directories:

*C:\Windows\Temp

*%TEMP%

*C:\Windows\Prefetch

Deletes files and folders inside these directories recursively.

Displays a message box after the cleaning process is complete.

**Requirements**

Windows operating system.

Python 3.x installed.

**Usage:**

1. Clone the repository:

$git clone https://github.com/YayForge/Clean-For-Windows.git

2. Run the Python script:

$python clean.py

After running the script, a message box will pop up notifying that the temporary files have been cleaned.

**Disclaimer**

This script is designed to be used with caution. Deleting files from system folders like Temp and Prefetch can impact the performance of certain applications.

Test the script in a safe environment before using it on production machines.

*******************************************************************************************************************************************************************************************************************************************************************************

***Geçici Dosya Temizleyici***

Bu Python betiği, Windows işletim sisteminde belirli geçici dizinleri temizlemek için tasarlanmıştır. Temp, Windows\Temp ve Prefetch klasörlerini temizler. Temizleme işleminden sonra bir mesaj kutusu görüntüleyerek geçici dosyaların başarıyla silindiğini kullanıcıya bildirir.

**Özellikler**

Aşağıdaki dizinleri temizler:

*C:\Windows\Temp

*%TEMP%

*C:\Windows\Prefetch

Bu dizinlerdeki dosya ve klasörleri özyinelemeli (recursive) olarak siler.

Temizleme işlemi tamamlandıktan sonra bir mesaj kutusu görüntüler.

**Gereksinimler**

Windows işletim sistemi.

Python 3.x kurulu olmalıdır.

**Kullanım**

1. Depoyu klonlayın:

$git clone https://github.com/YayForge/Clean-For-Windows.git

2. Python betiğini çalıştırın:

$python clean.py

Betiği çalıştırdıktan sonra, geçici dosyaların temizlendiğine dair bir mesaj kutusu açılacaktır.

**Uyarı**

Bu betik dikkatle kullanılmalıdır. Temp ve Prefetch gibi sistem klasörlerinden dosya silmek, bazı uygulamaların performansını etkileyebilir.

Betiği üretim ortamlarında kullanmadan önce güvenli bir ortamda test edin.
