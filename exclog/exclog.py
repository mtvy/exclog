#/==================================================================\#
# exclog.py                                           (c) Mtvy, 2022 #
#\==================================================================/#
#                                                                    #
# Copyright (c) 2022. Mtvy (Matvei Prudnikov, m.d.prudnik@gmail.com) #
#                                                                    #
#\==================================================================/#

#/-----------------------------/ Libs \-----------------------------\#
from typing    import Any, Callable, Literal
from traceback import format_exc as _exc
#\------------------------------------------------------------------/#


#\------------------------------------------------------------------/#
def logging(out : Callable[[str], None]=print, rtrn=False, t=''):
    """ 
        ### Exclog decorator.
        out -> 
            brief   : function that takes a string.
            default : print
        rtrn ->
            brief   : exclog return value
            default : False
        t ->
            brief   : Error indentation
            default : ''
            note    : Use tabulation or other symbols
    """

    RD="\033[1;35m"; GRY="\033[1;37m"; DF="\033[0m"
    
    def _logging(func : Callable) -> Any | Literal[False]:
        
        def wrap_func(*args, **kwargs) -> Any | Literal[False]:
            try:
                return func(*args, **kwargs)
            except:
                tr = _exc().split('\n')
                exc = (
                    f'{GRY}{t}│'
                       f'\n{t}└{RD}Erorr at: [{func.__name__}]{GRY}'
                       f'\n{t} │'
                       f'\n{t} └{RD}{tr[0]}'
                )
                for line in tr[1:]:
                    exc = f'{exc}\n{t}  {line}'
                out(f"{exc}{DF}")

            return rtrn

        return wrap_func
        
    return _logging
#\------------------------------------------------------------------/#
