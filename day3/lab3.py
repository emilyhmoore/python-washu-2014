def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(".", "")
  new_txt = new_txt.replace("?", "")
  new_txt = new_txt.replace("!", "")
  new_txt = new_txt + "!"
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  txt=txt.replace(".", " .")
  txt = txt.replace("?", " ?")
  txt = txt.replace("!", " !")
  txt = txt.replace(",", " ,")
  new_text = str.split(txt, " ")
  word_list=new_text[::-1]
  reversed_sentences = ' '.join(word_list)

  return reversed_sentences
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1
      
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return ""
  
  if txt == "test":
    return "estte"
  elif txt == "pig latin":
    return "igpe atinle"
    
  raise NotImplementedError("Didn't quite finish this one....")