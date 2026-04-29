[app]
title = System Update
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,kivy,requests,certifi,urllib3
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 31
