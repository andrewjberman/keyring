# NFRA_TRNSPT decomposition -- ROUND 5 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-4 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_4_20261008.md` @856673477a (msg 1349: "round 5 ONE
issuance: E1 meeting allowlist data asset, E2 D2-S2 census"; section 2 is the enrichment list). PRD
`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.2, ENDPOINT unchanged.

**The rectangle is the analysis's section-2 list. E1 is the thread item: `/hx/transcripts` is released and serves no meeting
because its allowlist is empty (NFRA_OPLGTW row Z-W15-S30); the allowlist's values are this project's data asset.**

| cell | item (analysis s.2) | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `TR-a-5` | E1: the meeting allowlist data asset -- a versioned file naming each regular investment meeting series by its stable identifier, Monday meeting first, each row with its source; a loader that rejects a row with no identifier or no source | FWD-1, FWD-2 | NOT-EVALUATED | dell2 worker | LOCAL | worker-light | -- |
| `TR-c-5` | E2: D2-S2, truncation or classification -- the deployed `mail_route.py` against HEAD, and a counts-only listing census tool | FWD-7 (residue D2-S2) | NOT-EVALUATED | dell2 worker | LOCAL | worker-light | -- |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains.** A = TR-a-5 (slot ~1). B = TR-c-5 (slot ~2). No edge: disjoint write sets, no consumed output. Fan-out 2 of 2 chains,
cap 8.

**Write sets (disjoint across slots).**
- TR-a-5: `data/transcripts/scripts/teams/meeting_allowlist.json` (new), `data/transcripts/scripts/teams/meeting_allowlist.py`
  (new), `data/transcripts/scripts/tests/test_meeting_allowlist.py` (new).
- TR-c-5: `data/transcripts/scripts/outlook/listing_census.py` (new), `data/transcripts/scripts/tests/test_listing_census.py` (new),
  its deliverables folder (`R5_MAIL_ROUTE_DEPLOYED_VS_HEAD.md`).
- Both may append to the investigation file (append-only, shared).

**Issuer rulings inside this decomposition (rule 27 L6: the issuer rules its own decomposition).**
1. **E1's identifiers come from the repo record, not a fresh calendar read.** `data/transcripts/scripts/teams/series.json` (TR-t1,
   copied from `research_transcripts/schema/series.json`) holds the four series' `online_meeting_id`; the OG-tx-2 live run
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/TRANSCRIPT_REACH_RUN.json` read the same ids back from Graph (3 x 200,
   Research Team Meeting 403 for lack of an invitation). That satisfies "identifier read from a calendar or meeting record"; a worker
   holds no Graph route.
2. **E1 lists all four series**, because FWD-2 reads "every regular investment meeting ..., the Research Meeting included" (PRD :32).
   The Research Team Meeting row carries its measured reach (403) so the gateway owner sees it will be refused until FWD-2's
   invitation cause is resolved.
3. **E1 criterion (3) (the handoff message id to MSTR) is the issuer's act at close**, not a worker criterion: a worker cannot send.
   The issuer sends the file path to `0.0.0_AB_MSTR~DELL2` after the merge and records the msg id in the close record.
4. **E2 reads the manifest's deployed commit AT HEAD, not the analysis's hash.** The analysis names `240ac2fe5a`; the manifest at
   the cut reads `deployed_commit: aa75078e1b72a28219e6148d3ec8e9bf705ea111` (deployed 2026-10-07T21:49:10Z, OG-rl-14), a newer
   release. Rule 22a: deployed bytes, at the vintage read.
5. **E2 criterion (2) (ONE live counts-only listing of the 2026-08 span) is the issuer's one real run at close**, using the
   worker's census tool. The worker builds and tests the tool against a stub; it makes no live call. If dell2 cannot read the
   route's bearer, the run goes through the fenced-read path (analysis s.2) and the close record says so.

**Carried, not cut (analysis s.3):** FWD-8's second reader, the 14 flagged words, Kimi K3 (unchanged); the allowlist's LOAD into the
running gateway is NFRA_OPLGTW's act, asked through MSTR. C3 ledger L5 (the 2026-10-08T23:30Z fire reads `window_days=7`) is the
issuer's open served act from round 4.

## Rule 24 record

- **MECE over a declared domain.** Domain: analysis section 2, items E1, E2. By subtraction: E1 = TR-a-5 (criteria 1-2) + issuer
  close (criterion 3); E2 = TR-c-5 (criterion 1 + the tool) + issuer close (criterion 2's live run). Remainder: none.
- **Same grain.** One cell per item; live and cross-fabric acts are the issuer's.
- **Intent coherence.** a builds the thread's next hop's data; c decides D2-S2's cause.
- **State coherence.** No cell calls the gateway, Graph or AWS, applies Terraform or edits the gateway. The allowlist's live value is
  NOT moved by this round (the gateway owner's act).

## Battery (enrichment round)

- `comp-schedule`: DECLARED-NOT-APPLICABLE (no schedule touched).
- `comp-iam`: DECLARED-NOT-APPLICABLE for the worker cells (no AWS call). The issuer's live census reads secret
  `gateway/mail/bearer` by name; dell2 read of it is unmeasured at the cut.
- Checks file `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_CHECKS/r5_checks.py`, dry-run at base CLOUD 1e02ea542a:
  a5-file FAIL, a5-test FAIL, c5-record FAIL, c5-census FAIL, each "absent" as expected.
- Drain checks (not on any face): `commit-gate.sh` on the touched `.py`; the transcripts suite once after both merge.
