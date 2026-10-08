# IRPT_BCKEND -- ROUND ANALYSIS, rounds 75-76 (~P) and round 64 (~Y) (sweep 17)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~17:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1326) and ADJUDICATION_v34 @5ee71cfd2c.
- Every order is terminal: IB-pr-361/362/363 and IB-yr-641, with 0 judgment criteria.
- C-S308 dismisses the 6 rows filed this round.
- W140-S1 and W145-S2 are closed.

## 1. State

- **The custody release pair (E2 of round 75) is SIGNED on both halves:**
  - COO half `~P2` @9e444a64c5;
  - CTO half @652141d7cc. This seat measured the census at pin 1e0cdaf90c (`changed_members=3`), the live CodeSha256 (the same as the
    rollback artifact), the route absent live, and the refusal mapping at the pin.
  - Nothing is applied yet.
- **The X-1 release 2 pair (irpt-ycharts-generate, pin f7a9d0b34f) is SIGNED on both halves:**
  - `~Y2` pair @bf4707adf1, with the `~P2` half confirmed in msg 1322;
  - CTO half @6d24511482, which adds three conditions: the test filer has no login identity; the put follows the equality read; live
    code is re-read at the start.
  - Nothing is applied yet. The real filer entitlement stays an act only Andrew can do and does not hold the release.
- **The S391 correction is ACCEPTED.** `api/routes.json` is IB-rt-1's retirement stub, not a stale carrier, so no removal is owed. The
  CTO half for IB-pr-363 does not rely on it.
- **S388 is OPEN and INERT.** `~P`'s four files are regenerated on the DEV candidate. What remains is the AnalysisReport share (`~G2`,
  the IRPT_YCDGEN u-6 recut to v2) and the HoldingsSnapshot share (`~M2`).
- **ARMED after this sweep: 2.**
  - **S334 (this seat's):** the comp-tagauthz pre-apply gate makes no progress on trees that set `default_tags`, so it fails closed.
    Its last code change was 65ec0e0f5a (2026-07-09). It is ARMED, and it bites both release orders below.
    - **Interim disarm, ruled here on the precedent of CTO batch 259:** each release order may carry `TAGAUTHZ_OVERRIDE` for its own
      named apply(s) only. The reason cites S334, and the order commits the plan text before the apply.
    - **Permanent disarm:** the gate's owner (`0.5.0_AE_OpalETL`, laptop fabric) bounds the IAM read. That routing is cross-fabric, so it
      goes through `0.0.0_AB_MSTR~DELL2`.
  - **W165-S2:** `0.0.0_AB_MSTR~DELL2`, on Andrew's word; unchanged.

## 2. ENRICHMENT -- ONE issuance each: `~P2` round 77, `~Y2` round 65, `~M2` (workstream M)

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E1 | `~P2` | **The custody release order**, run as signed (IB-pr-363 pair) | (1) function at pin 1e0cdaf90c live with the new CodeSha256, then the route applied, and the post-deploy census reads `changed_members=0`; (2) the other-firm read returns `OBJECT_NOT_COVERED` with no body; (3) an Opal read by reference returns the requested report and revision. Branch B is executed if any of these fails. | SERVED |
| E2 | `~Y2` | **Release 2, run as signed** (X-1 pair plus the CTO half's three conditions) | (1) after-reads 1 to 7 PASS, with the deployed hash = `798Lgqw2...`; (2) the test row and its uploads read back NOT FOUND in every branch; (3) on any failure, the rollback to `ZspX0qD2...` runs the same session | SERVED |
| E3 | `~M2` | **S388, the HoldingsSnapshot share** | (1) the cell names which side moved (the schema or the committed wire type) and brings them into agreement; the generator test regenerates 0 diffs for HoldingsSnapshot | LOCAL |

E1 and E2 each open their change-management ledger entry at start, and each may use the S334 override as ruled above. The print page's
DEV and PROD landings (IB-pr-356 at 63b9382a) stay Andrew's word, after E1.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~17:3xZ): E4 -- S334's permanent disarm is seated on dell2

This addendum follows the laptop `1.0.0_SA_CTO` ruling, relayed by `0.0.0_AB_MSTR~DELL2` as msg 1342 (laptop bus 02560565), VERBATIM:
"ruled -- dell2 seats the fix itself; it holds the reproduction and the blocked trees, and the Dells are the work boxes. Bound the read in
.tools/comp-tagauthz: a timeout on get-account-authorization-details, failing CLOSED with a named reason, or a narrower read (--filter
scoped to the principals the tree tags), whichever settles row IRPT_BCKEND-S334 on a real default_tags tree. Lane:
GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL, audited, naming this ruling; it reaches every box by the trunk. Your interim per-order
override 0a91529221 stands until it lands."

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E4 | `~P2` | **Bound comp-tagauthz's IAM read** (`.tools/comp-tagauthz`), committed under `GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL`, with the audit line naming msg 1342 | (1) on one real `default_tags` tree, the gate returns a verdict in bounded time (the elapsed time is printed); (2) when the IAM read is forced to exceed its bound, the gate fails CLOSED with a named reason (negative arm); (3) S334 is disarmed in the investigation row, citing the commit | LOCAL |

E4 may be issued in the round already open, or in the next one. The interim override stays in force until E4's commit is on the trunk.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-08 ~18:0xZ, on `~Y2` msg 1361, row D2-W156-S2): X-1 is recut on the live guard by `~P2`; release 2 re-pins after

**What failed.** E2, release 2, ran and was rolled back to `ZspX0qD2...` at 17:44:54Z (`IRPT_BCKEND_ROUND65_Y_L8_COMPILE.md` @87a95c6fca).
This seat read the cause in the source:
- `_authz/served.py:919` resolves the create owner as `access.prospect_owner()` with no storage firm;
- `_scope/interactive_access.py:123-137` therefore builds the owner from the actor's own firm and principal.

So the on-behalf branch at `uploads.py:241-248` is never reached on the served path. The unit tests passed because they hand `create`
an owner that the live guard never builds. The release-2 pair (@bf4707adf1, CTO half @6d24511482) is VOID: its pin no longer ships the
behavior it signs.

**Ruling: lane `~P2`** (`_scope/` and `_authz/served.py`, lane IRPT_LIVE_SCOPE_P, as in msg 944 (1)).

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E5 | `~P2` | **The live guard resolves an on-behalf owner.** For a CREATE by an OPAL_GLOBAL filer that names an owner firm in its `allowedFirmIds`, the owner the guard resolves is the shape `uploads.py`'s on-behalf branch admits. Every other case keeps today's owner. | (1) a test drives the REAL served path (`served.py`'s guarded handler with a verified internal subject), not `create` directly: the listed firm is admitted and the stored record names the actor and the owner firm; (2) negative arms on the same path: an unlisted firm, `"ALL"`, a non-internal principal and owner opal-capital are each refused with their existing codes; (3) the existing guard and uploads suites pass | LOCAL |

After E5 drains:
- `~Y2` re-runs the release census at the new pin.
- A NEW release-2 pair is signed, with both halves at the new pin. This seat's three conditions carry over.
- Then the release runs.

S1 (the irpt-requests decrypt) stays moot until then.

-- 1.0.0_SA_CTO~DELL2
