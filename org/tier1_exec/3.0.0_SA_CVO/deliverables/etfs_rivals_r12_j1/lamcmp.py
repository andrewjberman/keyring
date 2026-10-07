"""Compare each deployed rivalfunds Lambda's rivalfunds/*.py against git <pin> by content; negative control vs <ctl>."""
import io
import subprocess
import sys
import urllib.request
import zipfile
PIN, CTL = sys.argv[1], sys.argv[2]
FNS = ["rivalfunds-publish-page-lambda", "rivalfunds-build-canonical-shape-lambda", "rivalfunds-build-silver-lambda",
       "etfs-rivalfunds-daily-lambda", "etfs-rivalfunds-fetch-holdings-lambda"]
AWS = r"C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.tools\aws.cmd"


def git_blob(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:data/etfs/scripts/{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


for fn in FNS:
    out = subprocess.run([AWS, "lambda", "get-function", "--function-name", fn, "--query", "Code.Location", "--output", "text"],
                         capture_output=True, text=True).stdout.strip()
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(out).read()))
    files = [n for n in z.namelist() if n.startswith("rivalfunds/") and n.endswith(".py") and "/tests/" not in n]
    eq = neq = miss = ctl_diff = 0
    diffs = []
    for n in files:
        b = z.read(n)
        g = git_blob(PIN, n)
        if g is None:
            miss += 1
            diffs.append("MISSING@pin " + n)
            continue
        if g.replace(b"\r\n", b"\n") == b.replace(b"\r\n", b"\n"):
            eq += 1
        else:
            neq += 1
            diffs.append(n)
        c = git_blob(CTL, n)
        if c is None or c.replace(b"\r\n", b"\n") != b.replace(b"\r\n", b"\n"):
            ctl_diff += 1
    print(f"{fn}: {eq}/{len(files)} equal @{PIN}, {neq} differ, {miss} missing; control @{CTL}: {ctl_diff} files differ | {diffs[:6]}")
