from datetime import datetime
from models import engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi import Depends, FastAPI, HTTPException


from service.AnalysService import AnalysService
from models import UserCreate, UserUpdate, StatisticCreate, StatisticUpdate
from service.StatisticService import StatisticService
from service.UserService import UserService



app = FastAPI()




SessionLocal = sessionmaker(autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


userService = UserService()
statisticService = StatisticService()
analysService = AnalysService()

@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    try:
        return userService.get_people(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/statistics")
def get_statistics(db: Session = Depends(get_db)):
    try:
        return statisticService.get_statistics(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/users/{id}")
def delete_person(id: int, db: Session = Depends(get_db)):
    try:
        return userService.delete_user(id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/statistics/{id}")
def delete_statistic(id: int, db: Session = Depends(get_db)):
    try:
        return statisticService.delete_statistic(id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users/{id}")
def get_person(id: int, db: Session = Depends(get_db)):
    try:
        person = userService.get_person(db, id)
        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        return person
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/statistics/{id}")
def get_statistic(id, db: Session = Depends(get_db)):
    try:
        statistic = statisticService.get_statistic(db, id)
        if statistic is None:
            raise HTTPException(status_code=404, detail="Statistic not found")
        return statistic
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/users")
def create_person(user_create: UserCreate, db: Session = Depends(get_db)):
    try:
        return userService.save_user(user_create, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/statistics")
def create_statistic(statistic_create: StatisticCreate, db: Session = Depends(get_db)):
    try:
        return statisticService.create_statistic(statistic_create, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/users")
def update_person(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        return userService.update_person(id, user_update, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/statistics")
def create_statistic(statistic_create: StatisticCreate, db: Session = Depends(get_db)):
    try:
        return statisticService.create_statistic(statistic_create, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/users")
def update_person(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        return userService.update_person(id, user_update, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/statistics")
def update_statistic(id, statistic_update: StatisticUpdate, db: Session = Depends(get_db)):
    try:
        return statisticService.update_statistic(id, statistic_update, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/analys/all")
def get_metrics(db: Session = Depends(get_db)):
    try:
        return analysService.get_all_metrics(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/analys/user/{id}/{device_id}")
def get_metrics_by_user_and_device(id : int, device_id , db: Session = Depends(get_db)):
    try:
      return analysService.get_by_user_and_device(id, device_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analys/user/{id}")
def get_metrics_by_user(id : int, db: Session = Depends(get_db)):
    try:
        return analysService.get_metrics_by_user(id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analys/time/")
def get_statistics_by_time(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    try: 
        return analysService.get_statistics_by_time(start_date, end_date, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
