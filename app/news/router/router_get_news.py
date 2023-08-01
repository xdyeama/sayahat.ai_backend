from fastapi import Depends, Response

from app.utils import AppModel

from typing import List, Any, Optional

from ..service import Service, get_service
from . import router


class GetNewsResponse(AppModel):
    news: Any
 

@router.get(
    "/",
    status_code=200,
    response_model=GetNewsResponse
)
def get_news(
    # jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, list]:
    
    news_list = svc.repository.get_news()
    print(news_list)
    return GetNewsResponse(news=news_list)
    # return Response(status_code=200)
