# Ledger irpt-resident-st9-20261001, leg D1: fetch the signed install script on the host BY KEY, check its sha256, run it.
# Sent through Systems Manager by host_read.py after both halves are at HEAD and after the operator's head-object of the
# key printed the signed VersionId (the st6 addendum's form: the host role holds no s3:GetObjectVersion). No vendor call.
set -u
NEW=481166a8f2-st9
KEY=ec2/investor-reporting-ycharts/resident/resident_host_install_$NEW.sh
WANT=5350877bd4e1a16537f935d3e68717f5a831bd77f85c68e5c9de6bfe24a53332
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
echo "V1 resident_worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -c1-16) READ_BACK_CALCULATING_VISIBILITY_S mentions $(grep -c READ_BACK_CALCULATING_VISIBILITY_S $RUN/ycharts/generate/resident_worker.py)"
echo "V1 current_authority $(sha256sum $RUN/ycharts/generate/current_authority.py | cut -c1-16) is_service mentions $(grep -c is_service $RUN/ycharts/generate/current_authority.py)"
echo "V1 host_capture $(sha256sum $RUN/ycharts/session/host_capture.py | cut -c1-16) extract $(sha256sum $RUN/ycharts/extract/extract.py | cut -c1-16) resident_session $(sha256sum $RUN/ycharts/session/resident_session.py | cut -c1-16) recipe $(sha256sum $RUN/ycharts/generate/recipe.py | cut -c1-16) READ_BACK_POLLS line [$(grep -c '^READ_BACK_POLLS = 1$' $RUN/ycharts/generate/recipe.py)]"
echo "V1 host library $(sha256sum $H/ycharts_session.js | cut -c1-16) reason tokens $(grep -c "reason: '[A-Z_]*'" $H/ycharts_session.js) wrapper $(sha256sum $H/run-ycharts-session.sh | cut -c1-16)"
echo "V1 unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value)"
echo "V1 queue $(aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s ' \t' '/')"
exit $RC
