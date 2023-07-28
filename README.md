# django_parcel_boilerplate

Starter project for a full-stack Django application.

Idea is to keep the frontend stuff away from the Django applications. Treat Django views as
[Hypermedia APIs](https://htmx.org/essays/hypermedia-apis-vs-data-apis). Views can render either
`pages` or `components`.

Frontend project lives under the `frontend` folder. Project structure is as follows:

```
\_ frontend
  \_ public
  \_ src
    \_ components
    \_ layouts
    \_ pages
    \_ styles
```

- ``public``: For static assets like favicon.
- ``src``: Source code to be bundled.
- ``src/components``: Components are units of user interface (UI) code that can be used repeatedly.
- ``src/layouts``: Layouts are essentially design patterns for the UI shared among multiple pages.
- ``src/pages``: Pages are specific implementations of layouts, which are displayed through a view.
- ``src/styles``: Styles aren't obligatory. If they are located anywhere within the src/ directory, Parcel will manage and optimize them.

Frontend bundling is handled by [Parcel](https://parceljs.org/). To spice it up a little, there
are some popular javascript packages included, such as:

- Tailwind
- Alpinejs
- Preact
- React
- HTMX
- Lit

**Build Process**

Build pipeline approach is simple. Let Parcel to bundle all source frontend files and generate
static files ready for distribution. Django's collectstatic handles the rest.

```
+--------------+
| frontend/src |
+--------------+
       |
       | Parcel
       v
+-----------------+
|  frontend/dist  |
+-----------------+
       |
       | Django's collectstatic
       v
 +-------------+
 | static_root |
 +-------------+
```

**Backend setup**

*From the root directory*

```bash
# within a python virtual environment

pip install pip-tools

pip-compile --generate-hashes requirements.in
pip-compile --generate-hashes dev-requirements.in
pip-sync requirements.txt dev-requirements.txt

python manage.py migrate
python manage.py runserver
```

**Frontend setup**

*From the `frontend` directory*

```bash
npm install
npm run dev
```
