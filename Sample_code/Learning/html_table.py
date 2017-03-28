import HTML


HTML_COLORS = [[u'Chicken Biryani Cut - Skinless', u'3763', u'Adayar'], [u'Chicken Select', u'3765', u'CPU'], [u'Chicken Select', 
 u'3766', u'CPU'], [u'Chicken Curry Cut ( Skinless)', u'3767', u'CPU'], [u'Chicken Curry Cut ( Skinless)', u'3768', 
 u'CPU'], [u'Chicken Drumsticks', u'3769', u'CPU'], [u'Chicken Drumsticks', u'3770', u'CPU'], [u'Chicken Lollipop - Skinless', u'3771', u'CPU'], 
[u'Chicken Whole Leg ', u'3773', u'CPU'], [u'Chicken Whole Leg ', u'3774', u'CPU'], 
 [u'Chicken Breast Boneless', u'3775', u'CPU'], [u'Chicken Breast Boneless', u'3776', u'CPU'], [u'Chicken Biryani Cut - Skinless', u'3758', u'CPU'], [u'Chicken Biryani Cut - Skinless', u'3758', u'Adayar'], 
 [u'Chicken Biryani Cut - Skinless', u'3777', u'CPU']]


t = HTML.Table(header_row=['Name','Lot Number', 'Store'])
for colorname in HTML_COLORS:
    t.rows.append([colorname[0],colorname[1],colorname[2]])
    htmlcode = str(t)
print htmlcode
