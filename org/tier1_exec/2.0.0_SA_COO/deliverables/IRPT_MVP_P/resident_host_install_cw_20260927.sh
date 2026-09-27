set -uo pipefail
# Ledger irpt-resident-capture-env-20260927 leg R1 (CTO 101897): fe64236bbb-wf -> fe64236bbb-cw (the same package plus
# ycharts/generate/recipe.py + resident_worker.py + ycharts/session/host_capture.py from b6739556ea, ~Y's W11 fixes). The wf root
# stays for rollback. One command: stage, verify, controlled stop on an empty queue, install, verify, and roll back to wf on any failure.
NEW=fe64236bbb-cw
OLD=fe64236bbb-wf
R=/opt/irpt-resident
ROOT=$R/$NEW
UNIT=irpt-analysis-resident.service
Q=https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation
KEY=ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-cw.tar.gz
WANT_TAR=32e1122af87b9088cf63f270e36cd8c18510a6793919f5c43df2de77fb2298a6
WANT_RECIPE=5224b2245912a0687188376c9ed1a24cee283f0195fb51467df770f3ad18d52b
WANT_WORKER=d54bd0e55fcff1fcf3c843636623d2770ebae11d0c8ecaf37a54f508ea36b9e7
WANT_BROKER=3d490d6d719569c9abc9d4c7998156c25f1e1e72edbe32cec924e145131355a7
WANT_CAPTURE=2905c73b0cb8c85a4b45e652742099cace37df4f916abb3a0900b5b6041a8d1d
echo "before: active=$(systemctl is-active $UNIT) root=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)"
test -d $R/$OLD || { echo "ERROR: rollback root $OLD absent"; exit 10; }
rm -rf "$ROOT"; mkdir -p "$ROOT"
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$KEY" /tmp/irpt-resident-$NEW.tar.gz --only-show-errors --region us-east-1 || exit 11
[ "$(sha256sum /tmp/irpt-resident-$NEW.tar.gz | cut -d' ' -f1)" = "$WANT_TAR" ] || { echo "ERROR: tar is not the built bytes"; exit 16; }
tar -xzf /tmp/irpt-resident-$NEW.tar.gz -C "$ROOT" || exit 12
cd "$ROOT" || exit 13
sha256sum -c SHA256SUMS --quiet && echo "package SHA256SUMS OK ($(wc -l < SHA256SUMS) members)" || exit 14
[ "$(sha256sum ycharts/generate/recipe.py | cut -d' ' -f1)" = "$WANT_RECIPE" ] || { echo "ERROR: recipe.py is not b6739556ea"; exit 17; }
[ "$(sha256sum ycharts/generate/resident_worker.py | cut -d' ' -f1)" = "$WANT_WORKER" ] || { echo "ERROR: resident_worker.py is not b6739556ea"; exit 17; }
[ "$(sha256sum ycharts/session/broker.py | cut -d' ' -f1)" = "$WANT_BROKER" ] || { echo "ERROR: broker.py is not e2fdd01015"; exit 17; }
[ "$(sha256sum ycharts/session/host_capture.py | cut -d' ' -f1)" = "$WANT_CAPTURE" ] || { echo "ERROR: host_capture.py is not b6739556ea"; exit 17; }
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
          "written_at": "2026-09-27T13:5xZ", "ledger": "irpt-resident-capture-env-20260927"})
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
echo "running root $RUN recipe $(sha256sum $RUN/ycharts/generate/recipe.py | cut -d' ' -f1) worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -d' ' -f1) broker $(sha256sum $RUN/ycharts/session/broker.py | cut -d' ' -f1) capture $(sha256sum $RUN/ycharts/session/host_capture.py | cut -d' ' -f1)"
