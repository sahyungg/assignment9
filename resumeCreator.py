import json
data=open('contents.json', 'r')
resume=data.read()

content=json.loads(resume)

from fpdf import FPDF
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.image('sunghoon.jpg', 20, 20, 35)
pdf.set_font('helvetica', 'BU', 25)
pdf.cell(160, 33, 'Park Sunghoon', ln=True, align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(200, 0, 'I am taking the position as the main visual of Enhypen,', ln=True, align='C')
pdf.cell(200, 16, 'and I aspire to be as good or even better than Bangtan', ln=True, align='C')
pdf.cell(200, 0, 'in the near future and make music that is inspirational..', ln=True, align='C')

pdf.ln(10)

pdf.set_font('helvetica', 'B', 17)
pdf.cell(63, 10, "Contact Details", ln=True, align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(66, 10, content [0] ['phoneNumber'], ln=True, align='C')
pdf.cell(77, 10, content [0] ['email'], ln=True, align='C')

pdf.ln(6)

pdf.set_font('helvetica', 'B', 17)
pdf.cell(84, 10, "Education background", ln=True, align='C')

pdf.ln(3)

pdf.set_font('helvetica', 'U', 15)
pdf.cell(65, 10, "Senior High School", ln=True, align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(110, 10, content [0] ['seniorHigh'], align='C')
pdf.set_font('helvetica', 'I', 11)
pdf.cell(39, 10, content [0] ['schoolYear1'], ln=True, align='C')
pdf.set_font('helvetica', 'B', 12)
pdf.cell(35, 10, "Award:", align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(48, 10, content [0] ['rankSenior'], ln=True, align='C')
pdf.cell(124, 10, content [0] ['award1'], ln=True, align='C')

pdf.ln(3)

pdf.set_font('helvetica', 'U', 15)
pdf.cell(38, 10, "College", ln=True, align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(110, 10, content [0] ['collegeUniversity'], align='C')
pdf.set_font('helvetica', 'I', 11)
pdf.cell(39, 10, content [0] ['schoolYear2'], ln=True, align='C')
pdf.set_font('helvetica', 'B', 12)
pdf.cell(35, 10, "Award:", align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(22, 10, content [0] ['rankCollege'], ln=True, align='C')
pdf.cell(108, 10, content [0] ['award2'], ln=True, align='C')

pdf.ln(6)

pdf.set_font('helvetica', 'B', 17)
pdf.cell(62, 10, "Achievements", ln=True, align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(126, 10, content [0] ['achievement1'], ln=True, align='C')
pdf.cell(104, 10, content [0] ['achievement2'], ln=True, align='C')
pdf.cell(117, 10, content [0] ['achievement3'], ln=True, align='C')



pdf.output('DELROSARIO_IRISH.pdf')
