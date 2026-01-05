# PythonFOSDEM 2026 - Website

Official website for the Python FOSDEM 2026 conference, built with [Lektor](https://www.getlektor.com/).

## Technology Stack

- **Static Site Generator**: Lektor 3.3.10 (Flask-based)
- **Python**: 3.12.12
- **Templates**: Jinja2 3.1.2
- **Frontend**: Bootstrap 3.3.7
- **Automation**: Taskfile
- **Deployment**: Netlify (self-hosted)

## Prerequisites

- Python 3.12.12 (system installation or [mise](https://mise.jdx.dev/) global)
- [Task](https://taskfile.dev/) 3.45.4 (managed via `.tool-versions`)
- [mise](https://mise.jdx.dev/) for tool version management (recommended)

## Version Management

This project uses **mise** for tool version management.

### Setup with mise

1. **Install mise** (if not already installed):
   ```bash
   curl https://mise.run | sh
   # or on macOS: brew install mise
   ```

2. **Install Task** (from `.tool-versions`):
   ```bash
   mise install
   ```

3. **Install Python 3.12.12**:

   Python is managed separately to avoid Netlify mise conflicts:

   ```bash
   # Option 1: System installation (simplest)
   # Follow your OS-specific instructions

   # Option 2: mise global (not in project .tool-versions)
   mise use -g python@3.12.12
   ```

### Why Python is not in .tool-versions

Netlify uses mise internally and conflicts arise when `.tool-versions` specifies Python.
The project `.tool-versions` only contains Task to avoid these conflicts. Python is managed
via `PYTHON_VERSION` in `netlify.toml` for Netlify builds.

## Installation

Task handles virtualenv creation and dependency installation automatically:

```bash
# Quick start (creates venv + installs deps + starts server)
task serve

# Or step by step:
task venv                    # Create virtual environment
task dependencies:install    # Install dependencies
task serve                   # Start development server
```

**Note:** The Taskfile automatically creates `.venv` if it doesn't exist, so you can run `task serve` directly from a fresh checkout.

## Usage

### Local Development

Start the development server with hot reload:

```bash
task serve
```

The site will be accessible at http://localhost:5000

### Build the Site

Generate static files in the `./output/` folder:

```bash
task build
```

### Clean Artifacts

Remove build files:

```bash
task clean
```

### Dependency Management

Compile dependencies from `requirements.in`:

```bash
task dependencies:build
```

Update all dependencies to latest versions:

```bash
task dependencies:update
```

## Project Structure

```
/
├── content/          # Content pages (.lr format)
│   ├── talks/       # Conference talks
│   ├── speakers/    # Speaker profiles
│   └── ...
├── templates/        # Jinja2 HTML templates
│   └── blocks/      # Flow block templates
├── models/          # Schema definitions (.ini)
├── flowblocks/      # Reusable content block types
├── databags/        # Static data collections
├── packages/        # Custom Lektor plugins
├── assets/          # Static files (CSS, images)
├── output/          # Generated static site (ignored by git)
└── .venv/           # Python virtual environment
```

## Content Format

Content files use the `.lr` (Lektor Record) format:

```yaml
_model: page
---
title: My Page
---
body:

#### md-section ####
title: Section Title
----
content: Markdown content here
```

- `---` separates fields
- `####` separates flow blocks
- Directory hierarchy = URL structure

## Direct Lektor Commands

If you need more control:

```bash
# Server with specific options
.venv/bin/lektor serve --verbose --prune

# Build to custom output directory
.venv/bin/lektor build --output-path=/path/to/output

# Clean cache
.venv/bin/lektor clean
```

## Deployment

The site is automatically deployed to **Netlify** when pushing to the main branch. Netlify:

1. Detects changes on the GitHub repository
2. Installs Python 3.12.12 and dependencies
3. Runs `lektor build`
4. Publishes the `output/` folder content

No manual action is required for deployment.

## Common Workflows

### Add a New Page

1. Create a folder in `/content/`, e.g., `/content/my-page/`
2. Add a `contents.lr` file with the `page` model
3. Add content using flow blocks (md-section, location, etc.)
4. Optional: add to navigation in `/databags/menu.ini`

### Add a Speaker/Talk

1. Create `/content/speakers/speaker-name/contents.lr` with the `speaker` model
2. Create `/content/talks/talk-title/contents.lr` with the `talk` model
3. Link the talk to the speaker via the `author` field

## Custom Plugins

- **humanize_date**: Jinja2 filter to format dates (e.g., "January 01, 2026")

## Additional Documentation

- [Lektor Documentation](https://www.getlektor.com/docs/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [CLAUDE.md](./CLAUDE.md) - Detailed guide for Claude Code

## Project Configuration

The `PythonFOSDEM.lektorproject` file contains site configuration:
- Project name and event date
- GitHub and Twitter URLs
- CFP (Call for Proposals) dates

## Contributing

To contribute to the site:

1. Fork the project
2. Create a branch for your feature
3. Test locally with `task serve`
4. Submit a Pull Request

## License

See the LICENSE file for more information.
