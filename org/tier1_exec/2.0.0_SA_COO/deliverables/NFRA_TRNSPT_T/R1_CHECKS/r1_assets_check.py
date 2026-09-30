"""TR-a-1 AC2 -- every data asset is hash-pinned in ASSETS.lock.json and the measured facts are present (issuer's check).

Recut 2026-09-30 15:3xZ (issuer ruling on row NFRA_TRNSPT-W4-S3): the client-domain table is REGISTRY data
(tenant.email_domain on the FIRM rows of infra/logic/registry/scopes.json, already present at HEAD), so no client_domains.json may exist, and
authors.json carries only opalinvest addresses plus a firm_domain_rule -- no firm token anywhere in the assets.

Prints ASSETS-PINNED n=N names=M, else ASSETS-BAD <reason>. Base: FAIL as expected (no lock file).
"""
import hashlib
import json
import os
import re
import sys

ROOT = "data/transcripts/assets"
MEASURED_AUTHORS = {"manav@opalinvest.com", "yang@opalinvest.com"}
FIRM_TOKENS = re.compile(r"49financial|49f\b|inflection|cottonwood", re.IGNORECASE)
REGISTRY_DOMAINS = {"49financial.com", "inflectionwealth.com", "cottonwoodmail.com"}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    lock_path = os.path.join(ROOT, "ASSETS.lock.json")
    try:
        lock = json.load(open(lock_path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print("ASSETS-BAD no lock: %s" % e)
        return 1
    files = lock.get("files") or {}
    if not files:
        print("ASSETS-BAD lock lists no files")
        return 1
    for rel, meta in files.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("ASSETS-BAD %s listed but absent" % rel)
            return 1
        if sha(p) != meta.get("sha256"):
            print("ASSETS-BAD %s sha mismatch" % rel)
            return 1
        if not meta.get("provenance"):
            print("ASSETS-BAD %s has no provenance" % rel)
            return 1
    for dirpath, _dirs, names in os.walk(ROOT):
        for nm in names:
            rel = os.path.relpath(os.path.join(dirpath, nm), ROOT).replace("\\", "/")
            if rel not in files and rel not in ("ASSETS.lock.json", "README.md"):
                print("ASSETS-BAD %s present but not pinned" % rel)
                return 1
    if os.path.exists(os.path.join(ROOT, "client_domains.json")):
        print("ASSETS-BAD client_domains.json must not exist (the table is registry data)")
        return 1
    authors_text = open(os.path.join(ROOT, "authors.json"), encoding="utf-8").read()
    if FIRM_TOKENS.search(authors_text):
        print("ASSETS-BAD authors.json carries a firm token")
        return 1
    authors = json.loads(authors_text)
    addrs = {a.lower() for row in authors["authors"] for a in row.get("addresses", [])}
    if not MEASURED_AUTHORS <= addrs:
        print("ASSETS-BAD authors.json lacks %s" % (MEASURED_AUTHORS - addrs))
        return 1
    if not authors.get("firm_domain_rule"):
        print("ASSETS-BAD authors.json lacks firm_domain_rule")
        return 1
    try:
        sys.path.insert(0, ".")
        scopes = json.load(open("infra/logic/registry/scopes.json", encoding="utf-8"))["scopes"]
        reg = {(r.get("tenant") or {}).get("email_domain") for r in scopes
               if r.get("class") == "FIRM" and (r.get("tenant") or {}).get("email_domain")}
    except Exception as e:  # noqa: BLE001
        print("ASSETS-BAD registry unreadable: %s" % e)
        return 1
    if not REGISTRY_DOMAINS <= reg:
        print("ASSETS-BAD registry FIRM email_domain rows lack %s" % sorted(REGISTRY_DOMAINS - reg))
        return 1
    names = lock.get("name_dictionary_entries", 0)
    if names < 50000:
        print("ASSETS-BAD name dictionary entries=%s (< 50000)" % names)
        return 1
    print("ASSETS-PINNED n=%d names=%d registry_domains=%d" % (len(files), names, len(reg)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
