# READ ONLY (no write, no vendor call): window C's leg J afterwards -- the resident journal since leg S, the stored
# session's state, fence and generation as the resident's broker reads them (no cookie value), and the queue.
set -u
UNIT=irpt-analysis-resident.service
echo "leg J read $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "--- journal since 09:45Z (POLL handled=0 lines dropped)"
journalctl -u $UNIT --since "2026-10-02 09:45:00" --no-pager -o short-iso | grep -v "POLL handled=0" | cut -c1-240
echo "--- rotation lines: $(journalctl -u $UNIT --since '2026-10-02 09:45:00' --no-pager -o cat | grep -c IRPT_SESSION_ROTATION); eviction/refresh lines: $(journalctl -u $UNIT --since '2026-10-02 09:45:00' --no-pager -o cat | grep -c -E 'EVICT|REFRESH|CAPTURE')"
PID=$(systemctl show $UNIT -p MainPID --value)
ROOT=$(readlink /proc/$PID/cwd)
sudo -u ec2-user env -i HOME=/home/ec2-user PATH=/usr/bin:/bin PYTHONPATH="$ROOT" /usr/bin/python3.12 - "$ROOT" <<'PY' 2>&1 | cut -c1-240
import importlib, sys
root = sys.argv[1]
sys.path.insert(0, root + "/ycharts/generate")
import resident_main  # noqa: F401
runtime = importlib.import_module("resident_installed").build_resident_runtime()
current = runtime["assembly"].session.broker.current()
bundle = current.get("bundle") or {}
print("stored session: state %s fence %s generation %s persisted_at %s transport_updated_at %s cookie names %s" % (
    current.get("state"), current.get("fence"), str(current.get("generation"))[:8], bundle.get("persisted_at"),
    bundle.get("transport_updated_at"), current.get("cookie_names")))
PY
echo "queue irpt-generation $(aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s ' \t' '/')"
