# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Lektor static site generator** project for the Python FOSDEM conference website. Lektor is a flat-file CMS that generates static websites from content files (`.lr` format), Jinja2 templates, and data models.

**Technology Stack:**
- Lektor 3.3.10 (static site generator based on Flask)
- Jinja2 3.1.2 (templating)
- Python 3.12.12
- Bootstrap 3.3.7 (frontend)
- Taskfile for automation
- Deployed via Netlify

## Common Commands

**Setup:**
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux

# Install dependencies
task dependencies:install
```

**Development:**
```bash
# Serve locally with hot reload (http://localhost:5000)
task serve

# Build static site (outputs to ./output/)
task build

# Clean build artifacts
task clean
```

**Dependency Management:**
```bash
# Compile dependencies from requirements.in
task dependencies:build

# Update all dependencies to latest versions
task dependencies:update
```

**Direct Lektor Commands** (when you need more control):
```bash
# Serve with specific options
.venv/bin/lektor serve --verbose --prune

# Build to custom output directory
.venv/bin/lektor build --output-path=/path/to/output
```

## Architecture

### Directory Structure

- **`/content/`** - Content pages in `.lr` (Lektor Record) format, organized hierarchically (directory structure = URL structure)
- **`/templates/`** - Jinja2 HTML templates for rendering pages
- **`/models/`** - Schema definitions (`.ini` files) that define content structure and fields
- **`/flowblocks/`** - Reusable content block type definitions (`.ini` files)
- **`/databags/`** - Static data collections like navigation menus (`.ini` files)
- **`/packages/`** - Custom Lektor plugins (Python modules)
- **`/assets/static/`** - Static files (CSS, images, etc.)

### Content System

**Content Files** (`.lr` format):
```yaml
_model: page
---
title: Example Page
---
body:

#### md-section ####
title: Section Title
----
content: Markdown content here
```

The `.lr` format uses `---` to separate fields and `####` to separate flow blocks. Content hierarchy mirrors URL structure: `/content/example/contents.lr` becomes `/example/`.

### Models

Models (in `/models/*.ini`) define the schema for content types:

- **page** - Static pages with title and flow-based body (contains md-section, location, or schedule blocks)
- **talk** - Individual conference talks with author (links to speaker), title, subtitle, description, abstract, duration, day, start_at, stop_at
- **talks** - Container/parent model for talk children (paginated, ordered by day/start_at)
- **speaker** - Speaker profiles with name field
- **speakers** - Container/parent model for speaker children (paginated)

Note: Room and sponsor models were removed in 2022 but templates remain.

### Templates

**Main Templates:**
- `layout.html` - Base template with Bootstrap navbar, footer, menu from databag
- `index.html` - Homepage with flow blocks and sponsor listing
- `page.html` - Generic static page rendering
- `talk.html` / `talks.html` - Individual talk detail and talk listing
- `speaker.html` / `speakers.html` - Individual speaker and speaker listing

**Block Templates** (`/templates/blocks/`):
- `md-section.html` - Renders markdown content with optional title
- `location.html` - Embeds OpenStreetMap with coordinates and address
- `schedule.html` - Complex scheduling view that groups talks by day and room

**Template Features:**
- Query content: `site.query('/talks').filter(F.day == some_date)`
- URL generation: `this|url` or `record|url`
- Custom filter: `date|humanize_date` (from humanize_date plugin)
- Grouping: `talks|groupby('room')`
- Access databags: `bag('menu')`

### Flow Blocks

Reusable content components that can be embedded in pages with a flow-type field:

- **md-section** - Markdown section with title and content fields
- **location** - Google Map with title, body (HTML), latitude, longitude
- **schedule** - Dynamic schedule rendering (no fields, queries talk data)

### Custom Plugins

**humanize_date.py** (`/packages/`):
- Registers Jinja2 filter `humanize_date`
- Converts dates to formatted strings like "January 01, 2026"
- Auto-loaded by Lektor via `setup.py` entry points

### Project Configuration

**PythonFOSDEM.lektorproject:**
Contains project metadata including:
- Project name and event date
- GitHub repo and Twitter URLs
- CFP (Call for Proposals) dates

This file drives site-wide configuration accessible in templates via `config` object.

## Key Workflows

### Adding a New Static Page

1. Create directory in `/content/`, e.g., `/content/venue/`
2. Add `contents.lr` file with model `page`
3. Add content using flow blocks (md-section, location, etc.)
4. Add to navigation in `/databags/menu.ini` if needed

### Adding Talks/Speakers

Typically done via bulk import or individual `.lr` files:
1. Create `/content/speakers/speaker-name/contents.lr` with model `speaker`
2. Create `/content/talks/talk-slug/contents.lr` with model `talk`
3. Link talk to speaker via `author` field
4. Schedule block will automatically render them grouped by day/room

### Modifying Templates

Templates use Jinja2 with Lektor-specific features:
- Always extend `layout.html` for consistent site structure
- Use `this` to access current page context
- Use `site.query('/path')` to fetch other content
- Image handling: `this.attachments.images.get('name').thumbnail(width)`

### Creating New Flow Blocks

1. Define block in `/flowblocks/blockname.ini` with fields
2. Create template in `/templates/blocks/blockname.html`
3. Use in content by specifying flow block type between `####` markers

## Development Notes

- Lektor uses a flat-file structure where all content is version-controlled
- Changes to content require rebuild (automatic in `serve` mode)
- The schedule block queries are complex - be careful modifying grouping logic
- Templates expect certain content structures (e.g., schedule expects talks with room field)
- Historical note: Sponsor and room models were removed in 2022 but templates remain for potential future use
