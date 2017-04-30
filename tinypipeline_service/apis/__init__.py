from flask_restplus import Api

from tinypipeline_service.apis.paths import api as paths


api = Api(
    title='My Title',
    version='1.0',
    description='A description',
)

api.add_namespace(paths)
