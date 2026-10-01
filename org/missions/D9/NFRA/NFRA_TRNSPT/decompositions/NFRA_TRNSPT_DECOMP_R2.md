# NFRA_TRNSPT decomposition -- ROUND 2 (2026-09-30, issuer 2.0.0_SA_COO~T)

Cut on 1.0.0_SA_CTO's round-1 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND1_ANALYSIS_NFRA_TRNSPT_20260930.md`
@acd1033e60 (msg 103394: "cut round 2 from section 4 in one issuance"), over 3.0.0_SA_CVO's review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md` @ba199ff55b (L9 TR1-t4-AC3 PASS; Q1, Q2) and the
remediation rows in `surprise-channel/remediations/REMEDIATION_v1.md` owned by this seat (S6, S7, S8, S9, S10, W4-S8, W4-S10).
PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1 (unchanged; no endpoint change asked).

**The rectangle is the analysis's section-4 enrichment list, thread-breaking first, repairs batched into ONE cell.**

| cell | item (analysis section 4) | rows / rulings | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `TR-f-2` | 1: the lander unwraps the Graph `value` envelope; `load_tables` reads the ruled `authors.json` alone and the registry's tenant email domains | S9, S10; ruling 3a | FWD-7 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `TR-d-2` | 2 (its tool): the precision scan -- the criterion's booleans for EVERY message scanned, no text | ruling 3b | FWD-7 | NOT-EVALUATED | laptop | LOCAL | worker-light | TR-f-2 |
| `TR-w-2` | 4: the two missed wipe classes as PLANTED cases; each removed or a stated limit | W4-S8; ruling 4 | FWD-7 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `TR-v-2` | 5: FWD-2 beyond Monday -- silver for every held transcript of the three reachable archetypes | ruling 5 of section 4 item 5 (the transcript tools allow no new pull; the held bronze allows the parse) | FWD-2, FWD-5 | NOT-EVALUATED | laptop | SERVED | worker-light | -- |
| `TR-x-2` | 3: the batched repair -- package-qualified imports, universal-newline fixtures, listing fakes, proved in the DEPLOYED layout | S6, S7, S8; ruling 6; CVO Q2; CTO rule 103374 | FWD-1, FWD-7 | NOT-EVALUATED | laptop | WORLD (path floor: the Lambda handler; nothing applied) | worker | TR-f-2, TR-d-2, TR-w-2, TR-v-2 (it rewrites their imports; the batch cell runs last) |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains.** A = TR-f-2 -> TR-d-2 -> TR-x-2 (slot ~1). B = TR-w-2 (slot ~2). C = TR-v-2 (slot ~3). TR-x-2 joins A, B and C: it is
released only after TR-w-2 and TR-v-2 have drained. Fan-out 3 of 3 chains, cap 8.

**Write sets (disjoint while concurrent; TR-x-2 runs alone at the end).**
- TR-f-2: `data/transcripts/scripts/outlook/criterion.py`, `.../outlook/land_bronze.py`, `.../outlook/pull.py`, `.../tests/test_outlook_envelope.py`, `.../tests/fixtures/outlook_replay_envelope/`.
- TR-d-2: `data/transcripts/scripts/outlook/precision.py`, `.../tests/test_outlook_precision.py`.
- TR-w-2: `data/transcripts/scripts/outlook/wipe.py`, `.../tests/test_wipe_planted.py`.
- TR-v-2: `data/transcripts/scripts/teams/backfill_silver.py`.
- TR-x-2: every `.py` under `data/transcripts/scripts/` (teams, outlook, tests), the test fixtures' readers, `infra/aws/lambda/transcripts-pull/handler.py`, `infra/aws/lambda/transcripts-pull/build.sh`.
- The channel file is append-only and shared (CLAUDE.md 14b inversion); every drain resolves it as the union.

**The issuer's real runs at close (acts only this seat can perform; no worker holds a gateway tool).**
1. FWD-7's real row (ruling 3b). The admissible message is identified: Manav's 2026-08-11 reply "Re: Assistance with Portfolio
   Proposal" (Graph id `...ADC4phlAAA=`), to two 49 Financial advisors, a non-inline `application/pdf` "Ultra Long Term.pdf" of
   585,757 bytes, body "Attached is the YC report of the ultra-long-term portfolio." -- measured 2026-09-30 ~21:3xZ through the
   gateway: `sender_ok, client_recipient, ycharts_pdf` all true under the round-1 heuristic. Its `read_email` output arrived
   INLINE (not persisted by the harness), so it is not yet a byte-exact recording; the issuer records one admissible message whose
   tool output the harness persists to a file (four other confirmed YCharts candidates exist: 2025-11-06, 2026-05-07, 2026-07-27
   Manav; 2026-09-02 Yang), or states that the byte-exact recording waits on site Z's headless mail route. Then: `precision.py` over
   the recorded directory (every message's booleans printed), `pull.py --replay ... --apply` (bronze), `silver.py --apply`, and the
   silver READ by this project's named readers only (Andrew's IAM user from this seat; the second reader has no AWS principal yet --
   FWD-8, stated) before any other reader is admitted (the CVO's condition, adopted by the CTO).
2. FWD-1 and FWD-2: the thread trace re-run after TR-x-2 (the imports it rewrites are on the thread), and the silver census.
3. The Research Meeting refusal (manifest S07, read-only): the issuer reads the meeting chat's call events through the existing
   gateway chat tools for the organizer and meeting kind that explain `3003`, and records the cause or the next probe.

**Carried, not cut (analysis section 4 item 6):** FWD-1 hops 1-2 (site Z's transcript tools and headless route, accepted 103276);
the READY hook (IRPT_BCKEND S18); the slicer's real replay (ruling 5: through the hook's abstract fields, never a firm bucket; the six
fixture requests stand and the replay says so). S2 is CLOSED by relay and S3 CLOSED INERT (rulings 1, 2).

## Rule 24 record

- **MECE over a declared domain.** Domain: section 4 items 1-5 (item 6 is carried by the analysis's own words). By subtraction:
  item 1 = TR-f-2; item 2 = TR-d-2 (its tool) + the issuer's real run (its act); item 3 = TR-x-2; item 4 = TR-w-2; item 5 = TR-v-2
  (the parse) + the issuer's S07 probe (the read-only refusal investigation). Remainder: none.
- **Same grain.** One cell per item's buildable part; the acts only a gateway-holding seat can perform are the issuer's real runs.
- **Intent coherence.** f/d make FWD-7's input real; w measures the wipe; v extends FWD-2/FWD-5 over held data; x repairs the union.
- **State coherence.** No cell applies Terraform, grants a principal, calls a vendor model, sends mail or builds an alarm. Only TR-v-2
  writes the bucket (silver of already-held bronze, under Andrew's IAM user, the one key grantee).

## Battery (enrichment round)

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no cell touches a schedule; TR-i-1's desired rule is unchanged and unapplied.
- `comp-iam`: RUN -- `infra/aws/terraform/transcripts/main.tf` read at the cut: 1 KMS key policy (2 statements, 1 reader principal,
  Andrew's IAM user), 1 bucket policy (2 Deny statements, TLS-only and key-only). BLIND: the live IAM plane outside this root (0 of
  the account's roles read). TR-v-2's writes and the issuer's reads run under the one grantee; nothing is granted.
- `comp-adversary`: RUN on the union, because round 1's defects lived there: the combined suite at the cut is `SUITE-RED passed=95
  failed=23`, and the Lambda bundle extract at the cut loads bare `criterion`, `gateway_client` and `land_bronze` modules (the
  deployed-layout shape of S7). Both are TR-x-2's criteria, dry-run at the base.
- **CTO issuer rule 103374, stated as the analysis asks:** a cell whose diff changes an import in a script that runs from a
  deployed code prefix carries one criterion that imports the module from the deployed layout itself, on an exact extract of what the
  deploy ships, printed. It binds TR-x-2 (the Lambda bundle) and is its AC2.
