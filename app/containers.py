from dependency_injector import containers, providers

from app.auth.service import AuthService
from app.database import Database
from app.modules.posts.repository import PostRepository
from app.modules.posts.service import PostService
from app.modules.tags.repository import TagRepository
from app.modules.tags.service import TagService
from app.users.repository import UserRepository
from app.users.service import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.users.router",
            "app.auth.router",
            "app.auth.dependencies",
            "app.modules.posts.router",
            "app.modules.tags.router",
        ]
    )
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
    auth_service: AuthService = providers.Factory(
        AuthService, user_repository=user_repository
    )
    post_repository: PostRepository = providers.Factory(
        PostRepository, session_factory=db.provided.session
    )
    post_service: PostService = providers.Factory(
        PostService, post_repository=post_repository
    )
    tag_repository: TagRepository = providers.Factory(
        TagRepository, session_factory=db.provided.session
    )
    tag_service: TagService = providers.Factory(
        TagService, tag_repository=tag_repository
    )
