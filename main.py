name: Build APK
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build with Buildozer
        # استخدمنا هنا النسخة المستقرة والمباشرة
        uses: ArtemSBulat/buildozer-action@v1
        with:
          command: buildozer android clean debug
          buildozer_version: master

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-app-apk
          path: bin/*.apk
