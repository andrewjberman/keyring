set -uo pipefail
# Ledger irpt-resident-st4-yr201-yr211-20260929 leg D1: fe64236bbb-st3 -> fe64236bbb-st4 (st3 plus ycharts/generate/recipe.py and
# ycharts/generate/resident_worker.py @0357fc7e08 (rebuilt on IB-yr-221 amendment 1, CTO 102687/102724): IB-yr-201 (S194, a Comparison sends its models and refuses a PDF printing none) and
# IB-yr-211 (S193, a resolve RETRY is logged and re-offered in 60 s)). The st3 root stays for rollback. Factory pre-check on resident_main.py's sys.path.
NEW=fe64236bbb-st4
OLD=fe64236bbb-st3
R=/opt/irpt-resident
ROOT=$R/$NEW
UNIT=irpt-analysis-resident.service
Q=https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation
KEY=ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz
WANT_TAR=63a5e26a3caa3a00f03f4361dc2a8f2d1a21bc31797af665d45224b745dfd054
WANT_RECIPE=b2fbd720eefcd76751a16ae662a76d81e6ffbf99c98273771a26ed894d4f611f
WANT_WORKER=5288ff5abc7aacd994ee578f190e641c6ec0639d2760673b05acf552c2426c87
WANT_EXTRACT=719369d54841ca918adf2f698583c9862007f755ac01fc6644e6679968568b20
WANT_TEMPLATES=54656584f476b616622368d60c227b1519a70f3e9aced14edb88c776f9823866
WANT_PUBLICATION=6aa82b3ad2d30ea47dc74bb97dd0abfd04f95f7974432f386a95e871f5912184
WANT_PUBLISHER=68900af64ba49972dd5183440972bf4171e8a3b0ac4193634ffc16a7a5c36ea1
WANT_SOURCES=774eca9bde60a1dd4e9c1aaffc73b3b9ae41fbe85914a28cc4b506d3c9edba61
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
[ "$(sha256sum ycharts/generate/recipe.py | cut -d' ' -f1)" = "$WANT_RECIPE" ] || { echo "ERROR: recipe.py is not 0357fc7e08"; exit 17; }
[ "$(sha256sum ycharts/generate/resident_worker.py | cut -d' ' -f1)" = "$WANT_WORKER" ] || { echo "ERROR: resident_worker.py is not 0357fc7e08"; exit 17; }
[ "$(sha256sum ycharts/extract/extract.py | cut -d' ' -f1)" = "$WANT_EXTRACT" ] || { echo "ERROR: extract.py is not 12a67ed5ee"; exit 17; }
[ "$(sha256sum ycharts/generate/templates.json | cut -d' ' -f1)" = "$WANT_TEMPLATES" ] || { echo "ERROR: templates.json is not 6096ee740b"; exit 17; }
[ "$(sha256sum ycharts/extract/publication.py | cut -d' ' -f1)" = "$WANT_PUBLICATION" ] || { echo "ERROR: publication.py is not c1fd6c5e52"; exit 17; }
[ "$(sha256sum ycharts/generate/publisher.py | cut -d' ' -f1)" = "$WANT_PUBLISHER" ] || { echo "ERROR: publisher.py is not c1fd6c5e52"; exit 17; }
[ "$(sha256sum _scope/maintained_sources.py | cut -d' ' -f1)" = "$WANT_SOURCES" ] || { echo "ERROR: maintained_sources.py is not 15b9f85eb3"; exit 17; }
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
          "written_at": "2026-09-29T0xxxZ", "ledger": "irpt-resident-st4-yr201-yr211-20260929"})
open(path, "w").write(json.dumps(r, indent=2) + "\n")
PY
chown ec2-user:ec2-user SHA256SUMS $R/cutover_receipt.json
sudo -u ec2-user PYTHONPATH="$ROOT" /usr/bin/python3.12 - "$ROOT" <<'PY'
import sys
# the factory check runs on resident_main.py's OWN sys.path (ycharts/generate/resident_main.py:17-21): the st
# worker imports `extract` at module level, which lt's did not, so a reports-only path cannot import it
for rel in ('intake', 'ops', 'reports', '_keys', '_authz', '_gate', 'ycharts/session', 'ycharts/extract'):
    sys.path.insert(0, sys.argv[1] + '/' + rel)
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
