from datetime import datetime

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from models import User, StatisticCreate, Statistic, StatisticUpdate


class StatisticService:
    def delete_statistic(self, id: int, db: Session):
        statistic = db.query(Statistic).filter(Statistic.id == id).first()


        if statistic is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

        
        db.delete(statistic)  
        db.commit()  
        return statistic

    def get_statistics(db: Session):
        return db.query(Statistic).all()

    def create_statistic(self, statistic_create: StatisticCreate, db: Session):
        person = db.query(User).filter(User.id == statistic_create.user_id).first()
        if person is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        statistic = Statistic(x=statistic_create.x, y=statistic_create.y,
                              z=statistic_create.z, user_id=statistic_create.user_id,
                              device_id=statistic_create.device_id
                              )
        statistic.created_at = datetime.now()
        db.add(statistic)
        person.statistics.append(statistic)
        db.commit()
        return statistic


    def update_statistic(self, id: int, statistic_update: StatisticUpdate, db: Session):
        found = db.query(Statistic).filter(Statistic.id == id).first()
        if found is None:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        
        found = Statistic(x=statistic_update.x, y=statistic_update.y,
                          z=statistic_update.z, user_id=statistic_update.user_id,
                          device_id=statistic_update.device_id
                          )
        db.add(found)
        db.commit()
        return found


    def get_statistic(self, id: int, db: Session):
     
        result = db.query(Statistic).filter(Statistic.id == id).first()
        
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Статистика не найдена"})
        
        return result
