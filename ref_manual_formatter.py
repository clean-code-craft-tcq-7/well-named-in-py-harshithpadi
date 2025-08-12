def md_header():
   return '|pair Number | Major color | Minor Color |\n|'

def md_format_row(pair_number,major_color, minor_color):
   return f'|{pair_number}|{major_color}|{minor_color}|\n'

def printReferenceManual():
  print('Reference Manual')
  print(md_header(), end='')
  for i in range(1, len(MAJOR_COLORS)*len(MINOR_COLORS) + 1):
    major_color , minor_color = get_color_from_pair_number(i)
    print(md_formar_row(i,major_color , minor_color) ,end='')
