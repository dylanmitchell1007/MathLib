class Vector2(object):

    def __init__(self, VecX, VecY):
        self.VecX = xpos
        self.VecY = ypos

    def Add(self, Vec):        
        x = self.VecX + Vec2.xx
        y = self.VecY + Vec2.yy
        return Vector2(x, y)        

    def Sub(self, sub, Vec):
        x = self.VecX - Vec.xx
        y = self.VecY - Vec.yy
        return Vector2(x, y)

    def Mult(self, mult, Vec):
        x = self.VecX * Vec.xx
        x = self.VecY * Vec.yy

    def AddConst(self, ADDCONST):
        Vec2 = work
        work.xx = self.VecX * mult
        work.yy = self.VecY * mult
        return work

    def SubConst(self, SUBCONST):
        Vec2 = work
        work.xx = self.VecX - sub.xx
        work.yy = self.VecY - sub.yy
        return work

    def MultConst(self, MULTCONST):
        Vec2 = work
        work.xx = self.VecX * mult
        work.yy = self.VecY * mult
        return work

    def Vec2(self, equals):
        return self.VecX = self.VecX, self.VecY = self.VecY

    def Magnitude(Magnitude):
        return sqrt((VecX * VecX) + (VecY * VecY))

    def Normalize(Normalize):
        return Vec2(Vec2.xx / Magnitude(), Vec2.yy / Magnitude())

    def DotProd(dotprod):
        return (Vec2.xx * Vec2.xx) + (Vec2.yy * Vec2.yy)

    def GetY():
        return Vec2.yy
        print Vector2.GetY()
    def GetX():
        return Vec2.xx
        print Vector2.GetX()
