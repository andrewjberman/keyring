# 3.0.0_SA_CVO~Z -- work log 2026-09-03 20:15-20:45Z: four mechanisms, all withdrawn by their own authors

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_1915-2015Z_*`. **Push state as read:** local HEAD
e8f179bd8d; origin/SITEZ 001709c96e. **Loops:** none. Inbox empty throughout.

## 1. The verdict-correction cluster is CLOSED

`2.0.0_SA_COO~Z` filed three disarm records (Z-S72, Z-S73, Z-S74) closing Z-S53, Z-S56 and Z-S57. **Both of this
seat's own verdict defects are corrected in EVERY carrier**: the wrong denominator at 93e72ef53f in all THREE --
the face's census line, S1-AC3's fallback, and **the decomposition's OP-s-1 cell, which this seat never thought
of and which would have outlived both other fixes and re-seeded the error at the next cut**; and AMEND C's bar
scoped to the imported objects at 00fdc44a76 / dc8042045a.

**One record-keeping choice worth keeping:** the issuer recorded Z-S57's disarm under its own id rather than
folding it into Z-S53's, *"because the census reads per id, and because the two rows are different acts: Z-S53 is
the assignee finding the defect, Z-S57 is the verdict's author confirming."* That keeps who-caught-what legible
instead of collapsing it into one event.

## 2. The ACL-churn thread: FOUR mechanisms, every one withdrawn by its own author inside an hour

| row | seat | claim | fate |
|---|---|---|---|
| Z-S68 | `0.7.0_AE_CloudOps~S` | churn = state carries empty attrs the config does not produce | withdrawn by its author at Z-S75 |
| Z-S69 | **this seat** | "the config-versus-state asymmetry is CONFIRMED" | withdrawn at Z-S71 -- a TWO-plane claim from a ONE-plane read |
| Z-S70 | `2.0.0_SA_COO~Z` | control: "opal-gateway plans CLEAN on the identical idiom" | withdrawn by its author at Z-S77 -- that was the POST-apply reading |
| Z-S71 | **this seat** | "the deciding difference is in STATE" | withdrawn at Z-S76 -- a peer's hypothesis RELAYED as a conclusion |
| Z-S71 | **this seat** | "the config shape is NECESSARY AND NOT SUFFICIENT" | withdrawn at Z-S78 -- inferred from the control Z-S77 corrected |

**What the thread actually established**, per Z-S75: the churn is a PRE-APPLY artifact that RESOLVES ON APPLY --
opal-gateway churned identically before its apply and reads `No changes` rc=0 after; portal-auth does not resolve
after THREE applies. **So the open question is not what causes the churn but why apply converges one root and not
the other, and that is UNKNOWN.** Z-S75 says so and declines to offer a third guess, which after two refuted
mechanisms is the higher-value act.

**Three self-corrections from this seat on one thread**, and they are two DIFFERENT shapes, which matters for the
lesson: Z-S69 was the day's recurring one-plane-read-as-a-relation error (fourth instance, and the first where I
had transcribed the falsifier myself -- the S5-AC7 evidence I quoted reads `opal-gateway = 0`). Z-S71's state
clause was a NEW shape: a peer's hypothesis, correctly attributed in the notes, promoted to a conclusion in the
summary line **where attribution does not travel**. The estate banks the sender-side form of this and
`0.0.0_AB_MSTR~Z` disclosed the same shape against itself today. **A hypothesis that changes hands should keep the
word that marks it as one.**

**Z-S78 CONSOLIDATES rather than adding a fourth correction**: this seat's position was scattered across three
partial withdrawals, and a reader at L9 would have had to reconstruct it. One row now states it once -- measured
and standing, versus asserted and withdrawn with where each fell -- and it is the last this seat files on that
thread.

**WHAT STANDS FROM THIS SEAT, unaffected by any of the withdrawals:** the config-plane count (3
`managed_rule_group_statement`, 0 `version =`, 0 configs, 0 overrides -- a fact about the file); the DATING (those
blocks entered at 7987571c9a 15:40Z, every earlier vintage ZERO); the consequence that **TO-OP-S-5's filed
S5-AC7 PASS was correct at its vintage so nothing re-grades**, with two further completed faces checked clear;
and the **ROOT-not-FACE scoping**, which the issuer verified independently at `portal-auth/lambdas.tf:51` and
acted on by amending S1-AC5 @bc0d0ed2bd **before** the limb-2a apply.

**Practical dispositions, settled and untouched by the mechanism question:** S418-AC3's 0-diff limb files
`UNVERIFIABLE-BY-INSTRUMENT` for portal-auth only, with the live read and plan structure as substitute evidence;
every other module still owes a real 0-diff; destroy and forces-replacement clauses stay PLAN-WIDE.

## 3. Memory

Extended `spec-carriers-agreeing-never-establish-a-world-fact` with the fourth instance rather than writing a
near-duplicate, and rewrote its index line. The addition is narrow and was in nothing I held: **when a row QUOTES
a measurement from a neighbouring root, module or vintage, that quotation is a CONTROL on any mechanism the same
row asserts.** A falsifier does not stop being one because you copied it out yourself for a different purpose,
and nothing but the author will ever compare a row's own quoted evidence against its own conclusion.

## 4. State at close -- and the round is MUCH larger than five faces

Channel **78 rows**, 22 this seat's. Resolved-live ARMED: Z-S50 (two credential homes), Z-S60 (C-16 overstates
the log destination's controls), Z-S63 (the halt gate blind to a lane inbox), Z-S75 (the ACL non-convergence).
None is this seat's to disarm.

**MATERIAL CHANGE TO THE L9 HORIZON:** the task-order set now reads **22 orders, 8 complete** -- TO-OP-S-1
PENDING and the rest STAGED (S-4-18, S-6, S-7, S-9-11, S-10, S-12, S-13, S-14-21, S-15-19, S-20, S-22, S-23,
S-29). Round 2 is not the five faces this seat had been tracking. **L9 is a long way out and should be**, and the
resolved-state census is the instrument for it -- the raw `hazard_standing` field reads ARMED on far more rows
than are live, because the channel is append-only and a disarm lands as a LATER row.

**The one blocked item, unchanged:** the four round-1 closure rows (S2, S11, S13, S17). Gate here still
`c3ef3a2530`, 0 occurrences of `REMEDIATED`; the ruled exemption sits on the other device behind an ASSESS-ONLY
leg. Script ready, refuses over a dirty file. Cost: nothing live.
