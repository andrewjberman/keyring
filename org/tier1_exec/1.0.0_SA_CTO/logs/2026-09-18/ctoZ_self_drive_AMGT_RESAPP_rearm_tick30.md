# /self-drive AMGT_RESAPP -- ticks 27-30 (`1.0.0_SA_CTO~Z`, site Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`.
**state: ARMED.** Cadence 30m (`:17`/`:47`), cron `f3c95fac`. Last log: ticks 22-26 @`3cd9611d6d`, author time
`2026-09-17T19:36:03-04:00` (read from the COMMIT, never the filename). Ticks covered here: 27-30, 23:47Z to 00:4xZ.

## Scope and completion test

`AMGT_RESAPP`, one project, site-Z fabric. **COMPLETION TEST: NOT DONE** -- `org/projects/AMGT_RESAPP.json` does not read
`status: complete`. Denominator: 1 of 1 project in scope, 0 complete. Batch B is mid-flight: three of five acts landed
and verified, one in flight, one queued.

## Open calls in scope

**One, and it was ruled in this seat's own lane rather than pitched.** `2.0.0_SA_COO~Z` msg 23611 routed the Peers V
question here as a SCOPE question, and scope/PRD is the CTO's limb (L4), not the CVO's to adjudicate. Ruled the same
tick, with the CVO and CRO copied because one grades the round and the other's brief carries the split. Zero RESERVED;
the all-reserved tell did not fire.

## Driver acts taken (own lane only -- no TO cut, no apply, no seat keyed)

| tick | act | carrier |
|---|---|---|
| 27 | Signer's verification of **AMGT-rk-23** (23:33:34Z, `iGmDkRbA6Zen`) | row Z-S163 @`7a5ab8c6ba`, msgs 23608/23609 |
| 28 | **CTO RULING on the Peers V call** -- concur ship honest-ABSENT, option set corrected, round-14 cell re-classed as a PRD question | row Z-S164 @`b3e65cb2a7`, msgs 23612/23613/23614 |
| 29 | Signer's verification of **AMGT-rk-24 adapter** (00:12:01Z, `Jicv6u3NnACR`) | row Z-S165 @`dee9c50795`, msgs 23617/23618 |
| 27-30 | Three closures measured on the `%2F` question, one of them this seat's own offered instrument | in rows Z-S163 and Z-S165 |

## rk-23: the act met its bar and its own record grades it missed

Print serves 200 for **33 of 33** covered names including `BP/_LN_Equity` (105,220 B) and `NG/_LN_Equity` (106,048 B).
The act's own closed record reads `served_ok 31 of 33, failures UNCHANGED`. Both readings are internally correct and the
difference is the REQUEST: `portal/src/api/endpoints/amgt-lead-panel.ts:151` builds the URL with
`encodeURIComponent(securityKey)`, so a client sends `BP%2F_LN_Equity` -- three path segments, never reaching
`handler()`'s `len(rest)==3` refusal. The sweep behind the record used a literal slash, a shape no client produces.
`3.0.0_SA_CVO~Z` re-measured independently (msg 23610) and reproduced both readings on one instrument. **The grade stays
the CVO's;** this seat supplied the measurement and the call site, and warned that grading off the record's own AFTER
line would record a met bar as missed.

**This seat's own instrument was wrong first and is corrected in the row.** The first census split the
`derived/model_block/` keys on the first slash, truncating the two slash names to `BP` and `NG`, invoking two strings
that are not securities and never invoking the real names at all. Corrected denominator: 47 objects over 34 distinct
names, **33 carrying a 2026-09-16 pull generation** (the covered set); `NVDA_US_Equity` carries only 2026-09-11 objects
and is not covered, which is why its 404 was never an rk-23 failure.

## rk-24 adapter: both branches held, and one number in it would fail a passing act

Over all 33: **21 serve `ABSENT` with the STORED classed reason**, 12 serve `SERVED`, and the generic `NoSuchKey` string
the act existed to replace occurs **0 times**. The discriminator is the store side, read independently: the 21
served-ABSENT names are exactly the 21 carrying an `UNRESOLVED-SOURCE.source.json` under `filings/v1/`. A 1:1 partition
is what separates *read the stored reason* from *synthesised a plausible one*, which is the STOP the half names.

⚠ **A naive blank-reason sweep reports `12 blank of 33` against a half whose fail condition names a blank reason.** Those
12 are the SERVED names; they owe no reason and blank is correct. Scoped to the set where a reason IS owed: 21 of 21
populated, 0 blank. Flagged to `3.0.0_SA_CVO~Z` before it grades. **Also disclosed against this seat's own half:** HALF 3's
branch B anticipated an ABSENT name with no stored reason, and that set is EMPTY in the real population -- the half was
wider than the world, which is not a defect in either direction but must not be counted as a branch that passed.

## The %2F question: four instruments now measured, three of them closed this window

| instrument | verdict | measured by |
|---|---|---|
| direct Lambda invoke | closed -- constructs `rawPath` itself, certifies its own assumption | both seats |
| direct HTTPS to the gateway | closed -- uniform 401 including the positive control | `3.0.0_SA_CVO~Z` (23610) |
| authorizer CloudWatch logs | closed twice -- the 401s never invoked it (`IdentitySource ['$request.header.Authorization']`), and its own line reads `path: undefined` | `3.0.0_SA_CVO~Z` (23616) |
| **adapter CloudWatch logs** | **closed -- 0 events matching `rawPath`, `%2F` or `_LN_Equity` in 36h, positive control live at 00:13:37Z. The adapter does not log the request path at all** | **this seat** |

Gateway access logging is OFF on the `$default` stage, so there is no fallback. **Consequence, and it changes how rk-26
must be CUT:** the render capture must record the delivered path **at the browser network layer**. A cell cut as "capture
the render" and verified afterwards from CloudWatch would find nothing, and finding nothing would read as a clean pass.
Sent to `2.0.0_SA_COO~Z` now rather than at the cut. W27-S10 stays UNDER_INVESTIGATION with its discriminating
instrument named as absent -- agreed by both seats.

## The Peers V ruling

`2.0.0_SA_COO~Z` pitched two routes to a measured Peers V. Enumerated **by subtraction over the landed sources** there
are three: the model blocks pulled for 33 of 33 names carry Bloomberg mnemonics of their own. Measured against
`peers_v.FIELDS` (`peers_v.py:74-76`): `PE_RATIO` present, `CUR_MKT_CAP` and `CF_FREE_CASH_FLOW` present and derivable,
**`BEST_PE_RATIO`, `BEST_EPS`, `TRAIL_12M_EPS` absent** and estimate-only, so vendor-only and RESERVED.

**Ruled:** round 13 ships the honest-ABSENT state (concur). But a translation layer cannot close Peers V from landed
data, and substituting a trailing field for an absent `BEST_*` field is **a different measure wearing the same name** --
`peers_v.py:38` warns against that exact substitution. So round 14's cell must first settle what the measure MEANS
without the estimate surface: **a PRD question at L4, not a decomposition cell.** `2.0.0_SA_COO~Z` concurred (msg 23615)
and will not cut it as engineering work.

**`4.0.0_SA_CRO~Z`'s two-defect split is CONFIRMED with two independent causes:** the served bundle carries no `scores`
field at all (66 written objects unreachable by contract) AND Peers V computes ABSENT_SOURCE on 33 of 33 for vocabulary.
Closing either alone leaves the page wrong -- closing the first alone would surface the second as three ABSENT scores on
every name. Round 14 carries both, separately named.

## Movement of the seats owing the next limb

`2.0.0_SA_COO~Z` -- **MOVING** on both planes: last commit 20:10 ET, and its worker deployed and closed three acts inside
this window. `3.0.0_SA_CVO~Z` -- **MOVING on the message plane** (23610, 23616, both carrying fresh independent
measurements) while quiet on commits since 16:06 ET; that is a seat adjudicating into its own working record, not a
stall, and the commit-plane read alone would have misclassified it. `4.0.0_SA_CRO~Z` last commit 19:24 ET.
**Nothing routed to `0.0.0_AB_MSTR~Z`: no owing seat is stalled.** Worktree reads taken with
`rev-parse --show-toplevel` printed and equal to the worktree, per the husk lesson.

## Hazard raised and withdrawn

The batch-B branch's copy of `INVESTIGATION_v1.md` sat six rows behind HEAD while worker ~27 appended to it -- the banked
append-only-on-a-side-branch shape, which makes the drain a certain conflict rather than a probabilistic one. Raised to
`2.0.0_SA_COO~Z`, which answered (msg 23615) that it already resolves this at drain time by merge-base reconstruction
and will not touch a live worktree mid-flight. **Withdrawn as already-owned.**

## Still owed by this seat

Per-act verification rows for **rk-25** (in flight, entry opened 00:31Z) and **rk-30 adapter** (queued), each against its
own signed half and its own freshly read pre-act hash. Then, after round 13 drains: the D7 `OPAL_TICKET_VNEXT` source
read, the L3 tree landing and the client-view-first L4, in the order ruled @`533f216c74`.

## Compiler Tools

`git log` (author-anchored, commit author time as the cursor), `git ls-tree` across two refs with a positive control,
`git worktree list` + `rev-parse --show-toplevel`, live `lambda:Invoke` over the full covered set with the key encoded as
the page encodes it, `lambda:GetFunctionConfiguration`, `s3:ListObjectsV2` with printed denominators, `logs:FilterLogEvents`
and `logs:DescribeLogStreams` with positive controls, `apigatewayv2:GetAuthorizers`/`GetStages`, `.tools/safe-commit.sh`,
`.tools/surprise-row-gate.py`.

Push state: LOCAL on SITEZ.
