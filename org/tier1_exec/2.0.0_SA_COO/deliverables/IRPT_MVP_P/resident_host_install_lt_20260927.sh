set -uo pipefail
# Ledger irpt-resident-level-tolerated-20260927 leg R1 (~Y 101938): fe64236bbb-rs -> fe64236bbb-lt (the same package plus
# ycharts/generate/recipe.py + resident_worker.py from 49b85eacd2, the read-back tolerating level_as_of_type). The rs root stays for
# rollback. One command: stage, verify, controlled stop on an empty queue, install, verify, and roll back to rs on any failure.
NEW=fe64236bbb-lt
OLD=fe64236bbb-rs
R=/opt/irpt-resident
ROOT=$R/$NEW
UNIT=irpt-analysis-resident.service
Q=https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation
KEY=ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-lt.tar.gz
WANT_TAR=ae854f00cb0252d6fd319eb6726da2529cca835f297c7fb435eba323fc96322a
WANT_RECIPE=339e0c0ebf295ee420ad598a96e4df71519da0dd4cc6d66cc18a4b6a8caac738
WANT_WORKER=388f6e7fe77822c338ab9ba2d37e3517f8910ce3065f3f8f83e0b0bd3e060151
WANT_MAIN=0e5c17e7b9ccc2386e5104f7a9030e4cee18722f826b04a32dabfdebb493bfb1
WANT_BROKER=3d490d6d719569c9abc9d4c7998156c25f1e1e72edbe32cec924e145131355a7
WANT_CAPTURE=5170522cb2782b6c2b1b444b180d04c52a7b5bc79777fcbfea55fcafe9f5a0ab
echo "before: active=$(systemctl is-active $UNIT) root=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)"
test -d $R/$OLD || { echo "ERROR: rollback root $OLD absent"; exit 10; }
rm -rf "$ROOT"; mkdir -p "$ROOT"
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$KEY" /tmp/irpt-resident-$NEW.tar.gz --only-show-errors --region us-east-1 || exit 11
[ "$(sha256sum /tmp/irpt-resident-$NEW.tar.gz | cut -d' ' -f1)" = "$WANT_TAR" ] || { echo "ERROR: tar is not the built bytes"; exit 16; }
tar -xzf /tmp/irpt-resident-$NEW.tar.gz -C "$ROOT" || exit 12
cd "$ROOT" || exit 13
sha256sum -c SHA256SUMS --quiet && echo "package SHA256SUMS OK ($(wc -l < SHA256SUMS) members)" || exit 14
[ "$(sha256sum ycharts/generate/recipe.py | cut -d' ' -f1)" = "$WANT_RECIPE" ] || { echo "ERROR: recipe.py is not 49b85eacd2"; exit 17; }
[ "$(sha256sum ycharts/generate/resident_worker.py | cut -d' ' -f1)" = "$WANT_WORKER" ] || { echo "ERROR: resident_worker.py is not 49b85eacd2"; exit 17; }
[ "$(sha256sum ycharts/session/broker.py | cut -d' ' -f1)" = "$WANT_BROKER" ] || { echo "ERROR: broker.py is not e2fdd01015"; exit 17; }
[ "$(sha256sum ycharts/session/host_capture.py | cut -d' ' -f1)" = "$WANT_CAPTURE" ] || { echo "ERROR: host_capture.py is not ec5804f6e0"; exit 17; }
[ "$(sha256sum ycharts/generate/resident_main.py | cut -d' ' -f1)" = "$WANT_MAIN" ] || { echo "ERROR: resident_main.py is not ec5804f6e0"; exit 17; }
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
cp -p $R/cutover_receipt.json $R/cutover_receipt.$OLD.json
python3.12 - "$MAN" "$ROOT" <<'PY'
import json, sys
path = "/opt/irpt-resident/cutover_receipt.json"
r = json.load(open(path))
r.update({"package_manifest_sha256": sys.argv[1], "package_root": sys.argv[2], "written_by": "2.0.0_SA_COO~P",
          "written_at": "2026-09-27T15:5xZ", "ledger": "irpt-resident-level-tolerated-20260927"})
open(path, "w").write(json.dumps(r, indent=2) + "\n")
PY
chown ec2-user:ec2-user SHA256SUMS $R/cutover_receipt.json
sudo -u ec2-user PYTHONPATH="$ROOT" /usr/bin/python3.12 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + '/reports')
import resident_installed as ri
rt = ri.build_resident_runtime()
print('factory OK:', sorted(rt), 'enrolled', rt['assembly'].session.broker.enrolled_user_id)
PY
if [ $? -ne 0 ]; then cp -p $R/cutover_receipt.$OLD.json $R/cutover_receipt.json; echo "BLOCKED: factory failed; receipt restored, unit untouched"; exit 15; fi
DEPTH=$(aws sqs get-queue-attributes --queue-url $Q --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text)
echo "queue visible/in-flight: $DEPTH"
if [ "$(echo $DEPTH | tr -s ' \t' ' ')" != "0 0" ]; then cp -p $R/cutover_receipt.$OLD.json $R/cutover_receipt.json; echo "BLOCKED: queue not empty; receipt restored, unit untouched"; exit 20; fi
systemctl stop $UNIT
install_root() {
  PYTHONPATH="$R/$1" bash "$R/$1/ycharts/generate/install-resident.sh" "$R/$1" /usr/bin/python3.12 resident_installed:build_resident_runtime ec2-user $R/cutover_receipt.json
}
install_root $NEW
RC=$?
echo "install $NEW rc=$RC"
sleep 25
ACTIVE=$(systemctl is-active $UNIT)
POLLS=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "IRPT_RESIDENT_POLL")
TRACE=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "Traceback")
echo "active=$ACTIVE polls_30s=$POLLS tracebacks_30s=$TRACE"
if [ $RC -ne 0 ] || [ "$ACTIVE" != active ] || [ "$POLLS" -lt 1 ] || [ "$TRACE" -ne 0 ]; then
  echo "ROLLBACK to $OLD"
  systemctl stop $UNIT
  cp -p $R/cutover_receipt.$OLD.json $R/cutover_receipt.json
  install_root $OLD
  echo "rollback install rc=$?"
  sleep 20
fi
echo "final active: $(systemctl is-active $UNIT)"
systemctl show $UNIT -p MainPID -p ActiveEnterTimestamp -p NRestarts -p ExecStart | cut -c1-200
journalctl -u $UNIT --since "-1 min" --no-pager -o short-iso | cut -c1-200 | tail -6
RUN=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)
echo "running root $RUN recipe $(sha256sum $RUN/ycharts/generate/recipe.py | cut -d' ' -f1) worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -d' ' -f1) broker $(sha256sum $RUN/ycharts/session/broker.py | cut -d' ' -f1) capture $(sha256sum $RUN/ycharts/session/host_capture.py | cut -d' ' -f1) main $(sha256sum $RUN/ycharts/generate/resident_main.py | cut -d' ' -f1)"
