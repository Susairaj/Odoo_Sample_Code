@api.multi
    def _validate_project_date_range(self, project_line_ids):
        date_range_list = []
        for pro_range in project_line_ids:
            selected_date_range = None
            selected_date_range = validations.get_date_range(pro_range.start_date, pro_range.end_date)
            date_range_list.append(selected_date_range)
            if len(project_line_ids) != 1 and len(date_range_list) != 1:
                for added_date_range in date_range_list:
                    if selected_date_range != added_date_range:
                        for sd_date in selected_date_range:
                            for adr_date in added_date_range:
                                if sd_date == adr_date:
                                    raise UserError(_("'%s' date is already added in previous range in the project.")%(sd_date))
    
    def get_date_range(date_from, date_to):
        date_from_year = date_from[:4]
        date_from_month = date_from[5:7]
        date_from_date = date_from[8:11]
        
        date_to_year = date_to[:4]
        date_to_month = date_to[5:7]
        date_to_date = date_to[8:11]
        
        d1 = date(int(date_from_year), int(date_from_month), int(date_from_date))
        d2 = date(int(date_to_year), int(date_to_month), int(date_to_date))
        delta = d2 - d1
        date_range_list = []
        for i in range(delta.days + 1):
            r_date = d1 + td(days=i)
            date_range_list.append(str(r_date))
        return date_range_list
     
    @api.onchange('project_line_ids')
    def get_date_range(self):
        date_range_list = []
        self._validate_project_date_range(self.project_line_ids)
        for pro_range in self.project_line_ids:
            selected_date_range = None
            selected_date_range = validations.get_date_range(pro_range.start_date, pro_range.end_date)
            date_range_list.append(selected_date_range)
            if len(self.project_line_ids) != 1 and len(date_range_list) != 1:
                for added_date_range in date_range_list:
                    if selected_date_range != added_date_range:
                        for sd_date in selected_date_range:
                            for adr_date in added_date_range:
                                if sd_date == adr_date:
                                    raise UserError(_("'%s' date is already added in previous range in the project.")%(sd_date))