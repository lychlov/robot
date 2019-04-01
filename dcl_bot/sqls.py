wx_sql = "SELECT lte.eNodeB,lte.`name`,lte.area,ptnw.ptn,ptnw.`port`,ptnw.site FROM lte INNER JOIN ptnw ON lte.eNodeB = ptnw.eNodeB WHERE lte.eNodeB LIKE '%para%'"
yw_sql = """
SELECT
	ptnw.ptn,
	yw.yw,
	yw.AAA 
FROM
	ptnw
	LEFT JOIN yw ON ptnw.ptn = yw.prime 
WHERE
	ptnw.ptn LIKE '%para%'
"""
jz_sql = """
SELECT
	ptnw.ptn,
	ptnw.eNodeB,
	lte.`name`,
	lte.area,
	ptnw.site 
FROM
	ptnw
	LEFT JOIN lte ON ptnw.eNodeB = lte.eNodeB 
WHERE
	ptnw.ptn LIKE '%para%' 
"""
jf_sql = """
SELECT
	ptnw.site,
	ptnw.eNodeB,
	lte.`name`,
	lte.area 
FROM
	ptnw
	LEFT JOIN lte ON ptnw.eNodeB = lte.eNodeB 
WHERE
	ptnw.site LIKE '%para%'
"""
sqls = {'yw': yw_sql, 'jz': jz_sql, 'jf': jf_sql, 'wx': wx_sql}
