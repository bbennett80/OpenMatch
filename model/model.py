from adaptnlp import EasyTokenTagger
from pprint import pprint
from adaptnlp.model_hub import HFModelHub

tagger = EasyTokenTagger()

hub = HFModelHub()
model = hub.search_model_by_name('emilyalsentzer/Bio_ClinicalBERT', user_uploaded=True)[0]

doc_note = """
 Ms J. K. is an 83 year old retired nurse with a long history of hypertension that
was previously well controlled on diuretic therapy. She was first admitted to CPMC in 1995 when she
presented with a complaint of intermittent midsternal chest pain. Her electrocardiogram at that time
showed first degree atrioventricular block, and a chest X-ray showed mild pulmonary congestion, with
cardiomegaly. Myocardial infarction was ruled out by the lack of electrocardiographic and cardiac enzyme
abnormalities. Patient was discharged after a brief stay on a regimen of enalapril, and lasix, and digoxin,
for presumed congestive heart failure. Since then she has been followed closely by her cardiologist. 

"""


sentences = tagger.tag_text(text=doc_note, model_name_or_path=model)


print("List string outputs of tags:\n")
for sen in sentences:
    pprint(sen)
