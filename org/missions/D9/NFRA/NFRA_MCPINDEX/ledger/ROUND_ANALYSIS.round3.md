# NFRA_MCPINDEX -- ROUND 3 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-29 ~04:2xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 26440; `ADJUDICATION_v4.md` + `REMEDIATION_v3.md` @3572ded1b4). The fold reads
0 of 112 undispositioned. Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**Issuer: `2.0.0_SA_COO~MI`.** The recut is ONE issuance (section 5). The round-4 label is the next free one.

---

## 1. What round 3 did

- **L7:** 8 of 8 orders terminal (packet @5b5ddd7800).
  - MX-s-12 (PHASE B, the asset-dim REST pull as DEFAULT): the scheduled 22:10Z fire wrote the dim.
  - MX-s-13 (the Z-S31 redaction, 8 files).
  - MX-m-1 (the measure batch).
  - MX-x-1/x-2 (catalog rows; the ruling @8ed938b2d7 kept the raw key out of the catalog).
  - MX-i-4 (superseded to L10: 4 live Playwright legs; see Z-W8-S3 below).
  - MX-r-4 (the live enable of `opal_discover` + `portal_index`, deployed from deploy-only commit 0bce8d322a; gateway
    tree 09ccfc39ad = the G-A pin's).
- **L8:** 19 rows. 15 dismissed with every disarm re-read (Z-C-S26). 4 graduated OPEN (Z-C-S27). 2 new L9 findings
  graduated OPEN (Z-C-S28, Z-C-S29). Adopted as stated.
- **L9 (Z-C-S30):**
  - s10.J1 PASS: the scheduled fire's dim equals G1 on every column but `built_at`. MX-s-6's 42 cusip changes are the
    April -> 06:22Z one-time catch-up, not this fire.
  - s13.J1 PASS: 0 live-credential fingerprints in the 8 files at HEAD against 8 at the control commit, and 0 across
    all 43,706 tracked text files.
  - m1.J1 PASS.
  - **r4.J1 FAIL:** 1 of 4 A2 surfaces answered.
  - Adopted as stated.
- **G-A live cert** (this seat's ask, msg 26268): G6 PASS, G7 PASS (bytes identity). **G5 PARTIAL:** the catalog deny
  is exercised live; the other-firm and unresolved-principal arms need a non-master principal. See R-15.

## 2. Outcome grades

| FWD | grade | why (artifacts) |
|---|---|---|
| FWD-1 (discover routes a cold question to the right tool) | NOT_REALIZED | `opal_discover` is LIVE (MX-r-4; the CVO's calls at 03:27Z in `opal-mcp-audit`). But every `next_tool` it names is `query_v0`, even for mp.01, whose own tool `mdpf_get_aum_metrics` answered correctly when called directly (Z-C-S28). `query_v0` is absent from an MCP session's tool list, so the route is a dead end. The routing harness reads 23 of 27 (Z-W10-S1). The cold run by a non-author asker (A1) has not run; it needs G-B. |
| FWD-2 (portal figures equal the portal's) | NOT_REALIZED | r4.J1 FAIL (Z-C-S30): 1 of 4 A2 surfaces. `platinum/mdpf` is EQUAL on 4 of 4 fields (total.aum 2,083,228,453.05, 8,242 accounts, as-of 2026-09-25, VersionId N_KOsRfV...). `platinum/etfs` mis-routes to positioning rows (Z-W2-S8). `platinum/advi` is NOT_CATALOGUED. `json/*` routes to the right family with no tool and no figure. |
| FWD-3 (Schwab) | HELD (G-Q) | The thread now runs, so FWD-3's remaining gate is PRD V.5: NFRA_OPLGTW's Schwab tools enabled in deployment. That is NFRA_OPLGTW's act (switchover, G-C, never-widen), not a cell here. |
| FWD-4 (custodian and platform tools) | DEFERRED | The BD dim is current and scheduled (s10.J1 PASS). No tool is cut. 4 BD legs are dead (Z-W8-S3), and the transaction merge skips the dim join (Z-W11-S2), so a BD transactions tool would answer from an unjoined, stale substrate. |
| FWD-5 (ETF tools) | DEFERRED | No purpose-built ETF tool exists (close run, surface 2). |
| FWD-6..FWD-10 | DEFERRED | Nothing in round 3 moved them. |

**Round tally: 0 REALIZED, 2 NOT_REALIZED, 7 DEFERRED, 1 HELD.** Round 3 turned the thread on and proved one surface
end to end (mdpf, EQUAL). What stands between "live" and "realized" is two joins, the route to the tool and the answer
to the served object's vintage, plus three surfaces without a tool.

## 3. Rulings on the two decisions the slug hands this seat

**R-13, Z-C-S28 (discover never names the purpose-built tool): RULED -- join the route to the tool.** Where a catalog
row declares a purpose-built accessor (mp.01 -> `mdpf_get_aum_metrics`), `next_tool` names THAT tool with its exact
arguments (e.g. `scope=global`). `query_v0` is named only for a row with no purpose-built tool. When `query_v0` is
named, the answer says it is an HTTP route (`POST /query/v0`), not an MCP tool, so a client that lacks it knows it cannot
fetch. **Why:** FWD-1's own words are "routes ... to the right tool", and a route to a tool the session cannot call is
a dead end. The CVO measured that exactly on all 4 surfaces. Owner of the build: `2.0.0_SA_COO~MI` (item 2); this seat
records the ruling.

**R-14, Z-C-S29 (latest_value is the certification vintage): RULED -- keep the held value, and add ONE measured field
beside it.** Discover keeps `latest_value` as the catalog's certification vintage, labelled `claim: held`. It adds
`served_written_at`: the served object's S3 `LastModified`, read by one HEAD per SERVABLE row it returns, labelled
`claim: measured`. It does NOT parse the object to read its `period`; that stays the purpose-built tool's `as_of`,
one call later. When the HEAD fails, the field reads `absent` with the error class, never a guess. **Why:** A VALUE
MUST CARRY ITS CLAIM. The held label is honest, but the first date a user sees is 7 weeks older than the data, and one
HEAD per returned servable row (8 rows at most in the measured calls) replaces that first impression with a measured
write time, without turning discover into a data reader.

## 4. The four graduated-OPEN rows -- owner and cell

**R-15, Z-W8-S3 (ARMED): 4 dead BD Playwright legs still read `opal/bd/credentials` daily.** The legs are allocation,
realized, transaction and unrealized, fired by EventBridge `bd-allocation-pipeline-trigger` (cron 0 22), `bd-realized-`
(21:45), `bd-transaction-` (21:53) and `bd-unrealized-` (21:38), all ENABLED at this analysis (`aws events
list-rules --name-prefix bd-`). About 4 failed MFA logins per weekday; the lockout risk is unmeasured.
**RULED: disarm THIS round by DISABLING the 4 schedules. Disable, never delete.** Disarm owner: `2.0.0_SA_COO~MI`
(item 1), acting under a NEVER-2 ledger.
- **"Dead" is proven, not assumed.** Two parts:
  - (i) at the SSM-run grain, 21 of 21 retained runs per document read SSM Failed and log-failure (MX-m-1 (a), at
    `$LATEST`);
  - (ii) at the S3 log-object grain (latest version per key, the method that reproduced Z-S47's 69 of 121 for fees),
    the FIRST failing date and the LAST non-failing date are printed per leg, and each leg's own output prefix shows no
    object written since that last non-failing date.
  - A leg with ANY successful output since its first failure is NOT dead. It is not disabled, and it goes back to the
    issuer as a row.
- **Why disable:** a producer that writes nothing moves no served output when stopped (DELTA=0 by construction, and
  the cell proves it). A disable is reversible by re-enabling. It stops the daily secret read and the failed logins
  now, while the real remedy, a port to REST on the MX-s-12 pattern, is built.
- Not touched: `bd-asset-dim-pipeline-trigger` (the live REST leg, the cell's negative control),
  `bd-allocation-file-check-daily`, and every `bd-49f-*` rule.

**Z-W11-S2 (the transaction merge skips the dim join; the deployed script, 43,492 B, is not the repo file, 59,077 B):**
owner `2.0.0_SA_COO~MI`, a DS-lane silver cell. **It is sequenced after the transaction leg is ported** (item 6), because
the merge has had no input rows since the leg died. It is a stated dependency, not a round-4 cell.

**Z-W10-S1 (23 of 27 route; Q22 vocabulary, Q09/Q13/Q25 precision):** owner `2.0.0_SA_COO~MI`. It is item 4, joined
with Z-W2-S8 (the ETF one-common-word mis-route).

**Z-W13-S2 (the validator makes live S3 reads under a No-AWS bound; 1 of 36 rows reads family_mismatch_or_error):**
owner `2.0.0_SA_COO~MI`. It is item 7, the tooling cell.

**G5 PARTIAL -- rides the OPLGTW G-C controlled identity; no cell here.** `0.7.0_AE_CloudOps~OG` is producing that
identity: a controlled, non-privileged principal with verified tid/oid and one bounded grant (NFRA_OPLGTW OG-g-1). Once
this seat records G-C, `3.0.0_SA_CVO~O` runs G5's other-firm and unresolved-principal arms from that identity as its
live cert.
- By this seat's ruling of 2026-09-28 (msg 26343), a grant with no `portal_channels` gives NO catalog access. So if
  that identity's grant carries none, the arm exercises the fail-closed deny, which is a valid other-firm refusal.
- Only if the CVO judges that insufficient does G5 get its own cell.
- G-C is recorded by this seat. It is not cut here.

## 5. THE ENRICHMENT LIST ROUND 4 CUTS (one issuance, `2.0.0_SA_COO~MI`)

1. **Disarm Z-W8-S3: disable the 4 dead BD schedules** (WORLD; NEVER-2 ledger; Terraform through `safe-apply`; both
   never-widen halves, a CTO half and the CVO's second half, before the apply, naming the 4 rules and the per-rule
   re-enable rollback).
   First prove "dead" per R-15 (i)+(ii). Criteria:
   - (a) the 4 named rules read `DISABLED` 4 of 4, and `bd-asset-dim-pipeline-trigger` still reads `ENABLED` (negative
     control);
   - (b) the plan changes exactly those 4 rules' `state`, 0 other resources;
   - (c) the dead-proof table is committed with per-leg first-failing and last-non-failing dates and the output-prefix
     census.
2. **Route-to-tool join (R-13) + served write time (R-14)**, ONE narrow gateway release cut at the deployed commit
   (0bce8d322a's gateway tree), under never-widen halves. Criteria:
   - (a) `opal_discover('model portfolio AUM')` names `mdpf_get_aum_metrics` with `scope=global` as `next_tool` for
     mp.01, in-process on the pin;
   - (b) every servable row carries `served_written_at` with `claim: measured`, or `absent` with an error class;
   - (c) the MX-v-6 routing harness reads >= 23 of 27, so it does not regress.
3. **Portal tools for the missing A2 surfaces** (S3, FWD-2), ONE cell per surface, each a read-only purpose-built tool
   on the mdpf pattern:
   - (3a) `json/*` model-benchmark (mp.05), carrying the caveat MODEL-DESIGN returns, never client-realized;
   - (3b) `platinum/etfs`;
   - (3c) a catalog row for `platinum/advi`, then its tool.
   Each: figure and as-of equal to the served object, read by VersionId in the cell.
4. **Routing precision (Z-W10-S1 + Z-W2-S8):** catalog vocabulary for Q22; a NOT_CATALOGUED rule for weak
   one-common-word matches, graded on recall as well; the ETF ask routes to `platinum/etfs` rows. Criteria: harness
   ROUTING >= 25 of 27; ETF dataset ask routes first 1 of 1; recall on the MX-v-6 positive set does not fall.
5. **The thread re-run (WORLD, after 2 and 3 deploy)** -- the close run over the 4 A2 surfaces again, plus **the
   round's JUDGMENT criterion `r5.J1`, graded at L9 by `3.0.0_SA_CVO~O`, never self-graded:** per A2 surface, is the
   question answered by a purpose-built tool whose figure and as-of equal the portal's served object, and does the
   route discover gave name that tool? Denominator: 4 surfaces, printed. An answer that is right but reached through
   a route that named another tool is a FAIL on that surface.
6. **Port the transaction leg to REST (MX-s-12 pattern)**, the first of the 4 dead legs, because Z-W11-S2's merge
   depends on it. It runs under a NEVER-2 ledger and never-widen halves, and its acceptance is the next scheduled
   fire, never ad hoc. The other 3 legs follow one per round, each on its own port.
7. **Tooling cell:** Z-W13-S2 (the validator gets an offline mode, or is named a WORLD instrument, with the one
   mismatching row identified), plus the carried round-2 tooling items that are still open.

**Stated dependencies, not cells:** Z-W11-S2 (after item 6). FWD-3 (NFRA_OPLGTW's Schwab enable). The FWD-1 cold run
(G-B: Andrew admits a non-author asker; his speed test and Alyssa's run come first). G5's other-firm arm (G-C).
Z-S31's credential rotation (Andrew).

## 6. What this analysis does not do

- It does not apply, disable or deploy anything. Every act above is a cell.
- It re-measured only the BD schedule rules (`aws events list-rules --name-prefix bd-`: the 4 dead-leg triggers read
  ENABLED at ~04:2xZ). Every other figure is the slug's or the worker's, as cited.
- It does not rotate the BD credential or scrub history; both are Andrew's.
