# READ ONLY (no install, no write, no restart, no vendor call): can the host run a HEADED Playwright Chromium on a
# virtual display? Prints which shared libraries the headed chrome binary cannot resolve, and what dnf would install
# for the display. Sent through Systems Manager by host_read.py. Option A of CTO rulings batch 131.
set -u
echo "headed-deps-read $(date -u +%Y-%m-%dT%H:%M:%SZ)"
for d in /home/ec2-user/.cache/ms-playwright /root/.cache/ms-playwright; do
  for c in $(ls -d $d/chromium-* 2>/dev/null); do
    b=$(ls $c/chrome-linux*/chrome 2>/dev/null | head -1)
    [ -n "$b" ] || { echo "$c: no headed chrome binary"; continue; }
    missing=$(ldd "$b" 2>&1 | grep "not found" | awk '{print $1}' | sort -u | tr '\n' ' ')
    echo "$b: missing [${missing}]"
  done
done
echo "which playwright the library loads: $(cd /opt/investor-reporting-ycharts && node -e "try{console.log(require.resolve('playwright'))}catch(e){console.log('unresolved')}" 2>&1)"
echo "its chromium revision: $(cd /opt/investor-reporting-ycharts && node -e "try{const p=require('playwright');console.log(p.chromium.executablePath())}catch(e){console.log('unresolved: '+String(e.message).split('\n')[0])}" 2>&1)"
echo "dnf would install for the display: $(dnf -q --assumeno install tigervnc-server 2>&1 | grep -E '^ [a-z]' | awk '{print $1}' | tr '\n' ' ' | cut -c1-600)"
echo "fonts present: $(fc-list 2>/dev/null | wc -l)"
