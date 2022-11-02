# Mlogger

        Logging decorator.
        __write -> 
            brief   : function that takes a string.
            default : print
        __rtrn ->
            brief   : mlogging return value
            default : False
        __t ->
            brief   : Error indentation
            default : ''
            note    : Use tabulation or other symbols
## Import
```bash
> git submodule add https://github.com/mtvy/mlogger.git
```
## Usage
```python3
        import mlogger
        
        @mlogger.logging()
        def ...
        
        def fileWrite(text : str):
                ...
                
        @mlogger.logging(__write=fileWrite, __rtrn='Error!', __t='\t\t')
        def ...   
```
            
## Test
<img width="904" alt="Снимок экрана 2022-10-29 в 19 54 22" src="https://user-images.githubusercontent.com/44533918/198843754-a160f0d2-892c-48bb-8a9a-2ed9d2bb8834.png">
