==================
Exclog
==================

Logging decorator.
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
      
Import
------
      .. code-block:: bash
       
          pip install exclog
          
Usage
-----
.. code-block:: python

   import exclog

   @exclog.logging()
   def ...

   def fileWrite(text : str):
       ...
           
   @exclog.logging(__write=fileWrite, __rtrn='Error!', __t='\t\t')
   def ...
