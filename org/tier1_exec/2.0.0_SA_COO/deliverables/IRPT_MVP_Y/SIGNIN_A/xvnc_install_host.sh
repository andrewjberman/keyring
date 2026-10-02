# Ledger irpt-signin-a-20261002, leg I1: install the virtual display (Xvnc) on the resident host. NO vendor call, no
# restart, no service enabled, nothing listening after. Sent through Systems Manager by host_read.py after both
# halves are at HEAD. Option A of CTO rulings batch 131: the display exists only while an attended sign-in runs
# (live_walk/attended_signin_host.sh starts it bound to 127.0.0.1:5901 and tears it down).
set -u
echo "I1 start $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "before: Xvnc $(command -v Xvnc || echo absent); rpm $(rpm -q tigervnc-server-minimal tigervnc-server 2>&1 | tr '\n' ' ')"
if command -v Xvnc >/dev/null 2>&1; then
  echo "Xvnc already present; nothing installed"
else
  PKG=tigervnc-server-minimal
  dnf -q list available $PKG >/dev/null 2>&1 || PKG=tigervnc-server
  echo "installing $PKG"
  dnf -y install "$PKG" 2>&1 | tail -5
  echo "dnf rc ${PIPESTATUS[0]}; transaction: $(dnf history list 2>/dev/null | sed -n 3p)"
fi
echo "after: Xvnc $(command -v Xvnc || echo absent) $(Xvnc -version 2>&1 | head -1 | cut -c1-80)"
echo "enabled vnc units: [$(systemctl list-unit-files 2>/dev/null | grep -i vnc | grep -c enabled)] (0 expected)"
echo "listening on 5900-5910: [$(ss -ltnH | grep -c -E ':59(0[0-9]|10) ')] (0 expected)"
echo "resident unit $(systemctl is-active irpt-analysis-resident.service) since $(systemctl show irpt-analysis-resident.service -p ActiveEnterTimestamp --value) (unchanged)"
echo "I1 end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
