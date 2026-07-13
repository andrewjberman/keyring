"""Does the NNA reconciliation guard (sum(advisors) == firm_total) DETECT the deletion?
Exercised, not argued. If the invariant survives, the guard is a CANNOT-GO-RED instrument."""
import io
import boto3
import pandas as pd
s3 = boto3.client('s3', region_name='us-east-1')
B = 'opal-data-inf'
pager = s3.get_paginator('list_objects_v2')
keys = [o['Key'] for pg in pager.paginate(Bucket=B, Prefix='gold/canonical/canonical_nna_')
        for o in pg.get('Contents', [])]
g = pd.concat([pd.read_parquet(io.BytesIO(s3.get_object(Bucket=B, Key=k)['Body'].read())) for k in keys],
              ignore_index=True)
g['account_id'] = g['account_id'].astype(str)
CLASS_B = ['77', '100', '235', '302', '331', '360', '520', '735', '759', '963', '980', '1086', '1208', '1294']

def recon(df, label):
    per_adv = df.groupby('advisor_key')['net_nna'].sum()
    firm = df['net_nna'].sum()
    ok = abs(per_adv.sum() - firm) < 0.01
    print(f'  {label:<28} sum(advisors)=${per_adv.sum():>15,.2f}  firm_total=${firm:>15,.2f}  '
          f'TIES: {ok}')
    return per_adv, firm, ok

print('=== THE GUARD: sum(advisors) == firm_total. Does DELETION break it? ===\n')
before, fb, ok_b = recon(g, 'BEFORE (served today)')
after_df = g[~g.account_id.isin(CLASS_B)]
after, fa, ok_a = recon(after_df, 'AFTER (Class-B deleted)')

print(f'\n  money that VANISHED: ${fb - fa:,.2f}')
print(f'  guard verdict BEFORE: {"GREEN" if ok_b else "RED"}')
print(f'  guard verdict AFTER : {"GREEN" if ok_a else "RED"}   <<< the whole question')
print('\n=== PER-ADVISOR: who loses what, and does anything complain? ===')
for a in sorted(set(before.index) | set(after.index)):
    b = before.get(a, 0.0)
    aa = after.get(a, 0.0)
    d = aa - b
    flag = '   <<< SILENTLY LOSES MONEY' if abs(d) > 0.01 else ''
    print(f'  {a:<30} before=${b:>14,.2f}  after=${aa:>14,.2f}  delta=${d:>13,.2f}{flag}')
print('\n=== VERDICT ===')
if ok_b and ok_a:
    print('  *** THE GUARD IS GREEN ON BOTH SIDES. IT CANNOT SEE THE DELETION. ***')
    print('  *** A DELETION PRESERVES THE INVARIANT: the money leaves BOTH sides at once. ***')
    print('  *** This is a CANNOT-GO-RED instrument for this class -- exactly what the HOLD claims. ***')
else:
    print('  the guard DOES fire -- the hold\'s claim would be WRONG.')
