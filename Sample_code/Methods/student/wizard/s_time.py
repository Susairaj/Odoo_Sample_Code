from openerp import models, fields, api, _
VERIFY = [
          ('yes', 'Yes'),
          ('no', 'No')
          ]
class Verify_Time(models.Model):
    _name='verify.time'
    
    @api.model
    def default_get(self, fields_name):
        update_ids = []
        data = super(Verify_Time, self).default_get(fields_name)
        if self._context.get('active_id'):
            student_id = self._context.get('active_id')
            for record in self.env['student.student'].browse(student_id):
                for time_record in record.time_table_ids:
                    if time_record.is_check == True:
                        update_ids.append((0,0,{'standared_id':time_record.standared_id.id,
                                                'subject_id':time_record.subject_id.id,
                                                'start_time':time_record.start_time,
                                                'end_time':time_record.end_time}))
        data['s_time_ids'] = update_ids
        return data
   
    @api.multi
    def update(self):
        current = self.env['student.student'].browse(self._context.get('active_id'))
        for record in self:
            for time_record in current:
                for time_table in time_record.time_table_ids:
                    if time_table.is_check == True:
                        time_table.write({'is_verify':record.verify})  
        return True
    
    s_time_ids = fields.One2many('s.time', 'verify_id', 'Time', readonly=True)
    verify = fields.Selection(VERIFY, 'Verified?')
   
class S_Time(models.Model):
    _name='s.time'
    
    verify_id = fields.Many2one('verify.time', 'Verify')
    serial_no = fields.Integer('#')
    standared_id = fields.Many2one('standared.standared', 'Standared')
    subject_id = fields.Many2one('section.section', 'Subject')
    start_time = fields.Datetime('Start Time')
    end_time = fields.Datetime('End Time')