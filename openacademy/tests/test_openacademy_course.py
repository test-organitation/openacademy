# -*- coding: utf-8 -*- 
from psycopg2 import IntegrityError

from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger

class GlobalTestOpenacademyCourse(TransactionCase):
    '''
    Global test to openacademy course model.
    Test create course and trigger contrains.
    '''

    # Methods seudo-constructor of test setUp
    def setUp(self):
        # Define global variable to test methods
        super(GlobalTestOpenacademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(self, course_name, course_description, 
                      course_responsible_id):
        # create a course with parameets  recved
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    # Method of test startwith 'test_*(self)'

    # Mute error openerp.spl_db to don't see this in log
    @mute_logger('openerp.sql_db')
    def test_01_course_with_same_name_and_description(self):
        '''
        Create name, course with same name and description
        to test constrains of different to description
        '''
        # Error raised expetied with messege expeted.
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates' 
                ' check constraint "openacademy_course_name_description_check"'
                ):
            # Create a course with same name and scription to raise error.
            self.create_course('test', 'test', None)
