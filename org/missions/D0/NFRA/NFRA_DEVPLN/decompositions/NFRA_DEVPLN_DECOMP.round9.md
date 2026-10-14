# NFRA_DEVPLN decomposition -- round 9, ENRICHMENT: the closing repair (issuer 2.0.0_SA_COO~DV; cut 2026-10-14 ~14:3xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round8.md` @8cc3f585e7 (1.0.0_SA_CTO msg 109157), read at its committed bytes before the cut: section 1 grades FWD-1 to FWD-7 all REALIZED (project CLOSED on its outcomes); section 3 is the round's whole rectangle: one LOCAL worker-light cell with two repairs, "Its drain closes the project with no further analysis unless the cell fails". No addendum. The analysis names `.tools/dev_push_payload_gate.py`; the file is `.tools/portal-hooks/dev_push_payload_gate.py` (the CTO's path was short).
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~14:3xZ, HEAD 664a3e247b)

1. `.tools/portal-hooks/dev_push_payload_gate.py` line 162 reads `walk =git(portal, "rev-list", ...)`: no space after `=` (`grep -c "walk = git("` reads 0).
2. `.claude/skills/closer-drive/SKILL.md` step 5, line 35: `approval-lease --project NFRA_DEVPLN --branch cand/<box>/<slug>`: the project code is hard-coded in a skill every project uses (`grep -c "approval-lease --project <CODE>"` reads 0).
3. `python .tools/tests/test_dev_push_payload_gate.py` reads `cases=21/21 ok=True`.

## Cells

| item | cell | what | risk | served by |
|---|---|---|---|---|
| E1 | `DP-k-1` | the two DP-j-1 defects: the gate's `walk =git(` spacing; the closer-drive step 5 example's `--project NFRA_DEVPLN` becomes `--project <CODE>` | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` (worker-light) |

## Rule 24 (four postulates)

**Domain:** the CTO's section 3 (two items). **Subtraction:** item 1 -> DP-k-1 part 1; item 2 -> DP-k-1 part 2. No item is unowned. **Same grain:** two one-line repairs of one earlier order's own defects. **Intent coherence:** both make DP-j-1's output match its intent. **State coherence:** neither changes behaviour; the gate suite stays `cases=21/21`.

## Dependency chains and fan-out

One cell; no edge. M = 1 chain; N = 1 worker; cap 8.

## Battery (L5)

`comp-iam`: not applicable. `comp-adversary`: RUN, BLIND to the filesystem around the cited paths. Finding inlined: the criteria must not be satisfied by a text that already exists elsewhere in the skill (the skill carries `--project <CODE>` twice already), so AC2 greps the exact `approval-lease --project <CODE>` phrase.
