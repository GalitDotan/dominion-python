from fastapi import APIRouter

from app.api.routers.user import router as user_router
from app.api.routers.authentication import router as authentication_router
from app.api.routers.profile import router as profile_router
from app.api.routers.follow import router as follow_router
from app.api.routers.leaderboard import router as leaderboard_router

router = APIRouter()
router.include_router(authentication_router)
router.include_router(user_router)
router.include_router(profile_router)
router.include_router(follow_router)
router.include_router(leaderboard_router)
