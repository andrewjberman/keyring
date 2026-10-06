# OPAL_BBGTML -- Surprise-channel investigation doc v1

Opened 2026-10-06 by 0.0.0_AB_MSTR~Z at this project's first channel item, on 1.0.0_SA_CTO~Z msg 30002.
Append-only. `integrations/bloomberg/` is under Andrew's no-modify order, so any remedy is his word.

---

### OPAL_BBGTML-Z-S1 -- the sign-in fallback writes the OCR'd Terminal username to the pull log in plain text

```json
{
  "id": "OPAL_BBGTML-Z-S1",
  "project": "OPAL_BBGTML",
  "fabric": "site-z",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-10-06T11:30Z",
  "one_line": "The DAPI sign-in fallback's verify step prints the OCR'd Bloomberg Terminal username in plain text into the scheduled pull log: 3 lines in today's log, and 15 of the 31 logs in %USERPROFILE%\\opal_bbg_logs carry the line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:\\Users\\Opal Bloomberg\\opal_bbg_logs\\bbg_tplus1_20261006_070001.log lines 27, 43, 59: \"username OCR (observation only): '<username>' similarity 100%\" (value not reproduced here).",
      "Emitter: integrations/bloomberg/auth/bbg_verify.ps1:192-193 @598b791b19 (Write-Output of $ocr).",
      "Census: grep -l 'username OCR (observation only)' over %USERPROFILE%\\opal_bbg_logs\\*.log = 15 of 31 files, read 2026-10-06 ~11:28Z."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The fallback never prints credential values: its own fill line says 'user_len=12 pw_len=9 (values never printed)'.",
  "world_is": "The password stays masked, but the username is OCR'd from the screenshot and printed verbatim by the verify step, so the login identity sits in plain text in local pull logs.",
  "notes": "Local disk only; no upload of these logs was measured. No file was edited or redacted (no-modify zone, 1.0.0_SA_CTO~Z msg 30002). A remedy prints the similarity score alone and leaves the existing logs to Andrew's word."
}
```
