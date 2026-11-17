from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from pathlib import Path
root=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='Times-Roman',fontSize=27,leading=31,textColor=HexColor('#182d29'),spaceAfter=8))
styles.add(ParagraphStyle(name='SectionCV',fontName='Helvetica-Bold',fontSize=10,leading=13,textColor=HexColor('#176d59'),spaceBefore=16,spaceAfter=8))
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9,leading=13,spaceAfter=6,textColor=HexColor('#243831')))
story=[]
def p(t,s='BodyCV'): story.append(Paragraph(t,styles[s]))
p('Xirui Zhao','NameCV')
p('PhD Student in Optical Engineering | Beijing Institute of Technology')
p('School of Optics and Photonics, Beijing, China<br/>Email: gavinzhao1997@163.com | GitHub: github.com/OceandeepGavin')
p('RESEARCH INTERESTS','SectionCV')
p('Generative medical imaging; patient-specific anatomical reconstruction; anatomical landmark detection; intelligent orthopaedic surgical planning.')
p('EDUCATION','SectionCV')
p('<b>2023-present | PhD in Optical Engineering</b><br/>Beijing Institute of Technology. Supervisor: Prof. Jian Yang.')
p('<b>2022-2023 | Master\u2019s-stage study in Optical Engineering</b><br/>Beijing Institute of Technology. Transitioned to doctoral study.')
p('<b>2016-2020 | BEng in Optoelectronic Information Science and Engineering</b><br/>Beijing Institute of Technology.')
p('SELECTED FIRST-AUTHOR PUBLICATIONS','SectionCV')
p('<b>Pelvic Fracture Reduction Planning via Joint Shape-Intensity Reference.</b><br/><b>Xirui Zhao</b>, Deqiang Xiao, Teng Zhang, Long Shao, Danni Ai, Jingfan Fan, Tianyu Fu, Yucong Lin, Hong Song, Junqiang Wang, Jian Yang.<br/><i>IEEE Transactions on Medical Imaging</i>, 2026, 45(4):1352-1368.<br/><link href="https://doi.org/10.1109/TMI.2025.3621670" color="#176d59">doi:10.1109/TMI.2025.3621670</link>')
p('<b>Defect-adaptive landmark detection in pelvis CT images via personalized structure-aware learning.</b><br/><b>Xirui Zhao</b>, Deqiang Xiao, Teng Zhang, Jingfan Fan, Danni Ai, Tianyu Fu, Yucong Lin, Long Shao, Hong Song, Junqiang Wang, Jian Yang.<br/><i>Computerized Medical Imaging and Graphics</i>, 2026, 127:102693.<br/><link href="https://doi.org/10.1016/j.compmedimag.2025.102693" color="#176d59">doi:10.1016/j.compmedimag.2025.102693</link>')
p('PROJECT EXPERIENCE','SectionCV')
p('<b>Orthopaedic surgical navigation and robotics | Core project member</b><br/>Algorithm engineering, functional integration, prototype development, and performance validation. The team\u2019s system supports total knee, unicompartmental knee, and total hip replacement.')
p('SELECTED ACTIVITIES AND HONORS','SectionCV')
p('<b>2026:</b> Research presentation, ChinaVR Outstanding Doctoral Student Forum.<br/><b>2026:</b> First Prize, Medicine &amp; Health track, 5th Beijing University Student Innovation and Entrepreneurship Competition (Jingcai Dachuang); project lead.<br/><b>2026:</b> Excellence Award, 5th Beijing Institute of Technology Innovation and Entrepreneurship Competition (Lingjun Cup); Xihe Zhiguang project.')
doc=SimpleDocTemplate(str(root/'assets/Xirui_Zhao_CV.pdf'),pagesize=(595.28,841.89),leftMargin=46,rightMargin=46,topMargin=39,bottomMargin=35,title='Xirui Zhao - Curriculum Vitae',author='Xirui Zhao')
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#52645f'));c.drawString(46,23,'Updated November 2026');c.drawRightString(549,23,str(d.page))
doc.build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
r=PdfReader(root/'assets/Xirui_Zhao_CV.pdf');print('CV pages:',len(r.pages));assert len(r.pages)==1

