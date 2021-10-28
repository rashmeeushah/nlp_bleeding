# -*- coding: utf-8 -*-

#%% Program setup

import pandas as pd
import os
from datetime import date

drive = input('Enter the first part of the file path. ')

os.chdir('%s/Project_CliniThinkBleed_V2/' %drive)

today = date.today()

#%% Create SNOMED code list

addcodes = {
    23412002: ['Cardiac', 'Hemopericardium'],
    
    72189003: ['ENT', 'Hemorrhagic nasal discharge'],
    300101002: ['ENT', 'Bleeding pinna'],
    127276009: ['ENT', 'Injury of head with rhinorrhagia'],
    249366005: ['ENT', 'Bleeding from nose'],
    164279008: ['ENT', 'O/E - throat hemorrhage'],
    232354002: ['ENT', 'Anterior epistaxis'],
    232355001: ['ENT', 'Posterior epistaxis'],
    232356000: ['ENT', 'Traumatic epistaxis'],
    249417007: ['ENT', 'Bleeding in mouth and/or pharynx'],
    249351007: ['ENT', 'Blood in nasal cavity'],
    249467000: ['ENT', 'Bleeding from larynx'],
    277236000: ['ENT', 'Evidence of recent epistaxis'],
    35101000119106: ['ENT', 'Bleeding following tonsillectomy'],
    12441001: ['ENT', 'Epistaxis'],
    
    34436003: ['GU', 'Blood in urine'],
    44843000: ['GU', 'Hemorrhage of prostate'],
    87696004: ['GU', 'Hemorrhagic cystitis'],
    197887003: ['GU', 'Bladder hemorrhage'],
    197940006: ['GU', 'Microscopic hematuria'],
    281858008: ['GU', 'Recurrent microscopic hematuria'],
    198058000: ['GU', 'Scrotal hematoma due to non-traumatic cause'],
    369061000119104: ['GU', 'Genitourinary tract hemorrhage following transurethral procedure'],
    283948004: ['GU', 'Hematoma of penis'],
    283929003: ['GU', 'Hematoma of prostate'],
    89966002: ['GU', 'Hematoma of scrotum'],
    283938001: ['GU', 'Hematoma of seminal vesicle'],
    5223003: ['GU', 'Hematoma of spermatic cord'],
    283944002: ['GU', 'Hematoma of testis'],    
    283974005: ['GU', 'Hematoma of male perineum'],    
    236606001: ['GU', 'Hemorrhage from ureter'],    
    93475002: ['GU', 'Hemorrhage into epididymis'],    
    95571006: ['GU', 'Hemorrhage of kidney'],    
    50573001: ['GU', 'Hemorrhage of penis'],    
    62182006: ['GU', 'Hemorrhage of scrotum'],    
    8465005 : ['GU', 'Hemorrhage of seminal vesicle'],    
    33878005: ['GU', 'Hemorrhage of spermatic cord'],    
    77708008: ['GU', 'Hemorrhage of testis'],    
    405555006: ['GU', 'Hemorrhage of urethra'],    
    713036004: ['GU', 'Dissection of renal artery'],
    197812000: ['GU', 'Renal artery hemorrhage'],
    
    74474003: ['Gastrointestinal', 'Gastrointestinal hemorrhage'],
    197364000: ['Gastrointestinal', 'Central hemorrhagic necrosis of liver'],
    443826006: ['Gastrointestinal', 'Hemorrhage into peritoneal cavity'],
    276465001: ['Gastrointestinal', 'Anal margin hematoma'],
    281102003: ['Gastrointestinal', 'Blood in vomit - symptom'],
    282065004: ['Gastrointestinal', 'Hematoma of ileum'],
    300361008: ['Gastrointestinal', 'Vomit contains blood'],
    300362001: ['Gastrointestinal', 'Vomit contains fresh blood'],
    300364000: ['Gastrointestinal', 'Vomit contains old blood'],
    414991007: ['Gastrointestinal', 'Painful rectal bleeding'],
    414992000: ['Gastrointestinal', 'Painless rectal bleeding'],
    445162006: ['Gastrointestinal', 'Bleeding Meckels diverticulitis'],
    445163001: ['Gastrointestinal', 'Bleeding Meckels diverticulum'],
    445929002: ['Gastrointestinal', 'Hematoma of extraperitoneal space'],
    447096000: ['Gastrointestinal', 'Hematoma of abdominal wall'],
#    788951001: ['Gastrointestinal', 'Hemorrhage of digestive system'],
    414663001: ['Gastrointestinal', 'Melena due to gastrointestinal hemorrhage'],
    275782008: ['Gastrointestinal', 'Melena on examination of feces'],
    262858002: ['Gastrointestinal', 'Appendix hematoma'],
    262870003: ['Gastrointestinal', 'Colonic hematoma'],
    262865005: ['Gastrointestinal', 'Cecal hematoma'],
    262808009 : ['Gastrointestinal', 'Gallbladder hematoma'],
    282074002 : ['Gastrointestinal', 'Hematoma of anus'],
    6072007 : ['Gastrointestinal', 'Bleeding from anus'],
    262796008 : ['Gastrointestinal', 'Liver hematoma'],
    47977000: ['Gastrointestinal', 'Mesenteric hematoma'],
    236000006: ['Gastrointestinal', 'Intraperitoneal hematoma'],
    236001005: ['Gastrointestinal', 'Omental hematoma'],
    262814002: ['Gastrointestinal', 'Peri-bile duct hematoma'],
    262876009: ['Gastrointestinal', 'Rectal hematoma'],
    262818004: ['Gastrointestinal', 'Splenic hematoma'],
    262838003: ['Gastrointestinal', 'Stomach hematoma'],
    262852001: ['Gastrointestinal', 'Small intestinal hematoma'],
    324618004: ['Gastrointestinal', 'Pharyngeal hemorrhage'],
    307131005: ['Gastrointestinal', 'Mallory-Weiss tear'],
    2901004: ['Gastrointestinal', 'Melena'],
    405729008: ['Gastrointestinal', 'Hematochezia '],
    
    
    5309003: ['General', 'Subcutaneous hematoma'],
    48149007: ['General', 'Exsanguination'],
    95422003: ['General', 'Hemorrhage of muscle'],
    109859000: ['General', 'Ascorbic acid deficiency with hemorrhage'],
    110149000: ['General', 'Traumatic hemorrhage'],
    110265006: ['General', 'Postoperative hemorrhage'],
    131148009: ['General', 'Bleeding'],
    213261000: ['General', 'Intraoperative hemorrhage'],
    213262007: ['General', 'Postoperative hematoma formation'],
    234003006: ['General', 'Arterial hemorrhage'],
    234004000: ['General', 'Hemorrhage of transplant artery'],
    234076002: ['General', 'Venous hemorrhage'],
#    12234077006: ['General', 'Hemorrhage of transplanted vein'],
    234156005: ['General', 'Congenital arteriovenous fistula rupture'],
    234201003: ['General', 'Vascular graft hemorrhage'],
    234208009: ['General', 'Arteriovenous fistula rupture'],
    236129005: ['General', 'Stomal bleeding'],
    238824006: ['General', 'Paroxysmal hematoma of the finger'],
    239161005: ['General', 'Wound hemorrhage'],
    240124007: ['General', 'Intermuscular hematoma'],
    248252008: ['General', 'Bleeds profusely'],
    248706000: ['General', 'Broken blood vessel'],
    248707009: ['General', 'Burst blood vessel'],
    262938004: ['General', 'Secondary hemorrhage'],
    262969000: ['General', 'Intramuscular hematoma'],
    278365007: ['General', 'Anticoagulant-induced bleeding'],
    280969001: ['General', 'Disorder of arteriovenous shunt'],
    280974009: ['General', 'Arteriovenous graft hemorrhage'],
    280977002: ['General', 'Arteriovenous shunt hemorrhage'],
    297968009: ['General', 'Bleeding skin'],
    303290001: ['General', 'Ecchymosis of intraoral surface of lip'],
    308895003: ['General', 'Reactionary hemorrhage postprocedure'],
    308898001: ['General', 'Extraperitoneal hemorrhage postprocedure'],
    309750008: ['General', 'Extravasation following blood transfusion'],
    371100002: ['General', 'Extravasation injury'],
    385494008: ['General', 'Hematoma'],
    403691006: ['General', 'Hemorrhage following skin surgery'],
    405538007: ['General', 'Spontaneous hemorrhage'],
    405539004: ['General', 'Hemorrhage of blood vessel'],
    423051001: ['General', 'Hematoma of face'],
    446669006: ['General', 'Anastomotic bleeding'],
    698502005: ['General', 'Recurrent hemorrhage'],
    698584008: ['General', 'Postoperative wound hemorrhage'],
    698585009: ['General', 'Postoperative abdominal wound hemorrhage'],
    713891007: ['General', 'Bleeding during surgery requiring transfusion'],
    724863009: ['General', 'Hematoma of surgical wound of skin due to and following surgical procedure'],
    10421000132103: ['General', 'Bleeding requiring transfusion'],
    424131007: ['General', ' Easy bruising'],
    23097003: ['General', 'Kyasanur forest disease'],
    77643000: ['General', 'Ecchymosis'],
    423902002: ['General', 'Purpura'],
    355001: ['General', 'Hemmorhagic shock'],
    423716004: ['General', 'Petechial rash'],
    302873008: ['General', 'Thrombocytopenic purpura'],
    32273002: ['General', 'Idiopathic thrombocytopenic purpura'],
    20927009: ['General', 'Dengue hemorrhagic fever'],
    53751009: ['General', 'Batemans purpura'],
    308154003: ['General', 'Rectus sheath hematoma'],
    307390004: ['General', 'Hematoma of groin'],
    271813007: ['General', 'Petechiae'],
    
    274100004: ['Neurology', 'Cerebral hemorrhage'],
    21233002: ['Neurology', 'Meningeal hemorrhage'],
    49422009: ['Neurology', 'Cortical hemorrhage'],
    450425005: ['Neurology', 'Intracranial hematoma'],
    233983001: ['Neurology', 'Ruptured cerebral aneurysm'],
    1386000: ['Neurology', 'Intracranial hemorrhage'],
    21454007: ['Neurology', 'Subarachnoid hemorrhage'],
    230706003: ['Neurology', 'Hemorrhagic cerebral infarction'],
    234005004: ['Neurology', 'Vertebral artery rupture'],
    234006003: ['Neurology', 'Carotid artery rupture'],
    723857007: ['Neurology', 'Silent micro-hemorrhage of brain'],
    732923001: ['Neurology', 'Hemorrhage of medulla oblongata'],
    5471000124102: ['Neurology', 'Ruptured aneurysm of intracranial artery'],
    5571000124103: ['Neurology', 'Cerebrovascular accident with intracranial hemorrhage'],
    140881000119109: ['Neurology', 'Spontaneous cerebral hemorrhage with compression of brain'],
    141091000119105: ['Neurology', 'Nontraumatic subarachnoid hemorrhage with brain compression'],
    141151000119101: ['Neurology', 'Nontraumatic subdural hematoma with brain compression'],
    142851000119103: ['Neurology', 'Spontaneous cerebellar hemorrhage'],
    143521000119103: ['Neurology', 'Nontraumatic intraparenchymal cerebral hemorrhage'],
    291401000119102: ['Neurology', 'Spontaneous hemorrhage of subarachnoid space from left middle cerebral artery'],
    291571000119106: ['Neurology', 'Spontaneous cerebral hemorrhage'],
    291591000119107: ['Neurology', 'Subacute non-traumatic intracranial subdural hemorrhage'],
    330111000119103: ['Neurology', 'Ruptured acquired aneurysm of cerebral artery'],
    710864009: ['Neurology', 'Arterial dissection'],
    429251000124108: ['Neurology', 'Dissecting aneurysm of anterior cerebral artery'],
    429221000124104: ['Neurology', 'Dissecting aneurysm of cerebral artery'],
    45639009: ['Neurology', 'Hereditary cerebral amyloid angiopathy, Icelandic type'],

    5740008: ['OBGYN', 'Pelvic hematoma during delivery'],
    198903000: ['OBGYN', 'Placenta previa with hemorrhage'],
	106004004: ['OBGYN', 'Hemorrhagic complication of pregnancy'],
	283969002: ['OBGYN', 'Hematoma of female perineum'],
	47821001: ['OBGYN', 'Postpartum hemorrhage'],
    26623000: ['OBGYN', 'Failed attempted termination of pregnancy complicated by delayed and/or excessive hemorrhage'],
	38010008: ['OBGYN', 'Intrapartum hemorrhage'],
	38280009: ['OBGYN', 'Hematometra'],
	44216000: ['OBGYN', 'Retained products of conception, following delivery with hemorrhage'],
	48880000: ['OBGYN', 'Postcoital bleeding'],
	237130006: ['OBGYN', 'Mid-cycle bleeding'],
	76742009: ['OBGYN', 'Postmenopausal bleeding'],
	78095005: ['OBGYN', 'Hematosalpinx'],
	83294006: ['OBGYN', 'Hematoma of broad ligament'],
	88981003: ['OBGYN', 'Pyometra'],
	93476001: ['OBGYN', 'Hemorrhage of fallopian tube'],
	198645000: ['OBGYN', 'Incomplete miscarriage with delayed or excessive hemorrhage'],
	198656000: ['OBGYN', 'Complete miscarriage with delayed or excessive hemorrhage'],
	198706000: ['OBGYN', 'Incomplete legal termination of pregnancy with delayed or excessive hemorrhage'],
	198719001: ['OBGYN', 'Complete legal termination of pregnancy with delayed or excessive hemorrhage'],
	198745005: ['OBGYN', 'Incomplete illegal termination of pregnancy with delayed or excessive hemorrhage'],
	198757001: ['OBGYN', 'Complete illegal termination of pregnancy with delayed or excessive hemorrhage'],
	198807003: ['OBGYN', 'Failed attempted termination of pregnancy with delayed or excessive hemorrhage'],
	198875007: ['OBGYN', 'Failed medical termination of pregnancy, complicated by delayed or excessive hemorrhage'],
	698586005: ['OBGYN', 'Complete legal abortion complicated by excessive hemorrhage'],
	698587001: ['OBGYN', 'Complete illegal abortion complicated by excessive hemorrhage'],
	307735008: ['OBGYN', 'Complete inevitable miscarriage complicated by delayed or excessive hemorrhage'],
	307752007: ['OBGYN', 'Incomplete inevitable miscarriage complicated by delayed or excessive hemorrhage'],
	199993001: ['OBGYN', 'Obstetric trauma causing pelvic hematoma'],
	199995008: ['OBGYN', 'Obstetric pelvic hematoma - delivered'],
	199996009: ['OBGYN', 'Obstetric pelvic hematoma - delivered with postnatal problem'],
	69385001: ['OBGYN', 'Hematoma of vulva'],
	289530006: ['OBGYN', 'Vaginal bleeding'],
	248895001: ['OBGYN', 'Blood in vagina'],
	289242002: ['OBGYN', 'Finding of blood loss in labor'],
	371614003: ['OBGYN', 'Hematoma of obstetric wound'],
	386692008: ['OBGYN', 'Menorrhagia'],
	23431000119106: ['OBGYN', 'Rupture of uterus during labor'],
	44991000119100: ['OBGYN', 'Abnormal uterine bleeding'],
    283958000: ['OBGYN', 'Hematoma of fallopian tube'],
#    784409008:['OBGYN', 'Hematoma of ovary'],
    283962006:['OBGYN', 'Hematoma of uterus'],
#    5933004: ['OBGYN', 'Threatened abortion in second trimester'],
    
    246681007: ['Ophtho', 'Blood in eye'],
    31056006 : ['Ophtho', 'Orbital hemorrhage'],
    193474002: ['Ophtho', 'Choroidal hemorrhage and rupture'],
    7927006: ['Ophtho', 'Periorbital hematoma'],
    194016009: ['Ophtho', 'Exophthalmos due to orbital hemorrhage'],
    28998008: ['Ophtho', 'Retinal hemorrhage'],
    14460007: ['Ophtho', 'Hemorrhage in optic nerve sheaths'],
    50165004: ['Ophtho', 'Hemorrhagic detachment of retinal pigment epithelium'],
    698840003: ['Ophtho', 'Neovascular glaucoma due to hyphema'],
    21117005: ['Ophtho', 'Conjunctival hemorrhage'],
    232033003: ['Ophtho', 'Sickle cell-hemoglobin C retinopathy'],
    40788000: ['Ophtho', 'Hyposphagma'],

    95549001: ['Ret_hematoma', 'Retroperitoneal hemorrhage'],
    236002003: ['Ret_hematoma', 'Retroperitoneal hematoma'],
    
    95431003: ['Pulmonary', 'Respiratory tract hemorrhage'],
    11029002: ['Pulmonary', 'Pulmonary apoplexy'],
    31892009: ['Pulmonary', 'Hemothorax'],
    66857006: ['Pulmonary', 'Hemoptysis'],
    82872004: ['Pulmonary', 'Tracheostomy hemorrhage'],
    301290008: ['Pulmonary', 'Frank blood in sputum'],
    427562009: ['Pulmonary', 'Blood in upper airway'],
    
    81808003: ['Ortho', 'Hemarthrosis']

    }

print('Length of SNOEMD queries: ', len(addcodes)) #n=226

andnots = {
           'General': [423716004, 302873008, 32273002, 20927009, 53751009, 424131007, 23097003, 77643000, 423902002, 271813007],
           'Gastrointestinal': [324618004, 308154003],
           'Neurology': [710864009, 429251000124108, 429221000124104, 45639009],
           'GU': [197940006, 281858008, 713036004],
           'Cardiac': [],
           'ENT': [],
           'OBGYN': [5933004],
           'Ophtho': [21117005, 232033003, 40788000],
           'Ret_hematoma': [197812000, 713036004],
           'Ortho': [],
           'Pulmonary': [12441001] #Still getting nosebleed here
           }
#sets = ['Cardiac', 'OBGYN', 'ENT', 'GU', 'Gastrointestinal', 'Neurology', 'Pulmonary', 'Ortho', 'Ret_hematoma', 'Ophtho', 'General']

sets = pd.read_pickle('./data/sets.pkl')
andnot_sets = list(andnots.keys())
if len(andnot_sets) != len(sets):
    raise Exception('Dictionary does not have all the sets')
else:
    print('Dictionary matches the unique sets')

# <codecell> 

snomed_codes = pd.DataFrame(list(addcodes.items()))
snomed_codes.rename(columns={0: 'SNOMED_code'}, inplace=True)
snomed_codes[['Category','SNOMED_name']] = pd.DataFrame(snomed_codes[1].tolist(), index= snomed_codes.index)
snomed_codes.drop(columns=1, inplace=True)
snomed_codes['counter'] = snomed_codes.groupby('Category').cumcount()

for row in snomed_codes.iterrows():
    a=row[1]['Category']
    b=row[1]['counter']
    c=row[1]['SNOMED_code']
    d=row[1]['SNOMED_name']
    snomed_codes.at[row[0],'query'] = 'q\t*\t%s_%s_q\t243796009|Situation with explicit context|:{408731000|Temporal context|=410512000|Current or specified|,246090004|Associated finding|=%s|%s|,408732007|Subject relationship context|=410604004|Subject of record|,408729009|Finding context|=410515003|Known present|}' %(a,b,c,d)

# <codecell> 
f = open('./clinithink_%s/ads_afbleedmanual_%sv1.txt' %(today,today), 'w', newline='')

print('[Title]\trashmee_cancerafbleed_%sv1\tDescription: Find bleeding events in patients with af and cancer with manual method|Purpose: find events|Version: V1.0|Date: November 12 2020' %(today), file=f)
print('[Threshold]\t0.01\n', file=f)
print('q\t-\tSituation_with_explicit_context_q\t243796009', file=f)
print('q\t-\tPharmaceutical_biologic_product_q\t373873005', file=f)
print('q\t-\tFinding_with_explicit_context_situation_q\t413350009', file=f)
print('q\t-\tProcedure_with_explicit_context_situation_q\t129125009\n', file=f)

#First print all the queries
#Later compiled in c queries with OR or AND NOT
snomed_codes.sort_values(by=['Category','counter'], inplace=True)
for row in snomed_codes.iterrows():
    print(row[1]['query'], file=f)

#Create the c queries with OR and AND NOT STATEMENTS
for x in sets:
    #These are all the rows in this set based on matching category
    set_rows = snomed_codes.loc[snomed_codes['Category'] == x]
    #Create OR statements if the SNOMED code is not in the AND NOT dictionary
    andnots_for_x = andnots[x]
    set_ors = set_rows.loc[~set_rows['SNOMED_code'].isin(andnots_for_x)]
    set_nots = snomed_codes.loc[snomed_codes['SNOMED_code'].isin(andnots_for_x)]
    orqueries = '('
    notqueries = ''
    for row in set_ors.iterrows():
        temp = row[1]['counter']
        orqueries += '%s_%s_q OR ' %(x,temp)
    orqueries = orqueries[:-4]
    orqueries += ')'
    for row in set_nots.iterrows():
        temp = row[1]['counter']
        tempcat = row[1]['Category']
        notqueries += '%s_%s_q OR ' %(tempcat,temp)
    notqueries = notqueries[:-4]
    if len(notqueries)==0:
        print('c\t*\t%s\t%s\n' %(x,orqueries), file=f)
    else: 
        print('c\t*\t%s\t%s AND NOT (%s)\n' %(x,orqueries, notqueries), file=f) 
print('AND NOT (Ophtho OR Gastrointestinal OR Neurology OR Ortho OR OBGYN OR Pulmonary OR GU OR Cardiac OR ENT OR Ret_hematoma)', file=f)

f.close()

#Challenge with how to add this to "AND NOT" Because it is a body structure- manual adding this type of thing for ecchymoses and petechiae
#243796009|Situation with explicit context|:{408731000|Temporal context|=410512000|Current or specified|,246090004|Associated finding|=(404684003|Clinical finding|:{363698007|Finding site|=38866009|Body part structure|,116676008|Associated morphology|=77643000|Ecchymosis|}),408732007|Subject relationship context|=410604004|Subject of record|,408729009|Finding context|=410515003|Known present|} 
# Need to somehow manually add "and not" subconjunctival hemorrhage to general , 'Associated finding|=78768009|Subconjunctival hemorrhage'
# <codecell> Make the config file
allgroups = ''
for s in sets:
    allgroups += s + ','
allgroups = allgroups[:-1]


f = open('./clinithink_%s/config_afbleedmanual_%s.ini' %(today,today), 'w', newline='')

print('[trial]\n##\n# criteria_list = list of groupings for bleeding outcome', file=f)
print('##\ncriteria_list = %s' %allgroups, file=f)
print('\n', file=f)
print('permanent_include = 30', file=f)
print('permanent_exclude = -30', file=f)
print('temporary_include = 10', file=f)
print('temporary_exclude = -10', file=f)
print('\n\n\n', file=f)

for x in sets:
    y = '[%s]' %x
    print(y, file=f)
    print('effect = include\ntemporal = permanent\nfactor = 1\n', file=f)

f.close()


