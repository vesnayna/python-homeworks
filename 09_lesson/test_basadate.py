import pytest
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    with db.connect() as connection:
        with connection.begin() as transaction:

        # Вставка данных
            sql = text("INSERT INTO student(user_id, level, education_form, subject_id) VALUES (:user_id, :level, :education_form, :subject_id)")
            connection.execute(sql, {"user_id": 1111, "level": 4, "education_form": 'remote', "subject_id": 1})

        # Проверка вставки
            sql = text("SELECT * FROM student WHERE user_id = :user_id")
            result = connection.execute(sql, {"user_id": 1111}).fetchall()
            assert len(result) == 1, "Запись не была добавлена в таблицу"

        # Удаление тестовых данных
            sql = text("DELETE FROM student WHERE user_id = :user_id")
            connection.execute(sql, {"user_id": 1111})

def test_update():
    with db.connect() as connection:
        with connection.begin() as transaction:

            # Вставка данных
            sql = text(
                "INSERT INTO student(user_id, level, education_form, subject_id) VALUES (:user_id, :level, :education_form, :subject_id)")
            connection.execute(sql, {"user_id": 1111, "level": 4, "education_form": 'remote', "subject_id": 1})

            # Обновление данных
            sql = text(
                "UPDATE student SET level =:new_level , education_form=:new_education_form, subject_id=:new_subject_id where user_id=:new_user_id")
            connection.execute(sql, {"new_level": 3, "new_education_form": 'full-time', "new_subject_id": 7,
                                     "new_user_id": 1111})

            # Проверка вставки
            sql = text("SELECT * FROM student WHERE user_id = :user_id")
            result = connection.execute(sql, {"user_id": 1111}).fetchall()
            assert result[0][1] == '3', "Запись не была добавлена в таблицу"

            # Удаление тестовых данных
            sql = text("DELETE FROM student WHERE user_id = :user_id")
            connection.execute(sql, {"user_id": 1111})

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM student WHERE user_id =:id_to_delete")
    connection.execute(sql, {"id_to_delete": 1111})
    sql = text(
        "SELECT *  FROM student WHERE user_id=1111")
    result = connection.execute(sql)
    assert result.rowcount == 0

    transaction.commit()
    connection.close()