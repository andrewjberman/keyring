# READ ONLY (no write, no restart, no vendor call): what a person's sign-in on the resident host could use, and the history
# of the host's own sign-ins. Sent through Systems Manager by host_read.py. Prints tool presence, package availability,
# and capture outcomes by reason token only (no cookie, no credential, no body).
set -u
echo "signin-read $(date -u +%Y-%m-%dT%H:%M:%SZ) $(. /etc/os-release; echo $PRETTY_NAME) $(uname -m)"
for t in Xvfb x11vnc vncserver Xvnc websockify novnc_proxy node npx chromium chromium-browser google-chrome; do
  printf '%s=%s ' "$t" "$(command -v $t >/dev/null 2>&1 && echo present || echo absent)"
done; echo
H=/opt/investor-reporting-ycharts
echo "playwright browsers: $(ls -d /home/ec2-user/.cache/ms-playwright/* /root/.cache/ms-playwright/* 2>/dev/null | sed 's#.*/##' | tr '\n' ' ')"
echo "dnf candidates: $(dnf -q list available xorg-x11-server-Xvfb tigervnc-server x11vnc 2>/dev/null | awk 'NR>1{print $1}' | tr '\n' ' ')"
echo "ssm agent: $(systemctl is-active amazon-ssm-agent 2>/dev/null)"
echo "capture outcomes by reason token, all journal history of the session runner and the resident:"
journalctl --no-pager -o short-iso -u irpt-analysis-resident.service 2>/dev/null \
  | grep -o -E "CHALLENGE_[A-Z_]+|CAPTURE_(FAILED|OK|PUBLISHED)[A-Z_:]*|persisted_at|SESSION_PUBLISHED|LOGIN_[A-Z_]+" | sort | uniq -c | sort -rn | head -20
echo "capture lines with dates (last 12):"
journalctl --no-pager -o short-iso -u irpt-analysis-resident.service 2>/dev/null \
  | grep -E "CHALLENGE_|CAPTURE_" | sed -E 's/(CHALLENGE_[A-Z_]+|CAPTURE_[A-Z_:]+).*/\1/' | cut -c1-160 | tail -12
echo "runner logs on disk: $(ls -1t /var/log/irpt-ycharts* $H/logs 2>/dev/null | head -8 | tr '\n' ' ')"
