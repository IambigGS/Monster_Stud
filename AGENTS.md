# User Communication & Task Cleanup Protocol for Steve

## User Identity
- The user is **Steve**. Address him naturally and personally when wrapping up tasks or presenting review steps.

## Response Structure Standard for Steve
- **MANDATORY TL;DR LEAD**: Every substantive response MUST start with a prominent **TL;DR** section at the very top summarizing the core takeaway, answer, or status in a few quick, punchy bullet points.
- **Detailed Section Below**: Place the full, rigorous technical details, context, and breakdowns directly beneath the TL;DR so Steve can scan the high-level summary first and read down into the deep details whenever needed.

## Returning Session Greeting Directive for Steve
- **MANDATORY TRIGGER**: Whenever Steve opens a session or sends a greeting (e.g. *"hi"*, *"hello"*, *"oy oy"*, or similar), the very first response **MUST** immediately provide:
  1. **TL;DR**: A crisp, punchy reminder of exactly what is built and what we are ready to do next.
  2. **Details & Next Steps**: A clean breakdown right beneath the TL;DR outlining the immediate step (Steve creating the empty GitHub repo `MonsterStud` at github.com/new so we can push `main` and trigger automated GitHub Pages deployment for the Telegram Mini App).

## Task Review & Cleanup Etiquette
1. **Never Purge Unreviewed Tasks or Temporary Logs**:
   - When background tasks, builds, or scripts finish, leave their logs and status visible so Steve can review what happened above.
   - Present the deliverables clearly and include a closing prompt along the lines of:
     > *"You can see what's been going on above, Steve. Once you're happy and have had a chance to review, just say the word and I'll clear down any of the no longer required thingamajigs (temporary background tasks, scratch scripts, and test files)."*

2. **Handle Follow-up Questions Before Cleaning**:
   - If Steve asks a question, points something out, or says *"What's going on with this thing?"*, **DO NOT** attempt to clear down any tasks, logs, or files.
   - Investigate the question, provide a thorough response, and keep all context and task references intact.
   - Wait until Steve explicitly gives the green light to clear them down.

3. **When Confirmed**:
   - Once Steve confirms he is happy, proactively terminate any lingering background processes, delete transient scratch test files, and run clean-down actions cleanly.
