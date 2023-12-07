from app import db
from app.models import Post, likes


# Query the top posts by sorting option
def get_posts(sort, quantity):
    """
    :param sort: 'likes', otherwise sorting by date.
    :param quantity: the number of posts to be returned.
    :return: a list of post objects.
    """
    if sort == 'likes':
        posts = Post.query \
            .outerjoin(likes, Post.id == likes.c.post_id) \
            .group_by(Post.id) \
            .order_by(db.func.count(likes.c.post_id).desc(), Post.date_posted.desc()) \
            .limit(quantity).all()
    else:  # Default sort by date
        posts = Post.query.order_by(Post.date_posted.desc()).limit(quantity).all()
    return posts

