"""Read the walk password BY NAME into memory (never printed), then run one live script once.

    WALK_PW_NAME=/irpt/.../password WALK_EMAIL=... WALK_DEADLINE=2026-09-26T..+00:00 WALK_AUTHORITY="..." \
        [WALK_INPUT_ID=portfolio_...] python run_upload.py <out.json> [live_upload.py|live_submit.py]
"""
import os
import subprocess
import sys

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
for required in ("WALK_PW_NAME", "WALK_EMAIL", "WALK_DEADLINE", "WALK_AUTHORITY"):
    if not os.environ.get(required):
        print("ERROR: %s not set; nothing run" % required)
        sys.exit(2)
# Pass the name WITHOUT its leading slash: Git Bash rewrites a leading-slash env value into a Windows path.
name = "/" + os.environ["WALK_PW_NAME"].lstrip("/")
if ":" in name or "Program Files" in name:
    print("ERROR: parameter name was path-mangled (%r); pass it without the leading slash" % name)
    sys.exit(2)
out = subprocess.run([AWS, "ssm", "get-parameter", "--name", name, "--with-decryption",
                      "--query", "Parameter.Value", "--output", "text"], capture_output=True, text=True)
if out.returncode != 0 or not out.stdout.strip():
    print("ERROR: password read by name failed rc=%d (%s)" % (out.returncode, out.stderr.strip()[:200]))
    sys.exit(2)
env = dict(os.environ, WALK_PW=out.stdout.strip())
del out
here = os.path.dirname(os.path.abspath(__file__))
script = sys.argv[2] if len(sys.argv) > 2 else "live_upload.py"
sys.exit(subprocess.run([sys.executable, os.path.join(here, script), sys.argv[1]], env=env).returncode)
