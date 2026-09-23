import importlib
import json
import os
import sys
from pathlib import Path
root = Path(os.environ.get('IRPT_CTO_REVIEW_SOURCE_ROOT', str(Path(__file__).resolve().parent)))
sys.path.insert(0, str(root / 'infra/aws/lambda/investor-reporting/intake'))
resolution_kimi = importlib.import_module('resolution_kimi')
KimiAdvisory = resolution_kimi.KimiAdvisory
KimiFailure = resolution_kimi.KimiFailure
now = [0.0]
timeouts = []
events = []
def send(payload, *, timeout_seconds):
    timeouts.append(timeout_seconds)
    now[0] += 119
    if len(timeouts) == 1:
        raise KimiFailure('KIMI_HTTP', status=503)
    return {'choices': [{'finish_reason':'stop','message': {'content': json.dumps({'suggestion':'AAPL','confidence':0.9,'reason':'Synthetic typo control'})}}]}
result = KimiAdvisory(send=send, telemetry=events.append, clock=lambda: now[0]).call('check','ALPPL')
evidence = {'source_commit':'6cfe01c3e238e9a90e88d3a501b25ac0eaf41540','network_calls':0,'advertised_total_seconds':120,'elapsed_seconds':now[0],'transport_timeout_arguments':timeouts,'result':result,'finding_reproduced':result['failure'] is None and now[0] > 120}
print(json.dumps(evidence,indent=2))
assert evidence['finding_reproduced']

