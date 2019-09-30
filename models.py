from app import db
from datetime import datetime
from slugify import slugify




post_tags = db.Table('post_tags',
                     db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
                     db.Column('tags_id',db.Integer,db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    tags = db.relationship('Tag',secondary=post_tags,backref =db.backref('posts',lazy='dynamic'))

    def generate_slug(self):
        if self.tittle:
            self.slug = slugify(self.tittle)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()


    def __repr__(self):
        return '<Post id: {}, tittle: {}>'.format(self.id,self.tittle)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    slug = db.Column(db.String(140))

    def __init__(self,*args,**kwargs):
        super(Tag,self).__init__(*args,**kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id,self.name)