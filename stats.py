def get_num_words(book_contents):
  return len(book_contents.split())

def get_chars_count(book_contents):
  chars_count = {}
  for char in book_contents.lower():
    if char in chars_count: # if char key exists in the chars_count dictionary
      chars_count[char] += 1
    else:
      chars_count[char] = 1
  return chars_count

def sort_on(dict):
  return dict["count"]

def sort_chars_count(chars_count_dict):
  chars_count_list = []
  for key, value in chars_count_dict.items():
    chars_count_list.append({"char": key, "count": value})
  
  chars_count_list.sort(reverse=True, key=sort_on)
  return chars_count_list