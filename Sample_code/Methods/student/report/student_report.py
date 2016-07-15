from openerp import models, fields, api, _
from openerp.report import report_sxw

class student_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context): 
        if context is None:
            context = {}
        super(student_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_avg': self._avg_mark})
   
    def _avg_mark(self, total, tamil):
        if total:
            print tamil
            val = total/5
            return val
        return None
    
class report_studentqweb(models.AbstractModel):
    _name = "report.student.report_student_sample_qweb"
    _inherit = "report.abstract_report"
    _template = "student.report_student_sample_qweb"
    _wrapped_report_class = student_report