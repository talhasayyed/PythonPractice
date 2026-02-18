# inheritace from diff files
from Super_Class_file import Super_Class

class Base_Class(Super_Class):

    def BaseFeature(self):
        print('Base Class feature')


Obj_Base = Base_Class()
Obj_Base.BaseFeature()

Obj_Super = Super_Class()
Obj_Super.abbu_faature()