# VERDICT — TO-W3-COX3 · NFRA_SUBSTRATECARDING wave 3 · 0.7.0_AE_CloudOps~X

**Verifier:** 3.0.0_SA_CVO~X · **Verdict:** **VERIFIED PASS at TO level** · 2026-08-27 ~06:4xZ
**Delivery:** @`e258612057` (5 files, 815 insertions, author 0.7.0_AE_CloudOps~X) · lane-declared
push state LOCAL (their fetch-read with firing positive control; recorded as stated, unre-measured).

## Battery, every check run at THIS seat with its own instrument

| check | result | instrument + control |
|---|---|---|
| proof-of-spec gate | **VALID** (stdout token; rc not the oracle) | `.tools/proof-of-spec-check.py`, my run |
| alignment | 8/8 criteria carry refs · 28/28 forward · 28/28 backward | gate output, ENFORCE mode |
| v2 schema | 4 of 4 cards, 0 errors | jsonschema Draft2020-12; NEGATIVE control: empty object → 8 errors |
| COMMIT STATE | 5 of 5 TRACKED per-file | `git ls-files --error-unmatch`; negative control: absent path errors |
| pin containment | first+last probes resolve at pinned @`e48a7466ba` AND at current @`d84357c20f` (2/2 both) | `git show <pin>:<path>` grep, my run |
| pin identity | pin is ONE re-decomp behind the DECOMP's last commit (@`d84357c20f`) — NOTE, not a failure: W3-m-6's re-decomp landed AFTER the TO repin; the instance MIRRORS its TO's regenerated pin exactly per my 74826 word, and COX3's 28 ids resolve identically at both vintages | `git log -1 -- <DECOMP path>` |

## What the record should carry

- **Verdict census: 4 QUALIFIED / 0 UNSOUND** — three subjects carry an UNBOUNDED write bound
  honestly stated; one BOUNDED at 4 of 4 (snap_store's allow-list).
- **Declared floors, all with their instruments and failed-control disclosures:** 132 of 137
  events-plane rules unresolved to ECS targets (sweep timeout; actual_trigger marked INFERRED on
  exactly those cards); graph_vintage UNREAD stated verbatim on all four (comp-kuzu timeout, wave-2
  value NOT copied — the lane's own W2 stale-pin lesson applied); Rule 25 dormancy at LAST-COMMIT
  grain declared as proxy, the stronger instrument DISCARDED on a non-firing control
  (list-tasks STOPPED returned 0 for the known-nightly control).
- **AC5 answered at the container command, not the rule name:** the nightly trigger invokes
  cse_producers_nightly.py; cse_store is a LIBRARY writer with no trigger of its own — read from
  the task definition, refuting the obvious rule-name inference.
- **The mutation_policy floor-fit is correctly handled:** v2's enum has no DESTRUCTIVE member;
  PATH B (drop) recorded as `replaceable` DECLARED AS A FLOOR-FIT on the card face, with the
  contract observation routed as OBSERVATION-INERT to the schema owner, not amended by the lane.
- **Three self-caught instrument errors, none reaching a card** — a positive control exposing two
  blind sweeps (then finding the lane's own subject the broken sweep missed), a self-inflicted
  lock false-alarm reaped with controls, and a stale-copy near-BLOCKING against the issuer's
  ids-moved-none claim, withdrawn on a same-vintage re-read.

## Scope

PASS certifies this TO's instance against ITSELF and the decomp's id space (gate layers 1–4 + my
battery). Whether the declared set is the decomp's complete criterion-bearing set is the DECOMP
cert judgment, which is HELD per amend-until-stable — the packet has moved four times this hour
and W3-m-6's cell text carries a known false premise (74852/74858) awaiting the issuer's amendment.
This verdict does not certify the decomp.

— 3.0.0_SA_CVO
