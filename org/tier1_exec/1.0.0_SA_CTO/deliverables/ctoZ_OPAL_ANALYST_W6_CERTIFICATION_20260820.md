# CTO~Z CERTIFICATION — OPAL_ANALYST.W6 guardrails review (CERTIFIED-ON-STAGED; CLOSE gates on CVO~Z co-sign + the 0-diff laptop port)

**Certifier:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~1245Z · **Artifact certified:** `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/laneZ_D6_TOF_W6_GUARDRAILS_REVIEW_20260819.md` @de57e559c2 (author-half, 0.5.0_AE_OpalETL~Z) · **Bar:** OPAL_ANALYST.W6 C1–C6 verbatim + the four CTO amendments · **Proof instance:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_ANALYST.W6_PROOF_OF_SPEC.json` (validator rc recorded below) · **Agreement of record:** 205631Z/205801Z convergence — AE~Z authors, this seat certifies, CVO~Z second-reads layer classifications.

## VERDICT
**CERTIFIED-ON-STAGED — C1–C6 PASS at this seat.** **CLOSE is NOT declared here**: per the W6 TO's clarified GO-gate it falls when **(a)** CVO~Z co-signs the v0.2 index (second reads on the layer classifications in C1) **and (b)** the 0-diff laptop-lane port of `catalog_gate.py` + the staged catalog lands (port-time deltas re-exercise rows 4 and 7). TO status flips staged → **pending** (certified-on-staged), not complete. **Monitors proposed: ZERO. Gates implemented: ZERO.**

## 1. comp-adversary compose — run BEFORE this verdict (mandatory, @060cb1b130)
`python .tools/comp-adversary compose <artifact>` rc=0 · read-vintage HEAD @0e95185935 2026-08-20T12:38:39Z · artifact-vintage de57e559c2 · 4 complement sources run / 0 deferred / 6 declared-excluded (v1 contract). What it surfaced, each READ and DISPOSITIONED (not skimmed):
- **Source 2, cited-path vintage — `…/logs/2026-08-19/andrew_direct_1900Z_relay_findings_to_mstrz.md` MOVED-SINCE-AUTHORING.** DIRECT-CHECKED: file exists (4,315 B); `git log` shows ONE commit @8a92531dd2 (MSTR~Z integrator sweep, 22:41Z) = its FIRST landing, +51 lines = the whole file; content is the Andrew-direct ~1900Z relay verbatim. The BG seat does no git, so the cited record was uncommitted at authoring (21:11Z) and swept later. Citation resolves at HEAD. **Benign.**
- **Source 3, uncited sibling — `daily_guardrail_1300Z_wdac_pull_failure_verified.md`** (BG's 08-19 guardrail: the 07:00 pull FAILED on a WDAC block, served data still healthy). This is the state under the review's DECLARED exclusion *"cma env / WDAC policy = MSTR~Z's 08-20 07:00 acceptance domain."* That acceptance **PASSED 2026-08-20** (BG 2089 leg c: 0 CodeIntegrity blocks since 07:00 vs a 10-blocks/3-days positive control, genuinely exercised under a real scheduled run). The exclusion stands and its condition has cleared; WDAC is a box-policy layer, not an access surface in the W6 scope list — **no census row changes.**
- Source 4, comp-state drift excerpt — NFRA_COMPLEARN.P0 BEHIND; unrelated to W6. Source 1 — 0 commit pins in the artifact (it cites paths + tools, not hashes) — noted as the author's evidence profile, not a defect.
- v1 dot-truncation caveat: the declaration emitted **no GONE rows** → the DIRECT-CHECK-before-acting rule had nothing to act on.

## 2. Self-review mitigation — DISCHARGED at this seat (the author built `catalog_gate` + the channels)
**(i) Author battery re-run here, at HEAD:** `infra/aws/ec2/opal-gateway/app/graphql_plumbing/exercise_catalog_gate.py` → **13/13 PASS**, resolvable surface opal-internal=36 / firm:inflection=3 of 48 rows indexed, firm surface a strict subset. *(An author's battery re-run is a control on the artifact, not on the author — hence (ii).)*
**(ii) EIGHT independent probes, none from the author's case list** (scratch script, run from the workspace root against `workflows/atom_decomposition/catalog_v02/DATA_CATALOG.v0.2.staged.yaml`; mutants on SCRATCH copies only, staged catalog untouched, scratch deleted):

| # | Probe (mine, not the battery's) | Result |
|---|---|---|
| P1 | firm `cottonwood` asks `platinum/mdpf/inflection/aum-metrics.json` | DENY "may not read another scope's member key" |
| P2 | firm `49financial` asks an opal-internal serve row NOT in the battery (`json/benchmarks/model_portfolio_benchmarks.json`) | DENY "row firm='opal-internal' is not visible to firm principal" |
| P3 | floor case-insensitivity: `json/TICKETS/board.json` | DENY "RESOLVER FLOOR" |
| P4 | **MUTANT (ordering):** scratch catalog with a servable+ALLOWLISTED row whose key contains `ticket` | STILL DENIED by the floor — **the floor precedes lookup; a catalog edit cannot open the ticket surface through this gate** |
| P5 | **positive control, separate call:** opal-internal asks the P2 key | ALLOW "SERVE-WITH-CAVEAT" |
| P6 | **MUTANT:** `held-at-andrew` row (`json/benchmarks/benchmark_returns.json`, ALLOWLISTED) flipped to `serve` in scratch | real=DENY, mutant=ALLOW — **the verdict_class predicate is load-bearing** |
| P7 | **MUTANT:** the `{scope}` family row's `firm` relabeled `per-scope` → `49financial` in scratch | inflection now DENIED on its own member key, 49financial now ALLOWED — **the firm-scope predicate is load-bearing** (and see O-1) |
| P8 | firm surfaces for all three KNOWN_FIRMS | 3 / 3 / 3 keys, **pairwise DISJOINT, zero opal-internal rows** |

**8/8 PASS (denominator 8).** Three mutants FIRED as expected.

## 3. F10 — re-exercised from THIS seat (second non-BG seat, second day)
`whoami` on `opal-gateway-bbg` → **Opal Bloomberg** (opalbloomberg@opalinvest.com) · **target:** `search_email` → `identity_scope_denied`, `guard_denied: true`, reason naming OPAL_ANALYST PRD 4.3 + the widening route (Andrew via MSTR~Z) · **positive control, SEPARATE invocation:** `list_teams` → 200, 1 team (Opal Capital, 9c4ab816-…). Server-side deny confirmed from a seat the server answers; the BG seat's local G4 would have blocked pre-server.

## 4. C1–C6 — author evidence + certifier verification
| C | Author (artifact) | Certifier (this seat) | Verdict |
|---|---|---|---|
| C1 census | 10 rows = the 10-item scope list; 2 exclusions declared; rows 2+4 GATED with block + separate positive control; row 7 split gated-at-author-time / absent-in-production; rows 1/3/5/8 PROSE-DISCIPLINE; 6 PROSE; 9 MIXED; 10 ABSENT-declared | Denominator checked against the TO scope list (10/10); each layer label read against its evidence; row 7's GATED claim re-exercised here (13/13 + P1–P8); row 4's re-exercised here (§3). Layer classifications are CVO~Z's second read (co-sign) — not re-adjudicated by me | PASS |
| C2 inheritance + F9 | G1–G4 at vintage 2026-08-19 (relay 192059Z) + BG record; F9 do-not-refile carried | Vintage + record path DIRECT-CHECKED (adversary source 2); the 6 probe results + F9 note present | PASS |
| C3 F10 | deny 20:59Z + separate positive 21:00Z from AE~Z | re-run at this seat 12:4xZ 08-20, deny + separate positive control | PASS |
| C4 firm isolation | W5 (36/36 firm first-class, gate both directions), W7 (no firm axis downstream of person-scoped reach; REFUSE-pending-W9 in-channel), routes (auth-validator-edge on /api/scoped/*; advisor origin firm-parametric; ticket-API authz gap AT ANDREW since 08-12; trade-workflow-handler proven-in-source/unproven-in-use stated) | W5 isolation re-proven P1/P2/P7/P8 (pairwise disjoint); W7 + routes claims read as stated with the tool's own blind-spot disclosure quoted (DESIRED plane) — accepted as the TO's own instruction | PASS |
| C5 tightenings | T-1..T-5 each classified; monitors 0 | Classes checked against the TO's two-valued set (+ "already-at-Andrew" for T-4, which is carried not re-proposed); no gate implemented anywhere in the artifact; monitors 0 | PASS |
| C6 proof + log | author's draft instance validator-clean (author-half); no flip by author | Certifier's instance at the TO path, run WITHOUT a pipe (rc in the instance + my log); status flip = mine | PASS |

## 5. Certification observations (recorded, not findings against the bar)
- **O-1 (from P7):** the firm-isolation rule keys on the catalog row's `firm` label. A `{scope}` family row mislabeled from `per-scope` to a specific firm would let THAT firm read other scopes' member keys inside the family (the key-scope check lives only in the `per-scope` branch). The gate is correct — the catalog is the one truth — so the guard is **catalog-authoring integrity** (W5 lift + CVO~Z second read). **Recommended at port, owner 0.5.0_AE_OpalETL~Z: ONE battery case asserting every `{scope}` family row carries `firm: per-scope`.** A test assertion; no gate, no monitor.
- **O-2:** T-3 (the MCP service restart that activates `max_data_points` in the live tool signature) remains the single owned-blocking-item; it is verified by a CAPPED CALL at the laptop's next gateway touch, never by a config read.
- **O-3:** the artifact's evidence profile carries 0 commit pins (paths + tools only). Acceptable for a review artifact; the certifier's instance pins the vintages (@de57e559c2 artifact, @0e95185935 read, battery at HEAD).

## 6. Compiler tools (this certification's own)
comp-adversary compose (rc=0, read above) · comp-find --name catalog_gate* + content sweep (battery located: `exercise_catalog_gate.py`) · author battery at HEAD 13/13 · independent probe script 8/8 · proof-of-spec-check on the certifier instance (positional ids C1–C6, rc without a pipe) · opal-gateway-bbg whoami/search_email/list_teams (the F10 instruments).

## 7. What closes W6 (§9.0 program close rides this)
(a) CVO~Z index co-sign — request stands at CVO~Z (first domino per COO~Z 2100 item 6); layer classifications in C1 are theirs to second-read. (b) 0-diff laptop-lane port per TO-E DESIGN.md — port-time deltas re-exercise rows 4/7 (battery + P1–P8 are re-runnable from any seat with python + the staged file). On (a)+(b): status → complete, program-close declaration per §9.0 at this seat.

---

## CLOSE ~15:20Z -- (b) LANDED on the applied plane (on-instance read at this seat): W6 -> COMPLETE; OPAL_ANALYST PROGRAM CLOSE declared per sec9.0

**Trigger:** 0.7.0_AE_CloudOps' 1510Z frame (laptop port + apply landed; /query/v0 live; on-box battery 13/13 vs the deployed v0.2; zero-mint exercised), relayed by MSTR~Z 1512Z with the caveat "ground the flip on the landed state, not this relay". **Grounded at this seat, Rule 22a EC2 form (applied truth = an on-instance read), read-only via SSM on `opal-gateway` (`i-07dccb1615503ac99`, EC2_MANIFEST):**
- `/opt/opal-gateway/app/graphql_plumbing/catalog_gate.py` sha256 `f31c61f4aa57813d...` == repo HEAD `infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py` -- **BYTE-IDENTICAL** (the gate certified at 13/13 + P1-P8 is the gate running).
- `/opt/opal-gateway/app/refs/DATA_CATALOG.yaml` (1299 lines) vs the released staged v0.2 artifact @f8b50e8760 (1296 lines): **CONTENT-IDENTICAL** -- body hash from the first `channels:` line to EOF `c43d56c577530f6a` on BOTH sides; 36 rows / 15 channels on both; the only deltas are the PORTED header line (3 comment lines) and `version: 0.2-staged -> 0.2`, exactly the two deltas the port header declares. The certified catalog is the catalog the gate reads.
- `POST /query/v0` on the box (127.0.0.1:8080) -> **401** -- the route EXISTS and denies an unauthenticated caller (deny-by-default live; not 404). Service `opal-gateway` active, `ActiveEnterTimestamp 2026-08-20 15:05:30 UTC` (restarted at the port). `exercise_catalog_gate.py` present on-box (the applying seat's 13/13 ran there).
- **Row 4 re-exercised post-port from this seat:** `search_email` -> `identity_scope_denied` / `guard_denied: true` (PRD 4.3); separate invocation `list_teams` -> 200 (Opal Capital). Row 7: production enforcement is now PRESENT -- the deployed gate + catalog ARE the certified bytes (identity, above), so the certification's exercised rows (13/13, P1-P8 incl. the three fired mutants, 40/40 battery) hold on the deployed plane; the live 401 is the deployed deny path.
- CLOSE domino (a) was DONE at CVO~Z (second read 10/10 labels stand; v0.2 co-signed with amendments; conditions 1-7 discharged; PORT RELEASED @c368d66d98).

**Caveat, stated:** the applying seat's RECORD commit was not yet on origin/CLOUD at this read (tip @a13fa2c006 14:50Z); the flip grounds on the applied plane, not the record. LD-0428: nothing on the laptop was measured or verified -- the EC2 is estate infrastructure and the read was on-instance.

**VERDICT: OPAL_ANALYST.W6 -> COMPLETE. The OPAL_ANALYST program CLOSES per sec9.0** (W6 = the terminal wave; its close = the program close). Successor work is the sequenced v0.3 (OPAL_ANALYST.W5-V03, GO fired at COO~Z on this landing; my re-cert delta on rows 4/7 at its port) and the approved F8 fence tightening (Andrew-direct "rec approved" @ad2585793c, owner AE~Z). Monitors: ZERO. Gates created: ZERO.
