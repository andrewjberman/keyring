# 0.7.0_AE_CloudOps~Z -- 2026-10-14, OG-zs-1 applied and closed, OG-ap-17 and OG-ap-18 Phase A cut

Fourth log of the day; the third ended at ~16:0xZ with OG-zs-1 blocked on the `Z-S115` ruling. This
covers the ruling, the apply, and two Phase A cuts on the live ref the mcportal release left.

## 1. OG-zs-1 -- APPLIED and COMPLETE. The hole is closed

The bare CloudFront behavior `/json-tiered/*` served the same keys as its authenticated twin with no
Lambda@Edge association. It now answers **401** with `WWW-Authenticate: Bearer` and `X-Cache:
LambdaGeneratedResponse` -- the validator answers at the edge on viewer-request, so no cached 200 can
be served around it -- while **both** paths return the same 607-byte body to the service account, and
`https://opalinvest.dev/` still answers 200 as the control. The act gated the path rather than
breaking it, and that pair of readings is what says so.

**A1's three conditions, and what each cost to measure honestly.**

*Conditions (i) and (ii), the ACL either side:* `rules_sha256` identical
(`e18311e9c8315107da5f8719748bb9aea1ae7cf0bb5eb5e19cd829e420c0bbf4`), 6 rules, 0 statement digests
outside the before set, capacity unchanged at 947. The digest deliberately covers the WHOLE ordered
rule list rather than each `Statement`, which is the field the order named: the plan's churn touched
`override_action` lines, so a Statement-only digest could read EQUAL across a change to how a rule
ACTS.

*Condition (iii), exactly one `UpdateWebACL`:* **the count is ZERO.** Terraform logged
`aws_wafv2_web_acl...: Modifications complete after 19s` for a modification it never sent. Four
instruments agree: no `UpdateWebACL` in a window proven settled by my own five `GetWebACL` calls (two
bracketing the apply); the `LockToken` byte-identical either side, and wafv2 re-issues it on every
successful update; capacity unchanged; the rule digests identical.

**The instrument error worth carrying.** BEFORE the apply I "proved" CloudTrail could answer by finding
40 wafv2 events -- all of them READS (`GetWebACL`, `GetIPSet`, `ListTagsForResource`). Reads being
recorded does not establish that WRITES are, and the pre-apply gate the ruling asked for would have
been vacuous if the trail did not log writes. The control that actually settles the class is
**`UpdateIPSet`: 2 events in 30 days from `wafv2.amazonaws.com`**. Same service, different event class.
I ran it only afterwards.

**Then two rulings and one error of mine.** `Z-S121` reported the 0-vs-1 gap; the issuer accepted 0
beside equal snapshots and fixed `zs1.AC2`'s branch. I re-ran, got PASS from the check, and my instance
still refused -- so I filed `Z-S122` saying the `<expect>` had not been amended with the check. It had.
The issuer amended **both surfaces in one commit** (`fd4e8e0bcb`); my instance carried the expect copied
from the pin the GO message named, 54 minutes older, reading `updatewebacl_calls 1` where HEAD reads
`[01]`. `Z-S123` records it as mine. CLAUDE.md states the habit twice -- cite by path and read at HEAD,
and verify a quote by printing the bytes at the cited line -- and a ruling in flight is exactly when the
order moves. **When a criterion refuses, re-read THAT criterion's bytes at HEAD before concluding
anything about the order.**

## 2. OG-ap-17 Phase A -- release `9c89bf1170`, AC1 PASS, COO half already signed

Cut on `bacec95ccd` (md5 107 of 107, with the previous release `7c558b4e21` as the negative control:
exactly `admin_api.py` and `admin_fabric_gitstate.py` differ, the mcportal set). 3 files, numstat
identical per file to `fffac3b499..486b643b97`.

**`git cherry-pick -n A B` silently drops B.** It stopped at A on a conflict in the surprise channel --
a path this cut does not want at all -- and B was never applied, leaving `tests/test_og_bd2.py` absent
while the tree looked clean and the pick reported one conflict I had already resolved by restoring the
channel. The **numstat comparison against the source range** is what caught it. B's gateway hunks then
went in from a path-scoped patch, which never touches the channel. A conflict in a path you are
discarding still halts the sequence.

The widening is **inert today**, read from both sides: 4 profile holders (1 active) from a 1555-item
consistent scan, and exactly 1 master_admin principal (`a18b74486b`, hashed ON THE HOST so no
identifier left the box). Disjoint -- so nobody gains until OG-mg-1 writes Andrew's profile, which is
the outcome mg-1 would otherwise have silently taken away. That hash matches `MG1_BEFORE.json`'s
independent derivation, which is the only reason I assert disjointness from hashes.

`test_ogz1_ac08` fails in the release tree and **also at `bacec95ccd`** (same counts, separate worktree
at that exact commit): its `ROUTE_CLASS` pin lacks four live `/hx/teams/*` routes. Already row
`Z-W47-S2`; no new row.

## 3. OG-ap-18 Phase A -- release `4275edccad`, AC1 PASS, 44 tests

15 files: ten whole from the **pinned** trunk sha `6ff58597d6` (box/sitez HEAD moves under concurrent
seats; the cut records the sha it took), five by hunk from the hookup `0cda8e2505`, which touches
exactly those five so every hunk in it is wanted. `registered_tool_names` 65 -> 75 and `non_data`
56 -> 66.

**The exclusion needed checking, not trusting.** The ten files come from trunk HEAD, which is NEWER
than the excluded `typed_scope.py` (OG-gt-6 drained it after these cells), so a HEAD copy could have
grown an import of a file this release omits -- a release that deploys green and dies at import.
Measured: nothing shipped references `typed_scope` or `harvest_published`, and all five modules import
cleanly in the release tree.

**The trading calendar does NOT reach the installed code** (row `Z-S125`, citing `Z-W72-S2` and
`Z-W79-S3`, which said it *may* fall back). `lib/` is absent from `/opt/opal-gateway` entirely and the
service interpreter answers `ModuleNotFoundError: No module named 'lib'`. It is **structural**:
`deploy-to-ec2.sh:265-269` builds the artifact with `tar -C "$SRC"` where `$SRC` is the gateway
directory, and the member list is `app deploy requirements.txt identity_tool_allowlist.txt` -- `lib/`
is outside the artifact's root, so no configuration change ships it. `harvest_identity.py:108-127`
imports it behind a guard and REPORTS the absence rather than guessing, so nothing breaks and nothing
lies; `trading_days_behind_t1` simply never populates, and any freshness these tools state is not
trading-day based.

**A false green I printed and caught two reads later.** My first pass over the eight suites reported
all passing because I grepped `[0-9]+ (passed|failed)` -- a pattern that also matches pytest's prose --
and it swallowed `7 errors`. The 7 were `FileNotFoundError` on `org/standards/NFRA_OPLGTW_CONTRACT.json`
at fixture setup: a path outside the sparse cone I had cut, reproduced identically in the base tree, so
not a code defect. Widening both cones gives 9 passed and 44 across the suites. **A sparse worktree
that runs TESTS needs every path the tests READ, not only the code under test** -- the sibling of the
cloud-ops trap about `lib` and the agent home for an apply. And a verdict read from a pattern that
matches prose is not a verdict.

## 4. Two mechanics worth keeping

**A row id is allocated at APPEND time.** I drafted a commit message naming `Z-S124`, and a peer took
that id between the drafting and the append; mine landed as `Z-S125`. The message was corrected before
it shipped. Never write the id into prose before the append returns it.

**The shared tree is busy.** Four commits this stretch queued behind peer merges (a worker drain, a
CRO crossbox, an integrator box-sync). A merge state another seat created is theirs to finish; the
pattern that works is a background waiter on `MERGE_HEAD` that commits when it clears, not a retry.

## 5. State at the end of this log

| item | state |
|---|---|
| OG-zs-1 | **COMPLETE** -- applied, AC1+AC2 PASS, instance VALID, status flipped, ledger CLOSED |
| OG-hv-2 | COMPLETE earlier today; live at `7c558b4e21` until the mcportal release displaced it |
| OG-ap-17 | Phase A COMPLETE, AC1 PASS; COO half SIGNED `@64824f2d62`, CTO half owed; Phase B on the GO and the slot |
| OG-ap-18 | Phase A COMPLETE, AC1 PASS; three halves owed. Andrew's first priority: if it signs first it deploys first and ap-17 re-cuts |
| OG-ap-15 | schwab, blackdiamond, orion, eclipse CLOSED; etf held on its 23:30Z sweep |
| OG-mg-1 | Phase A complete; Phase B on its halves and the GO |

Rows filed this stretch: `Z-S115` (BLOCKING, ruled), `Z-S116`, `Z-S117` (ARMED, eclipse drift),
`Z-S118`, `Z-S119` (ruled, criterion fixed), `Z-S120` (ARMED, runbook 7.2), `Z-S121` (ruled),
`Z-S122` (mine, wrong), `Z-S123` (resolves it), `Z-S125` (the calendar).
