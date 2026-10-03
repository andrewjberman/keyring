# Ledger irpt-y4e-20261003, leg D2: fetch the signed install script on the host BY KEY, check its sha256, run it.
# Sent through Systems Manager by host_read.py after both halves are at HEAD and after the operator's head-object of the
# key printed the signed VersionId (the st6 addendum's form: the host role holds no s3:GetObjectVersion). No vendor call.
set -u
NEW=a6f6e7165e-st18
KEY=ec2/investor-reporting-ycharts/resident/resident_host_install_$NEW.sh
WANT=a44b55795b65d71288f2c398cb82fa6973504889a87bc109db3350c220bb64e6
T=/tmp/resident_host_install_$NEW.sh
H=/opt/investor-reporting-ycharts
R=/opt/irpt-resident
UNIT=irpt-analysis-resident.service
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$KEY" $T --only-show-errors --region us-east-1 || { echo "ERROR: fetch failed; nothing moved"; exit 30; }
[ "$(sha256sum $T | cut -d' ' -f1)" = "$WANT" ] || { echo "ERROR: the fetched script is not the signed bytes; nothing moved"; rm -f $T; exit 31; }
echo "install script sha256 verified on the host at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
bash $T
RC=$?
rm -f $T
echo "install script rc=$RC at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
RUN=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)
echo "V1 running root $RUN"
echo "V1 st18 resolution_kimi $(sha256sum $RUN/intake/resolution_kimi.py | cut -c1-16) KIMI_DEADLINE_INVALID mentions $(grep -c KIMI_DEADLINE_INVALID $RUN/intake/resolution_kimi.py) upload_suggestions $(sha256sum $RUN/intake/upload_suggestions.py | cut -c1-16) TOTAL_SUGGEST_SECONDS line [$(grep -c '^TOTAL_SUGGEST_SECONDS = 240$' $RUN/intake/upload_suggestions.py)] resident_worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -c1-16) unasked= mentions $(grep -c 'unasked=' $RUN/ycharts/generate/resident_worker.py)"
echo "V1 riding ops entry $(sha256sum $RUN/ops/entry.py | cut -c1-16) owned_requests $(sha256sum $RUN/ops/owned_requests.py | cut -c1-16) _frozen_composition mentions $(grep -c _frozen_composition $RUN/ops/owned_requests.py)"
echo "V1 host library $(sha256sum $H/ycharts_session.js | cut -c1-16) reason tokens $(grep -c "reason: '[A-Z_]*'" $H/ycharts_session.js) wrapper $(sha256sum $H/run-ycharts-session.sh | cut -c1-16)"
echo "V1 unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value)"
echo "V1 queue $(aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s ' \t' '/')"
exit $RC
