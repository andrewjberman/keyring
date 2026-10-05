# IRPT_BCKEND~Y: the YCharts firewall window, measured once, for READ_BACK_LEASE_TTL_S (ycharts/generate/recipe.py:688,
# CTO rulings batch 97 item 4: a redelivery 122 s later was challenged; about 900 s later answered 4 of 4). On
# 2026-10-05, five research windows 660 s apart were clean, so the window lies in (122, 660] s. Run AFTER Y-6 ends, with
# the queue empty and no job in flight, never between page runs.
# ONE run, waf_window_probe_map.json: 12 public-ticker /securities/securities_info reads (no client data), split by the
# runner's budget (YCD-r-4, contract 4.1) into 2 windows of 6 with the lease released and W seconds between, 8 s apart.
# Request 7 answered 200 => the window is at most W + ~48 s; challenged (202) => longer than W. A challenge STOPS the
# run (no retry), and the session then rests 660 s before any job. W=330 tests the 300 s evaluation window.
# THIS IS A LIVE YCHARTS READ (Andrew-direct ~17:3xZ 2026-10-03, record @ce20ca6854). Bundle fetched BY KEY, checked by
# sha256. No sign-in, no session write, no generate call. Bounded at 600 s. ASCII only.
set -u
umask 077
BUNDLE_KEY=ec2/investor-reporting-ycharts/resident/ycdgen/waf-probe-bundle-087de46e2c25.tar.gz
WANT=087de46e2c25a02b4747e95970c4dacada9eb25223c800949b78c7b7ef1bf8ac
WINDOW_S=${WINDOW_S:-330}
REQ=WAF-PROBE-$(date -u +%Y%m%dT%H%MZ)-W$WINDOW_S
PORTFOLIO=PROBE:waf-window  # its own index key: the model portfolio P:2377833 keeps its previous-run entry (FWD-2)
UNIT=irpt-analysis-resident.service
PID=$(systemctl show $UNIT -p MainPID --value)
ROOT=$(readlink /proc/$PID/cwd)
echo "waf probe start $(date -u +%Y-%m-%dT%H:%M:%SZ) W=$WINDOW_S resident pid $PID root $ROOT"
T=$(mktemp -d /tmp/irpt-ycdgen-XXXXXX)
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$BUNDLE_KEY" "$T/bundle.tar.gz" --only-show-errors --region us-east-1 || { echo "ERROR: fetch failed; nothing ran"; rm -rf "$T"; exit 30; }
GOT=$(sha256sum "$T/bundle.tar.gz" | cut -d' ' -f1)
[ "$GOT" = "$WANT" ] || { echo "ERROR: bundle sha256 $GOT is not the signed bytes; nothing ran"; rm -rf "$T"; exit 31; }
mkdir -p "$T/research"
tar -xzf "$T/bundle.tar.gz" -C "$T/research" || { echo "ERROR: extract failed; nothing ran"; rm -rf "$T"; exit 32; }
cat > "$T/drive.py" <<'PY'
import sys
root, research = sys.argv[1], sys.argv[2]
sys.path.insert(0, root + "/ycharts/generate")
import resident_main  # noqa: F401,E402  (the unit's own path setup)
sys.path.insert(0, root + "/lib")
sys.path.insert(0, research)
import runner  # noqa: E402
sys.exit(runner.main(sys.argv[3:]))
PY
chown -R ec2-user "$T"
cd "$T"
timeout 600 sudo -u ec2-user env -i HOME=/home/ec2-user USER=ec2-user LOGNAME=ec2-user LANG=C.UTF-8 \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin PYTHONPATH="$ROOT" PYTHONUNBUFFERED=1 \
  /usr/bin/python3.12 "$T/drive.py" "$ROOT" "$T/research" \
  --firm cottonwood --request "$REQ" --portfolio "$PORTFOLIO" --map "$T/research/waf_window_probe_map.json" \
  --bindings "$ROOT/reports/resident_bindings.json" --start "" --end "" --min-gap-s 8 \
  --requests-per-window 6 --window-seconds "$WINDOW_S" 2>&1 | cut -c1-300
RC=${PIPESTATUS[0]}
cd /
rm -rf "$T"
echo "waf probe end $(date -u +%Y-%m-%dT%H:%M:%SZ) runner rc=$RC work dir removed: $([ -d "$T" ] && echo no || echo yes)"
