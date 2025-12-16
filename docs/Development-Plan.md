# Phisherman Development Plan

**Created:** 04/Dec/2025 03:50 SGT

---

## Overview

This document outlines the step-by-step development plan for building the Phisherman MVP - a phishing simulation tool that sends test emails, tracks clicks, and educates users.

## Development Approach

Flask apps are built incrementally: routes first (to test URLs work), then database (to persist data), then templates (to make it pretty), then business logic (sending emails). Each piece can be tested as we build it.

---

## Development Phases

### Phase 1: Database Foundation ✅ COMPLETE
**Completed:** 04/Dec/2025 04:30 SGT

- [x] Import sqlite3 module
- [x] Create database initialization function
- [x] Define users table (id, email, name)
- [x] Define clicks table (id, user_id, tracking_token, clicked, click_timestamp)
- [x] Write helper functions to interact with database
- [x] Test: Verify database.db file is created with correct schema

### Phase 2: Routes (The Core) ✅ COMPLETE
**Completed:** 04/Dec/2025 18:55 SGT

- [x] Add route: `/track/<token>` - Captures clicks when user clicks link
- [x] Log click to database with timestamp
- [x] Add route: `/results` - Shows admin view of who clicked
- [x] Test: Access both routes and verify they work

### Phase 3: HTML Templates ✅ COMPLETE
**Completed:** 07/Dec/2025 19:15 SGT

- [x] Create `templates/` folder
- [x] Create `landing.html` - "You got phished!" educational page
- [x] Create `results.html` - Admin view displaying click data in table
- [x] Create `phishing_email.html` - HTML email template
- [x] Update routes to use `render_template()`
- [x] Test: View pages in browser

### Phase 4: Email System ✅ COMPLETE
**Completed:** 13/Dec/2025 (SGT)

- [x] Import smtplib and email modules
- [x] Write function to generate unique tracking tokens (UUID)
- [x] Write function to send emails via Gmail SMTP
- [x] Insert test users into database
- [x] Create tracking links with tokens
- [x] Test: Send email to yourself

### Phase 5: Command-line Trigger ✅ COMPLETE
**Completed:** 16/Dec/2025 (SGT)

- [x] Add command-line argument parsing
- [x] Create `send-campaign` command
- [x] Trigger: `python app.py send-campaign`
- [x] Test: Run command and verify emails are sent

### Phase 6: End-to-End Testing
- [ ] Send email to yourself using send-campaign
- [ ] Click the tracking link in email
- [ ] Verify click is logged in database
- [ ] Check `/results` page shows the click
- [ ] Verify educational landing page displays correctly
- [ ] Document any bugs or issues

---

## Success Criteria

✓ Can send phishing email to test addresses
✓ Clicking the link logs it in the database
✓ Can view results in a web page
✓ Educational landing page explains what user missed

---

## Technical Stack (MVP)

- **Backend:** Flask (single `app.py` file)
- **Database:** SQLite (file-based, zero config)
- **Email:** smtplib with Gmail SMTP
- **Frontend:** Plain HTML/CSS (no JavaScript frameworks)
- **Hosting:** Local development only

---

## Out of Scope for MVP

- Docker/containers
- React/Vue/any JS framework
- Redis/message queues
- Authentication/user management
- Multiple phishing templates
- CSV upload for email lists
- Scheduled campaigns
- Advanced analytics

These features are planned for future versions after MVP is complete and working.
