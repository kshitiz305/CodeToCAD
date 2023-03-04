# THIS IS AN AUTO-GENERATE FILE. 
# DO NOT EDIT MANUALLY.
# Please run development/capabilitiesJsonToPython/capabilitiesToPy.sh to generate this file.
# Copy this file and remove this header to create a new CodeToCAD Provider.

from typing import Optional

import core.CodeToCADInterface as CodeToCADInterface
import core.utilities as Utilities
from core.CodeToCADInterface import FloatOrItsStringValue,IntOrFloat,MaterialOrItsName,PartOrItsName,EntityOrItsName,LandmarkOrItsName,AxisOrItsIndexOrItsName,DimensionOrItsFloatOrStringValue,AngleOrItsFloatOrStringValue,EntityOrItsNameOrLandmark,PointOrListOfFloatOrItsStringValue,LengthUnitOrItsName
from core.utilities import (Angle, BoundaryBox, CurveTypes, Dimension,
                            Dimensions, Point, center, createUUIDLikeId,
                            getAbsoluteFilepath, getFilename, max, min)

class Entity(CodeToCADInterface.Entity): 
    
    
    name:str
    description:Optional[str]=None

    def __init__(self, name:str, description:Optional[str]=None):
        self.name = name
        self.description = description

    def isExists(self
    ) -> bool:
        
        raise NotImplementedError()
        

    def rename(self, newName:str, renamelinkedEntitiesAndLandmarks:bool=True
    ):
        
        return self
        

    def delete(self, removeChildren:bool
    ):
        
        return self
        

    def isVisible(self
    ) -> bool:
        
        raise NotImplementedError()
        

    def setVisible(self, isVisible:bool
    ):
        
        return self
        

    def apply(self
    ):
        
        return self
        

    def getNativeInstance(self
    ):
        
        raise NotImplementedError()
        

    def getLocationWorld(self
    ) -> 'Point':
        
        raise NotImplementedError()
        

    def getLocationLocal(self
    ) -> 'Point':
        
        raise NotImplementedError()
        

    def select(self, landmarkName:Optional[LandmarkOrItsName]=None, selectionType:str="vertex"
    ):
        
        return self
        

    def export(self, filePath:str, overwrite:bool=True, scale:float=1.0
    ):
        
        return self
        

    def clone(self, newName:str, copyLandmarks:bool=True
    ):
        
        return self
        

    def mirror(self, mirrorAcrossEntity:EntityOrItsName, axis:AxisOrItsIndexOrItsName, resultingMirroredEntityName:Optional[str]=None
    ):
        
        return self
        

    def linearPattern(self, instanceCount:'int', offset:DimensionOrItsFloatOrStringValue, directionAxis:AxisOrItsIndexOrItsName="z"
    ):
        
        return self
        

    def circularPattern(self, instanceCount:'int', separationAngle:AngleOrItsFloatOrStringValue, centerEntityOrLandmark:EntityOrItsNameOrLandmark, normalDirectionAxis:AxisOrItsIndexOrItsName="z"
    ):
        
        return self
        

    def translateXYZ(self, x:DimensionOrItsFloatOrStringValue, y:DimensionOrItsFloatOrStringValue, z:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def translateX(self, amount:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def translateY(self, amount:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def translateZ(self, amount:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def scaleXYZ(self, x:DimensionOrItsFloatOrStringValue, y:DimensionOrItsFloatOrStringValue, z:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def scaleX(self, scale:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def scaleY(self, scale:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def scaleZ(self, scale:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def scaleXByFactor(self, scaleFactor:float
    ):
        
        return self
        

    def scaleYByFactor(self, scaleFactor:float
    ):
        
        return self
        

    def scaleZByFactor(self, scaleFactor:float
    ):
        
        return self
        

    def scaleKeepAspectRatio(self, scale:DimensionOrItsFloatOrStringValue, axis:AxisOrItsIndexOrItsName
    ):
        
        return self
        

    def rotateXYZ(self, x:AngleOrItsFloatOrStringValue, y:AngleOrItsFloatOrStringValue, z:AngleOrItsFloatOrStringValue
    ):
        
        return self
        

    def rotateX(self, rotation:AngleOrItsFloatOrStringValue
    ):
        
        return self
        

    def rotateY(self, rotation:AngleOrItsFloatOrStringValue
    ):
        
        return self
        

    def rotateZ(self, rotation:AngleOrItsFloatOrStringValue
    ):
        
        return self
        

    def twist(self, angle:AngleOrItsFloatOrStringValue, screwPitch:DimensionOrItsFloatOrStringValue, interations:'int'=1, axis:AxisOrItsIndexOrItsName="z"
    ):
        
        return self
        

    def remesh(self, strategy:str, amount:float
    ):
        
        return self
        

    def createLandmark(self, landmarkName:str, x:DimensionOrItsFloatOrStringValue, y:DimensionOrItsFloatOrStringValue, z:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def getBoundingBox(self
    ) -> 'BoundaryBox':
        
        raise NotImplementedError()
        

    def getDimensions(self
    ) -> 'Dimensions':
        
        raise NotImplementedError()
        

    def getLandmark(self, landmarkName:str
    ) -> 'Landmark':
        
        raise NotImplementedError()
        
    
class Part(Entity,CodeToCADInterface.Part): 
    
    

    def createFromFile(self, filePath:str, fileType:Optional[str]=None
    ):
        
        return self
        

    def createPrimitive(self, primitiveName:str, dimensions:str, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createCube(self, width:DimensionOrItsFloatOrStringValue, length:DimensionOrItsFloatOrStringValue, height:DimensionOrItsFloatOrStringValue, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createCone(self, radius:DimensionOrItsFloatOrStringValue, height:DimensionOrItsFloatOrStringValue, draftRadius:DimensionOrItsFloatOrStringValue=0, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createCylinder(self, radius:DimensionOrItsFloatOrStringValue, height:DimensionOrItsFloatOrStringValue, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createTorus(self, innerRadius:DimensionOrItsFloatOrStringValue, outerRadius:DimensionOrItsFloatOrStringValue, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createSphere(self, radius:DimensionOrItsFloatOrStringValue, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def createGear(self, outerRadius:DimensionOrItsFloatOrStringValue, addendum:DimensionOrItsFloatOrStringValue, innerRadius:DimensionOrItsFloatOrStringValue, dedendum:DimensionOrItsFloatOrStringValue, height:DimensionOrItsFloatOrStringValue, pressureAngle:AngleOrItsFloatOrStringValue="20d", numberOfTeeth:'int'=12, skewAngle:AngleOrItsFloatOrStringValue=0, conicalAngle:AngleOrItsFloatOrStringValue=0, crownAngle:AngleOrItsFloatOrStringValue=0, keywordArguments:Optional[dict]=None
    ):
        
        return self
        

    def loft(self, Landmark1:'Landmark', Landmark2:'Landmark'
    ):
        
        return self
        

    def union(self, withPart:PartOrItsName, deleteAfterUnion:bool=True, isTransferLandmarks:bool=False
    ):
        
        return self
        

    def subtract(self, withPart:PartOrItsName, deleteAfterSubtract:bool=True, isTransferLandmarks:bool=False
    ):
        
        return self
        

    def intersect(self, withPart:PartOrItsName, deleteAfterIntersect:bool=True, isTransferLandmarks:bool=False
    ):
        
        return self
        

    def hollow(self, thicknessX:DimensionOrItsFloatOrStringValue, thicknessY:DimensionOrItsFloatOrStringValue, thicknessZ:DimensionOrItsFloatOrStringValue, startAxis:AxisOrItsIndexOrItsName="z", flipAxis:bool=False
    ):
        
        return self
        

    def hole(self, holeLandmark:LandmarkOrItsName, radius:DimensionOrItsFloatOrStringValue, depth:DimensionOrItsFloatOrStringValue, normalAxis:AxisOrItsIndexOrItsName="z", flip:bool=False, instanceCount:'int'=1, instanceSeparation:DimensionOrItsFloatOrStringValue=0.0, aboutEntityOrLandmark:Optional[EntityOrItsNameOrLandmark]=None, mirror:bool=False, instanceAxis:Optional[AxisOrItsIndexOrItsName]=None, initialRotationX:AngleOrItsFloatOrStringValue=0.0, initialRotationY:AngleOrItsFloatOrStringValue=0.0, initialRotationZ:AngleOrItsFloatOrStringValue=0.0, leaveHoleEntity:bool=False
    ):
        
        return self
        

    def assignMaterial(self, materialName:MaterialOrItsName
    ):
        
        return self
        

    def isCollidingWithPart(self, otherPart:PartOrItsName
    ):
        
        raise NotImplementedError()
        

    def filletAllEdges(self, radius:DimensionOrItsFloatOrStringValue, useWidth:bool=False
    ):
        
        return self
        

    def filletEdges(self, radius:DimensionOrItsFloatOrStringValue, landmarksNearEdges:list[LandmarkOrItsName], useWidth:bool=False
    ):
        
        return self
        

    def filletFaces(self, radius:DimensionOrItsFloatOrStringValue, landmarksNearFaces:list[LandmarkOrItsName], useWidth:bool=False
    ):
        
        return self
        

    def chamferAllEdges(self, radius:DimensionOrItsFloatOrStringValue
    ):
        
        return self
        

    def chamferEdges(self, radius:DimensionOrItsFloatOrStringValue, landmarksNearEdges:list[LandmarkOrItsName]
    ):
        
        return self
        

    def chamferFaces(self, radius:DimensionOrItsFloatOrStringValue, landmarksNearFaces:list[LandmarkOrItsName]
    ):
        
        return self
        
    
class Sketch(Entity,CodeToCADInterface.Sketch): 
    
    
    name:str
    curveType:Optional['CurveTypes']=None
    description:Optional[str]=None

    def __init__(self, name:str, curveType:Optional['CurveTypes']=None, description:Optional[str]=None):
        self.name = name
        self.curveType = curveType
        self.description = description

    def revolve(self, angle:AngleOrItsFloatOrStringValue, aboutEntityOrLandmark:EntityOrItsNameOrLandmark, axis:AxisOrItsIndexOrItsName="z"
    ):
        
        return self
        

    def extrude(self, length:DimensionOrItsFloatOrStringValue, convertToMesh:bool=True
    ):
        
        return self
        

    def sweep(self, profileCurveName:str, fillCap:bool=False
    ):
        
        return self
        

    def createText(self, text:str, fontSize:DimensionOrItsFloatOrStringValue=1.0, bold:bool=False, italic:bool=False, underlined:bool=False, characterSpacing:'int'=1, wordSpacing:'int'=1, lineSpacing:'int'=1, fontFilePath:Optional[str]=None
    ):
        
        return self
        

    def createFromVertices(self, coordinates:list[PointOrListOfFloatOrItsStringValue], interpolation:'int'=64
    ):
        
        return self
        

    def createPoint(self, coordinate:PointOrListOfFloatOrItsStringValue
    ):
        
        return self
        

    def createLine(self, length:DimensionOrItsFloatOrStringValue, angleX:AngleOrItsFloatOrStringValue=0.0, angleY:AngleOrItsFloatOrStringValue=0.0, symmetric:bool=False
    ):
        
        return self
        

    def createLineBetweenPoints(self, endAt:PointOrListOfFloatOrItsStringValue, startAt:Optional[PointOrListOfFloatOrItsStringValue]=None
    ):
        
        return self
        

    def createCircle(self, radius:'Dimension'
    ):
        
        return self
        

    def createEllipse(self, radiusA:'Dimension', radiusB:'Dimension'
    ):
        
        return self
        

    def createArc(self, radius:'Dimension', angle:AngleOrItsFloatOrStringValue="180d"
    ):
        
        return self
        

    def createArcBetweenThreePoints(self, pointA:'Point', pointB:'Point', centerPoint:'Point'
    ):
        
        return self
        

    def createSegment(self, innerRadius:'Dimension', outerRadius:'Dimension', angle:AngleOrItsFloatOrStringValue="180d"
    ):
        
        return self
        

    def createRectangle(self, length:'Dimension', width:'Dimension'
    ):
        
        return self
        

    def createPolygon(self, numberOfSides:'int', length:'Dimension', width:'Dimension'
    ):
        
        return self
        

    def createTrapezoid(self, lengthUpper:'Dimension', lengthLower:'Dimension', height:'Dimension'
    ):
        
        return self
        
    
class Landmark(Entity,CodeToCADInterface.Landmark): 
    
    
    name:str
    parentEntity:EntityOrItsName
    description:Optional[str]=None

    def __init__(self, name:str, parentEntity:EntityOrItsName, description:Optional[str]=None):
        self.name = name
        self.parentEntity = parentEntity
        self.description = description

    def getLandmarkEntityName(self
    ) -> str:
        
        raise NotImplementedError()
        
    
class Joint(CodeToCADInterface.Joint): 
    
    
    entity1:EntityOrItsNameOrLandmark
    entity2:EntityOrItsNameOrLandmark

    def __init__(self, entity1:EntityOrItsNameOrLandmark, entity2:EntityOrItsNameOrLandmark):
        self.entity1 = entity1
        self.entity2 = entity2

    def translateLandmarkOntoAnother(self
    ):
        
        return self
        

    def pivot(self
    ):
        
        return self
        

    def gearRatio(self, ratio:float
    ):
        
        return self
        

    def limitXLocation(self, min:Optional[PointOrListOfFloatOrItsStringValue]=None, max:Optional[PointOrListOfFloatOrItsStringValue]=None
    ):
        
        return self
        

    def limitYLocation(self, min:Optional[PointOrListOfFloatOrItsStringValue]=None, max:Optional[PointOrListOfFloatOrItsStringValue]=None
    ):
        
        return self
        

    def limitZLocation(self, min:Optional[PointOrListOfFloatOrItsStringValue]=None, max:Optional[PointOrListOfFloatOrItsStringValue]=None
    ):
        
        return self
        

    def limitXRotation(self, min:Optional[AngleOrItsFloatOrStringValue]=None, max:Optional[AngleOrItsFloatOrStringValue]=None
    ):
        
        return self
        

    def limitYRotation(self, min:Optional[AngleOrItsFloatOrStringValue]=None, max:Optional[AngleOrItsFloatOrStringValue]=None
    ):
        
        return self
        

    def limitZRotation(self, min:Optional[AngleOrItsFloatOrStringValue]=None, max:Optional[AngleOrItsFloatOrStringValue]=None
    ):
        
        return self
        
    
class Material(CodeToCADInterface.Material): 
    
    
    name:str
    description:Optional[str]=None

    def __init__(self, name:str, description:Optional[str]=None):
        self.name = name
        self.description = description

    def assignToPart(self, partName:PartOrItsName
    ):
        
        return self
        

    def setColor(self, rValue:IntOrFloat, gValue:IntOrFloat, bValue:IntOrFloat, aValue:IntOrFloat=1.0
    ):
        
        return self
        

    def addImageTexture(self, imageFilePath:str
    ):
        
        return self
        
    
class Animation(CodeToCADInterface.Animation): 
    
    

    def __init__(self):
        pass

    @staticmethod
    def default(
    ) -> 'Animation':
        return Animation()

    def createKeyFrameLocation(self, entity:EntityOrItsName, frameNumber:'int'
    ):
        
        raise NotImplementedError()
        

    def createKeyFrameRotation(self, entity:EntityOrItsName, frameNumber:'int'
    ):
        
        raise NotImplementedError()
        
    
class Scene(CodeToCADInterface.Scene): 
    
    
    name:Optional[str]=None
    description:Optional[str]=None

    def __init__(self, name:Optional[str]=None, description:Optional[str]=None):
        self.name = name
        self.description = description

    @staticmethod
    def default(
    ) -> 'Scene':
        return Scene()

    def create(self
    ):
        
        return self
        

    def delete(self
    ):
        
        return self
        

    def export(self, filePath:str, entities:list[EntityOrItsName], overwrite:bool=True, scale:float=1.0
    ):
        
        return self
        

    def setDefaultUnit(self, unit:LengthUnitOrItsName
    ):
        
        return self
        

    def createGroup(self, name:str
    ):
        
        return self
        

    def deleteGroup(self, name:str, removeChildren:bool
    ):
        
        return self
        

    def removeFromGroup(self, entityName:str, groupName:str
    ):
        
        return self
        

    def assignToGroup(self, entities:list[EntityOrItsName], groupName:str, removeFromOtherGroups:Optional[bool]=True
    ):
        
        return self
        

    def setVisible(self, entities:list[EntityOrItsName], isVisible:bool
    ):
        
        return self
        
    
class Analytics(CodeToCADInterface.Analytics): 
    
    

    def __init__(self):
        pass

    def measureDistance(self, entity1:EntityOrItsNameOrLandmark, entity2:EntityOrItsNameOrLandmark
    ) -> 'Dimensions':
        
        raise NotImplementedError()
        

    def measureAngle(self, entity1:EntityOrItsNameOrLandmark, entity2:EntityOrItsNameOrLandmark, pivot:Optional[EntityOrItsNameOrLandmark]=None
    ) -> 'list[Angle]':
        
        raise NotImplementedError()
        

    def getWorldPose(self, entity:EntityOrItsName
    ) -> 'list[float]':
        
        raise NotImplementedError()
        

    def getBoundingBox(self, entityName:EntityOrItsName
    ) -> 'BoundaryBox':
        
        raise NotImplementedError()
        

    def getDimensions(self, entityName:EntityOrItsName
    ) -> 'Dimensions':
        
        raise NotImplementedError()
        
    