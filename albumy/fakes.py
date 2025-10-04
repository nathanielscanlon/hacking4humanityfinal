# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import random

from PIL import Image
from faker import Faker
from flask import current_app
from sqlalchemy.exc import IntegrityError

from albumy.extensions import db
from albumy.models import User, Photo, Tag, Comment, Notification

fake = Faker()


def fake_admin():
    admin = User(name='Hacking4Humanity',
                 username='Stop_Online_Hate',
                 email='admin@helloflask.com',
                 bio="On a mission to stop online hate",
                 website='http://Hackathon.com',
                 confirmed=True)
    admin.set_password('helloflask')
    notification = Notification(message='Hello, welcome to Albumy.', receiver=admin)
    db.session.add(notification)
    db.session.add(admin)
    db.session.commit()


def fake_user(count=10):
    for i in range(count):
        user = User(name=fake.name(),
                    confirmed=True,
                    username=fake.user_name(),
                    bio=fake.sentence(),
                    location=fake.city(),
                    website=fake.url(),
                    member_since=fake.date_this_decade(),
                    email=fake.email())
        user.set_password('123456')
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_follow(count=30):
    for i in range(count):
        user = User.query.get(random.randint(1, User.query.count()))
        user.follow(User.query.get(random.randint(1, User.query.count())))
    db.session.commit()


def fake_tag(count=20):
    for i in range(count):
        tag = Tag(name=fake.word())
        db.session.add(tag)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_photo(count=30):
    # photos
    upload_path = current_app.config['ALBUMY_UPLOAD_PATH']


    #######
    filename = 'hachphoto1.jpg' 
    photo = Photo(
        description="Had a great day at the Rock Festival",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )
    tag = Tag(name='RockON')
    db.session.add(tag)

    photo.tags.append(tag)
    db.session.add(photo)

    filename = 'Pitt_image.jpg' 
    photo = Photo(
        description="Pittsburgh Skyline - 2/1/2025",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )
    tag = Tag(name='Pittsburgh')
    photo.tags.append(tag)
    db.session.add(photo)
    
    filename = 'Sky_Image.jpg' 
    photo = Photo(
        description="What a beautiful day!",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )

    tag = Tag(name='HappyLife')
    photo.tags.append(tag)
    db.session.add(photo)

    filename = 'Mountains_image.jpg' 
    photo = Photo(
        description="Behold the great smoky mountains!",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )

    tag = Tag(name='Breathtaking')
    photo.tags.append(tag)
    db.session.add(photo)

    filename = 'Flowers_Image.jpg' 
    photo = Photo(
        description="Can you smell the flowers",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )

    tag = Tag(name='Fresh')
    photo.tags.append(tag)
    db.session.add(photo)

    filename = 'Ronaldo_Image.jpg' 
    photo = Photo(
        description="Goallllll!",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )

    tag = Tag(name='Goal')
    photo.tags.append(tag)
    db.session.add(photo)

    filename = 'Car_Image.jpg' 
    photo = Photo(
        description="Old - School!",
        filename=filename,
        filename_m=filename,
        filename_s=filename,
        author=User.query.get(random.randint(1, User.query.count())),
        timestamp=fake.date_time_this_year()
    )

    tag = Tag(name='Car-Finatic')
    photo.tags.append(tag)
    db.session.add(photo)

    db.session.commit()


def fake_collect(count=50):
    for i in range(count):
        user = User.query.get(random.randint(1, User.query.count()))
        user.collect(Photo.query.get(random.randint(1, Photo.query.count())))
    db.session.commit()


def fake_comment(count=100):
    comment = Comment(
        author=User.query.get(random.randint(1, User.query.count())),
        body="White people suck",
        timestamp=fake.date_time_this_year(),
        photo=Photo.query.get(1)
    )
    db.session.add(comment)

    comment = Comment(
        author=User.query.get(random.randint(1, User.query.count())),
        body="Hope you had a fun time!",
        timestamp=fake.date_time_this_year(),
        photo=Photo.query.get(1)
    )
    db.session.add(comment)

    comment = Comment(
        author=User.query.get(random.randint(1, User.query.count())),
        body="I loved their last song!",
        timestamp=fake.date_time_this_year(),
        photo=Photo.query.get(1)
    )

    db.session.add(comment)

    comment = Comment(
        author=User.query.get(random.randint(1, User.query.count())),
        body="You look ugly. Delete this",
        timestamp=fake.date_time_this_year(),
        photo=Photo.query.get(1)
    )

    db.session.add(comment) 

    comment = Comment(
        author=User.query.get(random.randint(1, User.query.count())),
        body="No way, I was there too!",
        timestamp=fake.date_time_this_year(),
        photo=Photo.query.get(1)
    )
    db.session.add(comment) 


    for i in range(count):
        comment = Comment(
            author=User.query.get(random.randint(1, User.query.count())),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            photo=Photo.query.get(random.randint(2, Photo.query.count()))
        )
        db.session.add(comment)





    db.session.commit()
