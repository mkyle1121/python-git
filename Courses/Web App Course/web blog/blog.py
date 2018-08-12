from post import Post
from database import Database
import datetime
import uuid

class Blog(object):
    def __init__(self,author,title,description,author_id,_id=None):
        self.author=author
        self.author_id = author_id
        self.title=title
        self.description=description
        self._id=uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',data=self.json())

    def json(self):
        return {'author':self.author,
                'author_id':self.author_id,
                'title':self.title,
                'description':self.description,
                'id':self._id}

    @classmethod # uses cls?
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'_id':id})
        return cls (**blog_data)

        # return cls(author=blog_data['author'],
        #             title=blog_data['title'],
        #             description=blog_data['description'],
        #             id=blog_data['_id'])

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(collection = 'blogs', query={'author_id':author_id})
        return [cls(**blog) for blog in blogs]