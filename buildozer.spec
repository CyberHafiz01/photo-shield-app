[app]
title = System Update
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1

# أضفنا النسخ والمكتبات الضرورية للاتصال بالإنترنت
requirements = python3==3.11.1,kivy,requests,urllib3,openssl

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.accept_sdk_license = True

# هذه الإعدادات هي التي طلبها السيرفر في صورك الأخيرة
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = 

# مستوى السجل لرؤية الأخطاء بوضوح
log_level = 2
p4a.branch = master
