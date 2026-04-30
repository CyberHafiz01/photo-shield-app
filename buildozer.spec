[app]
title = System Update
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,json
version = 0.1

# 1. تحديث المكتبات (أهم خطوة ليعمل البوت والإنترنت)
requirements = python3,kivy,telethon,requests,urllib3,openssl,certifi,chardet,idna

# 2. إضافة تصريح الوصول لحالة الشبكة
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# 3. دعم المعالجات (إضافة armeabi-v7a ليعمل على أغلب الهواتف)
android.archs = arm64-v8a, armeabi-v7a

# 4. إعدادات الـ SDK (api 34 هو الأفضل حالياً للتوافق)
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

# 5. تفعيل ميزة التثبيت لمرة واحدة لضمان عدم حدوث تعارض
android.skip_update_check = False
