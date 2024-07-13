import Config as _

class encrypt:
    def __init__(self , data):

        def conversion(data):
            if _.shift >= 25:
                _.shift = 10
            elif _.shift < 5 and _.shift > -5:
                _.shift = -5
            elif _.shift <= -25:
                _.shift = -10
            
            self.result = ""
            for i in data:
                digit = ord(i)
                digit += _.shift
                char = chr(digit)
                self.result = self.result + char
            return self.result
        
        self.data = data
        self.encrypted_data_one = conversion(self.data)
        self.encrypted_data_raw = conversion(self.encrypted_data_one)
        self.encrypted_data = conversion(self.encrypted_data_raw)
        
    def get_encrypted_data(self):
        return self.encrypted_data