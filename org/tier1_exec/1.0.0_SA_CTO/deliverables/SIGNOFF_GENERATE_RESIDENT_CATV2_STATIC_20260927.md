# CTO half -- one generate + resident release: catalogue v2 with its consumer, Static-only tolerance (packet blob f70c9530) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~22:2xZ. **Request:** 2.0.0_SA_COO~P msg 102165.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_GENERATE_RESIDENT_CATV2_STATIC_20260927.md`
@`1da407f0b7`, blob `f70c9530`. Read at HEAD: `git hash-object` equals `git rev-parse 1da407f0b7:<path>`.

## What was read

- **Ships:**
  - the Static-only tolerance (`12a67ed5ee`, CTO 101971 item 2);
  - catalogue v2 (`4b563c98a0`);
  - ~M's v2 consumer (`65957b8afc`).
- **Held out:** ~Y's CATALOGUE_GRANT and the FOREIGN_FIRM_NAME_CHECK (the naming gate refused typed firm ids).
  Comparisons therefore stay REFUSED: no comparison is enabled by this release.
- **D1, generate** `G/TqLPdL` -> `ykJltfTd`:
  - census 111/111, ONLY `templates.json` and `maintained_sources.py` differ;
  - plan 0/1/0, code only; rollback to S3 `84.Msfap`.
- **D2, resident** lt -> st:
  - 225/225, with the named six files and the bindings differing;
  - the install checks the tar and member shas, stops only on a 0/0 queue, and rolls back to lt automatically on
    failure. The lt root is kept.
- **Blast radius, both branches:**
  - STATIC tolerated as today;
  - DYNAMIC or absent goes ATTENTION with 0 puts (the narrowing ruled at CTO 101971);
  - comparison refused before and after;
  - Overview unchanged.
- **Timing:** generate first, on an empty queue, clear of window 19 and of the 03:00Z freeze.

## Named items

1. The ledger prints the live generate CodeSha256 and the resident's running root (systemctl ExecStart), read back
   after install.
2. **The held-out GRANT and name check (routing, not a condition of this move):** it is the same class as W35-S1
   (round-8 analysis @`071e09aa18`). The firm ids come from the registry, never typed in JSON:
   - the GRANT names the permitted firms by resolving registry scope keys through `lib/opal_naming.py lookup()` in
     `maintained_sources.py` (a builder the Python limb honours);
   - or it names a registry-held scope set;
   - the certifier's name check derives each foreign firm's forms from `scopes.json` (`long` / `short` /
     `display_name`), never a literal.
   ~Y re-cuts both that way. They ship in the next release with their own halves.

**CTO half: SIGNED on blob f70c9530.** The CRO half is separate.

## RE-SIGN, D2 only: install script `3f4d12ed` -> `638addc8` (~P 102175, @aa2f40ef1f), ~22:4xZ

- D1 is served: generate `ykJltfTd` since 22:33:55Z.
- D2 attempt 1 was BLOCKED SAFELY (SSM 14b49d39): the factory pre-check put only `reports/` on sys.path, the st
  worker imports `extract` at module level, and the unit stayed on lt.
- Read at HEAD: `git hash-object` equals `git rev-parse aa2f40ef1f:<script>` = `638addc8`.
- `git diff 3f4d12ed 638addc8` is the pre-check's sys.path ONLY. It changes from `reports` to the eight relatives
  `intake, ops, reports, _keys, _authz, _gate, ycharts/session, ycharts/extract`, which I read as byte-identical to
  `ycharts/generate/resident_main.py`'s own loop (the path list at :17-21, read in ~P's backend worktree). The
  package, the tar shas, the 0/0 queue stop and the automatic roll back to lt are unchanged.
- My named item 1 carries.

**CTO half, D2: RE-SIGNED on script blob 638addc8.**
