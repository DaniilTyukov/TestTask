from typing import Any, Type

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models import User, UserCreate, UserUpdate


class UserService:
    def save_user(self, user_create: UserCreate, db: Session):
        person = User()
        person.name = user_create.name
        db.add(person)
        db.commit()
        db.refresh(person)
        return person
    
    def get_people(self, db: Session):
        return db.query(User).all()


    def delete_user(self, id: int, db: Session):
        # получаем пользователя по id
        person = db.query(User).filter(User.id == id).first()

        # если не найден, отправляем статусный код и сообщение об ошибке
        if person is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

        db.delete(person)
        db.commit()
        return person


    def get_person(self, db: Session):
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        return user

   
    def update_person(self, id: int, user_update: UserUpdate, db: Session):
        person = db.query(User).filter(User.id == id).first()

        if person is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

        person.name = user_update.name

        db.add(person)
        db.commit()
        db.refresh(person)
        return person
