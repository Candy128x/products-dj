from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import ImageFieldFile
import logging, magic, os

logger = logging.getLogger(__name__)


class ImageValidation:
    '''
        Image File Validation
        '''

    def image_validate(image):
        # logger.debug(f'---image_validate--funn---START---')

        # allowed_extention = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
        # if image.content_type not in allowed_extention:
        #     raise ValidationError("Upload valid image!")
        #
        # width, height = get_image_dimensions(image)
        # if width != height:
        #     raise ValidationError("Image must be square in dimention!")
        #
        # file_size = image.size
        # limit_mb = 2
        # if file_size > (limit_mb * 1024 * 1024):
        #     raise ValidationError("Max size of file is %s MB" % limit_mb)

        '''TRY_2'''
        # if image and isinstance(image, UploadedFile):
        #     logger.debug(f'---in-IF-condition--111---')
        #     w, h = get_image_dimensions(image)
        #
        #     if w != h:
        #         raise ValidationError("Image must be square in dimention!!")
        #
        #     max_width = max_height = 5000
        #     if w >= max_width or h >= max_height:
        #         raise ValidationError(u'Please use an image that is %s x %s pixels or less.' % (max_width, max_height))
        #
        #     main, sub = image.content_type.split('/')
        #     if not (main == 'image' and sub in ['jpg', 'jpeg', 'gif', 'png']):
        #         raise ValidationError(u'Please use a JPEG, GIF or PNG image.')
        #
        #     logger.debug(f'---image__len: {len(image)}')
        #     if len(image) > (8 * 1024 * 1024):
        #         raise ValidationError(u'Image file size may not exceed 8MB.')
        #
        # elif image and isinstance(image, ImageFieldFile):
        #     # something
        #     pass
        #
        # else:
        #     raise ValidationError(u'File must be image.')

        '''TRY_3'''
        # content_type = magic.from_buffer(image.read(), mime=True)
        # logger.debug(f'---content_type: {content_type}')
        # allowed_extention = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
        # if content_type not in allowed_extention:
        #     raise ValidationError('Upload valid image!')

        filesize = image.file.size
        # logger.debug(f'---filesize: {filesize}')
        if filesize > 8 * 1024 * 1024:
            raise ValidationError('Image file size may not exceed 8MB!')

        return image
