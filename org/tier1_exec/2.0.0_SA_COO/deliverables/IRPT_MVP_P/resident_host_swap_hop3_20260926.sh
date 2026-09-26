set -uo pipefail
# Ledger irpt-hop3-generate-resident-20260926 leg R1, step 2: the controlled stop install-resident.sh requires
# ("resident already active; use controlled drain/stop before replacement"). Step 1 staged /opt/irpt-resident/fe64236bbb
# and re-bound the receipt; the running unit stayed on f624e8a72f. Rollback on any failure: f624e8a72f reinstalled.
PIN=fe64236bbb
OLD=f624e8a72f
UNIT=irpt-analysis-resident.service
Q=https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation
R=/opt/irpt-resident
DEPTH=$(aws sqs get-queue-attributes --queue-url $Q --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text)
echo "queue visible/in-flight: $DEPTH"
[ "$(echo $DEPTH | tr -s ' \t' ' ')" = "0 0" ] || { echo "BLOCKED: queue not empty; unit untouched"; exit 20; }
test -f $R/$PIN/SHA256SUMS -a -d $R/$OLD -a -f $R/cutover_receipt.$OLD.json || { echo "ERROR: staged state missing"; exit 21; }
systemctl stop $UNIT
echo "stopped: $(systemctl is-active $UNIT)"
install_root() {
  PYTHONPATH="$R/$1" bash "$R/$1/ycharts/generate/install-resident.sh" "$R/$1" /usr/bin/python3.12 resident_installed:build_resident_runtime ec2-user $R/cutover_receipt.json
}
install_root $PIN
RC=$?
echo "install $PIN rc=$RC"
sleep 25
ACTIVE=$(systemctl is-active $UNIT)
NEWPID=$(systemctl show $UNIT -p MainPID --value)
POLLS=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "IRPT_RESIDENT_POLL")
TRACE=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "Traceback")
echo "active=$ACTIVE pid=$NEWPID polls_30s=$POLLS tracebacks_30s=$TRACE"
if [ $RC -ne 0 ] || [ "$ACTIVE" != active ] || [ "$POLLS" -lt 1 ] || [ "$TRACE" -ne 0 ]; then
  echo "ROLLBACK to $OLD"
  systemctl stop $UNIT
  cp -p $R/cutover_receipt.json $R/cutover_receipt.$PIN.failed.json
  cp -p $R/cutover_receipt.$OLD.json $R/cutover_receipt.json
  install_root $OLD
  echo "rollback install rc=$?"
  sleep 20
fi
echo "final active: $(systemctl is-active $UNIT)"
systemctl show $UNIT -p MainPID -p ActiveEnterTimestamp -p NRestarts -p ExecStart | cut -c1-200
journalctl -u $UNIT --since "-1 min" --no-pager -o short-iso | cut -c1-200 | tail -8
echo "HOST-ROOT-HOP3"
ROOT=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-f]*" | head -1)
echo "root $ROOT"
for f in custody_submission.py prospect_submission.py recipe.py recipe_snapshot.py submission.py templates.json; do
  echo "HOP3 $(sha256sum $ROOT/ycharts/generate/$f | cut -d' ' -f1) ycharts/generate/$f"
done
