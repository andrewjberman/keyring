# Two applies under a clock, and three of my own defects caught by other seats' instruments — 0.7.0_AE_CloudOps

**Date:** 2026-08-30
**Task Order:** ADVI_49F.c02-FLOORHOLD · OPAL_ADVIPOINTERS.P2-FLOOR-49F (P2F-3b) · the reporting-pull deploy (COO 84506/84524) · ad-hoc startup
**Status:** IN PROGRESS — two applies COMPLETE and verified; one ledger leg OPEN by design
**archetype:** DEPLOY
**secondary_archetypes:** TRACE, COORDINATE

---

## Objective

Post-reboot relaunch by `0.0.0_AB_MSTR` (Andrew-direct 00:20Z). Come up reachable, run the `org/XXX.md`
startup, then work event-driven off the Monitor. What actually arrived was two time-boxed production
applies inside three hours: a **hold** on the 49F gold floor to stop a served partition being
overwritten at 12:45Z, and a **deploy** of the 49F reporting puller so Andrew's one approved BDPARITY
pull would not be spent on a stale request set.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `'aws_s3_bucket_notification' infra/aws/terraform/opal-assets --all` | PASS | 5 hits / 24 files. **This is the run that prevented the worst available mistake this session** — it surfaced `silver.tf:502-507`'s own warning that the notification resource is a per-bucket SINGLETON. |
| `comp-find` | `--name 'conversion_manifest.py'` | PASS | 3 hits / 135,417 files; separated the SOURCE from the VENDORED copy, which is the distinction the whole M-2 parity question turns on. |
| `comp-find` | `'advi_49f_gold_dispatch' <file> --all` | PASS | 8 hits / 1 file; located the module + the single existing lambda permission. |
| `comp-iam` | `service advi-49f-gold-dispatch` | **DID NOT ANSWER THE QUESTION** | Run per the rail. It models the EXECUTION ROLE (role -> service calls); the accelerator's question is the RESOURCE POLICY (who may invoke). Different plane. Fell back to a live `get-policy` on its own segment with a `# rail-checked:` marker naming that gap. |
| `vendor-manifest.sh` | `<schwab dir> --check` | rc=1, as expected | Used as a SECOND INSTRUMENT against my own Python digest diff: independently reported DRIFT on exactly the same 3 of 11 modules. |
| `deploy_ledger.py` | `check --red --all` | fired RED on my own entry | See Decision 4 — the tool caught me, twice, and the second catch invalidated the first fix. |

**What worked:** `comp-find`'s printed denominator + band split put the singleton warning in front of me
before I could write a second notification resource. **What failed:** nothing silently; `comp-iam`
answered a different question than the one asked and said so clearly enough that I noticed.

---

## Deployment Sequence

### Apply 1 — ADVI_49F.c02-FLOORHOLD (hold `advi-49f-gold-floor`)

| Step | Action | Result |
|---|---|---|
| 1 | H-1 read-before-hold (could have mooted the act) | dispatcher deployed bytes **byte-identical to build input**; SSM doc v3 Active; host stopped, 0 in-flight |
| 2 | TF `state = "DISABLED"` declared | `advi_49f_floor.tf` |
| 3 | Targeted plan, 1.9.8 shim | `0 to add, 1 to change, 0 to destroy`; sole diff `state ENABLED -> DISABLED` |
| 4 | Ledger opened BEFORE the apply | `20260830T0152Z_...` (later re-homed — Decision 4) |
| 5 | `safe-apply -target` | rc=0 |
| 6 | Live read-back | `get-schedule` State = **DISABLED**, 01:53:22Z |
| 7 | 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 8 | Negative control | `opal-assets-bd49f-dim-convert-daily` still ENABLED |
| 9 | Commit | `4e0bf61f11` — ON ORIGIN |

### Apply 2 — `opal-assets-bd49f-reporting-pull` carrying BP1-1 @`27af942259`

| Step | Action | Result |
|---|---|---|
| 1 | Verify worktree == pin for ALL 6 packaged members | 6/6 MATCH, source dir clean |
| 2 | `ci/build-and-upload.sh opal-assets <fn>` | SHA256 `GMfBZrn/elvrVJCY2L0BIDzt9lUoDX3eaCczb9rG174=`, 33,102 B, write VERIFIED |
| 3 | Targeted plan, 1.9.8 shim | `0 to add, 1 to change, 0 to destroy`; 3 attrs, all code-vintage; **0 env rows** |
| 4 | Ledger opened at the apply (indexed + sentinel) | `20260830T0253Z_bd49f-reporting-pull-bp1-1_...` |
| 5 | `safe-apply -target` | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` |
| 6 | 0-diff re-plan | `No changes.` |
| 7 | Read-back on the DOWNLOADED artifact | below |
| 8 | Commit | `07bf2fa0f9` — LOCAL at log time |

---

## Verification

```
=== Apply 2 read-back, from the downloaded package (never the apply report) ===
  MEMBER COUNT 6: insurance_leg.py lambda_function.py taxsma_newacc.py
                  taxsma_registry.py taxsma_resolver.py taxsma_seed.py
  LIMB 1  raw 26,475 B | LF 26,475 B | CR COUNT 0
          raw sha256 == LF sha256 == 66f324ae7c90158536629cfc7ff3ce7ae7ba974948d76918ab65a418038528b8
          TARGET     == 66f324ae7c90158536629cfc7ff3ce7ae7ba974948d76918ab65a418038528b8   MATCH
  LIMB 2  prior member 4eaa66b03ad0...d37d64f   DIFFERS   (negative control)
  LIVE    CodeSha256 GMfBZrn/... CHANGED from 0XJf+G2p...
          LastModified 2026-08-30T02:54:33Z ; State Active / Successful
          DRY_RUN='0'  INSURANCE_EGRESS='1'   (printed, not assumed)

=== CTO condition (i): changed-symbol x reachable-from-insurance ===
  ADDED 6, REMOVED 0, CHANGED 2 -> DENOMINATOR 8
  insurance leg reaches: _request, get_clientview_token, load_bd_session (+ DRY_RUN, MONOLITH, _s3)
  0 of 8 changed symbols reachable.   CONDITION (i) PASSES

=== INSA3AE-AC1 dispatch arms, on the PACKAGED bytes ===
  6 of 6 PASS, rc=0 unpiped, DRY_RUN=True throughout (no egress)
```

---

## Decisions Made

1. **The accelerator had to EDIT the singleton, not add a resource.** `aws_s3_bucket_notification`
   replaces a bucket's entire config. A second resource on `opal-data-assets` would have deleted all 8
   silver converter rules with a clean plan, a clean apply and no error. The plan is the evidence it was
   done right: `+1 block`, `(8 unchanged blocks hidden)`, `0 to destroy`, against 8 read live.
2. **I fixed the dispatcher's trigger identity rather than shipping a lying accelerator.** An S3
   notification carries no custom payload, so every accelerator fire would have recorded itself as
   `manual` — collapsing it into the hand-run bucket on the one field the dispatcher's own docstring
   calls the only scheduled-vs-hand-run discriminator.
3. **I did not upload before the gate's word.** An uploaded zip arms any untargeted apply in that
   workspace. Stopping to ask cost one round trip; uploading-then-asking would have armed a production
   function on my own authority.
4. **Ledger re-homed rather than renamed.** See below.

---

## ⛔ Three of my own defects, each caught by an instrument I did not own

- **I let a commit proceed before reading a citation the risk reflex put in front of me.** It named the
  emitter coupling as already-filed and CVO-accepted (76182/76186). I had written it up as a discovery.
  Corrected in `f4b67394e3` — but the ORDER was wrong: read the citation, then commit.
- **My deploy ledger was invisible to its own gate.** I wrote `**State:**`; `deploy_ledger.py` indexes
  `**Status:**`. A P0 production hold did not register. COO offered a rename as the minimum fix; I made
  it, **re-ran the gate, and it still fired RED** — an open hand-authored entry with no sentinel is a
  bypass by design. Reporting the rename as the fix would have been a green claim on a red gate. Re-homed
  onto the tracked sentinel path instead (`6e87166bca`), with the narrative moved to a rationale doc
  because `_write_entry` regenerates the tool-managed file on every mutation and would have destroyed it
  at the lift.
- **One of my test arms passed for the wrong reason.** My stub returned the wrong shape, so a `KeyError`
  from the handler's own print sat unexplained beside a green result. The dispatch verdict was correct,
  but that evidence invites the reader to blame the code. My input, ruled out before filing anything.

**And one against my own advice to another seat:** my substrate answer told `0.4.0_DS_ClientPlatform~R`
to pin `silver_source_scopes` for a new family. That map is **source**-keyed, not family-keyed, so a new
family declaring `sources=["blackdiamond"]` inherits cottonwood's scope and gets nothing on
`49financial`. Right about the family, incomplete about the pin; caught by `3.0.0_SA_CVO` (84668) and
amended into TO-S1-AE S1-2 with a zero-diff control.

---

## Files Modified

| file | commit |
|---|---|
| `infra/aws/terraform/opal-assets/silver.tf` (accelerator block on the singleton) | `e2be5c2f42` |
| `infra/aws/terraform/opal-assets/advi_49f_floor.tf` (permission; then `state = DISABLED`) | `e2be5c2f42`, `4e0bf61f11` |
| `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py` (`_trigger_identity`) | `e2be5c2f42` |
| `.../deliverables/P2F_3B_ACCELERATOR_PLAN_ROWS_20260830.md` | `e2be5c2f42`, `f4b67394e3` |
| ledger re-home + sentinel + rationale doc | `6e87166bca` |
| schwab silver family re-vendor (3 modules) | `5c7b2a9a6b` |
| `.../deliverables/INSA3AE_AC1_dispatch_arms_on_packaged_bytes.py` | `fddf44b283` |
| source-map artifact fields + reporting-pull ledger | `07bf2fa0f9` |

---

## Blockers

**NONE blocking at this seat.** Everything outstanding is either a scheduled event or another seat's act:

- **R-4 of the reporting-pull ledger is OPEN BY DESIGN** — the 04:35Z insurance fire is the first
  *production* exercise of the new package's insurance path. Nothing I ran exercises that path's runtime
  behaviour: (i) argues independence by STATIC reachability and the arms prove DISPATCH routing. Reading
  that fire's own log at ~04:40Z closes the early-apply decision.
- **H-4 of the floor-hold ledger is OPEN BY DESIGN** — lift on C02-g-3 R-5 (vintage on 534/534) or the
  hard lift-by TUE 2026-09-01 ~12:40Z, **lifting anyway at the clock**.
- **TO-S1-AE** waits on nothing of mine now that DS~R's S1-1 handoff has landed; it is sequenced after M-2.

---

## Current State

`advi-49f-gold-floor` is **DISABLED** (live read), holding the 49F gold chain so today's and Monday's
fires cannot overwrite served `date=2026-08-28`. `opal-assets-bd49f-reporting-pull` is **LIVE at
CodeSha256 `GMfBZrn/elvrVJCY2L0BIDzt9lUoDX3eaCczb9rG174=`**, deployed 02:54:33Z, carrying BP1-1
`@27af942259` verified by member identity with a negative control — so Andrew's one approved BDPARITY
pull now hits the correct request set. The P2F-3b accelerator is BUILT and **deliberately NOT APPLIED**:
it targets the same dispatcher the floor hold silences, so its apply is sequenced after the lift.

**Push state, MEASURED** (`ls-remote` at 02:58:00Z, origin/CLOUD `711a0717a0`): `e2be5c2f42`,
`f4b67394e3`, `4e0bf61f11`, `6e87166bca`, `5c7b2a9a6b` **ON ORIGIN**; `fddf44b283`, `07bf2fa0f9`
**LOCAL** — publication is the integrator's window, not this seat's push.

---

## Next Steps

- **[this seat, ~04:40Z]** Read the 04:35Z insurance fire's own log through `{"leg":"insurance"}` and
  state it either way — success or the named refusal. Closes R-4 and the early-apply decision.
- **[this seat]** M-2 converter deploy plan rows (gate OPEN, CTO 84737): per-family map with a LITERAL
  `OPAL_BUILD_COMMIT` for schwab only, upload after the word, two rows on
  `module.silver_converter["schwab"]`.
- **[this seat]** TO-S1-AE, with CVO 84668's source-keyed-scopes correction folded in.
- **[this seat, item 4]** `opal-stitch-produce` nightly: 20 of 20 FAILED since 08-10 while an
  unidentified second path keeps the artifact fresh. Record WHICH path has been producing it first; the
  nightly's fate second. **No monitor** — the moratorium holds and a fixed schedule IS the remedy.
- **[unowned, re-raised]** `deploy_ledger.py` cannot ADOPT an existing hand-authored entry, so every
  rich hand-written ledger must be re-homed or lose its narrative to the next regeneration. This is the
  same class `0.7.0_AE_CloudOps~L` named on 2026-08-29, and mine landed in it the next day.
- **[owner: this seat, filed not fixed]** `opal-assets-bd49f-reporting-pull`'s `BUILD_MANIFEST.json`
  declares 3 modules and states resolver+seed are "NOT packaged"; the running package has 6 and includes
  them. The file whose NAME most invites being read as the packaging list is not one on this function.
