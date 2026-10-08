# TO NFRA_TRNSPT.TO-TR-d12 -- FWD-10 hops H3+H4: slicer over gold, and the Kimi K3 drafter behind an injected adapter

<to_id>NFRA_TRNSPT.TO-TR-d12</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-d-12` (`decompositions/NFRA_TRNSPT_DECOMP_R12.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-d-12`: hops H3 and H4 of FWD-10. Given ONE abstract request (built by H2: `request_id`, `yc_variant`, `comparison_keys`,
`account_type`, `themes`, `holdings_categories`, `requester`), pick precedent commentary with the existing slicer and write a DRAFT in Opal's
voice through Kimi K3 -- behind an injected model adapter, with NO real model call in this cell.

**Contracts (`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`):** C-SLICE :116 ("with no candidate the slicer falls back to the
nearest variant and the draft says so in its provenance; with none at all a draft is still produced and says it has no precedent");
C-KIMI :117 (Kimi K3, "input limited to abstract fields ... no client identity, no account ids. Output is a DRAFT ... Andrew's word is given
for the first call, and only after C-WIPE-GATE passes"); C-WIPE-GATE :114; C-GOLD-FIELDS :115 (gold rows: `record_id`, `yc_variant`,
`models_referenced`, `account_type`, `themes`, `body_text`, `paragraph_hashes`, ...).

**Read (do not edit):** `data/transcripts/scripts/outlook/slicer.py` (the built slicer: abstract request + gold rows -> candidate record ids
with provenance; never returns body text), `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:1-60` (the estate K3 pattern:
`MODEL = "kimi-k3"`, bounded budgets, "the installer supplies a deadline-enforcing HTTP/secret adapter ... There is no default network
client or credential read"; JSON-only prompts that treat inputs as data, not instructions).

**Build:**
1. `data/transcripts/scripts/commentary/drafter.py`:
   - `draft(request, gold_rows, *, model, wipe_gate_passed: bool, k=10) -> dict`: refuses (raises `DraftRefused("WIPE_GATE_NOT_PASSED")`)
     unless `wipe_gate_passed` is True; runs the slicer over `gold_rows` (held-out rows excluded); takes the chosen candidates' WIPED
     `body_text` by `record_id`; builds a prompt from the abstract request's whitelisted fields + the precedent texts; calls
     `model(prompt) -> str` (the injected adapter); returns `{"request_id", "draft_text", "provenance": {"candidates": [record_id...],
     "variant_used", "fallback": bool, "no_precedent": bool, "model": "kimi-k3"}, "status": "DRAFT"}`.
   - With 0 candidates: still calls the model with the abstract request alone and sets `no_precedent: True`; the draft text includes a line
     saying it has no precedent (C-SLICE).
   - The prompt is built ONLY from: `yc_variant`, `comparison_keys`, `account_type`, `themes`, `holdings_categories` and precedent body
     texts. Never `requester`, never any other key of the request.
   - `KimiAdapter` (a thin class taking `http_post` and `api_key_reader` callables, the resolution_kimi pattern; no default network or secret
     read) so the close can pass a real one; tests never construct it with real callables.
2. `data/transcripts/scripts/tests/test_commentary_drafter.py`, at least: `test_refuses_until_wipe_gate_passed`;
   `test_no_precedent_draft_says_so` (empty gold -> a draft, `no_precedent` True, the line present); `test_prompt_carries_no_client_identity`
   (a request with planted extra keys -- client name, account number, the requester -- and a fake model that records the prompt: none of the
   planted values is in it); a test that 12 synthetic gold rows yield at most 10 candidates and the held-out row is never used.

### ACCEPTANCE

<criterion id="TR12-d12-AC1" cell_refs="TR-d-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_CHECKS/r12_checks.py d12</invocation><expect>R12-D12-OK</expect></criterion>
`TR12-d12-AC1` -- the gate refusal, the no-precedent draft and the no-identity prompt tests pass by name.

<expected_criteria>TR12-d12-AC1</expected_criteria>

Dry-run at the base (box/dell2 846cbbe61e): `R12-D12-FAIL absent` -- FAIL as expected. The first real Kimi call is the issuer's close act.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. `slicer.py` and IRPT code are READ only.
- **LOCAL.** NO model call, no AWS, gateway or HTTP call, no secret read. Synthetic gold rows and a fake model only.
- **Refusal clause.** If the slicer's interface cannot take the abstract request as specified, adapt in `drafter.py` (never edit
  `slicer.py`) and file a surprise row (id `NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/commentary/drafter.py
data/transcripts/scripts/tests/test_commentary_drafter.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ. If
`data/transcripts/scripts/commentary/__init__.py` is absent in your worktree, your tests may import `drafter` by path; do not create it
(cell TR-e-12 owns it).

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R12.md</decomp_doc> (round 12), cell `TR-d-12`.
<owned_cells>TR-d-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR12-d12-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-d12.commentary-drafter.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR12-d12-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that actually contains it.
</proof_of_spec>

**REPORT:** the `draft` signature and output keys, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a drafter with an injected model; no schedule, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no secret read in this cell.
comp-adversary: RUN -- 4 sources read (PRD C-SLICE/C-KIMI/C-WIPE-GATE/C-GOLD-FIELDS, slicer.py, resolution_kimi.py :1-60); BLIND to real gold (0 objects at the cut) and to Kimi's real output. Traps: a real model call from a worker, client identity in the prompt, a draft that silently drops the no-precedent case; the face injects the model, whitelists prompt fields and tests the empty case.
lane: one commentary module, one test, the investigation file.
</preflight>

Source: Andrew-direct @a4fdb78bbe; CTO msgs 1763, 1780; decomposition round 12 cell TR-d-12 and issuer rulings 1-2, 4.
