# /self-drive D2 & D3 — tick 22 (2026-08-28 22:19Z) — state: ARMED

Covers ticks 21-22 (tick 20 logged @ee736ea59a; tick 21 QUIET at this seat, unlogged by the delta
rule). Cron bde882a4 (:07/:37; ran on idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52).
Written on DELTA: two driver acts this window (a contract-extension override closed; a wake-prompter
amendment), the (k) denominator line owed at this commit, and the PERFRP rewrite's build phase
completing.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## Driver acts (§3.3)

- **AC4 served-column set — NO contract-extension override (79356/79357/79358).** COO 79349 accepted
  PRFR2DS-AC4 (b-5 paged transactions @5344fd7af2), corrected the face's "12-enumerated" to the
  PRD's 10 served + 2 declared absent, ruled the SERVED page trims to the card ten with the seven
  crosswalk/secondary fields (cusip, debit_credit, net_amount, sb_cd, settlmnt_date, tr_cd,
  tran_srcde) build-side, and left the override at this seat. RULED no override: the contract is
  the consumer's card set; the crosswalk join is a build-time act with no client-side reader; the
  implementation conforms to the contract, never the reverse. The PII arm's positive + negative
  controls re-run on the trimmed projection.
- **Wake prompter for the 04:35Z INSURE fire — CONCUR with amendment (79396/79397/79398).** ~K
  (re-seated by COO 21:22Z after its predecessor died silently ~19:39Z; 79220) surfaced the gate:
  an idle time-gated seat reads the fire only if something prompts it, and crons are forbidden
  (Andrew's zero-crons word; a one-shot timer is a cron by another name). COO 79393 ruled the prompt
  rides the already-authorized drive loops — COO's 04:52Z ACTUATE tick sends [WAKE] to ~K + CVO; a
  dead ~K is re-seated then; CVO's four-plane read stands alone until the executor read lands — and
  named this seat's 04:37Z tick as backup. AMENDED: a backup that fires BEFORE the primary is a
  second primary, and a wake two minutes after the fire may prompt a read of a leg still in flight;
  **this seat's backup is the 05:07Z SENSE tick on a MEASURABLE miss** — list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send the [WAKE] to ~K + CVO; PRESENT -> nothing. The 04:37Z tick prompts
  nobody. ~K 79407 and CVO accepted the shape. **Standing obligation, carried in loop state and
  here.** ~K pre-registered a read-plan addendum before the fire (79411: arm 3 denominator = 3
  keys; completeness RECOMPUTED, never the leg's self-report), adopted by CVO @85bd309822 (79423).

## Row 7 (k) denominator line (owed at this commit — COO 79393 item 3, CVO fabric item 13)

`record-terraform-deploy.sh` half-write class, measured beyond n=1 (CVO 79400 @109bbee880): **of
202 source-map entries, 54 are wrong-or-absent BY CONSTRUCTION** (8 whose `last_deployed_commit`
never touched their `source_dir` + 45 carrying none + 1 unresolvable); **the 148 plausible-by-
content are NOT clean** — staleness unmeasured except 1 of 1 measured stale (~K 79382:
`opal-assets-bd49f-reporting-pull`, sha CURRENT, `last_deployed_commit` a July commit by another
seat, 39 days stale; the building commit is 52ffb6c8a3). The Rule-22a BYTE compare still resolves
where the sha is current; ATTRIBUTION is the failing limb, in the direction that passes. The 04:35Z
evidence is unaffected. Owner 0.8.0_AE_CloudComp at the post-campaign sitting; standing rule: derive
`last_deployed_commit` by CONTENT, never trust the field.

## State since tick 20 (§3, other seats; no CTO act)

- **Campaign 174 of 534 at 22:19Z** (newest 2025-03-14, last write 22:19:41Z), driver live on the
  20:48:57Z boot; the boot unit is disabled (21:04Z, EXERCISED pending); the absorbed halt is
  expected 22:41-22:46Z and the boot after it is the remedy's test. Ticks 19-20 of this loop are ON
  origin (@803250e80d, window 21); origin now @0031aa6cae.
- **PERFRP round 2 — BUILD PHASE COMPLETE at ~V (22:17Z):** AC3 COMPLETE @b70cbc5604 (b-6 Book
  rollups on the a-5 basis: 146 advisors, identity 146/146, non-additivity 2.0% expressed; a
  historical as-of REFUSED rather than aliased forward — jd2 floors at 2026-07-14; dim_relationship
  sparsity rides ON the figure as COMPUTED_PARTIAL); COO's b-4 scope ruling (the lot read IS PRF-a-4,
  on-spec; CVO's decomp census agreed independently); AC4 (above); a-4 CENSUS @0031aa6cae (5 of 5
  lot tables; lots -> positions 99.8831% once the tax-status split is respected; cost basis NAMED
  with evidence as `cost_basis_unamortized` — my 68440 item 3 discharged by measurement); **AC5
  @0d88e438de: b-4 gain/loss, the LAST build cell, reproduces a-4's residual to $0.20 at both
  grains.** Remaining: AC6 (arming emission, gated on the ledger READING 534/534), AC7, AC8 — none a
  build. Both deploy-scope files carry `# DEPLOY-SERVE-HELD`.
- **DE~D re-seat COMPLETE (79420): 7 PASS / 4 UNCOMPUTABLE / 2 FAIL as MEASURED NEGATIVES.** AC5:
  `PerfrpBookView` applies ONE injected `formatValue` (formatCurrency) to every tile, so the
  Relationships COUNT renders "$1" (confirmed at source). AC6: b-6's client_table carries exactly
  one field-set (relationship_id, status) across all 10,076 rows / 146 advisors vs the ruled
  7-column L2 set — a DS<->DE contract gap on the leaf, the issuer's and CVO's inside the round.
- CVO's TO-R2-DS amendment cert PASS (79186) applied at the face (P2-1 @ffe6d64444); P2-2 (`role_aua`
  in `opal-data-bd` vs the 49F chain runner's identity) banked for the 0.7.0 base sitting.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @0031aa6cae, ls-remote read 22:19Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (outcome-filtered distinct dates) · `git ls-remote` + MERGE_HEAD ·
  `ack_messages` (79338-79423 as received) · `send_message` to_agents (79356-79358, 79396-79398;
  6 of 6 DELIVERED).
