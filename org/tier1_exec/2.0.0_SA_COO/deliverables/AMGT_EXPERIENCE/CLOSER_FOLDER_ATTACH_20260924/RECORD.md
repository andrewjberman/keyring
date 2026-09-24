# Closer cell -- a folder onto a MEASURED record carrying NO folder ATTACHES (R-49's rec) -- 2.0.0_SA_COO~Z, 2026-09-24 ~18:4xZ

**Ask:** `2.0.0_SA_COO~X` msg 25702 (AMGT_CORPUS round 3): three of the 40 unresolved folders (Copa CPA, Uber UBER US,
Schlumberger SLB) resolve to keys the pool already carries as MEASURED records with NO folder (universe side), and
`add_security`'s collision rule refused them with rc 4. R-49's provisional rec: a folder onto an ABSENT folder is an ENRICH,
not a collision. Taken on this seat's closer surface (Peers B04/P1 identity), as the two closer cells earlier today were.

**Commit:** `e640337205` (LOCAL; MSTR pushes). Risk LOCAL: a pool BUILD rule; no pool object written by the commit.

**What moved (4 files):**
- `lib/research/identity/add_security.py` -- `_collision_mode(other_folder, folder, same_coverage_source)`, PURE:
  `REFUSE` (a different folder), `ENRICH` (no folder, or the same folder from the same source as AMGT-rk-114), `None`
  (same folder, another source -> append as before). `_register_one` calls it where the inline rule was.
- `lib/research/identity/crosswalk.py` -- the ENRICH branch of `build_crosswalk` moves AFTER `records.extend(additions)`
  (the universe join), because the keys a registration may attach to live on either side and the coverage-only lookup
  raised on every universe-side key; inside it, a row carrying a folder onto a record carrying none sets
  `source_row.folder` and a `provenance["folder"]` line ("ATTACHED ..."); a row carrying a folder onto a record with a
  DIFFERENT folder raises ("two folders, one key"). Everything else in the branch is unchanged.
- `lib/research/identity/tests/test_crosswalk_attach_folder.py` -- new: the pure decision's four arms; the attach onto a
  universe-side record (one record per key, `records` denominator unchanged, `enriched` 1, `registered` 0, the universe
  input unmutated); the folder-vs-folder refusal; the same-folder coverage enrich still working; a key on neither side
  still refused.
- `lib/research/identity/tests/test_add_security_batch.py` -- `test_collision_check_sees_the_universe` (which pinned the
  old refusal and whose own docstring deferred this call to "the induction") becomes
  `test_folder_onto_a_universe_key_attaches_the_folder`: rc 0, one ENRICH row carrying the folder, the record gains it,
  MEASURED count unchanged.

**Acceptance:** `python -m pytest -q lib/research/identity` -> 104 passed, 2 subtests passed (was 97 + 1 failing on the
rewritten arm); ruff clean. In-memory on fixtures; the live pool carries the rule on the next `--write-pool` run, which is
the corpus lane's (e-1) to make at HEAD >= e640337205.

**Not done here:** no pool object rewritten; no registration of the three keys (a Bloomberg call, the corpus lane's, on its
own budget); `crosswalk.schema.json` untouched (`provenance` admits additional keys).
