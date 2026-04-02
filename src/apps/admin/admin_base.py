from apps.admin.admin_auth import get_admin_auth_provider
from apps.admin.views.user_view import UserView
from core.core_dependency.db_dependency import get_db_engine
from database.models.user import User
from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin


def setup_admin(app: FastAPI) -> None:
    admin = Admin(
        engine=get_db_engine(),
        title="Admin",
        auth_provider=get_admin_auth_provider(),
    )

    admin.add_view(UserView(User))

    admin.mount_to(app=app)
