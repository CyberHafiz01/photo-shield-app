name: Build APK

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # خطوة مهمة جداً لضمان وجود جافا التي يحتاجها أندرويد
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: Build with Buildozer
        # استخدمنا النسخة المستقرة والمحدثة ArtemSerebrennkov
        uses: ArtemSerebrennkov/buildozer-action@master
        with:
          command: buildozer android debug
          buildozer_version: master

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Abdu-Security-App
          path: bin/*.apk
