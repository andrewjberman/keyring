# The cure landed in one line, and the finding that forced it became a schema genre — 0.7.0_AE_CloudOps~A

**Date:** 2026-10-04 (into 2026-10-05Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-aq-5 leg 3 / cell AMGT-aq-6 (AMENDMENT 2 @4d3db86faa, GO msg 29291 @e616511619); then msg 29329 (CVO verdict 29325)
**Status:** COMPLETE — aq-5 AC1–AC4 all PASS; four instances VALID (rc=0); nothing owed by this seat

> **Supersedes the Next Steps of `round67_aq5_grant_leg_and_code_leg.md` (@2f01774c21).** That log's
> step 3 names `1.0.0_SA_CTO~Z` as the owner of the PROOF_OF_SPEC reconciliation. It went to
> `3.0.0_SA_CVO~Z` as a governance fork and is now RESOLVED and landed. The earlier log is left
> unedited on purpose: it is a point-in-time record, and amending a committed log for a routing
> update is churn.

---

## Objective

Execute leg 3 — the cure I proposed at the code leg, adopted verbatim as cell AMGT-aq-6: grant the
scoped-API role read access to the `chatter_window` gold prefix so aq-2's FWD-36 window tone is
actually served, with **no code change**. Then reshape four instances under the new DEPLOY genre.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| opal_naming (builder) | `key("amgt","harvest","gold","chatter_window","date=1970-01-01")` | PASS | Rule 30: the prefix is builder OUTPUT, not typed. Returned `amgt/harvest/gold/chatter_window/`; the same call for `chatter_daily` reproduced the already-granted sibling's exact spelling as a control on the call shape. |
| comp-find | `comp-find "PROOF_OF_SPEC.schema.json" --files --band DOC --limit 15` | PASS | 1205 hits / 111,534 files. The denominator is what told me the schema is fabric-wide infrastructure (both worker agent definitions cite it), hence a CTO-class owner rather than a project channel. |
| comp-find | `comp-find '"group": "' --files --limit 6` | PASS | Found the `spec_ref.group` convention in existing instances — `OTHER` for a tree project — so the value was copied, not guessed. |
| comp-find | piped into `grep` twice | WARN (correctly) | The rail refused both times: a census piped into a receiver can erase its denominator. Used native `--limit`/`--files`/`--band` instead. The gate was right. |
| comp-iam | — | SKIPPED | Deliberately not consulted for this grant. It models `(action)` and never `(action, resource)`; see the prior log. |

**What worked:** the naming builder as a *control* (deriving the already-granted sibling's spelling
proved the call shape, not just the answer), and `comp-find`'s printed denominators.

**What failed:** nothing in the toolchain. Two self-inflicted failures are recorded below under
Postmortem, because both were mine and both were silent.

**Gap found:** none new; the `r67 c24` instrument gap from the prior log was closed by the issuer at
the leg-3 cut (a C2 clause counting the unreadable-table reason over every row).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Verify the blocking precondition — `amgt-corpus-r36-al5` closed | `**Status:** CLOSED … closed 20261004T231048Z`, sentinel gone. Unioned across **all 26 live worktrees** (present at HEAD in 1, absent in 25) — and the 25 absences are worthless, since those branches predate the sentinel commit |
| 1 | Re-read the base LIVE — it is al-5's code, NOT aq-5's | CodeSha256 `2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ=`, MemorySize 1769, CodeSize 41158959, LastModified `2026-10-04T22:42:11Z`. al-5's entry records BOTH `aoQ+WrefJ` (its base = my aq-5 result) and `2rFeF57l`; the live read equals the latter, so the chain aq-5 → al-5 → now is intact |
| 2 | Open my OWN NEVER-2 entry, sentinel committed BEFORE the act | `6ee42ebc09`, slug `amgt-resapp-r67-aq6-chatter-window-grant-20261004`, 2 legs |
| 3 | Derive the prefix from the builder, then add ONE list entry | `"amgt/harvest/gold/chatter_window/",` into `local.scoped_amgt_pool_prefixes`; `terraform fmt -check` rc=0, `validate` Success |
| 4 | Targeted plan + `show -json`, graded | 4 resource_changes, `{no-op: 3, update: 1}`; statement count **6 → 6 UNCHANGED**; both interpolated lists **30 → 31**, +1/−0 each; 0 destroy/create/replace; **0 non-no-op lambda**; Action still exactly `["s3:GetObject"]`; resources outside `opal-data-harvest`: 0 |
| 5 | AC4 BASE arm, before the apply | C1 implicitDeny, C2 implicitDeny, both `chatter_daily` controls allowed → `R67 AQ6 GRANT: NO` exit=1 |
| 6 | `safe-apply.sh` (Rule 18) | rc=0 — `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` |
| 7 | AC4 AFTER (CTO condition 2: before c24) | PASS on all four arms → `R67 AQ6 GRANT: YES` exit=0 |
| 8 | Confirm the code did not move | CodeSha256 / MemorySize / CodeSize / LastModified byte-identical to step 1. The STOP did not fire |
| 9 | Targeted 0-diff replan | `No changes`, `-detailed-exitcode=0` |
| 10 | Grade AC2 + its local control; re-read AC1, AC3 | See Verification |
| 11 | Close both legs, close the entry | 2 of 2 proven, sentinel removed, slug absent from `check --red` |
| 12 | Commit leg 3 | `768731795b` |
| 13 | Reshape 4 instances under genre DEPLOY (msg 29329) | `fc5728daff`, then pin correction `a8bed3d3af` |

---

## Verification

**AC4 — the applied plane.** The issuer's own `r67_grant_aq6.sh`, which is self-controlling: each
target arm sits beside an isolated control on the granted sibling `chatter_daily/`, one resource per
call, with `--context-entries` on the conditioned ListBucket arm.

```
BEFORE:  control GetObject chatter_daily/      allowed
         control ListBucket prefix chatter_daily/  allowed
         C1 GetObject chatter_window/          implicitDeny     FAIL
         C2 ListBucket prefix chatter_window/  implicitDeny     FAIL   -> GRANT: NO
AFTER:   all four                              allowed          PASS  -> GRANT: YES
```

Pre-flighted the script's call shape first (it uses bare `MSYS_NO_PATHCONV=1 aws`, which CLAUDE.md
bans in favour of the shim): bare `aws` resolves to `~/bin/aws`, both `aws`/`aws.cmd` present, and the
control arm returned `allowed` — so argv survived intact and it is not the raw-binary path.

**AC2 — the served plane.** One line granted both limbs, so the route could finally read the table:

| clause, each of days 30/90/365 | base (code leg) | after leg 3 |
|---|---|---|
| C2 unreadable-table rows | **95 of 95** | **0** |
| C1 mismatches | **74** | **0** |
| C1 old-reason | 0 (was 95 pre-code-leg) | 0 |
| C1 no-table-row | 21 | 21 |

`R67 C24 SERVED: NO` — and that NO is now C1's no-table-row clause **alone**, which is exactly the
state AC2's text always asked for: *"mismatches 0, old-reason 0, and a no-table-row count equal to a
local read of the same check run beside it (21 at the pin)."*

**The strongest single reading:** the local control run beside it is now **clause-for-clause identical**
to the deployed read — mismatches 0, old-reason 0, unreadable 0, no-table-row 21, `chatter_window rows
read 636`. At the code leg the two planes **disagreed** (deployed 74 against local 0), which is what
localised the fault to IAM. They now agree, so the single surviving failure exists on *both* planes and
cannot be this role or this code. It is the producer gap of rows `Z-W220-S1` / `Z-S344`.

**Re-reads, unchanged by a policy-only act as the order predicts:** AC1 `c23` SERVED YES exit=0 (0
offenders, 190 payloads, 128 non-empty); AC3 `c25` SERVED YES (9 of 9) and `c26` SERVED YES (DE 200 on
thesis and peers, ZZZZ control still 404) exit=0. No non-200 and no 502 anywhere.

**Neither STOP nor rollback fired.** The STOP branch was *"C2 still FAIL after AC4 reads YES"* — C2
passed. The rollback branch was *"mismatches above 74, a non-200 on any covered route, or c23/c25/c26
not YES"* — mismatches went 74 → 0.

**Scope discipline:** the r64/r65/r66 regression set and the cold reads were **not** run. Section 4b
asks for AC4, then AC2, then an AC1/AC3 re-read, and nothing else for a policy-only act. Recorded so
their absence reads as discipline, not omission.

### The DEPLOY genre reshape (msg 29329)

My 23:01 finding — that the schema had one genre and by its own Andrew-direct title *"A TO without a
schema-valid instance is NOT complete"* made the whole AE class incomplete — went CTO → CVO (verdict
29325) and came back as a new genre, landed at `3835c4368e`. Four instances then had to carry it.

| instance | verdict on committed bytes |
|---|---|
| aq-5 | **VALID (rc=0)** — AC1–AC4 PASS, 8 discriminating controls |
| ap-4 | **VALID (rc=0)** |
| ao-2 | **VALID (rc=0)** |
| an-7 | **VALID (rc=0)** |

The DEPLOY contract requires every control to **discriminate** (`expected_landed !=
expected_not_landed`) and voids an instance carrying a `DID-NOT-DISCRIMINATE` entry. Most pre-DEPLOY
controls were method or narrative notes with no landed/not-landed distinction, so relabelling them
would have been fabricating discrimination. Instead each instance carries its own base-vs-new
CodeSha256 as the discriminator, and **all 22 prior controls are carried verbatim** into
`forward_notes`, with the 5 inadmissible root fields. Nothing was deleted.

`deploy-genre: genre=DEPLOY; … controls: 8 of 8 named discriminate, 0 DID-NOT-DISCRIMINATE; rollback named`

---

## Postmortem — two silent self-inflicted failures

**1. The pin regex matched a backspace byte.** A patch written through a shell heredoc turned `\\b`
into a literal `0x08`, so `re.search(r"<BS>pin ([0-9a-f]{10})<BS>", blob)` could never match and all
three instances silently took aq-5's order commit as their `vintage_commit` — a WRONG figure in another
round's record. Caught because the reshaper printed `no vintage commit derivable`, then confirmed with
`cat -A`. **This is the banked site-Z heredoc-unescape trap, and I walked into it anyway.** Fix: write
patch scripts to a FILE with a non-shell writer, never through a heredoc; and the repair script now
proves no stray control bytes remain in the file.

**2. Two string insertions silently no-op'd.** `str.replace` on a mangled target returns the original
with no error, so the root-fold and invocation-literal passes were never inserted — and the only
symptom was violations that should have cleared. Caught by `grep -c ROOT_OK` → 0. Fix: after a
programmatic patch, **assert the marker is present** rather than trusting the exit code; the second
pass was written as its own file with `assert old in s`.

Both were mine, both reported, and neither reached the world: the three instances were restored with
`git checkout` and rebuilt from clean.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not start leg 3 on the GO | The GO's own precondition was unmet (al-5 OPEN). Verified across 26 worktrees rather than one shared-tree read, and the serialization is substantive: al-5's regression set includes r67 c24, so a grant landing mid-al-5 would confound its verify (CTO AMENDMENT 1). |
| Ran the graded checks from HEAD, not the aq-5 build pin | `r67_served.py` gained its C2 clause **at the leg-3 cut**; the pin's older copy would have missed the very clause that matters. There is no build commit for leg 3 — no code changed. |
| Derived the prefix from `opal_naming`, with the sibling as a control | Rule 30 and the file's own `research_dossier` precedent. A hyphen or a missing trailing slash would each be a silent widening. |
| Kept `controls` honest under DEPLOY instead of relabelling 22 notes | A `DID-NOT-DISCRIMINATE` entry voids the instance *by its own control*. Fabricating discrimination to reach rc=0 would defeat the contract I was asked to satisfy. |
| Re-validated the **committed** bytes | This caught the CCX-class pin defect: the reshape re-committed aq-5 at `fc5728daff`, which does not touch the `.tf`, so `PENDING-THIS-COMMIT` was wrong. Pinned to `768731795b`. Trusting the pre-commit run would have had me report four VALID while one was INVALID on disk. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/harvest/scoped-amgt-api.tf` | +1 prefix-list entry with its never-widen comment block | Yes — `768731795b` |
| `…/20261004T2313Z_amgt-resapp-r67-aq6-…_deploy_completion.md` + its sentinel | Opened, 2 legs closed with proof, CLOSED | Yes — `6ee42ebc09`, `768731795b` |
| `…/AMGT_RESAPP.TO-AMGT-aq-5.…proof_of_spec.json` | Leg 3 + AC4; AC2 FAIL→PASS; genre DEPLOY; pin fix | Yes — `768731795b`, `fc5728daff`, `a8bed3d3af` |
| `…/TO-AMGT-{ap-4,ao-2,an-7}.…proof_of_spec.json` | Reshaped under genre DEPLOY; no status revert | Yes — `fc5728daff` |

**Push state, measured:** all LOCAL. `origin/CLOUD` @ `3d5f1e2b7e` (`git ls-remote`).

---

## Blockers

None. Nothing is owed by this seat.

---

## Current State

`opal-amgt-scoped-api` serves at CodeSha256 `2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ=` (al-5's
code; leg 3 moved none of it), memory 1769, with a 0-diff plan in `infra/aws/terraform/harvest/`. Its
role now reads both the Security Scanner S&P 500 universe object (one ARN, siblings denied) and the
`amgt/harvest/gold/chatter_window/` prefix (object + listing, siblings unaffected), so FWD-36's window
tone is served and `r67 c24`'s only remaining failure is the 21-name producer gap present identically
on the deployed and local planes. Both NEVER-2 entries for round 67 are CLOSED with every leg proven.
Row `AMGT_RESAPP-Z-S346`'s hazard is CURED but still reads ARMED — **disarming it is
`2.0.0_SA_COO~Z`'s act**, not mine. aq-5 is the only task order ever issued to this lane that is
non-terminal, and its four criteria now all PASS.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`] Disarm row `AMGT_RESAPP-Z-S346`** — the hazard is cured (unreadable 0 of 95);
   the row names this seat's issuer as `disarm_owner`.
2. **[`2.0.0_SA_COO~Z`] Close aq-5 and carry it into L8** — AC1–AC4 PASS, instance VALID (rc=0).
3. **[`2.0.0_SA_COO~X` / the round-67 analysis] The producer gap** — `chatter_window` holds 212 names
   while the route serves 95 covered ones, 21 of which have no row at any window (`Z-W220-S1`,
   `Z-S344`). It is now the single remaining c24 failure.
4. **[`0.0.0_AB_MSTR`] Push CLOUD on Andrew's word** — 6 commits local; `origin/CLOUD` @ `3d5f1e2b7e`.
