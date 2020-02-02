
class Gates:
    
    @staticmethod
    def AND (input1, input2):
        if input1 == 1:
            if input2 == 1:
                result = 1
            else:
                result = 0
        else:
            if input2 == 1:
                result = 0
            else:
                result = 0
        
        return result

    @staticmethod
    def NAND(input1, input2):

        if input1 == 1:
            if input2 == 1:
                result = 0
            else:
                result = 1
        else:
            if input2 == 1:
                result = 1
            else:
                result = 1
        
        return result

    @staticmethod
    def OR(input1, input2):
    
        if input1 == 1:
            if input2 == 1:
                result = 1
            else:
                result = 1
        else:
            if input2 == 1:
                result = 1
            else:
                result = 0

        return result

    @staticmethod
    def XOR(input1, input2):

        if input1 == 1:
            if input2 == 1:
                result = 0
            else:
                result = 1
        else:
            if input2 == 1:
                result = 1
            else:
                result = 0

        return result

    @staticmethod
    def NOR(input1, input2):

        if input1 == 1:
            if input2 == 1:
                result = 0
            else:
                result = 0
        else:
            if input2 == 1:
                result = 0
            else:
                result = 1

        return result

    @staticmethod
    def XNOR(input1, input2):

        if input1 == 1:
            if input2 == 1:
                result = 1
            else:
                result = 0
        else:
            if input2 == 1:
                result = 0
            else:
                result = 1

        return result


