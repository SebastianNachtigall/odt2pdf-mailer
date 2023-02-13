# odt2pdf-mailer
A tool to convert ODT (Open Office Textfiles) email attachments to PDF documents and responds to the email with the PDF document. Also this will then run in a cloud service.

## This is how it works
1. check every x minutes if there is a new email with an ODT attachment in the inbox
    2. if so then download and convert new attachments
    3. to prevent an endless loop: mark email as read and move them to a different folder
    4. send out an answer email with the attached PDF
