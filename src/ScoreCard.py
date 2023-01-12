class ScoreCard:

    def __init__(self, card):
        self.card = list(card)
        self.lastThrow = 0

    def calcScoreBonus(self, throws):

        # Stores the score bonus.
        scoreBonus = 0

        for roll in throws:

            # If the roll is a number,
            # sum 'roll' to 'scoreBonus',
            # and assign 'roll' to 'lastThrow'.
            if roll.isdigit():
                scoreBonus += int(roll)
                self.lastThrow = int(roll)

            # If the roll is '-' (meaning the player has scored no points in this throw),
            # assign '0' to 'lastThrow'.
            if roll == '-':
                self.lastThrow = 0

            # If the roll is a strike (-),
            # sum 'roll' to 'scoreBonus'.
            if roll == 'X':
                scoreBonus += 10

            # If the roll is a spare (/),
            # substract 'lastThrow' to '10',
            # and sum the result to 'scoreBonus'.
            if roll == '/':
                scoreBonus += (10 - int(self.lastThrow))

        # Return the bonus score.
        return scoreBonus

    def calcScoreTotal(self):

        # Stores total score.
        scoreTotal = 0

        # Stores the current throw (roll) and will act as an index.
        currentThrow = 0

        # Stores the number of throw made.
        # There's two throws in a frame.
        throwTotal = 0

        # Stores the number of frames (turns) made.
        frame = 1

        for roll in self.card:

            # If roll is a number, 
            # sum the number to scoreTotal and assign it to 'lastThrow'.
            # Then if 'throwTotal' is greater than 0,
            # assign '0' to 'throwTotal' and sum '1' to frame.
            # Else, sum '1' to 'throwTotal'.
            # 'currentThrow' sums '1'.
            if roll.isdigit():
                scoreTotal += int(roll)
                self.lastThrow = roll
                if throwTotal > 0:
                    throwTotal = 0
                    frame += 1
                else:
                    throwTotal += 1
                currentThrow += 1

            # If roll is '-' (meaning the player has scored no points in this throw), 
            # assign '0' to 'lastThrow'.
            # Then if 'throwTotal' is greater than 0,
            # assign '0' to 'throwTotal' and sum '1' to frame.
            # Else, sum '1' to 'throwTotal'.
            # 'currentThrow' sums '1'.
            if roll == '-':
                self.lastThrow = 0
                if throwTotal > 0:
                    throwTotal = 0
                    frame += 1
                else:
                    throwTotal += 1
                currentThrow += 1

            # If roll is 'X' (strike), 
            # calls the function 'calcScoreBonus' given it
            # the position from the 'currentThrow' until the next three
            # (next three chars beggining from the 'currentThrow').
            # Finally sums '1' to both 'currentThrow' and 'frame'.
            if roll == 'X':
                scoreTotal += self.calcScoreBonus(self.card[currentThrow:currentThrow+3])
                currentThrow += 1
                frame += 1

            # If roll is '/' (spare), 
            # calls the function 'calcScoreBonus' given it
            # the position from the 'currentThrow' until the next two
            # (next two chars beggining from the 'currentThrow').
            # Finally sums '1' to both 'currentThrow' and 'frame',
            # and resets 'throwTotal' to '0'.
            if roll == '/':
                scoreTotal += int(self.calcScoreBonus(self.card[currentThrow:currentThrow+2]))
                currentThrow += 1
                throwTotal = 0
                frame += 1
            
            # If we are in the last frame,
            # calls the function 'calcScoreBonus' given it
            # the position from the 'currentThrow' until the next two
            # (all the chars beggining from the 'currentThrow').
            if frame == 10:
                scoreTotal += self.calcScoreBonus(self.card[currentThrow:])
                
                # Returns the final score.
                return scoreTotal
    
    def getScoreTotal(self):
        return self.calcScoreTotal()