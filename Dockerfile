# Використовуємо образ з JDK (компілятором), а не JRE
FROM eclipse-temurin:11-jdk-alpine

WORKDIR /app

# Копіюємо всі файли проекту
COPY . .

# Створюємо папку для скомпільованих файлів
RUN mkdir out

# Знаходимо всі .java файли і компілюємо їх у папку out
# Ця команда знайде файли навіть у підпапках (src/...)
RUN javac -d out $(find . -name "*.java")

# Відкриваємо порт
EXPOSE 8080

# ВАЖЛИВО: Заміни 'Main' на назву твого головного класу (де public static void main)
# Якщо клас в пакеті (наприклад package ua.knu;), пиши 'ua.knu.Main'
CMD ["java", "-cp", "out", "Main"]