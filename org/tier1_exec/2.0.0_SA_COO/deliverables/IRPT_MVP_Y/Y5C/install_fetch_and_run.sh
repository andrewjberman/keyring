# Ledger irpt-y5c-20261003, leg D2: fetch the signed install script on the host BY KEY, check its sha256, run it.
# Sent through Systems Manager by host_read.py after both halves are at HEAD and after the operator's head-object of the
# key printed the signed VersionId (the st6 addendum's form: the host role holds no s3:GetObjectVersion). No vendor call.
set -u
NEW=136ee09e9f-st20
KEY=ec2/investor-reporting-ycharts/resident/resident_host_install_$NEW.sh
WANT=b06a67203d7de3074e4bd171d76e2bdae3dba263621ca20dff9a2a571ce602ea
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
echo "V1 st20 recipe $(sha256sum $RUN/ycharts/generate/recipe.py | cut -c1-16) _cents mentions $(grep -c _cents $RUN/ycharts/generate/recipe.py) resident_worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -c1-16) echo_counts mentions $(grep -c echo_counts $RUN/ycharts/generate/resident_worker.py) portfolio $(sha256sum $RUN/intake/portfolio.py | cut -c1-16)"
echo "V1 unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value); library $(sha256sum $H/ycharts_session.js | cut -c1-16)"
