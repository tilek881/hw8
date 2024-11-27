import sqlite3


def connect_db():
    conn = sqlite3.connect("hw.db")
    return conn


def show_cities():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities;")
    cities = cursor.fetchall()
    conn.close()
    return cities

def show_students_by_city(city_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?;
    """, (city_id,))
    students = cursor.fetchall()
    conn.close()

    if students:
        for student in students:
            print(f"{student[0]} {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} км²")
    else:
        print("Нет учеников в этом городе.")

def main():
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cities = show_cities()
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    city_id = int(input("\nВведите id города для отображения учеников: "))

    if city_id == 0:
        print("Выход из программы.")
        return
    else:
        show_students_by_city(city_id)

if __name__ == "__main__":
    main()
