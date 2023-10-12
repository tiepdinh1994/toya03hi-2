#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333 and 4444!
"""

#endregion debai


#region bailam
def hi(*args, **kwargs):
  if len(args) > 1:
    name_list = args
    s = ', '.join(name_list[:-1])
    s2 = name_list[-1]
    return f'Hi {s}, and {s2}!'
  elif len(args) <= 1 or len(kwargs) > 0:
    name = args[0] if len(args) > 0 else None
    if len(kwargs) > 0:
      name = kwargs['name']
    if name == '' or name is None:
      return 'Hi!'
    return f'Hi {name}!'


#endregion bailam
print(hi('Mom'))
print(hi())
print(hi(None))
print(hi('Mom', 'Dad'))
print(hi('A', 'B', 'C'))
print(hi('1', '22', '333', '4444'))
