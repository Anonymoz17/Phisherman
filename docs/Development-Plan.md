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

### Phase 2: Routes (The Core)
- [ ] Add route: `/track/<token>` - Captures clicks when user clicks link
- [ ] Log click to database with timestamp
- [ ] Add route: `/results` - Shows admin view of who clicked
- [ ] Test: Access both routes and verify they work

### Phase 3: HTML Templates
- [ ] Create `templates/` folder
- [ ] Create `landing.html` - "You got phished!" educational page
- [ ] Create `results.html` - Admin view displaying click data in table
- [ ] Create `phishing_email.html` - HTML email template
- [ ] Update routes to use `render_template()`
- [ ] Test: View pages in browser

### Phase 4: Email System
- [ ] Import smtplib and email modules
- [ ] Write function to generate unique tracking tokens (UUID)
- [ ] Write function to send emails via Gmail SMTP
- [ ] Insert test users into database
- [ ] Create tracking links with tokens
- [ ] Test: Send email to yourself

### Phase 5: Command-line Trigger
- [ ] Add command-line argument parsing
- [ ] Create `send-campaign` command
- [ ] Trigger: `python app.py send-campaign`
- [ ] Test: Run command and verify emails are sent

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
