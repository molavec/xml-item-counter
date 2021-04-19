from lxml import etree
doc = etree.parse("catalogo2.xml")
count = doc.xpath("count(//item)")

print(count)