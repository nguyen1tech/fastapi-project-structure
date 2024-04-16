import logging
from app.modules.posts.repository import PostRepository
from app.modules.posts.schemas import CreatePostRequest

from app.modules.posts.models import Post

logger = logging.getLogger(__name__)


class PostService:

    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def create_post(
        self, author_id: int, post_request: CreatePostRequest
    ) -> int:
        logger.info(
            "Create post with author_id: %s, request: %s",
            author_id,
            post_request,
        )
        post = self.post_repository.insert(
            author_id=author_id,
            title=post_request.title,
            content=post_request.content,
        )
        return post.id

    def get_post_by_id(self, post_id: int) -> Post:
        logger.info("Get post by id: %s", post_id)
        return self.post_repository.get_by_id(post_id=post_id)
