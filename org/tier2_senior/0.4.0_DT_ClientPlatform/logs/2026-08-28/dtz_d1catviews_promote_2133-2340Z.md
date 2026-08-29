# 0.4.0_DT_ClientPlatform~Z -- D1_CATVIEWS portal DEV->PROD promote (chain step 4) + two /prod-deploy defects fixed before executing it

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Window:** 2026-08-28T21:33Z -> 23:40Z (session start to now). First log of this session.
**Serial:** `0.4.0_DT_ClientPlatform~Z` (site Z). Seat created this session -- ZERO DT seats had been
live all session, and `/prod-deploy` is DT-only, so the last step of Andrew's deliverable could only
be performed by a seat class that did not exist.

---

## Summary

Seated as the LONG POLE for the D1_CATVIEWS session deliverable: the portal promote that puts the
corrected SMA figure in front of advisors. Held warm for ~50 minutes while the chain ahead of me ran,
then executed the promote end to end. **PROD moved `d4a048fd` -> `1b91b197`, tag `portal-v2.1.171`,
CI success, and the served bundle filename moved -- which is the only proof that anything shipped.**

While loading the procedure warm I found and (on CTO+COO word) fixed two real defects IN the promote
procedure itself, one of which would have made the promote's own VERIFICATION step read a different
GitHub repository and return an empty result indistinguishable from "still building."

---

## Deployment Sequence (DT role addition) -- ACTUAL output

```
LEDGER OPEN   e141014152   written BEFORE the worktree existed; acceptance bar + stop conditions
                           recorded while the result was still unknown

Step 1  branch DEV; tree clean except ?? .frontend-dev/runners/__pycache__/ (a live peer's, inert,
        deliberately NOT cleared -- tidying a peer's tree mid-session is the shared-tree hazard)
        local HEAD == origin/DEV == db3df0b2, 0 ahead / 0 behind, fetch rc=0
Step 2  bun run typecheck                        rc=0, ZERO errors (tsc -b --noEmit)
Step 3  git update-ref refs/heads/PROD ...       rc=0; local PROD == origin/PROD == d4a048fd
        (the dry-run-pollution class, closed on EVERY promote not just after a known dry-run)
Step 4  worktree add .runtmp/portal-promote-20260828T222333Z  rc=0  (main tree NEVER left DEV)
        bun install FOREGROUND                   rc=0, 420 packages, 59.22s
        merge --no-ff -F <file>                  rc=0, 'ort', 17 files, +1839/-108, no conflicts
                                                 -> 1b91b1972957b1cc011fe366060115f112bc54e1
        PARITY GATE  git diff origin/DEV HEAD    0 BYTES -> PASS
          corroborated by a DIFFERENT instrument: merged tree
          2eff1e2720406644a9bee2e730568a986f185a04 == origin/DEV tree, and that is the value
          merge-tree PREDICTED before the merge existed. Prediction and outcome agree.
        PUSH 1/2 by 0.0.0_AB_MSTR~Z (GATE 5)     origin/PROD d4a048fd -> 1b91b197
Step 5  gh -R Opal-Capital/portal run list, enumerated BY headSha
          1 run at 1b91b197: "Deploy to Production" conclusion=success id=33216893773
          denominator of 1 is CONSISTENT with the prior promote d4a048fd (ci.yml fires on DEV,
          deploy.yml on PROD) -- checked, so it is not a missing workflow
        TAG PEEL  portal-v2.1.171: ls-remote object 09bc3763 -> commit 1b91b197 == PROD head
Step 6  pointer commit 240a85eec4 (portal 57701d5c -> db3df0b2)
        PUSH 2/2 by 0.0.0_AB_MSTR~Z              origin/SITEZ -> 240a85eec4
Step 7  worktree remove rc=255 "Filename too long" (documented Windows behaviour, acceptable)
        worktree prune rc=0; only the main tree remains, ON DEV; cwd back at workspace root
        .runtmp/ CONFIRMED ignored at .gitignore:426 and absent from status (checked, not assumed)
LEDGER CLOSE  8b614d5ecc
```

## Verification (DT role addition)

```
SCORED   bundle entry chunk  index-Ce258d2k.js -> index-BMmU0cpj.js   (css BrZ63NPq -> WQYUWqLe)
         Content-hashed, so a new URL IS the proof: nothing that shipped could keep the old name.
SCORED   served bytes  "Fee split unavailable" 1 -> 0 in the ModelPortfolios route chunk
         positive control "Asset Category Views" still 1; negative control 0
INFO     Last-Modified / Age / X-Cache -- PRINTED, NEVER SCORED. Demoted from a scored arm after
         1.0.0_SA_CTO~Z measured platinum's timestamp advancing 21:19:23Z on BYTE-IDENTICAL content
         from an unrelated QA run. A freshness proxy had already scored the wrong event tonight.
```

---

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise probe | PASS | forwarder RAN (produced its own banner); PATH 105 of 105 resolve bare |
| `.tools/safe-commit.sh` | 4 commits, all `-F` | PASS | msg-verify MATCH on all four (len 4523 / 2142 / 3362 / 3049) |
| `.tools/commit-gate.sh` | via safe-commit | WARN | "checked 0 of 1 file(s)" on .md and submodule commits -- the gate reads only .py/.sh/.tf/org/projects/*.json and SAYS SO; not cited as validation |
| `.tools/hooks/never-rules-gate.sh` | read at source :509-566 | PASS | GATE 5 confirmed to deny both promote pushes to this serial |
| `python .tools/to-check.py --all` | startup, both serial forms | PARTIAL | suffixed `~Z` returns total=0; BASE serial returns the real TO. The org/XXX.md B.1 warning is live and accurate for this lane. |
| `python .tools/audit-archive-invoker.py` | A.2 startup | WARN | 18 findings = 5 COVERAGE + 13 INTEGRITY (8 NON-APPEND-EDIT + 5 ERROR-FAILCLOSED); direction test 8 of 8 shrank, 0 grew -> the documented device-axis pattern. Not chased. |

**What worked:** the pre-merge `merge-tree` dry run. It computes the merge in the object store with
no worktree, no checkout and NO local-PROD write, so it predicted the parity gate's result without
creating the dry-run pollution that Step 3 exists to clean up. Prediction matched outcome exactly.

**What failed:** `gh run list` returned rc=1 on a TLS handshake timeout on first attempt. A failed
retrieval returns a VALUE -- without capturing rc, the empty result reads as "no CI runs yet" on the
step that verifies a PROD promote. Retried, rc=0.

**Gap found:** Rule 21 deviation, stated rather than hidden. Most inspection this session was raw
`grep`/`git show`/`curl` against SERVED BYTES and non-repo artifacts (a live HTTP bundle, a workflow
file at a remote ref), where comp-tools do not apply -- comp-find searches the WORKTREE and
structurally cannot read a non-checked-out commit. The one repo-corpus census (hardcoded paths in
`SKILL.md`) used raw grep with a printed denominator and no `head`.

---

## Blockers

**None outstanding.** Two were real and both discharged rather than worked around:

1. **GATE 5 -- all three of the procedure's pushes are denied to this serial**
   (`.tools/hooks/never-rules-gate.sh:509-566`, read in full at HEAD; identity resolves from the
   per-session serial file and UNRESOLVED FAILS TO DENY). Surfaced ~90 minutes before it would have
   blocked, at the last command of the last step with the merge already built.
   `0.0.0_AB_MSTR~Z` pre-committed and executed both. **No audited override used** -- the integrator
   was awake, and an override would have produced the same ref with a weaker record.
2. **Two Tier-1 GOs for one irreversible act.** `1.0.0_SA_CTO~Z` issued a promote GO while
   `2.0.0_SA_COO~Z` had explicitly reserved that word. I refused to adjudicate between two Tier-1
   seats on a PROD act and asked, while running every non-mutating step in parallel so the hold cost
   nothing. `1.0.0_SA_CTO~Z` withdrew the operative force of its GO; `2.0.0_SA_COO~Z` gave the word.
   Basis: "who authorized this PROD promote must have exactly one answer in the record, not two that
   happen to agree." Adopted by the issuer as a rule.

---

## Errors I made this session

Recorded because none were caught by me alone, and that is the point.

1. **A false-PASS marker (caught by `3.0.0_SA_CVO~Z`).** I scored the served-bytes leg on a marker
   whose OLD side was measured at `origin/DEV` while PROD served `2858e7f5ff`. The string went
   0 -> 1 -> 0 and NEVER REACHED PROD, so its pass condition was already met on the un-promoted
   bundle. Right instrument, wrong REFERENT. My bundle-filename control survived the same audit only
   because its baseline was read from the LIVE SERVED PAGE rather than a git ref -- anchored to the
   artifact, not a branch. That property, not cleverness, is why it was immune.
2. **A defect I introduced into my own fix, caught pre-commit.** Replacing the hardcoded laptop
   anchor, I first wrote Steps 6/7 as `cd "$(git rev-parse --show-toplevel)"`. Step 4 leaves the
   shell inside `$WORKTREE`, which is its own git worktree, so that returns THE WORKTREE. A path fix
   that would have stranded the promote one step from the end. Negative control caught it.
   "Derive, don't hardcode" has an unstated precondition: derive it WHERE the derivation is valid.
3. **A false ABSENCE I was one send from reporting.** My first read of `deploy.yml` said "no
   invalidation, no cloudfront." `git show origin/PROD:<path>` mangled under MSYS to
   `origin\PROD;...` and I had suppressed stderr, so a fatal returned a clean empty. `git ls-tree`
   proved the file was there all along. CLAUDE.md warns against `2>/dev/null` on a `git show` in
   those words and I did it anyway -- the positive control caught it, not the care.
4. **A retracted control carried as load-bearing for ~20 minutes.** `1.0.0_SA_CTO~Z` 14215 told me
   conservation was the arm that "cannot pass by accident"; 14278 retracted it (it passes on the
   un-relanded plane). I had written it into my GO-time trigger verbatim. Fixed in the artifact I
   would actually read at 2am, not just acknowledged in a message.

---

## Current State

**PROD is live and correct.** `origin/PROD 1b91b1972957b1cc011fe366060115f112bc54e1`, tag
`portal-v2.1.171` (peel-verified), CI run `33216893773` success. The served bundle is
`assets/index-BMmU0cpj.js` + `assets/index-WQYUWqLe.css` at `https://opalinvest.dev/`.
`1.0.0_SA_CTO~Z` verified AC3 at the live PROD edge with a three-arm control (real bearer 200 with
`SMA.aum 22,794,766.25`; no-auth 401; BOGUS bearer 401 -- the load-bearing arm). The edge-cache gap
is CLOSED by measurement (`X-Cache: Miss`, no `Cache-Control`), so no invalidation act is required.

**Portal repo:** main tree on DEV, `origin/DEV b26c6fe6458e8fd9858f4e0cfeddbbfce83ea13d`, local 0
ahead, clean. `origin/PROD..origin/DEV` is now **2 commits**, net +80/-7 in ONE file,
`src/components/CategoryViewTree.tsx` -- so a NEXT promote is already outstanding.

**Workspace:** branch `SITEZ`. My commits `8af1a32981`, `e141014152`, `240a85eec4`, `8b614d5ecc`.
Push state MEASURED at 23:40Z: first three ON ORIGIN; `8b614d5ecc` was LOCAL at the RAVC and the
integrator has since moved the branch. **Push state on this tree is a measured, perishable value,
never a remembered one.**

**Ledger:** `org/critical_paths/change_management/20260828T2222Z_d1-catviews-portal-dev-to-prod-promote_deploy.md`
OPEN `e141014152` -> CLOSED `8b614d5ecc`. Nothing half-landed.

**`/prod-deploy` procedure amended @`8af1a32981`** (CTO+COO word, sequence UNTOUCHED, mechanics only):
`gh` calls now `-R Opal-Capital/portal` scoped; the laptop anchor and a baked bun path replaced with
`git rev-parse --show-toplevel` and `command -v bun`, the latter failing CLOSED and LOUD.

**NOT ESTABLISHED, and nothing should infer it from the above:**
- **The visual render.** DATA is verified through the page's own route; the PIXEL check is a separate
  rung and was UNASSIGNED at close. `0.4.0_DE_ClientPlatform~Z` volunteered and holds the harness.
- **The scheduled pipeline.** Tonight's artifact came from an ad-hoc reland carrying
  `_provenance.trigger = "manual"` (MEASURED -- not the `"adhoc"` two seats predicted). Only Monday
  2026-08-31's fire settles it, scored AC1-S STRUCTURAL, never the market-valued AC1-L literal.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform~Z]** HOLD. Andrew's Call 2 (ad-hoc refire tonight vs Monday's scheduled
   fire) decides whether the next promote happens at all. Promote-readiness census is DONE and
   accepted; build is clean on the tip. **Any GO re-measures push state in BOTH repos at the moment
   of the act** -- standing rule, adopted by `2.0.0_SA_COO~Z` after this census aged out inside itself.
2. **[3.0.0_SA_CVO~Z]** The next promote needs a NEW content marker. `"Fee split unavailable"` is now
   0 on PROD and is SPENT -- reusing it passes BEFORE the promote runs. The entry-chunk-hash control
   still works but its baseline must be re-read at GO: `index-BMmU0cpj.js`, not `Ce258d2k`.
3. **[0.4.0_DE_ClientPlatform~Z]** The visual render rung is unassigned and volunteered-for. Someone
   should say yes.
4. **[2.0.0_SA_COO~Z]** `OPAL_ADVIPOINTERS.P4-PROMOTE-49F` (P1, issued 2026-08-18, 11 days open,
   dated R+3 on Schwab FAM resumption) is a SECOND queued DT promote that nobody has re-dated.
