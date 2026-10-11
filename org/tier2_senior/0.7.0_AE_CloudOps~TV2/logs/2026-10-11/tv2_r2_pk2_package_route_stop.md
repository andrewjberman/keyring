# The route's one caller is not deployed, so the gate written to compare it had nothing to read — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R2-pk2.package-route-narrows-code-dell2 (read at `dbb7aa26cf`)
**Status:** STOPPED at step 3 — order left `pending`; nothing built, planned or applied

---

## Objective

Deploy `opal-ticket-api` at `be67d1fd38` so `POST /api/scoped/tickets/{ticketId}/package` stops returning
the ticket (on its 200 and its changed-under-write 409) and its five 409s gain a `code`. Cell `R2-pk-2`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` + 5x `close-leg` + `close` | PASS | opened before any AWS read; closed 5/5 dispositioned; row read back ABSENT against a 23-row control |
| r2_checks.py | `pk-200` (AC1), `pk-codes` | PASS | 2/2 and 5/5, at the pin |
| comp-find | `opal_packager` unscoped; `--band SURFACED --all`; `--corpus aws ... LAMBDA` | PASS | the domain falsifier and the graph corroboration — what made this a sweep rather than a guess |
| comp-which | asked which tool answers "which deployed package contains this file" | WARN | none does; denominator built by hand and its scope stated |
| aws lambda get-function + download | the ticket package (STOP 2) and all 17 investor-reporting packages (STOP 3) | PASS | rollback target confirmed by content; 0 of 17 carry the packager, 0 unreadable |
| safe-apply / terraform | not run | SKIPPED | the STOP precedes the plan |
| safe-commit.sh | one commit per act, `-F` by a non-shell writer | PASS | `msg-verify MATCH`; surprise-row gate graded the row |

**What worked:** falsifying the domain *before* sweeping it. One unscoped `comp-find` confined every
first-party reference to `opal_packager` to two files under `investor-reporting/`, which is what made a
17-function sweep a real subtraction instead of a convenient subset.

**What failed:** nothing of mine. `comp-which` has no tool for "which deployed package contains this
file", so the sweep was hand-rolled — recorded, since the rail asks to be consulted first.

**Gap found:** one, S34. Plus an id race, recorded inside S34 rather than as a further row.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger first, then the union at `09:10:45Z` | **47 trees** (enumerated 47 == grepped 47), 28 ticket-family rows, 8 distinct; only this order's entry open; my four earlier entries this session all read closed |
| 1 | STOP 1 — the pin | 0 changed paths vs a **301** positive control over `org/`; 0 dirty; shipping file `cf10e19e…` == pin == required |
| 2 | STOP 2 — the rollback target | live package downloaded: 1 member hashing `ca3be343…`, package b64 == live `CodeSha256` → the object read IS the running artifact |
| — | AC1 | `PK-200-OK 2 of 2`; `PK-CODES-OK 5 of 5` |
| 3 | **STOP 3 — the one caller** | **FIRES.** No deployed Lambda runs `opal_packager.py` |
| 4 | BEFORE state (recorded anyway) | `W03VREoM…`, 8 env keys, ItemCount 21, control ticket 23 attrs / open / NULL / svc-commentary |
| 5–7 | build, upload, plan, apply, after-reads | **NOT RUN** — the GO says "do not plan" |
| 8 | Close, report once | ledger CLOSED 5/5; row S34; one report with one ask |

## Verification

```
STOP 3, established on two independent planes with printed denominators:

 domain falsified first (rule 24(i)):
   comp-find 'opal_packager' unscoped -> 98 hits / 88800 files scanned
   SURFACED band (first-party source, 22) -> ALL under investor-reporting/, 2 files:
     reports/resident_installed.py  :295 import  :303 "attach": live_attach  :306 handle_commentary_ready
     ycharts/generate/resident_worker.py:864  (a comment)
   everything else in the band is org/ logs and check scripts

 swept by content, all 17 investor-reporting functions the source map declares:
   carrying opal_packager.py : 0
   not carrying it           : 17
   unreadable (NOT absence)  : 0
   POSITIVE CONTROL: served.py IS in irpt-status (49 members)
                     generate_installed.py IS in irpt-ycharts-generate (104 members)

 served AWS graph, 235 LAMBDA nodes, vintage 2026-10-11 08:36:08 UTC:
   no packager-named function; the only commentary lambdas were among the 17

 why it is coherent:
   opal_packager.py added 2026-10-09T01:25:59Z (7e66decdff, AR-g-12), last changed 02:59:05Z today
   irpt-ycharts-generate live build 2026-10-09T09:32:22Z -- later, and does NOT contain it
   -> that build does not bundle research/
   the deploy that would carry it is IRPT_ANLREQ's, whose entry
   irpt-anlreq-t1-commentary-store-and-lambda-20261009 is OPEN with legs B, SIM, INVOKE stranded
   -> which is why no aws_lambda_function.commentary is live

nothing moved: artifact object still RI4EX8i.EL18LgmpA54Fixk.hmjLsH4h (content-sha256 == live
CodeSha256); live function still ca3be343...; the route still returns the ticket and its 409s
still carry no code
```

---

## Decisions Made

1. **Stopped rather than reasoned past the gate.** An absent caller plausibly makes this apply *safer* —
   no live consumer can break on the narrowed answers. But the CTO made step 1b a pre-plan gate with a
   named STOP, and the no-live-caller case falls outside its two branches (reads `ticket` → STOP;
   discards it → proceed). Deciding an absent caller satisfies a gate written for a present one is an
   adjudication, not a reading. I put it to the owners as one ask.
2. **Built a denominator instead of stopping at three guesses.** I checked `irpt-ycharts-generate` and
   both commentary lambdas first and they all missed — which is exactly the shape where an early stop
   and a true absence read identically. So I falsified the domain, swept all 17, and ran a positive
   control on the member test.
3. **Did not run the 401 after-read.** It would pass identically before and after, so it would evidence
   the authorizer and nothing about this order. Named as excluded rather than reported as a pass.
4. **Flagged that `cf10e19e…` must NOT go into the issuer's precheck list yet.** The live build is
   unchanged and already admitted; adding the pinned hash now would make `TICKET_OK` admit a build that
   is not running — the inverse of the S28 defect.
5. **Re-identified my own surprise row.** The CVO took `S33` between my next-free-id read and my append.
   I rewrote only my own trailing block to `S34` and left theirs untouched. Rule 14b warns that an
   append-only shared file races on the index; this one raced on the *id*, which the rule does not name.

---

## Files Modified

| File | Commit |
|------|--------|
| pk2 ledger + its `.open_deploys` row | opened by the tool; closed this commit |
| `TCKT_VNEXT.TO-APPLY-R2-pk2…proof_of_spec.json` | this commit |
| surprise channel: S34 | this commit |

No AWS resource was touched. The plan is the evidence — because there was none.

---

## Blockers

**One, and it is the order's own gate.** STOP 3 cannot be satisfied while the packager is undeployed.
Two resolutions exist and both belong to `2.0.0_SA_COO~V2` with `1.0.0_SA_CTO~DELL2`: restate the gate to
cover the no-live-caller case, or hold this apply until IRPT_ANLREQ's stranded commentary deploy lands so
step 1b has something to read.

STOPS 1 and 2 pass and AC1 reads clean, so the order is ready to run the moment the gate is resolved.

---

## Current State

`opal-ticket-api` is unchanged and running the R2-rr-2 build. The package route still hands the packager
the ticket. Nothing is stranded: no open deploy entry, no uploaded artifact, no partial apply.

---

## Next Steps

1. The issuer's and CTO's call on the gate (row S34). No further act from this seat until then.
2. AC2 to `3.0.0_SA_CVO` at L9 on the ledger entry. Not self-graded.
3. The order stays `pending` — its work is not done, and marking it complete would misreport a STOP as a
   delivery.
