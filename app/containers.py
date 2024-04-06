from dependency_injector import containers, providers

from app.database import Database
from app.users.repository import UserRepository
from app.users.service import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["app.users.router"])
    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository: UserRepository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
