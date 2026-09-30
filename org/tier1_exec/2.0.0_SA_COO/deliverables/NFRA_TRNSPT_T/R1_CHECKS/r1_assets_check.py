"""TR-a-1 AC2 -- every data asset is hash-pinned in ASSETS.lock.json and the measured facts are present (issuer's check).

Prints ASSETS-PINNED n=N names=M, else ASSETS-BAD <reason>. Base: FAIL as expected (no lock file).
"""
import hashlib
import json
import os
import sys

ROOT = "data/transcripts/assets"
MEASURED_AUTHORS = {"manav@opalinvest.com", "manav.shah@49financial.com", "yang@opalinvest.com"}
MEASURED_DOMAINS = {"49financial.com", "inflectionwealth.com", "cottonwoodmail.com"}


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
    for rel in os.listdir(ROOT):
        p = os.path.join(ROOT, rel)
        if os.path.isfile(p) and rel not in files and rel != "ASSETS.lock.json" and rel != "README.md":
            print("ASSETS-BAD %s present but not pinned" % rel)
            return 1
    authors = json.load(open(os.path.join(ROOT, "authors.json"), encoding="utf-8"))
    addrs = {a["address"].lower() for a in authors["authors"]}
    if not MEASURED_AUTHORS <= addrs:
        print("ASSETS-BAD authors.json lacks %s" % (MEASURED_AUTHORS - addrs))
        return 1
    domains = json.load(open(os.path.join(ROOT, "client_domains.json"), encoding="utf-8"))
    ds = {d["domain"].lower() for d in domains["domains"]}
    if not MEASURED_DOMAINS <= ds:
        print("ASSETS-BAD client_domains.json lacks %s" % (MEASURED_DOMAINS - ds))
        return 1
    names = lock.get("name_dictionary_entries", 0)
    if names < 50000:
        print("ASSETS-BAD name dictionary entries=%s (< 50000)" % names)
        return 1
    print("ASSETS-PINNED n=%d names=%d" % (len(files), names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
