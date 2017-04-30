from flask import Flask
from flask import request
from flask_restplus import Namespace, Resource, fields
from flask_restplus import reqparse

# from tinypipeline.core.paths import Paths


api = Namespace('paths', description='Map paths')


@api.route('/')
class PathsResource(Resource):

    """Class Documentation"""

    model = api.model('Path', {
        'path': fields.String(required=True, description='The mapped path')
    })

    parser = reqparse.RequestParser()
    parser.add_argument('project', type=str, help='The project name')
    parser.add_argument('program', type=str, help='The program name')
    parser.add_argument('folder', type=str, help='The maya folder')
    parser.add_argument('name', type=str, help='The asset name')
    parser.add_argument('kind', type=str, help='The asset kind')
    parser.add_argument('version', type=str, help='The version of an asset')
    parser.add_argument('ext', type=str, help='The file extension')
    parser.add_argument('filename', type=str, help='The file name')

    @api.expect(parser)
    @api.marshal_list_with(model)
    def get(self):
        """Get Documentation"""
        args = PathsResource.parser.parse_args()

        return args
        # return {'path': Paths.project(project=args['project'])}
