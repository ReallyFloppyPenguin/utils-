from typing import overload
from errs import PhonyException
class ProneList():
    @overload
    def __init__(self):...

    @overload
    def __init__(self, list):...

    def __init__(self, _list=None):
        """
        
        A modified version of a list in python;\n
        this might save you some time and effort;\n

        ```
        e.g.
        my_list = [True, False]
        if my_list[2] == True:
            # Do something...
        
        \"\"\"
        This would cause an error because my_list does not have a '2' index.
        But I try to fix this kind of thing with ProneList
        \"\"\"
        e.g.
        
        my_list = [True, False]
        my_list = ProneList(my_list)

        if my_list[2] == True:
            # Do something...
        

        \"\"\"
        This would not cause an error because my_list[2] is going to be None.
        This is because my_list or (ProneList) returns None if it can't
        find the index you're looking for.
        If say you're trying to append a new item to `my_list` 
        then you can do so like this:
        \"\"\"
        my_list = [True, False]
        my_list = ProneList(my_list)
        my_list.obj.append() # obj is basically the plain list object.
        ```
        """
        if _list:
            self._list = list(_list)
        else:
            self._list = list()

    def __add__(self, other):
        self._list += other

    def __getitem__(self, index):
        try:
            return self._list[index]
        except:
            return None
        
    def __setitem__(self, key, value):
        try:
            self._list[key] = value
        except Exception as e:
            PhonyException(e)

    def __repr__(self) -> str:
        repr_values = ', '.join([str(self._list)]).replace('[', '').replace(']', '')
        #repr_values = f'{[o for o in self._list]}'
        #print(repr_values, f'{self._list}', 'asdasdasd')
        return f"ProneList({repr_values})"
    
    def get_min(self):
        return min(self._list)

    def get_max(self):
        return max(self._list)

    @property
    def obj(self):
        return self._list

    @staticmethod
    def construct(*args, **kwargs):
        """
        Build a ProneList object with **kwargs as well\n
        e.g.
        ```
        >>> myList = ProneList.construct('a', 'b', 'c', d='d')
        >>> myList
        ProneList(ProneList('a', 'b', 'c'), {'d':'d'})
        ```
        """

        return ProneList([ProneList(args), kwargs])

#_list = ['a', 'b', 'c', 'd']
#plist = ProneList(_list)
#plist[2] = 'a'
#plist + _list
#plist.obj.append('a')
#print(plist)
#print(ProneList())
#print(ProneList(_list))
#print(ProneList.construct('a', 'b', 'c', d='d'))