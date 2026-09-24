"""BEFORE-state for the builder remedy (row AMGT_CORPUS-Z-S16): in-memory build through add_security's path on
CURRENT inputs (CLOUD bytes); prints records / MEASURED / UNRESOLVED / registered and the multi-claimed
association forms with their folders. READ-ONLY (one S3 list + get of universe/v1)."""
from collections import Counter, defaultdict
from lib.research.identity import add_security, crosswalk
universe, src = add_security._identity_universe(None)
rows, reg_path = crosswalk.load_registrations()
doc = add_security._build_document("2026-09-24", list(rows), reg_path, universe, src)
d = doc["denominators"]
print("registrations rows", len(rows), "| records", d["records"], "MEASURED", d["MEASURED"], "UNRESOLVED", d["UNRESOLVED"], "registered", d["registered"])
claims = defaultdict(list)
for r in doc["records"]:
    for k in r.get("association_keys") or []:
        claims[k].append((r["resolution"], r["source_row"].get("folder"), r["source_row"].get("coverage_source")))
multi = {k: v for k, v in claims.items() if len(v) > 1}
print("multi-claimed forms", len(multi), "of", len(claims))
folders_double = Counter()
for k, v in multi.items():
    for res, folder, srcl in v:
        folders_double[folder] += 1
print("folders with a double claim", len(folders_double))
for k, v in list(multi.items())[:4]:
    print(" ", k, "->", v)
