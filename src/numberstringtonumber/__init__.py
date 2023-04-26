from word2number import w2n


class NumberWordToNumber:

  def __init__(self, word):
    self.word = word

  def convert(self):
    val = 0
    num = 0
    wordls = self.word.split(' ')
    for word in wordls:
      lowerWord = word.strip().lower()
      if lowerWord in ['lakhs', 'lakh']:
        num = num * 100000
      elif lowerWord in ['crores', 'crore']:
        num = num * 10000000
      elif lowerWord in ['thousands', 'thousand']:
        num = num * 1000
      elif lowerWord in ['hundreds', 'hundred']:
        num = num * 100
      elif lowerWord in ['billions', 'billion']:
        num = num * 1000000000
      elif lowerWord in ['millions', 'million']:
        num = num * 1000000
      else:
        val += num
        try:
          num = w2n.word_to_num(word)
        except Exception as err:
          err
          num = 0
    val+= num
    return val if val else num



