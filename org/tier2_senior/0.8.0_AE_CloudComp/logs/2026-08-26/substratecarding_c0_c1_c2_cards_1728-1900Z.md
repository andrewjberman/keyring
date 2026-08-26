# Session log -- `0.8.0_AE_CloudComp~X` -- 2026-08-26 17:28Z - 19:00Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Serial:** `0.8.0_AE_CloudComp~X` (lane instance; SINGLE-PROJECT -- holds NFRA_SUBSTRATECARDING and nothing else)
**TO:** `NFRA_SUBSTRATECARDING.TO-W1-CCX.c0-c1-c2-cards` @`aae317509b`
**Decomp:** `workflows/atom_decomposition/runs/nfra-substratecarding/20260826T172918Z/DECOMP.md` @`c8aa46b1a5`
**Cells discharged:** 21 of 21 CARD_MATRIX (`SC-a-1..7`, `SC-b-1..7`, `SC-c-1..7`)
**Session start:** fresh lane, NOT REGISTERED at open; no predecessor session for `~X`.

---

## 1. What this window was

Lane startup, then the whole of TO-W1-CCX end to end: Rule 28 substrate cards for **C0** (facts/nodes),
**C1** (interactions/edges) and **C2** (motifs), plus the proof-of-spec instance. QUALIFY-ONLY throughout --
every defect found is a named row with a named owner, and **zero generator files were edited.**

## 2. Startup

`/watcher` armed a persistent Monitor (task `b1kj51jhh`, `TaskOutput -> running`). No orphan existed for this
serial -- `ps` showed zero matches -- so no reap was performed; PID identity was checked rather than inferred
from "fresh session", per the two exercised false-positives in the doctrine. `org/XXX.md` A.1/A.2/A.3, B, B.1,
C, D, E all run. **A.3: `PATH: 105 of 105 comp-tools resolve bare` AND a forwarder actually EXECUTED** (the
exercise half -- resolution is not execution). `/cloud-ops` loaded once.

**TO census, with its blindness printed:** `--assignee '0.8.0_AE_CloudComp~X' --all` -> `total=0` over
`scanned=2111`. Per `org/XXX.md` that zero tells me **nothing** (the lane read is measured-broken on
SEATED-prose notation). Base cross-check -> `total=8` across 5 projects, none seated to `~X`. I reported the
zero *with* its known defect and held rather than concluding idle -- COO~X's GO confirmed the hold was correct.

## 3. The three cards

| card | verdict | the row that decided it |
|---|---|---|
| **C0** facts/nodes | **QUALIFIED** | role mapping PARTIAL both ways -- 4 of 14 roles unbound, 6,285 of 27,035 nodes (23.2%) outside it |
| **C1** interactions/edges | **QUALIFIED** | 31 of 53 edge_types / 20,703 of 58,224 edges (35.6%) bound by no declared block |
| **C2** motifs | **UNSOUND** | declared population (12 named families) and served population (13 canon-tier class nodes) share **ZERO names**, differ 12-vs-13, joined by nothing |

All three: 3/3 VALID against `SUBSTRATE_CARD.schema.json`, 21 of 21 rows carrying `basis` + `evidence` +
`owner`, byte-identical wave `as_of`.

**C2 is a SOUND CARD ABOUT AN UNSOUND SUBJECT** and the card says so on its face. The deliverable IS the
finding.

## 4. The measurements that carried the cards

- **C1 declared-vs-live.** Rule bank declares 10 relations + 3 composites + 8 non-relations + 11
  frontend-adapter determinations = **32 names**; live graph carries **53 edge_types / 58,224 edges**.
  Mapped 22 of 53 by type, 37,521 of 58,224 (64.4%) by volume. ⛔ **And the volume figure is dominated by ONE
  edge type** -- `CONTAINS` alone is 29,271 of 58,224 (50.3%), so vocabulary coverage is far thinner than the
  volume number suggests. Both are quoted together in the card for exactly that reason.
- **C0 role mapping.** 58 node_types / 27,035 nodes; `node_bindings` maps 48 of 58 types, 20,750 of 27,035
  nodes (76.8%). 4 of 14 roles (`Custodian`, `Producer`, `Router`, `Source`) have **no** binding at all.
- **C2 grain + population.** 19 class + 6,207 instance = 6,226, and within the classes **13 canon-tier + 6
  deviation = 19**, both measured on the `population` props field and both summing exactly.
- **C2 vintage.** ⛔ **All 6,207 instances carry composed-against `nodes_snapshot_id 6164846518420675858`;
  ZERO carry the serving snapshot `2902399899597701830`.** Classes carry a third
  (`5352191184846104891`). **Three vintages coexist in one served layer.**
- **Cadence, both trigger planes.** Events plane carries the producer
  (`opal-globgrph-derive-runner-nightly` `cron(0 2 * * ? *)` ENABLED + `opal-globgrph-cloudtrail-mgmt`
  event-pattern ENABLED); scheduler plane carries 18 schedules, none a graph producer. `graph_nodes` `<6h`
  band at 5.1h vs `graph_edges` `<26h` band at 16.1h -- **an edge set can lag its own endpoints.**

## 5. Controls I ran, and the one that mattered most

- **Grain positive control (the canon MANDATES it):** `C3System grain=class -> 4`, `>0`, proving the grain
  predicate is usable at this vintage. Without it, `19`/`6,207` would have been artifacts, not measurements.
- **Snapshot-predicate positive control:** the `props CONTAINS nodes_snapshot_id` predicate returns **19** on
  the class nodes, so the **0** on the serving snapshot is a real zero and not a dead predicate.
- **Failure-mode battery, 4 arms, separate invocations.** Arm 1 genuine negative -> `0`. Arm 2 nonexistent
  node_type -> `0`. Arm 3 nonexistent edge_type -> `0`. **Arm 4 misspelled PROPERTY -> loud `Binder
  exception`.** Arms 1 and 2 are byte-identical; arm 4 proves the instrument CAN fail loudly, so the zeros
  are answers rather than a dead probe. **`distinguishable_from_true_negative: no`, exercised not asserted.**
- **Planted mutant:** deleted the entire `trust` block from C0 and re-ran the same validator that returned
  3/3 VALID -> **REJECTED**, `'trust' is a required property`. FIRED-AS-EXPECTED.
- **Determinism:** two same-input runs on both instruments (validator 3/3 twice; `comp-kuzu` count 6226
  twice, compared IDENTICAL). ⛔ **STABLE READER != REPRODUCIBLE PRODUCER** -- all three cards carry
  `determinism: unknown` precisely so that conflation cannot happen.

## 6. Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `"what generates the C0 facts / C1 edges / C2 motifs in the graph"` | **PARTIAL** -- declared near-tie (1.50/1.50/0.47 over 80 tools), named no generator. Took the documented `if_mismatch` branch and widened DELIBERATELY rather than concluding absent. |
| `comp-estate --layers` | bare | **PASS -- the highest-value call of the session.** Supplied the DECLARED side of all three coverage/key rows (C0 "14 roles", C1 "the 10 relations", C2 "12 families"). Without it the live counts had nothing to be measured against. |
| `comp-kuzu` | ~15 traversals, provenance header read every call | **PASS** -- header confirmed the read sits AT the wave pin (`2902399899597701830`, Nessie HEAD current), so no vintage caveat was needed. Its own disclosure that *"last-write is the TABLE's write time, NOT the age of the data in it"* prevented a false freshness claim. |
| `comp-find` | 4 calls, each with **exactly one** of {content pattern, `--name`} | **PASS.** Band grading was load-bearing: `-i 'motif:a-access'` -> 236 hits / 26,812 scanned, `HEAD=227`, and reading the BANDS showed every HEAD hit was inside the producer's own input specs rather than a mapping file -- the evidence behind C2's `declared_mapping: null`. |
| `comp-keys prefix --all` | `s3://opal-estate-report/` | **PASS** -- `129 of 129 keys shown`, kuzu match 1. Run **after** the trap correction landed and **with** `--all`. |
| `aws events` + `aws scheduler` | both planes, materialized client-side | **PASS** -- deliberately NOT `--query length()`, which returns the PAGE count on a paginated `list-*`. |
| `jsonschema` + `git ls-files` | card validation + tracked status | **PASS** -- 3/3 VALID, mutant REJECTED. `git ls-files` turned C2's second-persistence-surface finding into a measured binary fact: inputs TRACKED, the two composer output envelopes UNTRACKED. |
| `.tools/proof-of-spec-check.py` | the 7 CCX criteria | run at phase 3; cell-id join pre-verified 21 of 21 present in the DECOMP's 61-id harvest. |

**What worked:** reading `comp-estate --layers` BEFORE any live count. The whole value of these three cards is
the *distance* between declared and live, and that distance is unmeasurable without the declared side in hand.

**What failed, caught by me:** see §7.

## 7. Three errors I made and caught in-window

1. ⛔ **I truncated a census with `tail -50` and lost the HEAD rows.** The visible edge_types summed to
   ~14,000 against a known 58,224 -- *a well-formed answer about a truncated population*. Caught because the
   sum did not reconcile with the total I already held. Re-run from the head: `CONTAINS 29,271`, `OWNED_BY
   6,261`, `HAS_FIELD 4,269`. **CLAUDE.md names the `head` version of this; `tail` is the same defect facing
   the other way and is not named.**
2. ⛔ **I nearly published "C0 has no declared mapping."** My first pass compared 58 live node_types against
   the 14 role NAMES and got **0 of 58** -- which reads as total absence. Wrong object: `node_bindings` is a
   role -> [node_type] map, and the correct join gives **48 of 58**. *The 0-of-58 was true and about the
   wrong question.* Recorded inside the C0 `key` row rather than quietly fixed.
3. **Native Python spawning `comp-kuzu` died `FileNotFoundError`** -- the MSYS-binary-from-native-Python class
   CLAUDE.md names. Routed through bash instead.

## 8. Surprises surfaced (OBSERVATION, no action taken)

- **The DECOMP's `AC-F3` and the TO's `CCX-AC5` diverge.** `AC-F3` ties `INCOMPLETE` to *any row carrying
  `basis: absent`*; `CCX-AC5` + TO s.5 tie it to *genuinely unworked* and say explicitly that an `absent` row
  WITH evidence is worked and complete. **No effect here** -- 0 of my 21 rows carry `absent` -- but it bites
  any lane whose subject is expected to card empty.
- **This TO's s.2 carries CTO~X's held "13 canonical families."** Measurement resolves that to the GRAPH's
  canon tier (13 class nodes), **not** the declared catalog, which has **12** under entirely different names.
  True of one object, false of the other. Per COO~X 73046, reported the measurement rather than the expectation.

## 9. Fabric corrections I absorbed this window

Four arrived mid-work; **none changed the work**, and I acted on each same-turn:
`72892` cell ids renamed `SC-C0-*` -> `SC-a-*` (identifiers only, no measurement redone) · `72979` the
`nerves_resolve` reference card does not exist (I had not been hunting it) · `73000`/`73046` the `comp-find`
content-pattern-plus-`--name` trap · `73102`/`73078` `comp-keys prefix` truncates to 40 by default.

**My audits, denominators not self-assessment:** `comp-find` **4 of 4 clean** (26,828 / 28,794 / 28,794 /
26,828 scanned; the one 0-hit call is a MEASURED zero over 28,794). `comp-keys` **0 calls before the
correction**, so no row rested on a truncated sweep; I then ran it **with `--all`** and *upgraded* the
`s3://opal-estate-report/kuzu_nessie_db` entry in C0 and C1 from HELD to **MEASURED** via a second,
independent instrument (`s3api head-object`: 51,068,928 bytes, `2026-08-06T21:49:50Z`).

## 10. Blockers

**NONE.**

## 11. Next

Route to `3.0.0_SA_CVO~X` (proof-of-spec verifier), cc `2.0.0_SA_COO~X`. MCP `0.8.0_AE_CloudComp~Y` the
`SC-c-1` methodology finding -- **their D2 card is defined against C2's motifs and C2 is UNSOUND**, which is
the single thing they most need before writing D2.
