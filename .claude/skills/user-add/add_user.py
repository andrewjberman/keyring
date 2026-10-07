"""Provision one Opal portal user through the canonical script, with a generated temporary password.

Usage (from the repo root):
    python .claude/skills/user-add/add_user.py <firm> <email> "<Display Name>" [--role user|admin]
        [--advisor-role R --advisor-name N --advisor-key K]

It generates the temporary password, calls users/scripts/create_user_v2.py with --no-ses (no email is
sent to anyone), and prints the password ONCE on stdout. The password is written to no file.
ASCII-only output.
"""
import argparse
import os
import secrets
import string
import subprocess
import sys

CANONICAL = os.path.join("users", "scripts", "create_user_v2.py")


def temp_password() -> str:
    # No look-alike characters (O/0, I/l/1, o): the password is read off an email and typed.
    alphabet = (string.ascii_uppercase.replace("O", "").replace("I", "")
                + string.ascii_lowercase.replace("l", "").replace("o", "") + "23456789")
    while True:
        pw = "".join(secrets.choice(alphabet) for _ in range(14))
        if any(c.isupper() for c in pw) and any(c.islower() for c in pw) and any(c.isdigit() for c in pw):
            return pw[:5] + "-" + pw[5:10] + "-" + pw[10:]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("firm")
    ap.add_argument("email")
    ap.add_argument("name")
    ap.add_argument("--role", default="user", choices=["user", "admin"])
    ap.add_argument("--advisor-role", default=None)
    ap.add_argument("--advisor-name", default=None)
    ap.add_argument("--advisor-key", default=None)
    args = ap.parse_args()

    if not os.path.isfile(CANONICAL):
        print("ERROR: run from the repo root; %s not found" % CANONICAL)
        return 2

    pw = temp_password()
    cmd = [sys.executable, CANONICAL, "--firm", args.firm, "--email", args.email, "--name", args.name,
           "--password", pw, "--role", args.role, "--no-ses"]
    for flag, val in (("--advisor-role", args.advisor_role), ("--advisor-name", args.advisor_name),
                      ("--advisor-key", args.advisor_key)):
        if val:
            cmd += [flag, val]
    rc = subprocess.run(cmd).returncode
    print("SCRIPT_RC=%d" % rc)
    if rc == 0:
        print("USERNAME=%s" % args.email.lower().strip())
        print("TEMP_PASSWORD=%s" % pw)
    return rc


if __name__ == "__main__":
    sys.exit(main())
