set -uo pipefail
# Ledger irpt-hop3-generate-resident-20260926 leg R1 (CTO 101438/101441): the resident package moves
# f624e8a72f -> fe64236bbb (f624e8a72f + ~Y's six hop-3 files at a219094b1a). The f624e8a72f root stays for rollback.
PIN=fe64236bbb
OLD=f624e8a72f
ROOT=/opt/irpt-resident/$PIN
KEY=ec2/investor-reporting-ycharts/resident/irpt-resident-$PIN.tar.gz
VER=E.Ia.MwxvaDrgwD0XbQXN1Nr7ZT.fPy2
UNIT=irpt-analysis-resident.service
echo "before: active=$(systemctl is-active $UNIT) root=$(systemctl show $UNIT -p ExecStart | grep -o '/opt/irpt-resident/[0-9a-f]*' | head -1)"
test -d /opt/irpt-resident/$OLD || { echo "ERROR: rollback root $OLD absent"; exit 10; }
rm -rf "$ROOT"; mkdir -p "$ROOT"
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$KEY" /tmp/irpt-resident-$PIN.tar.gz --only-show-errors --region us-east-1 || exit 11
TARSHA=$(sha256sum /tmp/irpt-resident-$PIN.tar.gz | cut -d' ' -f1)
echo "tar sha $TARSHA bytes $(stat -c %s /tmp/irpt-resident-$PIN.tar.gz) (built: version $VER)"
[ "$TARSHA" = "05ac177e5cf01cbe3e68f6ef7ac3f208dfc1311d688a509d23556401511be95e" ] || { echo "ERROR: tar is not the built bytes"; exit 16; }
tar -xzf /tmp/irpt-resident-$PIN.tar.gz -C "$ROOT" || exit 12
cd "$ROOT" || exit 13
sha256sum -c SHA256SUMS --quiet && echo "package SHA256SUMS OK ($(wc -l < SHA256SUMS) members)" || exit 14
cp -a /opt/investor-reporting-ycharts/pydeps/. "$ROOT/"
rm -rf "$ROOT/bin"
chown -R ec2-user:ec2-user "$ROOT"
python3.12 - <<'PY'
import hashlib, os
rows = []
for dp, dn, fn in os.walk('.'):
    for f in fn:
        p = os.path.join(dp, f)
        if p == './SHA256SUMS':
            continue
        rows.append(hashlib.sha256(open(p, 'rb').read()).hexdigest() + '  ' + p)
rows.sort(key=lambda r: r.split('  ', 1)[1])
open('SHA256SUMS', 'w').write('\n'.join(rows) + '\n')
PY
MAN=$(sha256sum SHA256SUMS | cut -d' ' -f1)
echo "host members $(wc -l < SHA256SUMS) manifest_sha $MAN"
for f in custody_submission.py prospect_submission.py recipe.py recipe_snapshot.py submission.py templates.json; do
  echo "HOP3 $(sha256sum ycharts/generate/$f | cut -d' ' -f1) ycharts/generate/$f"
done
cp -p /opt/irpt-resident/cutover_receipt.json /opt/irpt-resident/cutover_receipt.$OLD.json
python3.12 - "$MAN" "$ROOT" <<'PY'
import json, sys
path = "/opt/irpt-resident/cutover_receipt.json"
r = json.load(open(path))
r.update({"package_manifest_sha256": sys.argv[1], "package_root": sys.argv[2], "written_by": "2.0.0_SA_COO~P",
          "written_at": "2026-09-26T19:1xZ", "ledger": "irpt-hop3-generate-resident-20260926"})
open(path, "w").write(json.dumps(r, indent=2) + "\n")
print("receipt keys:", sorted(r))
PY
chown ec2-user:ec2-user SHA256SUMS /opt/irpt-resident/cutover_receipt.json
sudo -u ec2-user PYTHONPATH="$ROOT" /usr/bin/python3.12 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + '/reports')
import resident_installed as ri
rt = ri.build_resident_runtime()
print('factory OK:', sorted(rt), 'queue', rt['queue_url'], 'enrolled', rt['assembly'].session.broker.enrolled_user_id)
PY
RC=$?
echo "factory dry-run rc=$RC"
if [ $RC -ne 0 ]; then
  cp -p /opt/irpt-resident/cutover_receipt.$OLD.json /opt/irpt-resident/cutover_receipt.json
  echo "BLOCKED: factory failed; receipt restored, unit untouched"; exit 15
fi
PYTHONPATH="$ROOT" bash "$ROOT/ycharts/generate/install-resident.sh" "$ROOT" /usr/bin/python3.12 resident_installed:build_resident_runtime ec2-user /opt/irpt-resident/cutover_receipt.json
echo "install rc=$?"
sleep 25
echo "active: $(systemctl is-active $UNIT)"
systemctl show $UNIT -p MainPID -p ActiveEnterTimestamp -p NRestarts -p ExecMainStatus -p ExecStart | cut -c1-220
journalctl -u $UNIT --since "-1 min" --no-pager -o short-iso | cut -c1-200 | tail -12
