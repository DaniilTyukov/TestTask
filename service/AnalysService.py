from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models import Statistic


class AnalysService:
    def get_statistics_by_time(self, start_date: datetime, end_date: datetime, db: Session):
        data = dict({"x": {}, "y": {}, "z": {}, "count": 0})

        result = db.query(
            func.max(Statistic.x).label('max_x'),
            func.min(Statistic.x).label('min_x'),
            func.sum(Statistic.x).label('sum_x'),
            func.percentile_cont(0.5).within_group(Statistic.x).label('median_x'),
            func.max(Statistic.y).label('max_y'),
            func.min(Statistic.y).label('min_y'),
            func.sum(Statistic.y).label('sum_y'),
            func.percentile_cont(0.5).within_group(Statistic.y).label('median_y'),
            func.max(Statistic.z).label('max_z'),
            func.min(Statistic.z).label('min_z'),
            func.sum(Statistic.z).label('sum_z'),
            func.percentile_cont(0.5).within_group(Statistic.z).label('median_z'),
            func.count(Statistic.x).label('count')
        ).filter(Statistic.created_at.between(start_date, end_date)).one()
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Нет данных в данном промежутке"})
        return self._pack_in_dict(data, result)

    def get_all_metrics(self, db: Session):
        data = dict({"x": {}, "y": {}, "z": {}, "count": 0})

        result = db.query(
            func.max(Statistic.x).label('max_x'),
            func.min(Statistic.x).label('min_x'),
            func.sum(Statistic.x).label('sum_x'),
            func.percentile_cont(0.5).within_group(Statistic.x).label('median_x'),
            func.max(Statistic.y).label('max_y'),
            func.min(Statistic.y).label('min_y'),
            func.sum(Statistic.y).label('sum_y'),
            func.percentile_cont(0.5).within_group(Statistic.y).label('median_y'),
            func.max(Statistic.z).label('max_z'),
            func.min(Statistic.z).label('min_z'),
            func.sum(Statistic.z).label('sum_z'),
            func.percentile_cont(0.5).within_group(Statistic.z).label('median_z'),
            func.count(Statistic.x).label('count')
        ).one()
        return self._pack_in_dict(data, result)

    def get_metrics_by_user(self, id, db: Session):
        data = dict({"x": {}, "y": {}, "z": {}, "count": 0})

        result = db.query(
            func.max(Statistic.x).label('max_x'),
            func.min(Statistic.x).label('min_x'),
            func.sum(Statistic.x).label('sum_x'),
            func.percentile_cont(0.5).within_group(Statistic.x).label('median_x'),
            func.max(Statistic.y).label('max_y'),
            func.min(Statistic.y).label('min_y'),
            func.sum(Statistic.y).label('sum_y'),
            func.percentile_cont(0.5).within_group(Statistic.y).label('median_y'),
            func.max(Statistic.z).label('max_z'),
            func.min(Statistic.z).label('min_z'),
            func.sum(Statistic.z).label('sum_z'),
            func.percentile_cont(0.5).within_group(Statistic.z).label('median_z'),
            func.count(Statistic.x).label('count')
        ).filter(Statistic.user_id == id).one()
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Нет данных по данному пользователю"})
        return self._pack_in_dict(data, result)

    def get_by_user_and_device(self, id, device_id, db: Session):
        data = dict({"x": {}, "y": {}, "z": {}, "count": 0})

        result = db.query(
            func.max(Statistic.x).label('max_x'),
            func.min(Statistic.x).label('min_x'),
            func.sum(Statistic.x).label('sum_x'),
            func.percentile_cont(0.5).within_group(Statistic.x).label('median_x'),
            func.max(Statistic.y).label('max_y'),
            func.min(Statistic.y).label('min_y'),
            func.sum(Statistic.y).label('sum_y'),
            func.percentile_cont(0.5).within_group(Statistic.y).label('median_y'),
            func.max(Statistic.z).label('max_z'),
            func.min(Statistic.z).label('min_z'),
            func.sum(Statistic.z).label('sum_z'),
            func.percentile_cont(0.5).within_group(Statistic.z).label('median_z'),
            func.count(Statistic.x).label('count')
        ).where((Statistic.user_id == id) & (Statistic.device_id == device_id)).one()
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Нет данных по данному пользователю и(или) девайсу"})
        return self._pack_in_dict(data, result)

    def _pack_in_dict(self, data, result):
        data["x"]["max_x"] = result.max_x
        data["x"]["min_x"] = result.min_x
        data["x"]["sum_x"] = result.sum_x
        data["x"]["median_x"] = result.median_x

        data["y"]["max_y"] = result.max_y
        data["y"]["min_y"] = result.min_y
        data["y"]["sum_y"] = result.sum_y
        data["y"]["median_y"] = result.median_y

        data["z"]["max_z"] = result.max_z
        data["z"]["min_z"] = result.min_z
        data["z"]["sum_z"] = result.sum_z
        data["z"]["median_z"] = result.median_z

        data["count"] = result.count
        return data
