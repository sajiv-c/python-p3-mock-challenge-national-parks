class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if isinstance(new_name, str) and (len(new_name) >= 3):
                self._name = new_name
            else:
                print("NAME MUST BE STRING OF AT LEAST 3 CHARACTERS")
        else:
            print("PARK ALREADY INSTANTIATED")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        if len(self.visitors()) < 1:
            return None
        else:
            visitors_list = [trip.visitor for trip in Trip.all if trip.national_park == self]
            return max(set(visitors_list), key = visitors_list.count)



class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            print("VISITOR MUST BE OF VISITOR TYPE")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, new_national_park):
        if isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            print("NATIONAL PARK MUST BE OF NATIONAL PARK TYPE")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        if isinstance(new_date, str) and (len(new_date) >= 7):
            self._start_date = new_date
            # months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        else:
            print("START DATE MUST BE STRING OF AT LEAST 7 CHARACTERS")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        if isinstance(new_date, str) and (len(new_date) >= 7):
            self._end_date = new_date
            # months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        else:
            print("END DATE MUST BE STRING OF AT LEAST 7 CHARACTERS")


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (1 <= len(new_name) <= 15):
            self._name = new_name
        else:
            print("NAME MUST BE STRING BETWEEN 1 AND 15 CHARACTERS")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        visits = [trip for trip in Trip.all if trip.visitor == self and trip.park == park]
        return len(visits)