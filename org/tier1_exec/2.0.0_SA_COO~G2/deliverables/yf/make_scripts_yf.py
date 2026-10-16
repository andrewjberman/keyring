"""Generate the three host scripts of the yfinance pydeps delivery (issuer 2.0.0_SA_COO~G2, IRPT_ANLREQ, CTO msgs 9070, 9075, 9143).

usage: python -I make_scripts_yf.py <wheels json> <host pydeps inventory file> <out dir>

Writes pre_read_yf.sh (read only), install_yf.sh (fetch by key, verify, install, check) and rollback_yf.sh (move the added entries aside; nothing is
deleted). The wheel table and the 22-distribution inventory are embedded from the two inputs; nothing is typed. ASCII only. Overrides through
YF_* environment variables exist for the offline test only (the host never sets them).
"""
import json
import sys
from pathlib import Path

WHEELS, INVENTORY, OUT = sys.argv[1:4]
doc = json.loads(Path(WHEELS).read_text(encoding="utf-8"))
wheels = doc["wheels"]
inv = [ln.strip() for ln in Path(INVENTORY).read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("COUNT ")]
LEDGER = "irpt-yf-pydeps-20261016"
B = "opal-313476888478-lambda-artifacts"
PFX = "ec2/investor-reporting-ycharts/resident/pydeps-wheels/yfinance-1.2.0"
table = "\n".join("%s|%s|%d" % (w["file"], w["sha256"], w["size"]) for w in wheels)
inv_lines = "\n".join(inv)
mods = [("yfinance", "yfinance"), ("pandas", "pandas"), ("numpy", "numpy"), ("requests", "requests"), ("curl_cffi", "curl_cffi"), ("bs4", "beautifulsoup4"),
        ("websockets", "websockets"), ("google.protobuf", "protobuf"), ("peewee", "peewee"), ("frozendict", "frozendict"), ("platformdirs", "platformdirs"),
        ("pytz", "pytz"), ("multitasking", "multitasking"), ("idna", "idna"), ("certifi", "certifi"), ("soupsieve", "soupsieve"), ("tzdata", "tzdata"),
        ("pyarrow", "pyarrow")]
mod_list = ", ".join('("%s", "%s")' % m for m in mods)
names17 = sorted({w["name"] for w in wheels})

HEAD = """set -u
# Ledger %(ledger)s. Written for IRPT_ANLREQ (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it under a signed never-widen pair.
LEDGER=%(ledger)s
B=${YF_BUCKET:-%(bucket)s}
PFX=%(pfx)s
H=${YF_H:-/opt/investor-reporting-ycharts}
PYD=${YF_PYD:-$H/pydeps}
PY=${YF_PY:-/usr/bin/python3.12}
BEFORE=$H/yf_before_$LEDGER.txt
ADDED=$H/yf_added_$LEDGER.txt
""" % {"ledger": LEDGER, "bucket": B, "pfx": PFX}

TABLE = "TABLE=$(cat <<'YFTABLE'\n%s\nYFTABLE\n)\n" % table
INV = "INVENTORY=$(cat <<'YFINV'\n%s\nYFINV\n)\n" % inv_lines

INV_CHECK = r'''
inventory_now() {
  for d in "$PYD"/*.dist-info; do
    [ -f "$d/METADATA" ] || continue
    n=$(grep -m1 '^Name: ' "$d/METADATA" | cut -d' ' -f2-)
    v=$(grep -m1 '^Version: ' "$d/METADATA" | cut -d' ' -f2-)
    echo "$n $v"
  done | sort
}
'''

PRE = HEAD + TABLE + INV + INV_CHECK + r'''
echo "PRE-READ yfinance pydeps delivery, ledger $LEDGER, at $(date -u +%Y-%m-%dT%H:%M:%SZ) (read only: no install, no import of the new packages, no network)"
echo "PRE host: $(uname -m) | python $($PY -c 'import sys;print(sys.version.split()[0])') | pydeps $PYD writable by $(id -un): $([ -w "$PYD" ] && echo yes || echo no)"
echo "PRE free space (KB) at $H: $(df -Pk "$H" | tail -1 | awk '{print $4}') (want at least 1000000)"
[ "$(df -Pk "$H" | tail -1 | awk '{print $4}')" -ge 1000000 ] || { echo "PRE ERROR: less than 1 GB free"; exit 21; }
COUNT=$(ls -1A "$PYD" | wc -l)
echo "PRE pydeps entries: $COUNT"
NOW=$(inventory_now)
EXPECT=$(echo "$INVENTORY" | sort)
if [ "$NOW" = "$EXPECT" ]; then echo "PRE inventory: 22 distributions equal the recorded inventory"; else echo "PRE ERROR: the pydeps distributions differ from the recorded inventory"; diff <(echo "$EXPECT") <(echo "$NOW") | head -20; exit 22; fi
[ ! -e "$ADDED" ] || { echo "PRE ERROR: $ADDED exists (a delivery under this ledger already ran)"; exit 23; }
HITS=$(YF_PYD="$PYD" $PY - <<'PYEOF'
import importlib.util, os, sys
sys.path.append(os.environ["YF_PYD"])
names = @NAMES@
extra = ["google", "bs4", "curl_cffi"]
print(",".join(n for n in names + extra if importlib.util.find_spec(n) is not None and n != "google"))
PYEOF
)
echo "PRE names already importable (want none): [$HITS]"
[ -z "$HITS" ] || { echo "PRE ERROR: a name of the delivery is already importable"; exit 24; }
echo "PRE wheels expected: $(echo "$TABLE" | wc -l)"
echo "PRE OK"
'''.replace("@NAMES@", json.dumps([n.replace("beautifulsoup4", "bs4").replace("protobuf", "google").replace("-", "_") for n in names17]))

INSTALL = HEAD + TABLE + INV + INV_CHECK + r'''
W=${YF_W:-/tmp/$LEDGER.wheels}
fetch() {
  if [ -n "${YF_FETCH_DIR:-}" ]; then cp "$YF_FETCH_DIR/$(basename "$1")" "$2"; else aws s3 cp "s3://$B/$1" "$2" --only-show-errors --region us-east-1; fi
}
echo "INSTALL yfinance pydeps delivery, ledger $LEDGER, at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
[ ! -e "$ADDED" ] || { echo "ERROR: $ADDED exists; nothing moved"; exit 45; }
mkdir -p "$W"
echo "$TABLE" | while IFS='|' read -r f s z; do
  fetch "$PFX/$f" "$W/$f" || { echo "ERROR: fetch of $f failed; nothing installed"; exit 41; }
  [ "$(sha256sum "$W/$f" | cut -d' ' -f1)" = "$s" ] || { echo "ERROR: sha256 of $f is not the approved value; nothing installed"; exit 42; }
  [ "$(stat -c %s "$W/$f")" = "$z" ] || { echo "ERROR: size of $f is not the approved value; nothing installed"; exit 43; }
  "$PY" -c "import sys, zipfile; z = zipfile.ZipFile(sys.argv[1]); sys.exit(1 if z.testzip() else 0)" "$W/$f" || { echo "ERROR: $f is not a sound zip; nothing installed"; exit 44; }
  echo "D1 wheel $f sha256 and size verified"
done
FETCHRC=$?
[ "$FETCHRC" = 0 ] || exit "$FETCHRC"
[ "$(ls -1 "$W"/*.whl | wc -l)" = "$(echo "$TABLE" | wc -l)" ] || { echo "ERROR: the wheel count in $W is not the approved count; nothing installed"; exit 49; }
ls -1A "$PYD" | sort > "$BEFORE"
echo "D2 before listing: $(wc -l < "$BEFORE") entries, sha256 $(sha256sum "$BEFORE" | cut -d' ' -f1)"
"$PY" -m pip install --no-index --no-deps --only-binary=:all: --no-cache-dir --no-compile --disable-pip-version-check --no-warn-script-location --target "$PYD" "$W"/*.whl
PIPRC=$?
echo "D2 pip rc=$PIPRC"
ls -1A "$PYD" | sort > "$H/yf_after_$LEDGER.txt"
comm -13 "$BEFORE" "$H/yf_after_$LEDGER.txt" > "$ADDED"
REMOVED=$(comm -23 "$BEFORE" "$H/yf_after_$LEDGER.txt" | wc -l)
echo "V1 entries added: $(wc -l < "$ADDED"); removed: $REMOVED (want 0); dist-info added: $(grep -c '\.dist-info$' "$ADDED") (want 17)"
[ "$PIPRC" = 0 ] || { echo "ERROR: pip failed; the added entries are listed in $ADDED; run the rollback script"; exit 46; }
[ "$REMOVED" = 0 ] || { echo "ERROR: an existing entry vanished; run the rollback script and stop"; exit 47; }
ALLOWED=$("$PY" - "$W" <<'PYEOF'
import glob, sys, zipfile
tops = set(["bin"])
for p in glob.glob(sys.argv[1] + "/*.whl"):
    for n in zipfile.ZipFile(p).namelist():
        tops.add(n.split("/")[0])
print("\n".join(sorted(tops)))
PYEOF
)
STRAY=$(comm -23 <(sort "$ADDED") <(echo "$ALLOWED" | tr -d '\r' | sort))
echo "V1 added entries outside the wheels' own top-level names (want none): [$STRAY]"
[ -z "$STRAY" ] || { echo "ERROR: an entry the wheels do not own was added; run the rollback script"; exit 48; }
[ "$(grep -c '\.dist-info$' "$ADDED")" = 17 ] || { echo "ERROR: dist-info count is not 17; run the rollback script"; exit 48; }
NOW=$(inventory_now | grep -v -E '^(@NEWNAMES@) ' )
EXPECT=$(echo "$INVENTORY" | sort)
if [ "$NOW" = "$EXPECT" ]; then echo "V1 the 22 pre-existing distributions are unchanged"; else echo "ERROR: a pre-existing distribution changed; run the rollback script"; exit 50; fi
YF_PYD="$PYD" "$PY" - <<'PYEOF'
import importlib, importlib.metadata as md, os, sys
pyd = os.environ["YF_PYD"]
sys.path.append(pyd)
bad = 0
for mod, dist in [@MODS@]:
    try:
        m = importlib.import_module(mod)
        where = os.path.dirname(getattr(m, "__file__", "") or "")
        print("V2 IMPORT OK %s %s under_pydeps=%s" % (mod, md.version(dist), os.path.normcase(os.path.realpath(where)).startswith(os.path.normcase(os.path.realpath(pyd)))))
    except Exception as exc:
        bad += 1
        print("V2 IMPORT FAIL %s %s" % (mod, type(exc).__name__))
print("V2 imports failed: %d (want 0)" % bad)
sys.exit(1 if bad else 0)
PYEOF
IMPRC=$?
echo "V2 import rc=$IMPRC"
[ "$IMPRC" = 0 ] || { echo "ERROR: an import failed; run the rollback script"; exit 52; }
echo "INSTALL OK ledger $LEDGER at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
'''.replace("@MODS@", mod_list).replace("@NEWNAMES@", "|".join(sorted({w["name"].replace("_", "[-_]") for w in wheels})))

ROLLBACK = HEAD + r'''
echo "ROLLBACK yfinance pydeps delivery, ledger $LEDGER, at $(date -u +%Y-%m-%dT%H:%M:%SZ) (moves the added entries aside; deletes nothing)"
[ -s "$ADDED" ] || { echo "ERROR: $ADDED is absent or empty; nothing to move"; exit 51; }
D=$H/pydeps.removed-$LEDGER
mkdir -p "$D"
while read -r e; do
  [ -e "$PYD/$e" ] || { echo "ROLLBACK note: $e is absent"; continue; }
  mv -- "$PYD/$e" "$D/$e" || { echo "ERROR: could not move $e"; exit 53; }
  echo "ROLLBACK moved $e"
done < "$ADDED"
ls -1A "$PYD" | sort > "$H/yf_after_rollback_$LEDGER.txt"
if cmp -s "$H/yf_after_rollback_$LEDGER.txt" "$BEFORE"; then echo "ROLLBACK listing equals the before listing"; else echo "ERROR: the listing after the rollback differs from the before listing"; exit 54; fi
echo "ROLLBACK OK; the moved entries are in $D"
'''

out = Path(OUT)
out.mkdir(parents=True, exist_ok=True)
for name, text in (("pre_read_yf.sh", PRE), ("install_yf.sh", INSTALL), ("rollback_yf.sh", ROLLBACK)):
    if any(ord(c) > 127 for c in text):
        raise SystemExit("REFUSE: non-ASCII in " + name)
    (out / name).write_text(text, encoding="ascii", newline="\n")
    print("wrote", name, len(text))
