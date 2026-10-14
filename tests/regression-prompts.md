# Regression prompts

Run these after editing any skill. Each lists the setup, the prompt, and the behavior that must hold.

## R1: Attachment wins over unrelated example text (the 1.0.1 bug)
- **Setup:** attach a spec for system A (e.g., a clinic management spec). No mention of A in the prompt.
- **Prompt:** `/software-design-doc:sdd-author Write a design doc for this backend. It needs custom aliases, click analytics, and about 10M redirects/day. Stack: FastAPI, Postgres, Redis.`
- **Expected:** Claude notices the prompt (a URL shortener) conflicts with the attachment (system A) and asks which to design, quoting both. It does not draft a URL shortener SDD, and it does not silently drop the attachment.

## R2: Attachment only
- **Setup:** attach a spec for system A.
- **Prompt:** `Use sdd-author to write the software design document based on the attached file.`
- **Expected:** reply opens with `Subject:` naming system A and `Based on:` naming the file; terminology matches the spec; each `REQ-` cites its source section; no details from other systems.

## R3: Consistent prompt and attachment
- **Setup:** attach a spec for system A that does not name a stack.
- **Prompt:** `Write the design doc for this. Use FastAPI and Postgres.`
- **Expected:** no conflict question; FastAPI and Postgres appear as user-requested technology choices; anything else not in the spec is `[ASSUMPTION]`.

## R4: No attachment
- **Prompt:** `Write a design doc for a URL shortener with custom aliases and 10M redirects/day.`
- **Expected:** subject comes from the message; missing facts are `[ASSUMPTION]` / `[TBD]`; no questions about attachments.

## R5: Mixed languages
- **Setup:** attach a Persian-language spec.
- **Prompt (English):** `Write the SDD based on the attached file.`
- **Expected:** Claude asks, or states, which language the SDD will be written in; identifiers and standard names (e.g., FHIR) stay in original form; section numbering is unchanged.

## R6: Reviewer uses the uploaded document
- **Setup:** upload an existing SDD without pasting it.
- **Prompt:** `Use sdd-reviewer on my design doc.`
- **Expected:** Claude finds and reads the uploaded file and reviews it; it does not write a new document.
