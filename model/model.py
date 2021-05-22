from adaptnlp import EasyTokenTagger
from adaptnlp.model_hub import HFModelHub

from pprint import pprint


def load_model():
  hub = HFModelHub()
  model = hub.search_model_by_name('emilyalsentzer/Bio_ClinicalBERT', user_uploaded=True)[0]
  return model

def get_note():
  doc_note = """
   Ms J. K. is an 83 year old retired nurse with a long history of hypertension that
  was previously well controlled on diuretic therapy. She was first admitted to CPMC in 1995 when she
  presented with a complaint of intermittent midsternal chest pain. Her electrocardiogram at that time
  showed first degree atrioventricular block, and a chest X-ray showed mild pulmonary congestion, with
  cardiomegaly. Myocardial infarction was ruled out by the lack of electrocardiographic and cardiac enzyme
  abnormalities. Patient was discharged after a brief stay on a regimen of enalapril, and lasix, and digoxin,
  for presumed congestive heart failure. Since then she has been followed closely by her cardiologist. 

  """
  return doc_note

 
def note_results():
  tagger = EasyTokenTagger()
  sentences = tagger.tag_text(text=get_note(), model_name_or_path=load_model())
  
  for sen in sentences:
    pprint(sen)

if __name__ == "__main__":
    note_results()
