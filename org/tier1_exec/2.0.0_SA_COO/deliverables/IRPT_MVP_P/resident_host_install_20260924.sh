set -uo pipefail
PIN=ab2e088b5b
ROOT=/opt/irpt-resident/$PIN
P=s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/resident
# the first install's unit is failing on the mangled census path; replace the package under it
systemctl disable --now irpt-analysis-resident.service || true
systemctl reset-failed irpt-analysis-resident.service || true
rm -rf "$ROOT"; mkdir -p "$ROOT"
aws s3 cp "$P/irpt-resident-$PIN.tar.gz" /tmp/irpt-resident-$PIN.tar.gz --only-show-errors --region us-east-1 || exit 11
echo "tar sha $(sha256sum /tmp/irpt-resident-$PIN.tar.gz | cut -c1-16)"
tar -xzf /tmp/irpt-resident-$PIN.tar.gz -C "$ROOT" || exit 12
cp -a /opt/investor-reporting-ycharts/pydeps/. "$ROOT/"
rm -rf "$ROOT/bin"
chown -R ec2-user:ec2-user /opt/irpt-resident
cd "$ROOT" || exit 13
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
echo "members $(wc -l < SHA256SUMS) manifest_sha $MAN"
python3.12 - "$MAN" <<'PY'
import json, sys
r = {"instance_id": "i-0167fd745ad906a66", "legacy_probe_disabled": True, "per_job_power_cycle_disabled": True,
     "other_queue_consumers_disabled": True, "shared_authority_factory_installed": True,
     "package_manifest_sha256": sys.argv[1], "evidence_path": "/opt/irpt-resident/RESIDENT_CUTOVER_EVIDENCE_20260924.json",
     "package_root": "/opt/irpt-resident/ab2e088b5b", "written_by": "2.0.0_SA_COO~P", "written_at": "2026-09-24T09:4xZ"}
open("/opt/irpt-resident/cutover_receipt.json", "w").write(json.dumps(r, indent=2) + "\n")
PY
chown ec2-user:ec2-user SHA256SUMS /opt/irpt-resident/cutover_receipt.json
echo "bindings census path: $(python3.12 -c "import json;print(json.load(open('$ROOT/reports/resident_bindings.json'))['census']['path'])")"
# a dry factory build as the service user BEFORE the unit: pins + clients + stores, no poll, no vendor call
sudo -u ec2-user PYTHONPATH="$ROOT" /usr/bin/python3.12 - <<'PY'
import sys
sys.path.insert(0, '/opt/irpt-resident/ab2e088b5b/reports')
import resident_installed as ri
rt = ri.build_resident_runtime()
print('factory OK:', sorted(rt), 'queue', rt['queue_url'], 'enrolled', rt['assembly'].session.broker.enrolled_user_id)
PY
echo "factory dry-run rc=$?"
PYTHONPATH="$ROOT" bash "$ROOT/ycharts/generate/install-resident.sh" "$ROOT" /usr/bin/python3.12 resident_installed:build_resident_runtime ec2-user /opt/irpt-resident/cutover_receipt.json
echo "install rc=$?"
sleep 20
echo "active: $(systemctl is-active irpt-analysis-resident.service)"
systemctl show irpt-analysis-resident.service -p MainPID -p ActiveEnterTimestamp -p NRestarts -p ExecMainStatus
journalctl -u irpt-analysis-resident.service --since "-2 min" --no-pager -o short-iso | cut -c1-200 | tail -25
