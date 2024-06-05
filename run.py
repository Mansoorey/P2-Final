from factory import DocumentFactory
doc_fac = DocumentFactory()
create_doc = doc_fac.create_file("word")
create_doc.open()
create_doc.read()
create_doc.save()