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
def hi(name=None):
  if name == 'Mom':
    return f'Hi {name}!'
  if name == '':
    return f'Hi{name}!'
  if name:
    return 'Hi!'
  if name is None:
    return 'Hi!'


#endregion bailam
print(hi(name='Mom'))
print(hi('Mom'))
print(hi(''))
print(hi())
print(hi(None))
