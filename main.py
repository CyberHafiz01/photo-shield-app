
name: Final Build
on: [push]

jobs:
  build:
    runs-on: ubuntu-20.04  # هذا هو السر، نظام مستقر جداً
    steps:
      - uses: actions/checkout@v4

      - name: Build with Buildozer
        uses: kivy/buildozer-action@master
        with:
          command: buildozer android debug
          buildozer_version: master

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Fixed-APK
          path: bin/*.apk
