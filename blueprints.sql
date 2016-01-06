SELECT * FROM invTypes WHERE published=1 AND typeID IN (
SELECT A.typeID FROM industryActivityMaterials AS A, industryActivityMaterials AS B, industryActivityMaterials AS C WHERE A.materialTypeID = 2869 AND B.materialTypeID = 2870 AND C.materialTypeID = 2875 GROUP BY A.typeID ORDER BY A.typeID
) ORDER BY typeName;