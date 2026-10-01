# Parallel Evidence Work

## Roles are not worker limits

A owns novelty analysis; B owns problem/significance analysis. The lead owns scheduling, budget, reconciliation, scoring, and the gate. These are responsibilities, not three permanently occupied worker slots. Run independent search queries, source retrievals, venue checks, and per-paper reading tasks concurrently where tools support it.

Default `max_concurrent_paper_reads = 10`. This is a ceiling, not a requirement to create ten workers. Actual concurrency is the minimum of this setting, available authorized host capacity, ready unique tasks, and remaining budget. If the host permits fewer readers, use fewer and disclose the observed peak. Do not claim ten reads ran in parallel unless they did. Do not bypass host limits by nested spawning.

Concurrent retrieval alone is not concurrent intellectual reading. A download is retrieval; a paper read requires inspecting the assigned content and producing an evidence note. Distinguish tool batching from actual parallel reader execution in the run summary.

The concurrent-read ceiling is separate from the default aggregate ceilings of 100 audited works and 15 fully read works. For example, two waves can process 10 then 5 unique full reads; the cap is never 15 per reviewer or per wave. Audits and full reads both occupy the concurrent paper-read pool while active. Browsing searches and venue-page checks need not consume a paper-read slot, but still respect host-wide limits.

## Shared queue

The lead is the sole scheduler and writer of `reading-queue.json`. A/B propose sources and questions; the lead canonicalizes work identity before enqueueing. One work requested by both roles gets one read with both requested questions. Sharing factual extraction does not require sharing independent interpretive judgments.

Record source_id, canonical_work_id, URL/version, requesting_roles, questions, scope (audit/full), status (queued/reserved/running/completed/failed/cancelled), worker_id, attempt, timestamps, assigned_output, budget_reservation, and failure/access notes. Keep run settings, active count, completed counts, and observed peak concurrency in the queue metadata.

Before dispatch, atomically reserve a read slot and a unique-source budget allowance. A full read reserves both an audited-work allowance and a full-read allowance if not already consumed. Upgrading an audited source to full only reserves the additional full-read allowance. Failed access is not a completed audit; record attempts separately. Inspection that actually occurred still counts even if the task later fails. Final counters derive from recorded inspection, not launch counts.

Fill available slots from ready tasks. On completion, ingest the note, release the active slot, and dispatch the next ready task without waiting for an entire wave. Keep synthesis dependent on its required evidence. Do not start a dependent comparison before its inputs arrive.

If spawning A/B as long-running coordinators would exhaust slots, let them return search plans first and release their slots; then run readers and resume synthesis. Reuse idle agents when supported. Otherwise use fewer readers or sequential passes. Capability honesty matters more than the requested maximum.

On failure, preserve attempt logs, diagnose the specific error, and retry only where useful; avoid simultaneous duplicate attempts. Do not silently replace unavailable full text with abstract-only evidence. Mark the reduced access scope and notify the owning reviewer. Never mark a timed-out worker as completed or let it write shared state. Before retrying, terminate or reconcile the prior attempt so late results cannot overwrite a newer note.

Prioritize closest prior art and decisive problem/contradiction evidence. Do not fill ten slots with irrelevant papers. Stop when the evidence is sufficient, the user stops work, or a budget is exhausted. Reconcile any active work before finalizing counts.

## Per-paper reader prompt

You are a source reader, not the final idea judge. You receive one source, its assigned scope, the confirmed idea revision, factual questions from A and/or B, and a unique output path.

Read the available assigned content. Return:

1. Verified source identity, version, date, venue, URL/DOI, and access limitations.
2. Exact inspected sections and audit/full-read status.
3. Research question, assumptions, method, and main claims.
4. Evidence supporting those claims and limitations; distinguish author assertions from demonstrated results.
5. Relevance to each assigned question with section/page locators where available.
6. What overlaps with the proposed idea and what does not.
7. Contrary evidence, boundary conditions, and unresolved interpretation.

Do not invent citations, inaccessible text, or findings. Do not give a final academic score, GO/NO-GO, or personal utility judgment. Do not launch additional readers or exceed the assigned source scope without returning the request to the lead. Write only your assigned attempt file and return its path and actual completion status.
