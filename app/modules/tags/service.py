import logging
from app.modules.tags.repository import TagRepository
from app.modules.tags.schemas import CreateTagRequest

from app.modules.tags.models import Tag

logger = logging.getLogger(__name__)


class TagService:

    def __init__(self, tag_repository: TagRepository) -> None:
        self.tag_repository = tag_repository

    def create_tag(self, user_id: int, tag_request: CreateTagRequest) -> int:
        logger.info(
            "Create tag with user_id: %s, request: %s",
            user_id,
            tag_request,
        )
        post = self.tag_repository.insert(
            user_id=user_id,
            name=tag_request.name,
            description=tag_request.description,
        )
        return post.id

    def get_tag_by_id(self, tag_id: int) -> Tag:
        logger.info("Get tag by id: %s", tag_id)
        return self.tag_repository.get_by_id(tag_id=tag_id)
