class achievement():
    def __init__(self,right_number,wrong_number):
        self.right_number = right_number
        self.wrong_number = wrong_number
    
    def get_right_number(self):
        return self.right_number

    def get_wrong_number(self):
        return self.wrong_number

    def get_accuracy(self):
        return (str(self.right_number/(self.right_number+self.wrong_number)*100) + '%')
