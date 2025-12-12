import pytest
from sqlalchemy import create_engine, text



db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student(user_id, level, education_form, subject_id) values (:user_id, :level, :education_form, :subject_id)")
    connection.execute(sql, {"user_id":1, "level":4, "education_form": 'remote', "subject_id":1 })
    transaction.commit()
    sql = text(
        "SELECT *  FROM student WHERE user_id=1")
    result=connection.execute(sql)
    assert result.rowcount ==1
    sql = text("DELETE FROM student WHERE user_id =:id_to_delete")
    connection.execute(sql, {"id_to_delete": 1})
    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE student SET level =:new_level , education_form=:new_education_form, subject_id=:new_subject_id where user_id=:new_user_id")
    connection.execute(sql, {"new_level": 3, "new_education_form": 'full-time', "new_subject_id": 7, "new_user_id": 2})

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM student WHERE user_id =:id_to_delete")
    connection.execute(sql, {"id_to_delete": 1})
    sql = text(
        "SELECT *  FROM student WHERE user_id=1")
    result = connection.execute(sql)
    assert result.rowcount == 0

    transaction.commit()
    connection.close()