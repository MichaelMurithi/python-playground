class Address:
    def __init__(self,street,city,state,pincode,street2=''):
        self.street = street
        self.city = city
        self.state = state
        self.pincode = pincode
        self.street2 = street2
    
    def __str__(self):
        lines = [self.street]

        if self.street2:
            lines.append((self.street2))
        lines.append(f"{self.city}, {self.state}, {self.pincode}")
        return '\n'.join(lines)
