# Builds the episode 1 thumbnail (1280x720) in the Programme Zero style.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1280,720
ACC=(176,92,62); G1=(31,31,31); G2=(45,45,45)
img=Image.new('RGB',(W,H),(0,0,0)); d=ImageDraw.Draw(img)
import os
SORA=os.environ.get('SORA_DIR','')  # folder holding sora-latin-<weight>-normal.woff
W_={'Regular':400,'SemiBold':600,'Bold':700}
def font(n,s): return ImageFont.truetype(os.path.join(SORA,'sora-latin-%d-normal.woff'%W_[n]),s)
def pill(x0,y0,x1,y1,c): d.rounded_rectangle((x0,y0,x1,y1),radius=(y1-y0)//2,fill=c)
# brand bars on the right edge, running off the page
rows=[(850,1280),(930,1280),(1010,1280)]
ys=range(34,H-20,52)
import random; random.seed(4)
for i,y in enumerate(ys):
    x0=random.choice([770,830,890,950,1010]); pill(x0,y,W+40,y+18,G2 if i%3==0 else G1)
# orange accent bars + diamonds
pill(700,244,1010,262,ACC)
d.polygon([(668,253),(680,241),(692,253),(680,265)],outline=(255,255,255),width=2)
# photo circle with soft dark ring
ph=Image.open('images/nadeem-lone.jpg').convert('RGB').resize((400,400),Image.LANCZOS)
mask=Image.new('L',(400,400),0); ImageDraw.Draw(mask).ellipse((0,0,399,399),fill=255)
cx,cy=1000,360
d.ellipse((cx-218,cy-218,cx+218,cy+218),fill=(0,0,0))
d.ellipse((cx-208,cy-208,cx+208,cy+208),outline=ACC,width=4)
img.paste(ph,(cx-200,cy-200),mask)
# text
d=ImageDraw.Draw(img)
d.text((80,92),'EP 01   ·   SEASON 1',font=font('SemiBold',22),fill=ACC)
tf=font('SemiBold',56)
for i,l in enumerate(['So you want to','hire AI people?']):
    d.text((80,162+i*84),l,font=tf,fill=(255,255,255))
d.text((80,370),'with Nadeem Lone',font=font('Regular',32),fill=(190,190,190))
d.text((80,420),'Founder & Director, Codesearch AI',font=font('Regular',21),fill=(130,130,130))
# logo
lg=Image.open('images/logo.png').convert('RGBA'); lw=300; lh=int(lg.size[1]*lw/lg.size[0]); lg=lg.resize((lw,lh),Image.LANCZOS)
img.paste(lg,(80,H-lh-70),lg)
img.save('images/ep1-hire-ai-people.jpg',quality=88,optimize=True)
