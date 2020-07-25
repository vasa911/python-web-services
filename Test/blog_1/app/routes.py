from flask_restful import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from . import api
from . import models
from . import db
from . import schemas

post_schema = schemas.PostSchema()


class PortListApi(Resource):

    def post(self):
        try:
            post = post_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(post)
        db.session.commit()
        return post_schema.dump(post), 201

    def get(self):
        posts = db.session.query(models.Post).all()
        return post_schema.dump(posts, many=True)


class PostApi(Resource):
    def get(self, uuid):
        post = db.session.query(models.Post).filter_by(uuid=uuid).first()
        if post is None:
            return "", 404
        return post_schema.dump(post)

    def put(self, uuid):
        post = db.session.query(models.Post).filter_by(uuid=uuid).first()
        if post is None:
            return "", 404

        try:
            post = post_schema.load(request.json, instance=post, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        
        db.session.add(post)
        db.session.commit()

        return post_schema.dump(post)
    
    def delete(self, uuid):
        post = db.session.query(models.Post).filter_by(uuid=uuid).first()
        if post is None:
            return "", 404
        db.session.delete(post)
        db.session.commit()
        return "", 204



api.add_resource(PortListApi, '/posts')
api.add_resource(PostApi, '/posts/<uuid>')
