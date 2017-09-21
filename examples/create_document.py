import sys
sys.path.append("..")
import eversign

client = eversign.Client("MY_KEY")

document = eversign.Document()
document.title = "Tile goes here"
document.message = "tester@gmail.com"

recipient = eversign.Recipient(name="Test", email="john.doe@eversign.com")

file = eversign.File(name="Test")
file.file_url = 'raw.pdf'

signer = eversign.Signer(name="Jane Doe", email="jane.doe@eversign.com")
'''
or:
signer = eversign.Signer()
signer.name = "Jane Doe"
signer.email = "jane.doe@eversign.com"
'''

document.add_file(file)
document.add_signer(signer)
document.add_recipient(recipient)

field = eversign.SignatureField()

field.identifier = "Test"
field.x = "120.43811219947"
field.y = "479.02760463045"
field.page = 1
field.signer = 1
field.width = 120
field.height = 35
field.required = 1

document.add_field(field)
finished_document = client.create_document(document)