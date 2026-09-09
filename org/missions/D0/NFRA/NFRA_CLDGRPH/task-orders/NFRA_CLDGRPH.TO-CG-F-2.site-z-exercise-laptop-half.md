# TO NFRA_CLDGRPH.TO-CG-F-2 -- CG-s-22 (ADDED at decomposition v0.6 on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S22, on ANDREW'S ALLOCATION 2026-09-09 ~17:3xZ "Recs approved" @7caee0ad5d): THE SITE-Z EXERCISE OF FWD-7's PERSON HALF -- THE LAPTOP HALF. A seat on this laptop and a seat on site Z ask D-8's fixed question through the public gateway at the SAME FIXED UTC INSTANTS and record their answers whole; the CVO grades the pair for byte-identical rows under ONE vintage inside D-8's window, each machine's local-copy census 0 with a control. This order is the laptop's asks; site Z's seat is carried by `0.0.0_AB_MSTR` over the agentbus with the same instants

<to_id>NFRA_CLDGRPH.TO-CG-F-2</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO = the COO handing this order to slot ~1 by CONTINUING the same subagent after TO-CG-F-1 (CG-s-21) is terminal and merged, with CLOUD merged into your branch (spine v3 L7 drain). ROUND 6 of NFRA_CLDGRPH (the recut as ONE issuance on the CTO's round-5 analysis @30027295be / msg 94610). Slot ~1's SECOND and LAST order. THE INSTANTS ARE FIXED BY THE ISSUER AND SHARED WITH SITE Z THROUGH 0.0.0_AB_MSTR: T0 = 2026-09-09T19:00:00Z, T1 = 2026-09-09T20:00:00Z, T2 = 2026-09-09T21:00:00Z. You ask at ALL THREE (site Z matches whichever it reaches); if handed after T0 has passed, you ask at the remaining instants and say which were missed; if handed after T2, you ask at T3 = 22:00:00Z and T4 = 23:00:00Z and the record says so (a row). PREMISE RE-GROUND at hand-off: F-1's instance VALID at your HEAD (the two stores gone: `ls -d` 0 of 2); `bash .tools/comp-kuzu --json "<the fixed question>"` answers with a VINTAGE line; if any fails, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS; the L8 seat reads the record; the CVO grades the PAIR at L9 against site Z's record.</status>

**Directive:** D0 · **Fabric:** laptop (this half) + site-z (the other half, via MSTR) · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.6 @`30027295be` (FWD-7 person half; s.7 row S22; S17 clause 2) · **Decomp cell:** `CG-s-22` (decomposition v0.6, this recut) · **Lane:** this order's deliverables only · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~1`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** Every script and capture carries `f2_` in its name.
- **Surprise = ONE ROW, never a message** (id `NFRA_CLDGRPH-W1-S<k>`, continuing your W1 numbering from F-1; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`.** The wait for an instant is NOT a criterion invocation: a bounded sleep-until loop (`while [ "$(date -u +%s)" -lt "$T" ]; do sleep 5; done`, printing the clock every 60 s) is the only long-running act and it is polled, never a bare sleep of an hour.
- **NEVER:** create, open or download a local graph (the exercise is the served graph only); run an engine; write to S3; edit code; a second transport (the laptop asks through `.tools/comp-kuzu` -> the public gateway -> the service, nothing else); non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free.

## THE CELL (decomposition v0.6, this recut, s.1a; PRD v0.6 s.7 row S22 verbatim in its accept)

> **CG-s-22** | S22 THE SITE-Z EXERCISE -- S17 clause (2) lifted into its own row on Andrew's allocation 2026-09-09 ~17:3xZ ("Recs approved": name (a) first): a seat on site Z and a seat on this laptop ask D-8's fixed question through the public gateway inside D-8's window and receive byte-identical answers under ONE vintage, no local copy on either machine | FWD-7 (person half) | claim: absent (D-8 exercised two MACHINES driven by one worker -- C-S22, C-S36: the four conjuncts named, none exercised) | status: OPEN -- ROUND 6 (recut) | executors: site Z's seat via `0.0.0_AB_MSTR`'s agentbus + this laptop's seat (this order); fabric site-z + laptop | verb verify | depends_on: CG-s-17 -> DONE; CG-s-21 -> DONE (the exercise reads on a device with no local copy) | **closes on (the PRD's accept, verbatim):** two answers from two machines driven by two SEATS, byte-identical, one vintage, WINDOW_S inside D-8's (4.229 s, or the window the face states); each machine's local-copy census 0 with a control; the CVO grades against both records

**PRD acceptance 7 (verbatim):** *"One story, no older copy. With every developer machine off, two people on two machines ask the same question at the same moment and get the same answer, and there is no local copy left that either could have read instead. (FWD-7)"*

## MEASURED BY THE ISSUER AT THE CUT -- and the ONE design choice the issuer made for both seats

- **The fixed question (D-8's, unchanged):** `MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC, t` (deterministic ordering). The laptop asks it exactly as D-8 did: `bash .tools/comp-kuzu --json "<cypher>"` (stderr captured for its VINTAGE line; the answer's `rows` array is the payload compared).
- **"THE SAME MOMENT" ACROSS TWO SEATS THAT CANNOT MESSAGE EACH OTHER is solved by FIXED INSTANTS, not by a handshake.** Both seats ask at the same UTC instants, read from their own clocks (`date -u`), and record T_START and T_END around each ask. The issuer names the instants in this face AND in the message `0.0.0_AB_MSTR` carries to site Z: **T0 = 2026-09-09T19:00:00Z, T1 = 2026-09-09T20:00:00Z, T2 = 2026-09-09T21:00:00Z.** You ask at ALL THREE; site Z asks at whichever it reaches; the CVO grades the pair whose instants match. **The window the face states: each seat's ask begins within 5 s of the instant** (clock skew between the two machines is measured by each seat printing `date -u` beside an NTP-free reference -- the gateway's `Date` response header, which both seats see from the SAME server; state the skew).
- **The vintage:** the pointer advances about hourly (the marker-driven worker); if it advances between the two seats' asks at one instant, the vintage lines DIFFER and that pair fails -- which is why there are three instants. Print `LAPTOP_VINTAGE_T<n>=` for each.
- **"No local copy on either machine (proven)":** the laptop = the MAIN workspace's `infra/aws/globgrph/` by absolute path AFTER F-1: `ls C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/ | grep -c -E 'kuzu_nessie_db|kuzu_db|kuzu_ac7'` -> 0 with a positive control (`grep -c kuzu_stitch_db` -> non-zero, S26's, deliberately still present and SAID SO) and the worktree's own `ls`. Site Z's seat runs the same census on its device (its face says so).
- **What you CANNOT do and must not try:** read site Z's record (it lands on site Z's tree and reaches this device by MSTR's integration later); compare the pair yourself (L9's); message anyone. Your record is ONE HALF; it says so in its first line.

## DELIVERABLE -- in this order

1. **The census** (both `ls` reads with the control) BEFORE T0.
2. **`f2_ask_at.sh <instant>`**: wait until the instant (polled), stamp `T_START` from `date -u +%FT%T.%3NZ`, fire the ask, stamp `T_END`, print `LAPTOP_ROWS_SHA256_T<n>=<sha256 of the rows array as canonical JSON>`, `LAPTOP_VINTAGE_T<n>=<vintage>`, `LAPTOP_START_T<n>=`, `LAPTOP_END_T<n>=`, `LAPTOP_SKEW_S_T<n>=` (own clock vs the gateway's Date header), and the WHOLE JSON answer into `f2_answer_T<n>.json`.
3. **Three asks** at T0, T1, T2 (each attempt recorded whole; a missed instant is printed `MISSED` with the clock, never omitted).
4. **The record** `CG-s-22.site-z-exercise.laptop-half.result.md`: first line `THIS IS THE LAPTOP HALF; SITE Z'S RECORD IS THE OTHER HALF; THE PAIR IS GRADED AT L9`; one fenced JSON block `{machine: "laptop <worktree path>", question, cypher, instants: [{t, start, end, skew_s, rows_sha256, vintage, rows_count, answer_file}], local_db_census: {main_workspace: 0, worktree: 0, control: "<n> kuzu_stitch_db (S26's)"}, site_z_half: "carried by 0.0.0_AB_MSTR; not readable from this device"}` then the raw transcripts. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="F2-AC1" cell_refs="CG-s-22"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f2_instants_kept.sh</invocation><expect>INSTANTS_KEPT=([0-9]) of \1 within 5s[\s\S]*INSTANT_PROBE_CONTROL=FIRED</expect></criterion>
`F2-AC1` -- EVERY ASK BEGAN WITHIN 5 s OF ITS INSTANT: for each recorded instant, `T_START - T` in [0, 5) s (`INSTANTS_KEPT=<n> of <n>` over the instants actually attempted, missed ones printed by name and excluded from the numerator AND the denominator, never silently); a planted late start is caught.

<criterion id="F2-AC2" cell_refs="CG-s-22"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f2_answers_recorded.sh</invocation><expect>ANSWERS_RECORDED=([0-9]) of \1[\s\S]*ROWS_COUNT_EACH=(58,?)+[\s\S]*VINTAGE_EACH_PRESENT=true</expect></criterion>
`F2-AC2` -- EVERY ASK ANSWERED AND RECORDED WHOLE: each answer file parses, carries a `rows` array (58 rows as D-8 measured, printed per instant) and a vintage line; the sha256 of the canonical rows per instant printed (the value site Z's record must match).

<criterion id="F2-AC3" cell_refs="CG-s-22"><invocation>ls C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/ | grep -c -E 'kuzu_nessie_db|kuzu_db|kuzu_ac7'</invocation><expect>^0$</expect></criterion>
`F2-AC3` -- NO LOCAL COPY OF THE CANONICAL GRAPH ON THIS MACHINE, read by absolute path against the MAIN workspace (the worktree's own `ls` is a second read in the record; the stitch store's presence is printed as the control and named as S26's).

<criterion id="F2-AC4" cell_refs="CG-s-22"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f2_skew.sh</invocation><expect>SKEW_S_MAX=[0-9]+(\.[0-9]+)?[\s\S]*SKEW_SOURCE=gateway Date header</expect></criterion>
`F2-AC4` -- THE CLOCK SKEW IS MEASURED, NOT ASSUMED: the laptop's clock against the gateway's `Date` response header at each instant, the maximum printed (site Z prints its own against the same server, so the pair's skew is derivable at L9 without a handshake).

<criterion id="F2-AC5" cell_refs="CG-s-22" judgment="true"/> `F2-AC5` -- THE HALF, READ HONESTLY: what this record proves alone (a seat on this machine asked at the instants and recorded answers under vintages, with no local copy), what it cannot prove (that site Z asked, matched, or that the two seats were two PEOPLE), and what the CVO needs from site Z's record to grade the pair (the same instants, the rows sha256, the vintage, the census). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9 against BOTH records.

<expected_criteria>F2-AC1, F2-AC2, F2-AC3, F2-AC4, F2-AC5</expected_criteria>

## SURFACES

`.tools/comp-kuzu` (READ; run) · the D-8 record and scripts `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/{CG-x-7.two-machines.result.md, two_machines.sh}` (READ: the ask shape, the canonical-JSON comparison) · the gateway (the public HTTPS path the thin client already uses).

## BOUNDS

- **Reads only.** Three asks (five at most if handed late), each recorded whole. No retry inside an instant.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-F-2.site-z-exercise-laptop-half.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.6 (this recut), cell CG-s-22 (s.1a; ADDED on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S22, on Andrew's allocation @7caee0ad5d).
<owned_cells>CG-s-22</owned_cells>
Read-dependencies, NOT claimed: CG-s-17 (DONE), CG-s-21 (TO-CG-F-1, terminal and merged before this order is handed). The OTHER HALF: site Z's seat, carried by 0.0.0_AB_MSTR -- not yours.
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25); the C3 moratoria bind BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- the thin client's bearer path, the instrument D-8 used; no principal, policy or grant changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5); the deliverable's validator context is the L9 seat's compose over BOTH halves.
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `F2-AC1`..`F2-AC5`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-F-2.site-z-exercise-laptop-half.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> F2-AC1,F2-AC2,F2-AC3,F2-AC4,F2-AC5` BEFORE the complete flip. `F2-AC1` and `F2-AC3` are the controls that must be able to FAIL. `F2-AC5` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance pinning them), and the face says so.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE T0: `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/two_machines.sh --for "how the laptop ask is fired, how the rows array is canonicalised and hashed, and how the vintage line is captured"`. No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-F-1's drain).**
