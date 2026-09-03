# TO NFRA_COMPEFFICACY.TO-CE-G-2 -- the DISCLOSE-ONLY order on the stale-served graph: every answer from a tool that LOADS THE KUZU UNIVERSE (comp-blast, comp-trace) carries the served graph's VINTAGE and AGE on its disclosure line, in the form comp-find --corpus aws already prints -- NO engine change (the rebuild/labeled-stale seam and its fallback sink are NFRA_CLDGRPH's CG-s-8; the local path serves for weeks until that switch-off and is UNBOUNDED today, S31)

<to_id>NFRA_COMPEFFICACY.TO-CE-G-2</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~J</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: 1.0.0_SA_CTO's L4 RULING 93837 (CE-g-2 SPLIT: engine half CARRIED to NFRA_CLDGRPH CG-s-8 + CG-x-7; the DISCLOSURE half is this project's and is cut as the disclose-only order) with 3.0.0_SA_CVO's input 93833 (row S31 @ce5c7babea: a `--budget 60` comp-blast call ran the full ~17-minute rebuild and was killed outside with no line -- FWD-7's sentence false on the LOCAL path today); decomp v0.2.7 @9c4a688102; PRD v0.6 @7138c4a176 (v0.7 landing at the CTO with G-2 SPLIT / G-3 CARRIED, no FWD changed); Andrew's word "/drive COMPEFFICACY to completion." @dd040c447b. Seated on the Codex lane that completed T-23 (continuity on one project).</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.6 @`7138c4a176` (s.4.2 disclosure; s.7 rows G-2, G-5, T-6, T-19; FWD-7 "the freshness surface ... bounded or disclosed") · **Decomp cell:** `CE-g-2`, its DISCLOSURE half (closes on an EXERCISED comp-blast answer AND a comp-trace answer each carrying the served graph's vintage + age on the disclosure line; engine bytes byte-identical before/after) · **Lane:** the DISCLOSURE lines of `org/modules/graph/cli.py` (comp-blast's engine) and comp-trace's engine (name it from `.tools/comp-trace`'s header), reading the vintage the graph ALREADY carries (`built:` from the DB's own provenance -- the line comp-find --corpus aws prints today: `VINTAGE: DB: kuzu_nessie_db  (27206 nodes / 58550 edges)  built: 2026-09-03T17:13:01Z (age: 0.3h)`) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~J/g-2-disclosure.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~J` (a CODEX seat) holds NFRA_COMPEFFICACY only.

---

## THE CELL

CE-g-2 (PRD s.7 G-2, FWD-7): the stale-served path `kuzu_nessie_db.fallback.jsonl` -- 16 `inc-served-labeled-stale` events ~34 h behind at the CRO's F5 measurement; the closes-on "the age is bounded by a schedule OR stated on the answer -- never silent (AC-7)". The BOUND belongs to the engine the sibling project is retiring (CG-s-8) -- not touched here. The STATEMENT is this order: **whatever graph a tool serves, the answer says which graph and how old.** comp-find `--corpus aws` already does it (its `VINTAGE:` line); comp-blast prints a comp-kuzu provenance block (`DB: kuzu_nessie_db (N nodes / M edges)`, `source: nessie`, snapshot ids, `graph_nodes: last-write 0.3h ago`) but no single `built: <ts> (age: Nh)` line at the answer's disclosure grain, and the stale label (when the seam serves the old DB) is not on the answer at all; comp-trace's disclosure is to be measured by you first.

## DELIVERABLE -- in this order

1. **MEASURE FIRST (read-only):** one real default run of each tool on a real subject, output captured whole; quote what each prints today about the served graph (the vintage, the age, a stale label -- present or ABSENT, line by line). Read the DB's own provenance source (the `built:` value comp-find prints; where `_canonical.py`'s serve-stale path writes its label/age -- READ ONLY, cite the lines) so the disclosure reads the SAME carrier, never a second clock.
2. **THE DISCLOSURE LINE, one form, both tools:** on EVERY answer (clean, NOT-FOUND, AMBIGUOUS, partial, JSON mode as a field), one line at the disclosure grain: `VINTAGE: DB: <name> (<nodes> nodes / <edges> edges)  built: <ISO-8601 Z> (age: <N.N>h)` and, when the served graph is the stale one (the seam's label), the same line carries ` STALE-SERVED: <label from the seam>` -- never a silent stale. The age is computed from `built:` at answer time, printed with one decimal in hours; a graph whose `built:` cannot be read prints `built: UNREAD (reason)` and `age: UNKNOWN` -- never a default, never omitted. `--json` carries `vintage: {db, nodes, edges, built, age_h, stale_served}`.
3. **NO ENGINE CHANGE:** `infra/aws/globgrph/_canonical.py`, `kuzu_nessie_load.py`, `kuzu_cli.py`, the fallback sink and the rebuild/labeled-stale seam are byte-identical before and after (sha256 of each quoted); the change lives in the two tools' disclosure code only. A tool whose disclosure cannot be added without touching the seam STOPS and reports which line forces it -- that is CG-s-8's, and the report says so.
4. **THE BATTERY**, NEW: `.tools/tests/test_g2_disclosure_battery.py` -- arms: fresh graph (age printed, no STALE-SERVED), stale-served graph (planted via the seam's OWN label file/flag, read-only to the seam; STALE-SERVED present with the label), unreadable `built:` (UNREAD + UNKNOWN, never a default), JSON field present, comp-trace arm and comp-blast arm; a RED mutant per arm (the mutant that prints today's block without `built:`; the mutant that prints `age: 0.0h` on UNREAD; the mutant that omits STALE-SERVED). Direct AND pytest at the FILE grain; `.tools/commit-gate.sh` clean on every .py touched.
5. **THE EXERCISE (the closes-on):** one real comp-blast answer and one real comp-trace answer, post-commit, each quoted with its VINTAGE line; then the deliverable `g-2-disclosure.result.md` (the T-16 shape's 4.2 disclosure fields for the two tools, before/after, the seam files' shas, the battery numbers at both grains) and the proof instance; FWD-9: one run of each from a seat other than yours (ask the issuer with the exact commands).

## ACCEPTANCE

<criterion id="G2-AC1" cell_refs="CE-g-2"/> `G2-AC1` -- MEASURED FIRST: each tool's disclosure today quoted whole from a real run; the vintage carrier named at source (file:line, read only).
<criterion id="G2-AC2" cell_refs="CE-g-2"/> `G2-AC2` -- THE LINE: every answer class of both tools carries `VINTAGE: DB ... built: <ts> (age: N.Nh)` and `STALE-SERVED: <label>` when the seam serves the stale graph; UNREAD/UNKNOWN on an unreadable `built:`, never a default; `--json` carries the field.
<criterion id="G2-AC3" cell_refs="CE-g-2"/> `G2-AC3` -- NO ENGINE CHANGE: the five engine/seam files byte-identical (sha256 before/after quoted); any forced touch is a STOP-and-report naming the line.
<criterion id="G2-AC4" cell_refs="CE-g-2"/> `G2-AC4` -- THE BATTERY: NEW, six arms, a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean.
<criterion id="G2-AC5" cell_refs="CE-g-2"/> `G2-AC5` -- EXERCISED: one real post-commit answer from each tool quoted with its VINTAGE line; FWD-9 from a distinct seat; push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.
<expected_criteria>G2-AC1, G2-AC2, G2-AC3, G2-AC4, G2-AC5</expected_criteria>

## SURFACES

`org/modules/graph/cli.py` (comp-blast's engine; its provenance block and disclosure lines) @6df07696ea · comp-trace's engine (name it from the shim) · `.tools/comp-find`'s `--corpus aws` VINTAGE line (the PATTERN, read only) · `infra/aws/globgrph/_canonical.py` and `kuzu_nessie_load.py` (READ ONLY: the `built:` carrier and the stale label) · `.tools/_compbudget.py` (consumed) · PRD s.4.2 + s.7 G-2/G-5 @`7138c4a176` · row S31 @ce5c7babea (the measurement).

## BOUNDS

- **NO engine change** (step 3): the seam, the loader, the CLI, the fallback sink are NFRA_CLDGRPH's CG-s-8 / CG-s-9 -- byte-identical after; a forced touch is a STOP.
- **One clock:** the age derives from the graph's own `built:`; no second vintage source, no new sensor or monitor (standing moratorium).
- **No new dependency; no new file outside the two tools' disclosure code, the NEW battery, the deliverable and the proof instance.**
- **The graph is READ, never rebuilt by this order** (`--check` and default runs only; never `--force` on a stale graph -- S31's 17-minute ambush lives on that path until T6-AC7 lands at ~G).
- **A spec-vs-world divergence is a ROW** in `surprise-channel/investigations/INVESTIGATION_v1.md` (append + commit in the same act, pathspec the file only; a co-worker's valid row is admitted by the gate; an invalid one is reported to the issuer, never amended); never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

**PUSH (standing law on this CODEX seat's face):** a shared branch (CLOUD / DEV / PROD / main / SITEZ) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the terminal (LD-0367/0368, LD-0522). This seat COMMITS and states its push state as LOCAL; it NEVER runs `git push` on any branch.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @9c4a688102 (v0.2.7), cell CE-g-2 (s.1a; PARALLEL; the DISCLOSURE half -- SPLIT at v0.2.7 on CTO 93837; the engine half CARRIED to NFRA_CLDGRPH CG-s-8 + CG-x-7).
<owned_cells>CE-g-2</owned_cells>
Read-dependencies, NOT claimed: CE-g-5 (DONE; the serve-stale contract this disclosure names), CE-t-6 (T6-AC7 at ~G: the budget bounding the load -- parallel, different lines), CE-t-22 (met).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (read at 2026-09-03 15:40Z); 0 armed gates name NFRA_COMPEFFICACY or these tools.
comp-iam: DECLARED-NOT-APPLICABLE -- the tools read a repo-local graph; no AWS principal, policy or resource is read or changed by this order.
comp-adversary: RUN -- rc 0 at read-vintage @afe26cae61 (2026-09-03T17:37:13Z); 5/5 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 5 attempted / 3 stable / 2 flagged (NFRA_COMPEFFICACY.TO-CE-G-2.disclose-only.proof_of_spec.json GONE; g-2-disclosure.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `G2-AC1`..`G2-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~J/NFRA_COMPEFFICACY.TO-CE-G-2.disclose-only.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. G2-AC3's byte-identical seam and G2-AC2's UNREAD arm are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/cli.py --for "every disclosure line the blast command prints, the provenance block, where the served DB's built timestamp is read, and the JSON output's shape"`; `comp-read .tools/comp-trace --for "the engine it names and its disclosure lines"`; `comp-read infra/aws/globgrph/_canonical.py --for "where the stale label and the served DB's build time are written and read"` (READ ONLY). BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: the two real answers quoted; FWD-9 from a distinct seat.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, the two tools' disclosure before/after, the seam files' shas, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
