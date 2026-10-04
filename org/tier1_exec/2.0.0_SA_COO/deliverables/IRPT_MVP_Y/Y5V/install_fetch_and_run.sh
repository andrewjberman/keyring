# Ledger irpt-y5v-20261003, leg D2: fetch the signed install script on the host BY KEY, check its sha256, run it.
# Sent through Systems Manager by host_read.py after both halves are at HEAD and after the operator's head-object of the
# key printed the signed VersionId (the st6 addendum's form: the host role holds no s3:GetObjectVersion). No vendor call.
set -u
NEW=a163441fb0-st19
KEY=ec2/investor-reporting-ycharts/resident/resident_host_install_$NEW.sh
WANT=f940529db4853dd76d1cc8fd581b18f05bffb829675c1cf0eef27b47ffbdd261
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
echo "V1 st19 portfolio $(sha256sum $RUN/intake/portfolio.py | cut -c1-16) value=named mentions $(grep -c 'value=named' $RUN/intake/portfolio.py) enforce $(sha256sum $RUN/_authz/enforce.py | cut -c1-16) reporting_read mentions $(grep -c reporting_read $RUN/_authz/enforce.py)"
echo "V1 unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value); library $(sha256sum $H/ycharts_session.js | cut -c1-16)"
