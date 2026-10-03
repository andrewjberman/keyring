# READ-ONLY preflight for leg A (no vendor call, nothing started): the attended run's refusal conditions, read ahead.
set -u
H=/opt/investor-reporting-ycharts
echo "preflight at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Xvnc: $(command -v Xvnc || echo ABSENT)"
echo "vncpasswd: $(command -v vncpasswd || echo ABSENT)"
echo "listening on 5901: [$(ss -ltnH | grep -c ':5901 ')]"
echo "Xvnc processes: [$(pgrep -c Xvnc 2>/dev/null || echo 0)]"
echo "library attended mode: YC_ATTENDED mentions $(grep -c YC_ATTENDED $H/ycharts_session.js) holdForPerson mentions $(grep -c holdForPerson $H/ycharts_session.js) sha $(sha256sum $H/ycharts_session.js | cut -c1-16)"
echo "wrapper sha $(sha256sum $H/run-ycharts-session.sh | cut -c1-16)"
echo "leftover attended files: [$(ls /root/irpt-attended 2>/dev/null | wc -l)]"
echo "resident unit: $(systemctl is-active irpt-analysis-resident.service)"
