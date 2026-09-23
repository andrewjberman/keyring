import importlib
import json
import os
import sys
from pathlib import Path
root=Path(os.environ['IRPT_CTO_REVIEW_SOURCE_ROOT'])
os.environ['IRPT_FIRM_DESTINATION_POLICY']=str(root/'firm_destination_policy.json')
sys.path.insert(0,str(root/'infra/aws/lambda/investor-reporting/ycharts/session'))
broker=importlib.import_module('broker')
controller=importlib.import_module('controller')
refreshes=[]
class Broker:
    def refresh(self, prior, count, factory):
        refreshes.append(count)
        return {'allowed':True,'why':None,'session':{'generation':'new'},'read':{'state':'OK'},'transport':factory('new')}
class Store:
    def get_state(self,job_id):
        return {'state':'CREATED','detail':{}}
class Job:
    def __init__(self,transport):
        self.tx=transport
        self.record={'steps':[]}
    def run(self,**kwargs):
        info,body=self.tx.request('/application-read')
        ok=info['status']==200
        self.record['steps'].append({'step':'application-read','status':info['status'],'ok':ok})
        if not ok:
            self.tx.request('/healthy-diagnostic-probe')
        return {'ok':ok,'why':None if ok else 'APPLICATION_READ_FAILED'}
def factory(generation):
    return broker.tx.ReplayTransport({('GET','/application-read'):{'status':200 if generation else 401,'body':{'ok':True} if generation else controller.SIGNED_OUT},('GET','/healthy-diagnostic-probe'):{'status':200,'body':{'ok':True},'content_type':'application/json'}})
result=broker.run_with_recovery(Broker(),Job,{},factory,'job',Store(),'old')
evidence={'source_commit':'4173322f457aeeb390033b410e85bebadc49a3e3','scenario':'known signed-out application read followed by healthy unrelated diagnostic probe','network_calls':0,'outcome':result['outcome'],'refreshes':refreshes,'record':result['record'],'finding_reproduced':result['outcome']=='NOT_AN_EVICTION' and not refreshes}
assert evidence['finding_reproduced']
(root/'failure-correlation.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
print(json.dumps(evidence,indent=2))