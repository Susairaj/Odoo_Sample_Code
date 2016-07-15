from openerp.osv import osv
from openerp import SUPERUSER_ID

"""  Author : Nivas M  """    
class res_users(osv.osv):
    _inherit = "res.users"
    
    def get_store(self, cr, uid, context=None):
        store = self.browse(cr, uid, uid).active_store_id or False
        if store: 
            store_name = store.name or 'Aurangabad'
            company = store.company_id.name or 'EMC Limited'
            project = store.project_id.name or 'RGGVY Bihar'
            return "Store : %s | Company : %s | Project : %s" % (store_name, company, project)
        return ''
    
    # Purpose : Set 'Setting' group as default in Administration category. category  in res user form - Added by Nivas 
    def _get_group(self,cr, uid, context=None):
        dataobj = self.pool.get('ir.model.data')
        result = []
        try:
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_user')
            result.append(group_id)
            # Purpose : Set 'Setting' group as default in Administration category. category - Added by Nivas 
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_system')
            result.append(group_id)
            # End
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_partner_manager')
            result.append(group_id)
        except ValueError:
            # If these groups does not exists anymore
            pass
        return result
    
    _defaults = {
        #'password': 'psit_@123',
        'groups_id': _get_group,
    }
    
""" End """ 