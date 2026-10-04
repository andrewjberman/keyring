# Ledger irpt-y5d-20261004, leg D2: fetch the signed install script on the host BY KEY, check its sha256, run it.
# Sent through Systems Manager by host_read.py after both halves are at HEAD and after the operator's head-object of the
# key printed the signed VersionId (the st6 addendum's form: the host role holds no s3:GetObjectVersion). No vendor call.
set -u
NEW=3f29017cfc-st21
KEY=ec2/investor-reporting-ycharts/resident/resident_host_install_$NEW.sh
WANT=8c3a4fc1e8bbb5026604bf379b7afbb7b307a9a16221d501a32334693ac2643b
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
echo "V1 st21 normalized_input $(sha256sum $RUN/ycharts/generate/normalized_input.py | cut -c1-16) _cents mentions $(grep -c _cents $RUN/ycharts/generate/normalized_input.py) resident_worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -c1-16) bind_upload_or_attention mentions $(grep -c bind_upload_or_attention $RUN/ycharts/generate/resident_worker.py)"
echo "V1 unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value); library $(sha256sum $H/ycharts_session.js | cut -c1-16)"
