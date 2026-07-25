# CVO~Z session log addendum — 2026-07-25, LD-0318 cycle 1 + hook-path fix verification

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## 1 · LD-0318 cycle 1 (cron `9c8c11b7`, first fire)

`comp-system --check` = CURRENT before the sweep. Ran `infra/system/system_parity.py` for a live
per-domain read: comp-tools 7/7, infrastructure 4/4 (+1 assumption unit), engineering 5/5, ontology 4/5
— one live mechanical FAIL. Picked `ontology`'s `ont-rulebank-version-current` for the molecule+verify
pass (not freshly re-checked this cycle).

**Independently ground-truthed, not accepted from the script's own report:** grepped
`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml` myself — live `version: "1.2"`. Grepped all 4 required
`/system` representation files myself for the literal `rule-bank v` marker — zero hits in any of them.
They cite the rule-bank as canonical source (correct "cited not copied" design) but stamp no version
number anywhere.

**Verdict: DRIFTED — confirmed, unchanged from the already-documented state.** `scope_contract.json`
itself notes this "currently FAILS by design" pending WS-4 (CTO-arch-gated). Not a new regression, not
silently worse — re-grounded and it sits exactly where it was recorded to be. No action taken (not mine
to close solo). Reported to MSTR. The other 3 domains read mechanically clean per the same script run,
flagged as NOT independently re-derived unit-by-unit this cycle (script-clean != CVO-verified for those
three today).

## 2 · Hook-path fix verification (CTO~Z @`fbc91c6e28`)

CTO~Z fixed the `/c/...`-hardcoded-path defect I flagged as a REC-1 addendum (`install-stitch-refresh.sh`
baked an install-time pwd-derived absolute path into `.git/hooks/post-commit`) — repointed to resolve via
`git rev-parse --show-toplevel` at run time, matching what the inner script already did correctly.
Explicitly asked me not to take their word for it.

**Independently verified, own shell, own commands:**
- Read `.git/hooks/post-commit` directly: now `_ws="$(git rev-parse --show-toplevel 2>/dev/null)" &&
  [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/stitch-refresh-post-commit.sh"` — matches the described fix.
- Ran `git rev-parse --show-toplevel` myself in this shell: resolves to `C:/Users/AndrewBerman/Desktop/
  ajb_workspace` — a native Windows-style path, NOT an MSYS `/c/...` alias or a Cygwin `/cygdrive/c/...`
  alias. `sh -c "test -f \"$_ws/.../stitch-refresh-post-commit.sh\""` found it. **The fix doesn't just
  work around the `/c/` vs `/cygdrive/c/` mismatch this session hit twice — it sidesteps the mount-alias
  ambiguity entirely**, since git's own toplevel resolution emits a form every shell flavor on this box
  can consume without a mount table lookup.
- **Live exercise, this commit:** this very log file's commit is a real post-commit hook firing test.
  If the hook fires clean, no `sh: ... No such file or directory` line should appear in this commit's
  output — recording the observed result in the commit-gate note below rather than asserting it in
  advance.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `.tools/comp-system --check` | CURRENT | LD-0318 cycle precondition |
| `python infra/system/system_parity.py` | PASS — live per-domain read | mechanical denominator, not accepted as CVO-verified on its own |
| `grep` (source, NFRA_ONTOLOGY_RULE_BANK.yaml + 4 /system files) | PASS | independent ground-truth of the ontology FAIL — confirmed real, not a stale-grep artifact |
| `git rev-parse --show-toplevel` + `sh -c test -f` | PASS | independent re-derivation of CTO~Z's hook-path fix, own shell |
