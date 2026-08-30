# /self-drive D2 & D3 — tick 90 (2026-08-30 13:39Z; covers ticks 89–90) — state: ARMED

Covers the acts since the tick-88 log (`d0e31c2b56`, LOCAL; origin @`b6dad1f773` unchanged since the 13:10Z
CLOSE — ls-remote read 13:39Z). Tick 89 (13:27Z) was quiet and wrote nothing. Cron `1c261f82` :07/:37.
Paired `/drive D2 & D3 @ 2.0.0_SA_COO` (its ticks 16–17).

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **24** on the register (D2 20 + D3 4; the
register has not yet re-counted the MAPVINTAGE close and the A07STAMP / c02-g-11 cuts — surfaced, not
absorbed). Ledger **19 / 0 unconsumed**. Acked READ since the tick-88 log: 87495, 87508, 87510, 87515,
87520, 87526, 87529, 87532.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 6** (R1–R5 unchanged; R6 = the C02-g-11 capability card, pending AE~L's filing;
driver's REC YES). The all-reserved tell noted; each citation has been through review.

## Verdicts since the tick-88 log (§3)

**0 on pitched calls.** Rulings/grades read:
- **COO 87526 / 87532:** A7-2 RULED (a) — `_classifier_vintage` excluded by name; A7-3(ii) MET only at
  "exactly one writer"; **the gate's widen REC ACCEPTED** — C02-g-10 carries a00:353-354's helper line
  (one commit, six stamp lines removed; C02-g-12 ABSORBED); **C02-g-13** (deterministic vintage) cut with
  the gate's V-1 form, V-2 both polarities + the digest-field census, V-3 the 1,080-partition limit, V-4
  two consecutive fires same vintage.
- **CVO 87510 / 87529:** the P2F-MARKER-DS earlier grade stands only under history (a) — answered (a) by
  DS~V on `TZ=UTC git log` (87520) and confirmed on the gate's own read; the vintage finding verified on the
  CVO's control (4 processes → 4 digests at the default seed; seed 0 → identical; sorted set → identical);
  OBSERVATION × INERT, owner DS~N; the consumer's real substrate identity is the manifest's `content_hash`.

## Driver's own acts (tick 88 → 90)

1. **C02-g-9 E-1 halting set** (AE~L 87495): SEVEN inputs, not six — `dim_transaction` (c01:232, an inline
   f-string the DEF-band census missed); `rc.read_partition` RAISES by default (runner_common.py:81); fam
   is read at a resolved latest and cannot raise; domain = 539; no new ruling needed — read and acked.
2. **P2F-MARKER-DS self-report** (DS~V 87508): three pin fields carried "this round" — a pointer that
   expires on success; repaired to landed hashes @`c7e1199b79`, VALID unpiped; V-4 NOT YET DUE with the
   amended reason (converter deployed 03:37Z; Sunday sweep converted 0 partitions by construction;
   `meta/complete/` 0 vs control 482). The gate accepted (87512) — both classes already mechanised (the
   checker's 05:00:15Z arm; the re-verify-after-landing step) — then **withdrew one clause** (87517): it had
   asserted history (a) before the fact that decides it; DS~V measured (a) (close 01:52:05Z; the arm
   05:00:15Z; checker in force 95d0b1d10e) and the gate's own UTC read agrees to the second (87534).
   DS~V also caught its own literal-Z citation ("01:00Z" for the arm) that would have produced history (b).
3. **C02-g-10 A7-2 NOT MET as written** (DS~N 87515): a third mover, `_classifier_vintage`, digests
   `str()` of a DynamoDB string SET → per-process random under hash randomization (3 runs → 3 vintages,
   `content_hash` identical; PYTHONHASHSEED=0 control identical). **Gate rulings (87522):** (1) exclude by
   name in this cell, the deterministic form is its own cell, and the convention line — a digest is a PURE
   FUNCTION of the content it claims to digest; (2) REC widen to a00's one-line reroute (0-byte delta = the
   arm) — accepted by the issuer. **V-1 RULED (87534):** `canon-json-v1` — `json.dumps(sort_keys=True,
   separators=(",",":"), default=canon)` with sets → sorted lists, Decimal → str, any other type refused, no
   `str()` of any container; sha256 of the UTF-8 bytes; a sibling `_classifier_vintage_form` field so old
   (random) and new (deterministic) values are distinguishable by claim; arms — determinism (baseline
   first), discrimination (alias added → different; reordered → same), chain-wide digest-field census.
4. **Memory written:** a digest over `str()` of a set is random per process.
5. **/exec-sum (bare) rendered for Andrew at 13:25Z** (12 live directives carded); the drift it found on
   this seat's broker summary ("tick 76") re-set.

## In motion, not mine

DS~N: A7-1 commit (a07 + a00), the three-table A7-2 read, A7-4 before a NAMED 12:45Z fire, **the Monday
pre-registration from the READ 08-30 map (landed ~13:16Z; the line not yet sent)**; AE~L: E-1/E-2 build to
the seven-input set, the C02-g-11 R-1 card (then MSTR carries R6 once); AE base: the dispatch billing leaf
retirement (both halves signed) + the (k) schema read; DS~V: the first single-writer read; the CVO's
grades; Andrew's word on R2 (W1/W2) and R6; S1e at 04:35Z. LOCAL, riding the next window: `d0e31c2b56`,
this log, `c7e1199b79`, `e88205d404`… (the 13:10Z CLOSE pushed everything before it).

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, project JSON statuses, the ledger count, inbox listing by timestamp,
`ls-remote` + `merge-base --is-ancestor`; `TZ=UTC git log --date=format-local` on four commits (the (a)/(b)
read); the exec-sum grounding (telemetry 389,767 rows / 143 files; `comp-state --self-test` PASS 4/4;
`get_live_agents` 21). No comp-find, no comp-state beyond the exec-sum run.

state: ARMED · next log at a verdict or tick 96 (floor)
