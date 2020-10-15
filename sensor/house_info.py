from datetime import date
class HouseInfo(object):
    def __init__(self,data):
        self.data = data
    def get_data_by_area(self, field, rec_area=0): # filter the data using rec_area as the key, and field as the value
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):   # filter data records by area
                field_data.append(record[field])
        return field_data
    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []
        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:     # filter data records by date
                field_data.append(record[field])
        return field_data




